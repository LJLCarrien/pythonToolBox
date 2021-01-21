
import json;


def makeJson(obj):
    """
    传入dic/list，生成json字符串
    """
    rstr = json.dumps(obj, indent=4)
    return rstr


def readJsonFile(jsonFileFullPath):
    """
    加载python json格式文件
    """
    with open(jsonFileFullPath, 'rb')as f:
        data = json.load(f)
        # print(data)
        # print(type(data))
    return data


def jsonStr2Json(jsonStr):
    """
    将json格式的字符串转为python数据类型的对象
    """
    jsonData = json.loads(jsonStr)
    # print(jsonData)
    # print(type(jsonData))
    return jsonData
