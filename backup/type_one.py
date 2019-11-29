from mylib.push_without_proxy import push_url_one
from threadpool import ThreadPool, makeRequests

if __name__ == '__main__':
    pool = ThreadPool(32)
    arg = []
    for x in range(0, 32):
        arg.append('http://www.aidshe.com')
    request = makeRequests(push_url_one, arg)
    [pool.putRequest(req) for req in request]
    pool.wait()
