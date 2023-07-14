import os
import configparser
from core.rest_client import RestClient

#获取setting.ini中的配置项
config = configparser.ConfigParser()
BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
config.read(os.path.join(BASE_PATH,'config/setting.ini'), encoding='utf-8')
api_root_url = config.get('host','api_root_url')

user_url = config.get('URLs', 'user_url')
users_url = config.get('URLs', 'users_url')
role_url = config.get('URLs', 'role_url')
roles_url = config.get('URLs', 'roles_url')
department_url = config.get('URLs', 'department_url')
departments_url = config.get('URLs', 'departments_url')
post_url = config.get('URLs', 'post_url')


class User_management(RestClient):
    def __init__(self, api_root_url, **kwargs):
        super(User_management, self).__init__(api_root_url, **kwargs)

    def post_add(self,**kwargs):
        return self.post(post_url,**kwargs)

    def role_add(self,**kwargs):
        return self.post(role_url,**kwargs)

user_management = User_management(api_root_url)