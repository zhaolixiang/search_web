import requests
from tools.push_tools import PushTool
from urllib import parse

success_code = 0
fail_code = 0
server = PushTool.https_target()
cookie = PushTool.get_cookies()


def https_push(domain):
    global success_code
    global fail_code
    url = ''
    while True:
        try:
            r = PushTool.rand_all(domain)
            i = PushTool.rand_all(domain)
            headers = {
                'User-Agent': PushTool.user_agent(),
                'Referer': r,
                'Accept': '*/*',
                'Connection': 'keep-alive',
                'Host':'sp0.baidu.com',
            }
            conn = requests.Session()
            conn.headers = headers
            # print(headers)
            # 将cookiesJar赋值给会话
            cookiesJar = requests.utils.cookiejar_from_dict(cookie, cookiejar=None, overwrite=True)
            conn.cookies = cookiesJar
            target = '%s?r=%s&l=%s' % (server, r, i)
            # http = requests.get(target, headers=headers)
            http = conn.get(target)
            url = parse.unquote(http.url)
            if http.content == b'' and http.status_code == 200:
                success_code += 1
                print('成功 %s 失败 %s %s' % (success_code, fail_code, url))
            else:
                fail_code += 1
                print('成功 %s 失败 %s %s' % (success_code, fail_code, url))
        except:
            fail_code += 1
            print('成功 %s 失败 %s %s' % (success_code, fail_code, url))
