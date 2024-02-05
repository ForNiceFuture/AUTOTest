import os
import yaml


# 写入可以清除的文档；追加
def write_yaml(data):
    with open("extract.yaml", encoding="utf-8", mode="a+") as file:
        yaml.dump(data, stream=file, allow_unicode=True)


# 写入：根据key覆盖数据
def write_yaml_by_key(data, key):
    with open("extract.yaml", "r") as file:
        existing_data = yaml.safe_load(file)

    if key in existing_data:
        existing_data[key] = data
    else:
        existing_data[key] = data

    with open("extract.yaml", "w") as file:
        yaml.safe_dump(existing_data, file)


# 写入无需清除的文档；追加
def write_yaml_Undelete(data):
    with open("undelete_extract.yaml", encoding="utf-8", mode="a+") as file:
        yaml.dump(data, stream=file, allow_unicode=True)


# 读取
def read_yaml(key):
    with open("extract.yaml", encoding="utf-8", mode="r") as file:
        value = yaml.load(file, yaml.FullLoader)
        return value[key]


# 读取无需清空的文档
def read_yaml_undelete(key):
    with open("undelete_extract.yaml", encoding="utf-8", mode="r") as file:
        value = yaml.load(file, yaml.FullLoader)
        return value[key]


# 清空
def clear_yaml():
    with open("extract.yaml", encoding="utf-8", mode="w") as file:
        file.truncate()


# 根据key清空
def clear_yaml_by_key(key):
    with open("extract.yaml", "r") as file:
        data = yaml.safe_load(file)
    if key in data:
        del data[key]
    with open("extract.yaml", "w") as file:
        yaml.safe_dump(data, file)


# 读取测试用例
def read_yaml_case(yamlpath):
    with open(os.getcwd() + "/" + yamlpath, encoding="utf-8", mode="r") as file:
        value = yaml.load(file, yaml.FullLoader)
        return value
