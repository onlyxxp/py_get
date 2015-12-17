__author__ = 'xxp'


def test():
    re = "response: <script language=parent.retmsg_invcode('1');</script>"
    print "result", re.find(r"retmsg_invcode('1')")

test()