# views.py: 路由+视图函数
from flask import Blueprint, jsonify, request
from .models import *

# 蓝图:先声明，还没有创建app
blue = Blueprint('user', __name__)


@blue.route('/get', methods=['GET'])
def get_articles():
    return jsonify({"Hello": "World"})


@blue.route('/add', methods=['POST'])
def add_articles():
    title = request.json['title']
    body = request.json['body']

    articles = Articles(title, body)
    db.session.add(articles)
    db.session.commit()
    return 'OK'
