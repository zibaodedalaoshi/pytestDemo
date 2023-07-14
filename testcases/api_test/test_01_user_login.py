import pytest
import allure
from operation.user import pingtai_login
from testcases.conftest import error_code
from common.logger import logger



@allure.step("步骤1 ==>> 获取所有用户信息")
def step_1():
    logger.info("步骤1 ==>> 获取所有用户信息")


@allure.step("步骤1 ==>> 获取某个用户信息")
def step_2(username):
    logger.info("步骤1 ==>> 获取某个用户信息：{}".format(username))


@allure.severity(allure.severity_level.TRIVIAL)
@allure.epic("针对单个接口的测试")
@allure.feature("获取用户信息模块")
class TestLogin():
    """用户登录模块"""

    @allure.story("用例--用户登录失败")
    @allure.description("TT-XXXXX")
    @allure.testcase("https://work.fineres.com/browse/TT-66666", name="点击，跳转到对应用例的链接地址")
    @pytest.mark.single
    @pytest.mark.parametrize("errorCode,errorMsg",
                             [tuple(error_code['user_not_available'].values())])
    def test_user_login(self,errorCode,errorMsg):
        logger.info("*************** 开始执行用例 ***************")
        res = pingtai_login()
        assert res['errorCode'] == errorCode
        assert res['errorMsg'] == errorMsg
        logger.info("*************** 结束执行用例 ***************")

if __name__ == '__main__':
    pytest.main(["-q", "-s","test_00_user_login.py"])
