__author__ = 'xxp'

import random

proxy_list = [
    "124.206.133.227:80",
    "221.176.14.72:80",
    "120.195.201.16:80",
    "120.195.201.196:80",
    "117.136.234.8:80",
    "218.97.194.223:80",
    "124.88.67.22:80",
    "218.97.194.222:80",
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


def get_speed():
    global proxy_list
    ip_size = len(proxy_list)
    if ip_size == 0:
        return 2
    return 2/float(ip_size)


def get_ip_size():
    return len(proxy_list)