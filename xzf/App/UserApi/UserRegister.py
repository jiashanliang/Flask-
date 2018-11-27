
import uuid

from flask import render_template
from flask_cache import Cache
from flask_mail import Message
from flask_restful import reqparse, Resource, fields, marshal_with
from werkzeug.security import generate_password_hash

from App.ext import mail
from App.models import User, db

parser = reqparse.RequestParser()
parser.add_argument(name='name',type=str,required=True,help='用户名字不能为空')
parser.add_argument(name='password',type=str,required=True,help='密码不能为空')
parser.add_argument(name='email',type=str,required=True,help='邮箱不能为空')

cache = Cache(config={
    'CACHE_TYPE':'redis'
})

def init_cache(app):
    cache.init_app(app=app)

class UserResource(Resource):

    user_fields={
        'id':fields.Integer,
        'u_name':fields.String,
    }

    result_fields={
        'returnCode':fields.String,
        'returnValue':fields.Nested(user_fields)
    }

    @marshal_with(result_fields)
    def post(self):
        parse = parser.parse_args()
        name = parse.get('name')
        password = parse.get('password')
        email = parse.get('email')
        user = User()
        user.u_name = name
        password = generate_password_hash(password)
        user.u_password = password
        user.u_email = email
        token = str(uuid.uuid4())
        user.u_token = token

        try:
            db.session.add(user)
            db.session.commit()
            cache.set(token,user.id, timeout=180)
            msg = Message(subject='激活',sender='m17670473079@163.com',recipients=[email])

            html_content = render_template('registerinfo.html',name=name,url='127.0.0.1:6000/account/?token='+ token)

            msg.html = html_content

            mail.send(msg)

        except Exception as e:
            return {'returnCode':'0','returnValue':str(e)}

        return {'returnCode':'0','returnValue':user}


