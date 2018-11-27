from App.BlogAPI.Blogregister import BlogcreateResource
from App.BlogAPI.DeleteBlog import DeleteResource
from App.BlogAPI.UpdateBlog import UpdateBlogResource
from App.UserApi import api

api.add_resource(BlogcreateResource,'/createblog/')#博客创建
api.add_resource(UpdateBlogResource,'/updateblog/')#博客修改
api.add_resource(DeleteResource,'/deleteblog/')#博客删除




