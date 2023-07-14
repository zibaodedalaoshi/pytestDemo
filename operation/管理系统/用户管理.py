import json
from common.read_data import data
from api.user_management import *

#获取setting.ini中的配置项
SYSPWD = data.load_ini()["host"]["SYSPWD"]
header = json.loads(data.load_ini()["host"]["headers"])

# def create_user(userName, password=SYSPWD, email=""):
#     # 创建用户（如果用户已存在，则先删除再重新创建用户）
#     # 参数: userName - 用户名；password - 密码；email - 邮箱
#     isExist = check_user_exist(userName)
#     if isExist == False:
#         user = create_new_user(userName, password, email)
#     else:
#         user = recreate_user(userName, password, email)
#     isExist = check_user_exist(userName)
#     return user

def createPost(postName):
    res = user_management.post_add(json=postName,headers=header)
    return res

def createRole(roleName,auth):
    auth = 'Bearer ' + auth
    header['Authorization'] = auth
    payload = {
        "description" : "",
        "text" : roleName
    }
    res = user_management.role_add(json=payload, headers=header)
    return res

def character_add(character,parentId="decision-dep-root",auth=None):
    '''
    ...    格式：${rsp}    character_add    用户名称(user)
    ...    返回值dictionary：${user}   id=    name=    (pwd=)
    ...    如果在部门下添加子部门，不需要character_add 直接用character_link
    '''
    # 检查格式是否正确
    assert '(' in character and ')' in character
    # 解析字符名称和类型
    char_name = character.split('(')[-2]
    char_type = character.split('(')[1].split(')')[0]
    # 检查类型是否正确，如果不正确则抛出异常
    if char_type not in ['user', 'role', 'post', 'dept']:
        raise AssertionError('类型错误')
    rsp = None
    for i in ['user', 'role', 'post', 'dept']:
        if char_type == 'user':
            #rsp = createUser(char_name)
            rsp = None
        elif char_type == 'post':
            rsp = createPost(char_name)
        elif char_type == 'dept':
            #rsp = createDept(char_name, parentId)
            rsp = None
        else:
            rsp = createRole(char_name,auth)
    return rsp
