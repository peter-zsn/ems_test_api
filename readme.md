```
ems_rest_api
├─ .gitignore
├─ app.py ----主入口
├─ apps -- 逻辑功能
│  ├─ __init__.py
│  ├─ index.py
│  ├─ routers.py    ----跟路由
│  └─ systems
│     ├─ __init__.py
│     ├─ routers.py --- 系统路由
│     └─ views.py   ----视图
├─ libs
│  ├─ jwt_test.py   ---- 获取auth0token
│  └─ jwt_util.py ---- jwt验证
├─ loggers  ----日志包
├─ middlewares ---自定义中间件
│  └─ auth_milldewares.py ----鉴权中间件
├─ readme.md
└─ request.txt
```