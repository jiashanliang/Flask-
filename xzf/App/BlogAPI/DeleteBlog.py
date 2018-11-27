from flask_restful import Resource, reqparse
from sqlalchemy.dialects.mysql import pymysql

from App.models import Blog, db

#删除博客
cursor = db.cursor()

parser = reqparse.RequestParser()
parser.add_argument(name='title', type=str, required=True, help='标题不能为空')
class DeleteResource(Resource):
    def post(self):
        parse= parser.parse_args()
        title =parse.get('title')
        blogtitles =Blog.query.filter(title == Blog.b_title)
        if blogtitles.count() > 0:
            # 在数据库中查询blog的标题
            blog= blogtitles.get()
            if blog:
                db.begin()
                sql="delete from blog where b_title ='{}'".format(title)
                cursor.execute(sql)
                db.commit()
                return {'msg': '用户信息删除成功'}
            else:
                return {'msg': '用户信息删除失败'}
        else:
            return {'msg':'没有这条博客内容'}




