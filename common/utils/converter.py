from werkzeug.routing import BaseConverter


class MobileConverter(BaseConverter):
    """
    手机路由自定义
    手机格式
    """
    regex = r'1[3-9]\d{9}'


def register_converters(app):
    """
    # 想Flask app中添加转换器
    :param app: Flask app对象
    :return:
    """
    app.url_map.conerters['mob'] = MobileConverter
