__author__ = 'xxp'

file_name = "../url.txt"


def get_url():
    file_object = open(file_name, 'r', buffering=-1)
    url = file_object.read()
    print "config url = ", url
    print ""
    file_object.close()
    return url

# get_url()
