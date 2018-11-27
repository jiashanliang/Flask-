
from flask_restful import Resource, reqparse

from App.UserApi.UserRegister import cache
from App.models import User, db

parser = reqparse.RequestParser()

parser.add_argument('icon',type=str)


class AccountResource(Resource):
    #需求  要修改当前数据的active状态
    #方案：通过inco获取active 然后修改状态
    def get(self):
        parse = parser.parse_args()
        #获取了参数为inco的值
        icon = parse.get('icon')
        print('-------------------------')
        id = cache.get(icon)
        print(id)
        if id:
        # 注意此时users是一个basequery类型的对象 那么获取basequery中的对象的方法是first（）
            users = User.query.filter(User.u_id.__eq__(id))

            if users.count() > 0:
                user = users.first()

                user.u_active = True

                db.session.add(user)

                db.session.commit()
                return {'msg': 'i am account'}
        else:
            return {'msg':'i am not account'}
