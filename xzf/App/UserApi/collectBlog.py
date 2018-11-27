from flask_restful import Resource, reqparse
from App.models import Blog, db, User, Collection

#收藏博客

parser = reqparse.RequestParser()
parser.add_argument(name='u_name', type=str, required=True, help='用户名不能够为空')
parser.add_argument(name='b_title', type=str, required=True, help='要收藏的博客标题不能够为空')

class CollectResource(Resource):
    def post(self):
        parse=parser.parse_args()
        user_name=parse.get("u_name")
        blog_title =parse.get("b_title")
        blogs =Blog.query.filter(Blog.b_title ==blog_title) #获得标题对应的博文信息
        users =User.query.filter(User.u_name == user_name) # 获得名字对应的用户信息
        if blogs.count() > 0 and users.count() >0:
         #获得blog与user信息
            bloginfo =blogs.get()
            userinfo =users.get()
            collect=Collection()
         #将收藏信息填入收藏表中
            if bloginfo and userinfo:
                collect.u_id =userinfo.u_id
                collect.b_id = bloginfo.b_id
                db.session.add(collect)
                db.session.commit()
                return {'msg': '该博文收藏成功'}
            else:
                return {'msg': '该博文收藏失败'}
        else:
            return {'msg':'没有这条博客内容'}

