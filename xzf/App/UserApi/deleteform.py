#用户逻辑删除
from flask_restful import reqparse, Resource


from App.models import User, db

parser = reqparse.RequestParser()
parser.add_argument(name='name',type=str,required=True,help='用户名字不能为空')
parser.add_argument(name='is_delete',type=bool,required=True,help='必须填写，删除为1，不删除为0')

class DeleteResource(Resource):
    def post(self):
        parse = parser.parse_args()
        # 解析请求参数
        name = parse.get('name')
        isdelete = parse.get('is_delete')

        users = User.query.filter(User.u_name.__eq__(name))
        if users.count() > 0:
            # 在数据库中查询user
            user = users.first()
            if isdelete ==1 and user.is_delete==False:
                user.is_delete = True

                db.session.add(user)

                db.session.commit()
                return {'msg': '用户信息删除成功'}
            else:
                return {'msg': '用户信息删除失败'}


