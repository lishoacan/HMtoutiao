# 用户模块
from flask import Blueprint
from flask_restful import Api
from utils.contants import APP_URL_PREFIX
from werkzeug.routing import BaseConverter
from app.resource.user.passport import SMSCodeResource
# 1.创建蓝图对象
from utils.output import output_json

user_bp = Blueprint('user_bp', __name__, url_prefix=APP_URL_PREFIX)
# 2.将蓝图对象包装成具备restful风格的api对象
user_api = Api(user_bp)
# 3.自定义类视图

# 4.类视图添加路由信息
user_api.add_resource(SMSCodeResource,'/sms/codes/<mob:mobile>')

# 5.app中注册蓝图对象[回到init工厂方法中注册蓝图对象]

# 6.给用户模块自定义返回的json字符串格式
"""
{
    "message":"ok",
    "data":{数据}
}
"""
user_api.representation(mediatype="application/json")(output_json)