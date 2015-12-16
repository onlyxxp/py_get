import urllib

__author__ = 'xxp'


# !/usr/bin/env python
import urllib2
import time
from threading import Thread

success_result = []

class GetUrlThread(Thread):
    def __init__(self, word):
        self.code = word
        super(GetUrlThread, self).__init__()

    def run(self):
        value = {'reginvcode': self.code, "action": 'reginvcodeck'}
        value_encoded = urllib.urlencode(value)
        url = 'http://clsq.co/register.php'
        user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        headers = {'User-Agent': user_agent}

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
        print("response:" + resp_read)
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
    for code in list(code_list):
        t = GetUrlThread(code)
        threads.append(t)
        t.start()
        time.sleep(1)
    for t in threads:
        t.join()
    print "Elapsed time: %s" % (time.time() - start)
    print "^_^ : "
    print success_result