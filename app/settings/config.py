# 默认配置信息
class DefaultConfig(object):
    # session混淆加密字符串
    SECRET_KEY = 'python'
    # 不允许中午转换成ASCII编码
    JSON_AS_ASCII = False


class DevelopmentConfig(DefaultConfig):
    DEBUG = True

    #  mysql数据库配置信息
    SQLALCHEMY_DATABASE_URI = 'msyql://lishaocan:msyql@192.168.16.6:3306/HMtoutiao_db'
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    #  redis数据库配置信息


class ProductionConfig(DefaultConfig):

    DEBUG = False

    #  mysql数据库配置信息
    #  redis数据库配置信息

config_dict = {
    "dev":DevelopmentConfig,
    "pro":ProductionConfig
}

