import pytest

'''=========================fixture名字作为用例的参数====================================='''
# fixture的名字直接作为测试用例的参数
@pytest.fixture()
def fixtureFunc():
    return 'fixtureFunc'

def test_fixture(fixtureFunc):
    print('我调用了{}'.format(fixtureFunc))

class TestFixture():
    def test_fixture_class(self,fixtureFunc):
        print('在类中使用fixture{}'.format(fixtureFunc))




'''===================使用@pytest.mark.usefixtures("fixture")装饰器======================'''
# 每个函数或着类前使用@pytest.mark.usefixtures('fixture')装饰器

@pytest.fixture
def login():
    print('输入账号，密码先登录')

@pytest.fixture
def login2():
    print("please输入账号，密码先登录")


@pytest.mark.usefixtures("login2", "login")
def test_s11():
    print("用例 11：登录之后其它动作 111") 


'''===============================使用autouse参数====================================='''
# 指定fixture的参数autouse = Ture这样每个测试用例会自动调用fixture(未考虑到fixture范围)
@pytest.fixture(autouse=True)
def everydef():
    print('---autouse---')