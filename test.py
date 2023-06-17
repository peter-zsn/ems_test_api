# import uvicorn
# from loggers.logger import LOGGING_CONFIG


# uvicorn.run("app:app", host='127.0.0.1', port=8080, workers=1, log_config=LOGGING_CONFIG)



'''
# gunicorn app:app -b 127.0.0.1:8080 --worker-class uvicorn.workers.UvicornWorker 失败

# gunicorn -c gunicorn.conf app:app 失败
gunicorn -k uvicorn.workers.UvicornWorker  app:app 失败


uvicorn app:app --host 0.0.0.0 --port 8080 --workers 4

暂时推荐这种方式运行
uvicorn app:app --host 0.0.0.0 --port 8080 --workers 4 --log-config uvicorn.json
'''