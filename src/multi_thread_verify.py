import random
import urllib

__author__ = 'xxp'


# !/usr/bin/env python
import urllib2
import time
from threading import Thread

user_agents = [
    "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0) ",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.2) ",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)",
    "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT 6.0)",
    "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT 5.2)",
    "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT 5.1)",
]

proxys = [
    "124.206.133.227:80",
    "118.244.151.157:3128",
    # "114.41.143.186:3128",
    # "221.228.248.244:8085",
    # "101.81.67.13:9797",
    # "116.1.233.53:8080",
    # "58.67.159.50:80",
    # "183.5.199.62:9797",
    # "183.135.152.61:9999",
    # "218.75.26.44:808"
]

success_result = []

class GetUrlThread(Thread):
    def __init__(self, word):
        self.code = word
        super(GetUrlThread, self).__init__()

    def run(self):
        proxy_index = random.randint(0, len(proxys) - 1)
        ip = proxys[proxy_index]

        value = {'reginvcode': self.code, "action": 'reginvcodeck'}
        value_encoded = urllib.urlencode(value)
        url = 'http://clsq.co/register.php'
        # user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        user_agent_ = user_agents[random.randint(0, len(user_agents) - 1)]
        headers = {
            'User-Agent': user_agent_,
            # "X-Forwarded-for": ip
        }

        print(ip + " " + user_agent_ + "  -->")

        proxy = urllib2.ProxyHandler({'http': ip})
        opener = urllib2.build_opener(proxy)
        urllib2.install_opener(opener)

        req = urllib2.Request(url, data=value_encoded, headers=headers)
        resp = urllib2.urlopen(req, timeout=10)

        # retry
        if resp.getcode() != 200:
            time.sleep(1)
            resp = urllib2.Request(url, data=value_encoded, headers=headers)
        if resp.getcode() != 200:
            time.sleep(1)
            resp = urllib2.Request(url, data=value_encoded, headers=headers)
        if resp.getcode() != 200:
            time.sleep(1)
            resp = urllib2.Request(url, data=value_encoded, headers=headers)

        resp_read = resp.read()
        print("     response: " + resp_read)
        if len(str(resp_read).strip()) > 0:
            success = str(resp_read).find("parent.retmsg_invcode('1');") < 0
        else:
            success = False
        if success:
            success_result.append(self.code)

        print url, success, self.code


def get_responses(code_list):
    start = time.time()
    threads = []
    i = 1
    default_ip = "21.23.44."

    for code in list(code_list):
        t = GetUrlThread(code)
        threads.append(t)
        t.start()
        time.sleep(1)
        i += 1
    for t in threads:
        t.join()
    print "Elapsed time: %s" % (time.time() - start)
    print "^_^ : "
    print success_result