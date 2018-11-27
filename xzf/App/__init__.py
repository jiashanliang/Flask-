from flask import Flask

from App import settings
from App.UserApi import init_apis
from App.UserApi.UserRegister import init_cache

from App.ext import init_ext


def create_app(env_name):
    app = Flask(__name__)
    app.config.from_object(settings.env.get(env_name))
    # 当浏览器显示中文乱码的时候  那么需要加这个忽略编码格式
    app.config.update(RESTFUL_JSON=dict(ensure_ascii=False))
    init_ext(app)
    init_apis(app)
    init_cache(app)
    return app