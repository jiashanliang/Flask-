from flask_restful import Resource, reqparse
from werkzeug.security import check_password_hash

from App.models import User

parser = reqparse.RequestParser()

parser.add_argument(name='name',type=str,required=True,help='用户名字没有写')
parser.add_argument(name='password',type=str,required=True,help='密码没有写')

# 验证码和密码登录（密码实现数据安全）
class LoginResource(Resource):
     def post(self):
         parse = parser.parse_args()

         name = parse.get('name')
         password = parse.get('password')

         users = User.query.filter(User.u_name.__eq__(name))

         if users.count() > 0:
             #在数据库中查询user
             user = users.first()
             if user:
                 if user.is_delete ==False:
                     if check_password_hash(user.u_password,password):
                         if user.u_active == 1:
                             return {'msg':'登录成功，欢迎你'}
                         else:
                             return {'msg':'用户没有激活，请检查邮件激活邮件'}
                     else:
                         return {'msg':'密码不正确'}
                 else:
                      return {'msg':'该用户已经被删除，不能够登录'}
             else:
                 return  {'msg':'用户名或者密码错误'}
         return {'msg':'用户名字不存在'}




