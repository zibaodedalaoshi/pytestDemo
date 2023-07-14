import pytest
from common.logger import logger


@pytest.fixture(scope="function")
def testcase_data(request):
    logger.info("前置步骤开始 ==>> 清理数据")