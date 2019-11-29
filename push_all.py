from threadpool import ThreadPool, makeRequests
from configparser import ConfigParser


config = ConfigParser()
config.read('push_config.ini', 'utf-8')
https = int(config.get('bd_push', 'https'))
thread_num = int(config.get('bd_push', 'thread'))
# targets = config.get('bd_push', 'target').split(',')
targets=[]
with open('urls.txt') as f:
    for y in f.readlines():
        targets.append(y.strip())
if https == 1:
    from mylib.https_push import https_push

    pool = ThreadPool(len(targets))
    arg = targets
    # for x in range(0, thread_num):
    #     arg.append(targets)
    # print("-2-2-",arg)
    request = makeRequests(https_push, arg)
    [pool.putRequest(req) for req in request]
    pool.wait()
elif https == 0:
    from mylib.push_without_proxy import push_url_two

    # pool = ThreadPool(thread_num)
    pool = ThreadPool(len(targets))
    arg = targets
    # for x in range(0, thread_num):
    #     arg.append(targets)
    # print("-3-3-", arg)
    request = makeRequests(push_url_two, arg)
    [pool.putRequest(req) for req in request]
    pool.wait()


