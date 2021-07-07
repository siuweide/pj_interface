import pytest
import allure
from fixture.tool_fixture import *

class TestDept():


    def test_dept(self, http, get_token):
        allure.dynamic.title('门店用例')
        url = 'http://192.168.10.116:9902/admin/commission/department/list'
        data = {"keyword":"","pageNumber":2,"pageSize":15,"partnershipType":-1,"deptStatus":2,"system":"pc","model":"pc","appId":"commission","role":"","uid":"0a14020acc0346c7a2c034a08c83414f"}
        headers = {"satoken": get_token}
        response = http.post(url, data, headers).json()
        assert response['msg'] == 'SUCCESS'

if __name__ == '__main__':
    pytest.main(['-s', '-v'])