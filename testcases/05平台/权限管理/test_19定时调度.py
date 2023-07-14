import pytest
import allure
from operation.user import pingtai_login
from testcases.conftest import error_code
from common.logger import logger

@allure.severity(allure.severity_level.NORMAL)
@allure.epic("针对单个接口的测试")
@allure.feature("获取用户信息模块")
class TestLogin():
    """定时调度模块"""

    @allure.story("文件处理-BI模板-邮件通知-勾选正文预览和使用附件")
    @allure.description("TT-45285")
    @allure.testcase("https://work.fineres.com/browse/TT-45285", name="点击，跳转到对应用例的链接地址")
    @pytest.mark.single
    def test_01(self):
        logger.info("*************** 开始执行用例 ***************")
        res = pingtai_login()
        logger.info("*************** 结束执行用例 ***************")

if __name__ == '__main__':
    pytest.main(["-q", "-s","test_00_user_login.py"])