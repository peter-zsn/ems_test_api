import functools
import logging
import os
import time
from logging import handlers
from pathlib import Path


class SafeTimedRotatingFileHandler(logging.handlers.TimedRotatingFileHandler):
    def __init__(self, filename='', when='h', interval=1, backupCount=0, encoding=None, delay=False, utc=False,
                 atTime=None, maxBytes=50 * 1024 * 1024):
        super().__init__(filename, when, interval, backupCount, encoding, delay, utc, atTime)
        self.maxBytes = maxBytes

    def shouldRollover(self, record):
        """
        Determine if rollover should occur.

        record is not used, as we are just comparing times, but it is needed so
        the method signatures are the same
        """
        t = int(time.time())
        if t >= self.rolloverAt:
            return 1
        if self.stream is None:  # delay was set...
            self.stream = self._open()
        if self.maxBytes > 0:  # are we rolling over?
            msg = "%s\n" % self.format(record)
            self.stream.seek(0, 2)  # due to non-posix-compliant Windows feature
            if self.stream.tell() + len(msg) >= self.maxBytes:
                return 1
        return 0

    def doRollover(self):
        if self.stream:
            self.stream.close()
            self.stream = None
        # get the time that this sequence started at and make it a time_tuple
        current_time = int(time.time())
        dst_now = time.localtime(current_time)[-1]
        t = self.rolloverAt - self.interval
        if self.utc:
            time_tuple = time.gmtime(t)
        else:
            time_tuple = time.localtime(t)
            dst_then = time_tuple[-1]
            if dst_now != dst_then:
                if dst_now:
                    addend = 3600
                else:
                    addend = -3600
                time_tuple = time.localtime(t + addend)
        dfn = self.rotation_filename(self.baseFilename + "." +
                                     time.strftime(self.suffix, time_tuple))

        # 存在删除逻辑去掉
        self.rotate(self.baseFilename, dfn)
        if self.backupCount > 0:
            for s in self.getFilesToDelete():
                os.remove(s)
        if not self.delay:
            self.stream = self._open()
        new_rollover_at = self.computeRollover(current_time)
        while new_rollover_at <= current_time:
            new_rollover_at = new_rollover_at + self.interval
        # If DST changes and midnight or weekly rollover, adjust for this.
        if (self.when == 'MIDNIGHT' or self.when.startswith('W')) and not self.utc:
            dst_at_rollover = time.localtime(new_rollover_at)[-1]
            if dst_now != dst_at_rollover:
                if not dst_now:  # DST kicks in before next rollover, so we need to deduct an hour
                    addend = -3600
                else:  # DST bows out before next rollover, so we need to add an hour
                    addend = 3600
                new_rollover_at += addend
        self.rolloverAt = new_rollover_at

    def rotate(self, source, dest):

        if not callable(self.rotator):
            # 增加os.path.exists(dest)，如果目标存在，不再rename
            if os.path.exists(source):
                if os.path.exists(dest):
                    os.remove(dest)
                os.rename(source, dest)
        else:
            self.rotator(source, dest)


def setup_log(name='EMS_REST_API'):
    log_formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(filename)s[%(lineno)d] - %(funcName)s - %(message)s ')

    # file handler
    log_dir = Path(__file__).parent.parent.joinpath('logs')
    if not log_dir.is_dir():
        log_dir.mkdir()
    file_name = str(log_dir.joinpath(f"daily_log_{name}.log").absolute())
    file_handler = SafeTimedRotatingFileHandler(
        file_name, when='MIDNIGHT', backupCount=0, encoding='utf8', maxBytes=1024 * 1024 * 1024)
    file_handler.setFormatter(log_formatter)

    # stream handler
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(log_formatter)
    
    g_logger = logging.getLogger()
    g_logger.setLevel(logging.INFO)
    if g_logger.handlers:
        g_logger.handlers = list()
    g_logger.addHandler(file_handler)
    g_logger.addHandler(stream_handler)
    
    return g_logger


class LogDecorator(object):
    def __init__(self):
        self.logger = logging.getLogger()

    def __call__(self, fn):
        @functools.wraps(fn)
        def decorated(*args, **kwargs):
            try:
                self.logger.info("{0} - {1} - {2}".format(fn.__name__, args, kwargs))
                result = fn(*args, **kwargs)
                self.logger.info(result)

                return result
            except Exception as ex:
                self.logger.info("Exception {0}".format(ex))
                raise ex

        return decorated


# logger = setup_log('zfb')



LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "default": {
            "()": "uvicorn.logging.DefaultFormatter",
            "fmt": "%(asctime)s - %(name)s - %(levelname)s - %(filename)s[%(lineno)d] - %(funcName)s -  %(message)s",
            "use_colors": None,
        },
        "access": {
            "()": "uvicorn.logging.AccessFormatter",
            "fmt": '%(asctime)s - %(name)s - %(levelname)s - %(filename)s[%(lineno)d] - %(funcName)s - %(message)s ',
        },
    },
    "handlers": {
        "default": {
            "formatter": "default",
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stderr",
        },
        "access": {
            "formatter": "access",
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stdout",
        },
        "default_file": {
            "formatter": "default",
            "class": "loggers.logger.SafeTimedRotatingFileHandler",
            "filename": str(Path(__file__).parent.parent.joinpath('logs').joinpath(f"daily_log_EMS_REST_API.log").absolute()),
            "when": "MIDNIGHT",
            "backupCount": 0,
            "maxBytes": 1024 * 1024 * 1024,
            "encoding": 'utf-8',
        },
         "access_file": {
            "formatter": "access",
            "class": "loggers.logger.SafeTimedRotatingFileHandler",
            "filename": str(Path(__file__).parent.parent.joinpath('logs').joinpath(f"daily_log_EMS_REST_API.log").absolute()),
            "when": "MIDNIGHT",
            "backupCount": 0,
            "maxBytes": 1024 * 1024 * 1024,
            "encoding": 'utf-8',
        },
    },
    "loggers": {
        "uvicorn": {"handlers": ["default", "default_file"], "level": "INFO", "propagate": False},
        "uvicorn.error": {"level": "INFO"},
        "uvicorn.access": {"handlers": ["access", "access_file"], "level": "INFO", "propagate": False},
    },
}