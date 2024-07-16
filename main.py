import sys

import execjs
import requests


class SpidersRemote:
    def __init__(self):
        pass

    def get_code(slef, url):
        code = requests.get(url).text
        return code

    def get_fas_trace_id(self):
        trace_id = execjs.compile(
            self.get_code("https://raw.githubusercontent.com/Javer-Hff/SpidersRemote/main/js/tujia/utils.js")).call("w",8)
        return trace_id


function_map = {
    "getFasTraceId": SpidersRemote().get_fas_trace_id
}

if __name__ == '__main__':
    function_name = sys.argv[1]
    print(function_map[function_name]())
