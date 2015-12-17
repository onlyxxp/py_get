__author__ = 'xxp'

import random

proxys = [
    "124.88.67.22:83",
]

def get_ip_with_port():
    lenth = len(proxys)

    if lenth <= 0:
        return ''

    proxy_index = random.randint(0, lenth - 1)
    ip = proxys[proxy_index]
    return ip