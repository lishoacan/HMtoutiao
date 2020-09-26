import jwt
from flask import current_app


def generate_jwt(payload, expiry, secret=None):
    """
    生成jwt
    :param payload: dict 载荷-只保存用户信息
    :param expiry: 有效期时间戳 expiry
    :param secret: 密钥-从配置文件读取
    :return: token
    """
    # 过期时间字典
    _payload = {'exp': expiry}
    # update字典更新添加键值对
    _payload.update(payload)

    """
    _payload = {
        "user_id"： value,
        "exp":  xxx
    }
    """

    if not secret:
        # 从配置文件中读取配置信息
        secret = current_app.config['JWT_SECRET']

    token = jwt.encode(_payload, secret, algorithm='HS256')
    return token.decode()


def verify_jwt(token, secret=None):
    """
    检验jwt
    :param token: jwt
    :param secret: 密钥
    :return: dict: payload
    """
    if not secret:
        secret = current_app.config['JWT_SECRET']

    try:
        payload = jwt.decode(token, secret, algorithm=['HS256'])
    except jwt.PyJWTError:
        payload = None

    # 返回的载荷字典可能为空
    return payload
