# !/usr/bin/env python
import threading

__author__ = 'xxp'
import random
import urllib
import urllib2
import time
from src import _ip_
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

max_retry_num = 6

success_result = []
bad_ip = []
http_failed_codes = []

success = False

mutex = threading.Lock()
current_thread_count = 0
max_thread_count = _ip_.get_ip_size()


class GetUrlThread(Thread):
    def __init__(self, word, index, url, ip_with_port):
        self.code = word
        self.index = index
        self.url = url
        self.ip_with_port = ip_with_port
        super(GetUrlThread, self).__init__()

    @staticmethod
    def thread_count_increase():
        global current_thread_count
        mutex.acquire(100)
        current_thread_count += 1
        mutex.release()

    @staticmethod
    def thread_count_decrease():
        global current_thread_count
        mutex.acquire(100)
        current_thread_count -= 1
        mutex.release()

    def build_request(self):
        ip_with_port = str(self.ip_with_port)
        url = str(self.url)

        value_encoded = urllib.urlencode(
            {
                'reginvcode': self.code,
                "action": 'reginvcodeck'
            }
        )
        global user_agents
        user_agent_ = user_agents[random.randint(0, len(user_agents) - 1)]
        headers = {
            'User-Agent': user_agent_
        }

        if ip_with_port.strip() != '':
            headers["X-Forwarded-for"] = ip_with_port.split(":")[0]
            proxy = urllib2.ProxyHandler({'http': ip_with_port})
            opener = urllib2.build_opener(proxy)
            urllib2.install_opener(opener)

        # print self.index, "==> ip=", ip_with_port,  "  url=", self.url
        req = urllib2.Request(url, data=value_encoded, headers=headers)
        return req, url

    def transact_http_result(self, resp, url):
        global success, success_result, bad_ip
        resp_read = str(resp)
        if len(str(resp_read).strip()) > 0:
            success = str(resp_read).find(r"retmsg_invcode('0');") > 0
            print self.index, "<==", self.ip_with_port, success, self.code, "   response: " + resp_read
        else:
            success = False
            self.append_to_bad_ip(self.ip_with_port)
            print self.index, "<==", self.ip_with_port, success, self.code, "   response is EMPTY ", self.ip_with_port
        if success:
            success_result.append(self.code)

    def append_to_bad_ip(self, ip_with_port):
        global bad_ip
        _ip_.remove_bad_ip(ip_with_port)
        if ip_with_port not in bad_ip:
            bad_ip.append(ip_with_port)

    def run(self):
        self.thread_count_increase()
        global max_retry_num, http_failed_codes, bad_ip, success_result, success
        req, url = self.build_request()
        for i in range(max_retry_num):
            try:
                resp = urllib2.urlopen(req, timeout=5).read()
                self.transact_http_result(resp, url)
                break
            except:
                if not success and (i < max_retry_num - 1):
                    print 'URLError: retry later ...', self.ip_with_port
                    time.sleep(2)
                    continue
                else:
                    self.append_to_bad_ip(self.ip_with_port)
                    http_failed_codes.append(self.code)
                    print 'URLError: <urlopen error timed out> All times is failed ', self.ip_with_port
        self.thread_count_decrease()


def get_responses(code_list, url):
    global success, success_result, http_failed_codes, bad_ip, current_thread_count, max_thread_count
    start = time.time()
    threads = []

    index = 1
    for code in list(code_list):
        t = GetUrlThread(code, index, url, _ip_.get_ip_with_port())
        threads.append(t)
        t.start()
        index += 1
        if success:
            print 'skip because success'
            break
        while current_thread_count >= max_thread_count:
            time.sleep(_ip_.get_speed())

    for t in threads:
        t.join()

    print "================================================"
    print "bad ip is ", bad_ip
    print "http error code size ", len(http_failed_codes)
    print "Elapsed time: %s" % (time.time() - start)
    print "^_^ : "
    print "code is ", success_result
    print "================================================"

    if len(http_failed_codes) > 0:
        time.sleep(2)
        get_responses(http_failed_codes, url)
