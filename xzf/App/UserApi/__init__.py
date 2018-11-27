from flask_restful import Api

from App.UserApi.AccountRegister import AccountResource
from App.UserApi.ColloctBlogforAllUser import CollectBlogforallUser
from App.UserApi.LoginForm import LoginResource
from App.UserApi.UpdateForm import UpdateResource
from App.UserApi.UserRegister import UserResource
from App.UserApi.collectBlog import CollectResource
from App.UserApi.deleteform import DeleteResource
from App.UserApi.searchuserBlog import SearchallblogResource

api = Api()

def init_apis(app):
    api.init_app(app=app)

api.add_resource(UserResource,'/register/')#用户email注册（邮箱验证）
api.add_resource(AccountResource,'/account/')#激活
api.add_resource(LoginResource,'/login/')#用户登录（删除用户不可得登录）
api.add_resource(UpdateResource,'/updateinfo/')# 用户信息修改
api.add_resource(DeleteResource,'/deleteinfo/')#用户信息删除
api.add_resource(CollectResource,'/collectblog/')#收藏博客
api.add_resource(SearchallblogResource,'/searchblog/')#获取某用户的所有收藏
api.add_resource(CollectBlogforallUser,'/showbloguser/')#获取收藏某博客的所有用户



