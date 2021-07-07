
import pytest
from config.url_config import UrlConf
from common.http_requests import HttpRequests

@pytest.fixture(scope='function', autouse=True)
def http():
    http = HttpRequests()
    return http

@pytest.fixture(scope='function', autouse=True)
def get_token(http):
    response = http.post(url=UrlConf.test_url.value,
                         data={"account":"13100000007","password":"123456","system":"pc","model":"pc","appId":"commission","role":"","uid":""})
    token = response.json()['data']['tokenValue']
    return token


if __name__ == '__main__':
    print(get_token().json()['data']['tokenValue'])

