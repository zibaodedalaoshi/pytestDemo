import logging

import pytest

@pytest.fixture(scope="function")
def testcase_data(request):
    logging.log("页面自动化")