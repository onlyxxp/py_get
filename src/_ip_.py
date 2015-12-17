__author__ = 'xxp'

import random

proxys = [
    "124.88.67.22:83",
]

def get_ip_with_port():
    proxy_index = random.randint(0, len(proxys) - 1)
    ip = proxys[proxy_index]
    return ip