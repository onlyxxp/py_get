__author__ = 'xxp'

import random

proxy_list = [
    "124.88.67.22:83",
    "124.88.67.77:80",
    "119.6.136.122:80",
    "118.114.77.47:8080",
    "124.88.67.22:82",
    "115.159.5.247:8080",
    "222.45.85.53:8118",
    "120.198.231.22:8081",
    "140.207.100.114:8080",
    "119.188.115.27:8080",
    "115.159.5.247:8080"
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
