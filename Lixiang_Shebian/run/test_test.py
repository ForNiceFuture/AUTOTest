import json
import os
import random
import string

import pytest
import requests
import yaml
from _pytest.skipping import Skip

from Lixiang_Shebian.util.yaml_util import write_yaml, read_yaml_case, read_yaml, clear_yaml, clear_yaml_by_key, \
    write_yaml_by_key


class Test:

    def test_demo(self):
        url = 'https://vrdos-workbench-soa-api.ptest.k8s.chehejia.com/api/v1/soa-service/transform-detail/1405/9665'
        header = {
            'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6IjFOY25YbiJ9.eyJqdGkiOiIwVXdDSVV5VWJ3ZXZpYnNJQm5sTnBBIiwiYXVkIjoiNG5PeWUyNHR6U3pJamNjeW96SlY2NSIsImlhdCI6MTcwNjU4MTgyNSwibmJmIjoxNzA2NTgxODI1LCJleHAiOjE3OTI5ODE4MjUsImNsaSI6IjRSVmdnb014VWp6eUhxSnpCRFlSMHIiLCJpc3MiOiJodHRwczovL2lkLW9udGVzdC5saXhpYW5nLmNvbS9hcGkvZGlzY292LzRSVmdnb014VWp6eUhxSnpCRFlSMHIiLCJzY29wZXMiOlsid29ya2JlbmNoLXNvYTpkZW1vIl0sInNpZCI6IjdoOHVFdk9JaGtXdlljako1NWd1SUJ5N204VyIsInN1YiI6ImV5SmhiR2NpT2lKa2FYSWlMQ0psYm1NaU9pSkJNVEk0UTBKRExVaFRNalUySWl3aWEybGtJam9pZDJOV1owVWlmUS4uNlpqdndYeWNtTEtSc2lCdVprQjhqZy5rYTgtMGlmaEFxaC1aRnlhNU1COUlCQkV0d2NYd01UNkJ1c3NGYTRMLW1leGY4cEM5UzZFVEZ5V3ZKU3dMaXBoSG9ueFE0MEoyWW1IZHF5d1k1T1JKWjZQMFFqZldTZ3Ruek11Q3VKLU40QjVLMEVKZG9OaGo3SGptcHVWUWdRaGdEeTdaWHVpUWZWYkZERUI2SkxlWWZPcWdFN0o3Nlh3YVMwWE11RGkxSG5OcUFMazRUQ1R0WEgwNGFCaldyaktIUFd0ZmJESDZQeGtaZnFhOUZyU3VfZk81Ylo5ZFc2QlNjN0x0SjJFMnpubXlpSVFHclBvRlNPNkxuSVRmRXVMbVpvSWNETGo4SXVLWF8wUy1WaXhLbUx3SVVxZ2xrQjFycDVJYl9LdC1CYy5lT3FkNkNmaDZmczEtbXdFWVFESlZBIn0.BclupyLFPDuBB9Yya4t5OGxvOI9smvZFisMpbZzCQGn1P3yUsSDHOGsrXC0berwW9n78xHPQl5FpBzxaAjudOb8khvd0QfE7ZWNmvkaF6foxP7-27emyyZhQZj3XzGSA1HZgWkqy8WcW9h03aVP0BSiOJoEozqvqxcvli1uRayzbyJQp3kcFqPqpd51pa_nVE2eTfCAcNEQf5fkhzbgQIR3_aJCPnAUkYwN9DRril-zZ5ceAjh_zr528UE7aLjj75_scd-X51KGjoiWfs_ygoXrUS4gLuM6PbKsVGxIsEm4FsPA7GSW_8wBGw0PBNBMIuvaSjHmIMlAGZoGgMO509w'}
        response = requests.request(method='get', url=url, headers=header)
        assert response.status_code == 200
        assert response.json()['msg'] == 'SUCCESS'
        print(response.json())
        Test.id = response.json()['data']['id']
        clear_yaml_by_key("id")
        write_yaml({"id": Test.id})
        print('请求url：' + url)
        write_yaml({"url": url})

    @Skip
    def test_demo2(self):
        url = 'https://id-ontest.lixiang.com/api/token'
        header = {'content-type': 'application/json'}
        params = {"client_id": "6zwubonpCJhILjAt5QhlXo", "grant_type": "authorization_code",
                  "code": "BJ.34vRY1rNWcqzuFJNIB4RSu", "code_verifier": "8skn22y4QrfwcgCL~CD4O3xyp0RGXvwAOGZWymJaZm-"}
        Result = requests.request(method='POST', url=url, headers=header, json=params)

        Test.token_type = Result.json()['4bLxNxl5BiVlLMck51wtiR']['token_type']
        Test.access_token = Result.json()['4bLxNxl5BiVlLMck51wtiR']['access_token']
        # assert Result.json()['4bLxNxl5BiVlLMck51wtiR']['token_type'] == 'Bearer'
        # assert Result.status_code == 200
        Test.newToken = Test.token_type + ' ' + Test.access_token
        print(Test.newToken)

    # @pytest.mark.parametrize("caseinfo", read_yaml("extract.yaml"))
    # def test_demo3(self):

    # clear_yaml()
    #
    # json_str = '{"name": "John", "age": 1000, "city": "New York"}'
    #
    # # 将字符串类型转换为JSON类型
    # json_data = json.loads(json_str)

    # print('.....................')
    # json_json = {"name": "John", "age": 30, "city": "New York"}
    # # 将JSON类型转换为字符串类型
    # string_data = json.dumps(json_json)
    # carId = read_yaml("data")
    # print("车型id：{}".format(carId))
    # clear_yaml_by_key("data")


def Moon():
    # path = os.getcwd()
    # print(path)
    # i = list("ASDFGHJKLTYUIOPVBNMGHJK")
    # e = random.choice(i)
    # print(e)
    # 生成一个包含所有英文字母的列表
    letters = list(string.ascii_letters)

    # 随机选择五个字母
    random_letters = random.sample(letters, 5)
    # 打印这五个字母
    print(random_letters)


if __name__ == '__main__':
    # 解析测试配置文件并运行测试用例
    pytest.main(['-vs', 'test_test'])


