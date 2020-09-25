from flask import Flask
from app.settings.config import config_dict
from utils import contants
import os, sys

BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE_PATH + '/common')


def create_flask_app(type):
    """
    内部调用生产app的方法
    :param type: app对象的配置信息
    :return: 对应配置的app对象
    """
    app = Flask(__name__)

    app.config.from_object(config_dict[type])
    app.config.from_envvar(contants.EXTRA_EVN_CONFIG,silent=True)

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

    # 3.注册蓝图初始化组件
    return app
