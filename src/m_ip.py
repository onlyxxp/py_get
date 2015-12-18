__author__ = 'xxp'

import random

proxy_list = [
    # "127.0.0.1:16808",
    # "120.52.73.39:8080",
    # "120.52.73.37:8080",
    # "124.88.67.22:81",
    # "187.254.216.157:8080",
    # "222.39.112.12:8118",
    # "113.255.129.42:80",
    # "117.136.234.8:80",
    # "218.97.194.223:80",
    # "222.45.85.210:8118",
    # "218.97.194.222:80",
]

def get_ip_with_port():
    global proxy_list

    if len(proxy_list) <= 0:
        print "All ip is bad !!!!!!!!!!!!!!"
        return ''

    proxy_index = random.randint(0, len(proxy_list) - 1)
    ip = proxy_list[proxy_index]
    return ip


def remove_bad_ip(ip_with_port):
    global proxy_list
    print "remove bad ip XXXXX ", ip_with_port
    if ip_with_port in proxy_list:
        proxy_list.remove(ip_with_port)


def get_ip_size():
    return len(proxy_list)