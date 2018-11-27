from flask_restful import Resource, reqparse, marshal_with, fields

#创建博客功能
from App.models import User, db, Blog

parser = reqparse.RequestParser()
parser.add_argument(name='title',type=str,required=True,help='标题不能够为空')
parser.add_argument(name='content',type=str,required=True,help='内容不能为空')

user_fields = {
    'title': fields.String,
    'content':fields.String
}

result_fields = {

    'returnblogCode': fields.String,
    'returnblogValue': fields.Nested(user_fields)
}

class BlogcreateResource(Resource):
    @marshal_with(result_fields)
    def post(self):
        parse =parser.parse_args()
        # 解析请求参数
        title= parse.get('title')
        content = parse.get('content')
        print(title)
        print(content)
        # 创建Blog对象
        blog=Blog()
        blog.b_title=title
        blog.b_content =content

        try:
            db.session.add(blog)
            db.session.commit()
        except Exception as e:
            return {'returnCode': '1', 'returnValue': str(e)}

        return {'returnCode': '1', 'returnValue': blog}


