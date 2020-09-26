from flask_restful import Resource
import random
from flask_restful.inputs import *
from sqlalchemy.orm import load_only

from app import redis_cli, db
from model.user import User
from utils import parser as type_parser
from utils.contants import SMS_CODE_EXPIRE
from flask_restful.reqparse import RequestParser


# 验证码类视图
class SMSCodeResource(Resource):

    def get(self, mobile):
        """
        短信验证码视图
        :param mobile:
        :return:
        """
        # 产生随机6位短信验证码
        random_smscode = '%06d' % (random.randint(0, 999999))
        random_smscode = '123456'  # todo:仅开发阶段使用的字段

        # redis保存对应mobile的验证码
        key = "app:codes:{}".format(mobile)
        redis_cli.setex(name=key, time=SMS_CODE_EXPIRE, value=mobile)

        # 调用发送验证码第三方模块
        print("发送短信验证码成功 手机号码: {} 短信验证码: {}".format(mobile, random_smscode))
        # 返回短信验证码/手机号码
        return {
            'mobile': mobile,
            'smscode': random_smscode  # todo:仅开发阶段返回的字段
        }


# 登陆类视图
class LoginRegisterResource(Resource):
    def post(self):
        """
        # 1.获取参数
        # 2.参数校验
        # 3.逻辑处理
        # 4.返回值处理
        :return:
        """
        parser = RequestParser()
        parser.add_argument("mobile", required=True, location='json', type=type_parser.mobile)
        parser.add_argument('code', required=True, location='json', type=regex(r'\d{6}'))
        ret = parser.parse_args()
        moblie = ret["mobile"]
        code = ret["code"]

        key = "app:code:{}".format(moblie)
        redis_smscode = redis_cli(key)
        if redis_smscode is None or redis_smscode != code:
            return {"message": "invalid smscode"}, 400

        user = User.query.options(load_only(User.id)).filter(User.mobile == moblie).first()

        if user is None:
            user = User(name=moblie,moblie=moblie,last_login=datetime.now())
            db.session.add(user)
        else:
            user.last_login = datetime.now()
        try:
            db.session.commit()
        except Exception as e:
            return {'message':e},506



        # todo:jwt登陆验证登陆


