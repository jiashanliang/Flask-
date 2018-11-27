import uuid

from flask_restful import Resource, reqparse, marshal_with, fields
from werkzeug.security import check_password_hash, generate_password_hash

from App.models import User, db

# class User(db.Model):
#     u_id =db.Column(db.Integer,primary_key=True,autoincrement=True)
#     u_name=db.Column(db.String(64),unique=True)
#     u_email=db.Column(db.String(128))
#     u_password =db.Column(db.String(64))
#     u_icon =db.Column(db.Integer)
#     u_active=db.Column(db.Boolean,default=False)
#     is_delete =db.Column(db.Boolean)

parser = reqparse.RequestParser()

#用户信息修改


user_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'email':fields.String
}

result_fields = {

    'returnCode': fields.String,
    'returnValue': fields.Nested(user_fields),
    'eg':fields.String
}

class UpdateResource(Resource):
    def post(self):
        parse = parser.parse_args()
        # 解析请求参数
        name = parse.get('name')
        password = parse.get('password')
        email = parse.get('email')
        # 创建user对象，并且修改用户信息
        user = User()
        user.u_name = name
        password = generate_password_hash(password)
        user.u_password = password
        user.u_email = email
        users = User.query.filter(User.u_name.__eq__(name))

        if users.count() > 0:
            # 在数据库中查询user
            user = users.first()
            if user:
                if user.is_delete == False:
                    if check_password_hash(user.u_password, password):
                        if user.u_active == 1:
                           commituserdata(user)
                        else:
                            return {'msg': '用户没有激活，请检查邮件激活邮件'}
                    else:
                        return {'msg': '密码不正确'}
                else:
                    return {'msg': '该用户已经被删除，不能够登录'}
            else:
                return {'msg': '用户名字不存在'}
        return {'msg': '用户名或者密码错误'}


@marshal_with(result_fields)
def commituserdata(user):
    try:
        db.session.add(user)
        db.session.commit()
    except Exception as e:
        return {'returnCode': '0', 'returnValue': str(e), 'eg': '报错咯'}
    return {'returnCode': '0', 'returnValue': user, 'eg': '信息修改成功'}





