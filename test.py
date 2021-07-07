import pytest

@pytest.fixture()
def user():
    print("获取用户名")
    a = 'admin'
    return a


def test_1(user):
    assert user == 'admin'

def test_2(user):
    assert user == 'admin'

if __name__ == '__main__':
    pytest.main(["-s", "test.py"])
