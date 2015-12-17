# !/usr/bin/env python
__author__ = 'xxp'
import random
import urllib
import urllib2
import time
from src import _url_
from threading import Thread

user_agents = [
    "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0) ",
    "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2) ",
    "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1) ",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0) ",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.2) ",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1) ",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 6.0)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.2)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)",
    "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT 6.0)",
    "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT 5.2)",
    "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT 5.1)",
]

proxys = [
    "54.86.216.36:3128",
    # "118.244.151.157:3128",
    # "183.135.152.61:9999",
    # "218.75.26.44:808"
]

max_retry_num = 6

success_result = []

# user_proxy = True
user_proxy = False

success = False

class GetUrlThread(Thread):
    def __init__(self, word, index, url):
        self.code = word
        self.index = index
        self.url = url
        super(GetUrlThread, self).__init__()

    def build_request(self):
        proxy_index = random.randint(0, len(proxys) - 1)
        ip = proxys[proxy_index]
        value = {'reginvcode': self.code, "action": 'reginvcodeck'}
        value_encoded = urllib.urlencode(value)
        user_agent_ = user_agents[random.randint(0, len(user_agents) - 1)]
        headers = {
            'User-Agent': user_agent_,
            "X-Forwarded-for": ip.split(":")[0]
        }
        print self.index, "==>", ip,  " ", self.url

        if user_proxy:
            proxy = urllib2.ProxyHandler({'http': ip})
            opener = urllib2.build_opener(proxy)
            urllib2.install_opener(opener)

        req = urllib2.Request(self.url, data=value_encoded, headers=headers)
        return req, self.url

    def transact_success_result(self, resp, url):
        resp_read = str(resp)
        if len(str(resp_read).strip()) > 0:
            success = str(resp_read).find("parent.retmsg_invcode('1');") < 0
            print self.index, "<==", url, success, self.code, "   response: " + resp_read
        else:
            success = False
            print self.index, "<==", url, success, self.code, "   response is EMPTY "
        if success:
            success_result.append(self.code)

    def run(self):
        req, url = self.build_request()
        for i in range(max_retry_num):
            try:
                resp = urllib2.urlopen(req, timeout=5).read()
                self.transact_success_result(resp, url)
                break
            except:
                if i < max_retry_num - 1:
                    print 'URLError: retry later ...'
                    time.sleep(5)
                    continue
                else:
                    print 'URLError: <urlopen error timed out> All times is failed '


def get_responses(code_list):
    start = time.time()
    threads = []
    index = 1

    for code in list(code_list):
        t = GetUrlThread(code, index, _url_.get_url())
        threads.append(t)
        t.start()
        index += 1

        time.sleep(1)

        if success:
            print 'skip because success'
            break

    for t in threads:
        t.join()

    print "Elapsed time: %s" % (time.time() - start)
    print "^_^ : "
    print success_result