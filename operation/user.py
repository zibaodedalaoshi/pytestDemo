from api.common import common
from common.read_data import data
import json

username = data.load_ini()["host"]["SYSUSER"]
password = data.load_ini()["host"]["SYSPWD"]

def pingtai_login(username=username,password=password):
    header = json.loads(data.load_ini()["host"]["headers"])
    header["X-Requested-With"] = "XMLHttpRequest"
    payload = {
        "username": username,
        "password": password
    }
    res = common.login(json=payload,headers=header)
    return res.json()

if __name__ == '__main__':
    res = pingtai_login()
    print(res)

