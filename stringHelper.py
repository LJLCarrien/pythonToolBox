
import json;

def makeJson(obj):
    """
    传入dic/list，生成json字符串
    """
    rstr = json.dumps(obj, indent=4)
    return rstr
