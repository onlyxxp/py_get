__author__ = 'xxp'

file_name = "../url.txt"

url = ""

def get_url():
    global url

    if len(url) > 0:
        return url

    file_object = open(file_name, 'r', buffering=-1)
    url = file_object.read()
    print "config url = ", url
    print ""
    file_object.close()

    return url

get_url()
