import re
import base64
from datetime import datetime


def email(email_str):
    """
    邮箱校验
    :param email_str: 邮箱字符串
    :return:
    """
    if re.match(r'^([A-Za-z0-9_\-\.\u4e00-\u9fa5])+\@([A-Za-z0-9_\-\.])+\.([A-Za-z]{2,8})$', email_str):
        return email_str
    else:
        return ValueError('{} is not valid email'.format(email_str))

def mobile(mobile_str):
    """
    手机号码格式校验
    :param mobile_str: 手机号码字符串
    :return:
    """
    if re.match(r'^1[3-9]\d{9}$', mobile_str):
        return mobile_str
    else:
        return ValueError('{} is not valid mobile'.format(mobile_str))

def id_number(value):
    """
    身份证号码校验
    :param value: 身份证字符串
    :return:
    """
    id_number_pattern = r'(^[1-9]\d{5}(18|19|([23]\d))\d{2}((0[1-9])|(10|11|12))(([0-2][1-9])|10|20|30|31)\d{3}[0-9Xx]$)|(^[1-9]\d{5}\d{2}((0[1-9])|(10|11|12))(([0-2][1-9])|10|20|30|31)\d{2}$)'
    if re.match(id_number_pattern,value):
        return value.upper()
    else:
        return ValueError('Invalid id number.')
