import execjs
import requests

def get_code(url):
    code = requests.get(url).text
    return code
def get_fas_trace_Id():
    trace_id = execjs.compile(get_code("https://raw.githubusercontent.com/Javer-Hff/SpidersRemote/main/js/tujia/utils.js")).call("w", 8)
    return trace_id;


















