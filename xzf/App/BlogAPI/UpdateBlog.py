from flask_restful import Resource, reqparse

from App.models import Blog, db

parser = reqparse.RequestParser()

parser.add_argument(name='title',type=str,required=True,help='标题必须写')
parser.add_argument(name='content',type=str,required=True,help='内容必须写')
class UpdateBlogResource(Resource):
    def post(self):
        # 修改博客
        parse= parser.parse_args()
        title = parse.get('title')
        content = parse.get('content')

        blogtitles = Blog.query.filter(title == Blog.b_title)
        if blogtitles.count() > 0:
            # 在数据库中查询blog的标题
            blog = blogtitles.get()
            if content:
                blog.b_title = title
                blog.b_content = content
                db.session.add(blog)
                db.session.commit()
                return {'msg': '博客修改成功'}
            else:
                return {'msg': '博客修改失败'}
        else:
            return {'msg': '没有这条博客内容'}
