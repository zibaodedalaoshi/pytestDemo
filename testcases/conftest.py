import pytest
import os
import allure
from common.read_data import data
from common.logger import logger
from operation import user

BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))


def get_data(yaml_file_name):
    try:
        data_file_path = os.path.join(BASE_PATH, "data", yaml_file_name)
        yaml_data = data.load_yaml(data_file_path)
    except Exception as ex:
        pytest.skip(str(ex))
    else:
        return yaml_data



error_code = get_data("errorcode.yml")


@allure.step("前置步骤 ==>> 清理数据")
def step_first():
    logger.info("******************************")
    logger.info("前置步骤开始 ==>> 清理数据")


@allure.step("后置步骤 ==>> 清理数据")
def step_last():
    logger.info("后置步骤开始 ==>> 清理数据")


@allure.step("前置步骤 ==>> 管理员用户登录")
def step_login(username, password):
    user.pingtai_login()
    logger.info("前置步骤 ==>> 管理员 {} 登录，返回信息 为：{}".format(username, password))



@pytest.fixture(scope="session")
def login_fixture():
    logger.info("登录")
