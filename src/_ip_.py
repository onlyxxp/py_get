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
    proxy_index = random.randint(0, len(proxy_list) - 1)
    ip = proxy_list[proxy_index]
    return ip

def get_speed():
    global proxy_list
    return 1/float(len(proxy_list))
