from flask import Flask
from flask_migrate import Migrate
from app.settings.config import config_dict
import os, sys
from flask_sqlalchemy import SQLAlchemy
from redis import StrictRedis

BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE_PATH + '/common')
from utils import contants
from utils.converter import MobileConverter

db = SQLAlchemy()
redis_cli = None  # type: StrictRedis


def create_flask_app(type):
    """
    内部调用生产app的方法
    :param type: app对象的配置信息
    :return: 对应配置的app对象
    """
    app = Flask(__name__)

    app.config.from_object(config_dict[type])
    app.config.from_envvar(contants.EXTRA_EVN_CONFIG, silent=True)

    return app


def create_app(type):
    """
    外部调用生产app的工厂方法
    :param type: 配置的类型
    :return: app
    """
    # 1.调用内容方法生产app
    app = create_flask_app(type)

    # 2.注册拓展初始化组件
    register_extensions(app)

    # 3.注册蓝图初始化组件
    regiter_blueprint(app)

    return app


def register_extensions(app: Flask):
    """
    注册拓展初始化
    :param app:
    :return:
    """
    # 延后加载app,进行mysql数据库对象初始化
    db.init_app(app)

    global redis_cli

    redis_cli = StrictRedis(
        host=app.config['REDIS_HOST'],
        port=app.config['REDIS_PORT'],
        decode_responses=True
    )
    app.url_map.converters['mob'] = MobileConverter

    Migrate(app, db)
    # todo:模型类迁移需要导入需迁移的model文件
    from model import user


def regiter_blueprint(app: Flask):
    """
    蓝图注册
    :param app:
    :return:
    """
    # TODO: 注意循环导包问题
    from app.resource.user import user_bp
    app.register_blueprint(user_bp)
