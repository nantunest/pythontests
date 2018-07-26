import string
import random
import urllib.request

population = string.ascii_lowercase + string.ascii_uppercase + string.digits


while(True):

    rand_url = "".join([random.choice(population) for i in range(6)])
    url = "https://goo.gl/" + rand_url

#    print(url)

    try:
        content = urllib.request.urlopen(url)
        print("something here " + url)
    except:
        pass
