from operation.管理系统.用户管理 import *
from operation.user import pingtai_login

res = pingtai_login()
print(res)
auth =res['data']['accessToken']
res = character_add('a-ABCD(role)',auth=auth)
print(res)

