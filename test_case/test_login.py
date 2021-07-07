
import pytest
import allure
from common.tools import Tools
from fixture.tool_fixture import *

@allure.feature('登录功能')
class TestLogin():

    @allure.story('登录用例')
    def test_success_login(self):
        allure.dynamic.title("登录成功")

        params = Tools().get_params('LoginSucess')
        url = params['url']
        headers = params['headers']
        data = params['data']

        return params

if __name__ == '__main__':
    case = TestLogin()
    case.success_login()