import os
import configparser
from core.rest_client import RestClient

#获取setting.ini中的配置项
config = configparser.ConfigParser()
BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
config.read(os.path.join(BASE_PATH,'config/setting.ini'), encoding='utf-8')
api_root_url = config.get('host','api_root_url')

class Common(RestClient):

    def __init__(self, api_root_url, **kwargs):
        super(Common, self).__init__(api_root_url, **kwargs)

    def login(self, **kwargs):
        return self.post("/login", **kwargs)

common=Common(api_root_url)