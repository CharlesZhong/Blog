from flask import render_template,request
from flask_sqlalchemy import Pagination
import pymongo

from . import hupu
from .. import mongo
from datetime import datetime,timedelta

@hupu.route('/index')
def index():
    total = mongo.db.BXJItem.find({"reply_count": {"$gt": 10}}, {'_id': 0}).count()
    page = request.args.get('page', 1, type=int)
    capacity = request.args.get('limit', 30, type=int)

    light_items = mongo.db.BXJItem \
                      .find({"reply_count": {"$gt": 10}}, {'_id': 0}) \
                      .sort('reply_count', pymongo.DESCENDING) \
                      .skip((page -1) * capacity).limit(capacity)
    BXJItems = [item for item in light_items]
    pagination = Pagination(query=None, page=page, per_page=capacity, total=total, items=BXJItems)
    return render_template('hupu/index.html', BXJItems=BXJItems,pagination=pagination)

@hupu.route('/yesterday')
def yesterday():

    dt = datetime.now() - timedelta(days=1)
    yesterday = dt.strftime('%Y-%m-%d' )

    total = mongo.db.BXJItem.find({"create_date": yesterday,"reply_count": {"$gt": 10}}, {'_id': 0}).count()
    page = request.args.get('page', 1, type=int)
    capacity = request.args.get('limit', 30, type=int)

    light_items = mongo.db.BXJItem \
                      .find({"create_date": yesterday,"reply_count": {"$gt": 10}}, {'_id': 0}) \
                      .sort('reply_count', pymongo.DESCENDING) \
                      .skip((page -1) * capacity).limit(capacity)
    BXJItems = [item for item in light_items]
    pagination = Pagination(query=None, page=page, per_page=capacity, total=total, items=BXJItems)
    return render_template('hupu/index.html', BXJItems=BXJItems,pagination=pagination)



@hupu.route('/date/<date>')
def someday(date):
    total = mongo.db.BXJItem.find({"create_date": date,"reply_count": {"$gt": 10}}, {'_id': 0}).count()
    page = request.args.get('page', 1, type=int)
    capacity = request.args.get('limit', 30, type=int)

    light_items = mongo.db.BXJItem \
                      .find({"create_date": date,"reply_count": {"$gt": 10}}, {'_id': 0}) \
                      .sort('reply_count', pymongo.DESCENDING) \
                      .skip((page -1) * capacity).limit(capacity)
    BXJItems = [item for item in light_items]
    pagination = Pagination(query=None, page=page, per_page=capacity, total=total, items=BXJItems)
    return render_template('hupu/index.html', BXJItems=BXJItems,pagination=pagination)



