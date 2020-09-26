# from pymysql import install_as_MySQLdb
# install_as_MySQLdb()
# 默认配置信息
class DefaultConfig(object):
    # session混淆加密字符串
    SECRET_KEY = 'python'

    # 不允许中午转换成ASCII编码
    RESTFUL_JSON = {'ensure_ascii':False}

    #  mysql数据库配置信息
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://lishaocan:mysql@192.168.16.6:3306/HMtoutiao_db"
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    #  redis[主库]数据库配置信息
    REDIS_HOST = '192.168.16.6'
    REDIS_PORT = 6379

    # jwt加密密钥
    JWT_SECRET = "DmWdySUcvyJYBhw1g2gtTcmgOH0EGocmXRB4Ngk7StU="
    # 2小时有效
    JWT_LOGIN_EXPIRE = 2
    # 14天有效
    JWT_REFRESH_EXPIRE = 14

class DevelopmentConfig(DefaultConfig):
    DEBUG = True



class ProductionConfig(DefaultConfig):

    DEBUG = False

    #  mysql数据库配置信息
    #  redis数据库配置信息

config_dict = {
    "dev":DevelopmentConfig,
    "pro":ProductionConfig
}

