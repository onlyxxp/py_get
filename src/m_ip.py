__author__ = 'xxp'

import random

proxy_list = [
    # "52.32.242.236:3128",
    # "142.4.200.240.136:3129",
    # "173.39.116.254:80",
    # "182.92.155.193:80",
    # "203.195.162.96:80",
    # "119.188.115.26:80",
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
    return max(len(proxy_list), 1)