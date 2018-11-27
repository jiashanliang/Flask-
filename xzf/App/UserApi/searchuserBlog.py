from flask_restful import Resource, reqparse, marshal_with, fields
from App.models import Blog, db, User, Collection

#查看一个用户所有收藏的博文

cursor = db.cursor()

parser = reqparse.RequestParser()
parser.add_argument(name='u_name', type=str, required=True, help='用户名不能够为空')

userinfo ={
    'id':fields.Integer,
    'name':fields.String,
}

bloginfo ={
    'blogtitle':fields.String,
    'blogcontent':fields.String
}

user_blog ={
    'user':fields.Nested(userinfo),
    'blog':fields.List(fields.Nested(bloginfo))
}


class SearchallblogResource(Resource):

    def post(self):
        parse = parser.parse_args()
        user_name = parse.get("u_name")
        users = User.query.filter(User.u_name == user_name)
        if users.count()>0:
            user= users.first()
            collects= Collection.query.filter(Collection.u_id == user.id)
            if collects.count()>0:
                collect=collects.all()
                blog =Blog.quert.filter.filter(Blog.id ==collect.b_id)
                bloginfo= blog.all()
                inputform(user,bloginfo)
            else:
                return{ 'msg':'该用户没有该收藏'}
        else:
            return {'msg':'哈哈哈 没有该用户，请先注册 '}

@marshal_with(user_blog)
def inputform(user,bloginfo):
    return {'user': user,
            'blog': bloginfo,
            }