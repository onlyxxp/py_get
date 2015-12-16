__author__ = 'xxp'

import urllib
import urllib2


def verify_code(code):
    value = {'reginvcode': code, "action": 'reginvcodeck'}
    value_encoded = urllib.urlencode(value)
    url = 'http://clsq.co/register.php'
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    headers = { 'User-Agent' : user_agent }

    req = urllib2.Request(url, data=value_encoded, headers=headers)

    response = urllib2.urlopen(req, timeout=10)
    response_data = response.read()
    print(code)
    print(response_data)

    return True

def installProxy():
    proxy_handler = urllib2.ProxyHandler({"http": 'http://127.0.0.1:1080'})
    opener = urllib2.build_opener(proxy_handler)
    urllib2.install_opener(opener)