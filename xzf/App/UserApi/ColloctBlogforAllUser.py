from flask_restful import Resource, reqparse, marshal_with, fields
from App.models import Blog, db, User, Collection

#查看收藏一个博文所有的用户


parser = reqparse.RequestParser()
parser.add_argument(name='blog_title', type=str, required=True, help='博客的标题不能够为空')

userinfo ={
    'id':fields.Integer,
    'name':fields.String,
}

bloginfo ={
    'blogtitle':fields.String,
    'blogcontent':fields.String
}

user_blog ={
    'user':fields.List(fields.Nested(userinfo)),
    'blog':fields.Nested(bloginfo),

}

class CollectBlogforallUser(Resource):

    def post(self):
        parse = parser.parse_args()
        blog_title= parse.get("blog_title")
        blogs =Blog.query.filter(Blog,blog_title == blog_title)
        if blogs.count()>0:
            blog= blogs.first()
            collects= Collection.query.filter(Collection.b_id == Blog.id)
            if collects.count()>0:
                collect=collects.all()
                user =User.quert.filter(User.id ==collect.u_id)
                userinfo= user.all()
                inputform(blog,userinfo)
            else:
                return{ 'msg':'该收藏中没有该用户'}
        else:
            return {'msg':'对不起，没有这篇博文 '}

@marshal_with(user_blog)
def inputform(blog,userinfo):
    return {'user': userinfo,
             'blog': blog,
            }