import os
import random
import re

import pytest
import requests
from pip._internal.network import session

from Lixiang_Shebian.util.yaml_util import write_yaml, read_yaml, read_yaml_case


# lst = ['a', 'b', 'c','d','e','f']

# lst.append('g') #在列表尾部添加值
# lst.pop(0)#删除索引位置的值
# lst[0] # 取index=0的值
# lst[1:3] # 取index从0开始（不包括），到index=3的值
# print(lst)

# i=random.randrange(1,5)
# print(i)
#

class TestAPI:
    sess = session.requests

    # token=""
    # username=""
    @pytest.mark.parametrize("caseinfo", read_yaml_case("caseList/geToken.yaml"))
    def test_getToken(self, caseinfo):
        getToken_url = caseinfo["request"]["url"]
        method = caseinfo["request"]["method"]
        getToken_result = TestAPI.sess.request(method=method, url=getToken_url)
        write_yaml({"token": getToken_result.json()["token"]})
        # TestAPI.token=getToken_result.json()['token']
        # print(TestAPI.token)
        # value = re.search('"token":"(.+?)"', getToken_result.text)
        # Jianquan_token = value.group(1)

    @pytest.mark.parametrize("caseinfo", read_yaml_case("test_zhuce.yaml"))
    def test_zhuce(self, caseinfo):
        zhuce_Url = caseinfo["request"]["url"]

        i = random.randrange(1, 1000)

        TestAPI.username = "test{}".format(i)
        write_yaml({"username":TestAPI.username})
        methods = caseinfo["request"]["method"]
        data = {
            "username": read_yaml("username"),
            "pwd": caseinfo["request"]["params"]["pwd"],
            "nickname": caseinfo["request"]["params"]["nickname"],
            "describe": caseinfo["request"]["params"]["describe"]
        }
        headers = {
            "token": read_yaml("token")
        }
        zhuce_resule = TestAPI.sess.request(method=methods, url=zhuce_Url, data=data, headers=headers)
        print(zhuce_resule.text)
        print("注册的用户名为{}".format(caseinfo["request"]["params"]["username"]))
        print("密码为{}".format(caseinfo["request"]["params"]["pwd"]))

    def test_login(self):

        login_url = 'http://testingedu.com.cn:8081/inter/index.html'
        login_data = {
            "username": TestAPI.username,
            "pwd": "123456"
        }

        headers = {
            "token": read_yaml("token")
            # "Content-Type" : "application / javascript"

        }
        login_result = TestAPI.sess.request('post', url=login_url, data=login_data, headers=headers)

        print(login_result.text)
