from app import create_app
from flask import jsonify

app = create_app('dev')


@app.route('/index')
def index():   # 字典推导式
    route_dict = {
        rule.rule: rule.endpoint for rule in app.url_map.iter_rules()
    }
    return jsonify(route_dict)

    # 返回所有路由信息
