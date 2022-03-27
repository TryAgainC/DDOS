import requests
import random
import time
import threading

def regist():
    url = "https://72vpn.xyz/api/v1/passport/auth/register"
    qq_num = random.randint(1,9999999999)

    qq_email = "%d@qq.com" % qq_num

    qq_password = random.randint(1,999999999999)

    data = {
        "email": qq_email,
        "password": qq_password,
        'invite_code': 'xiaoxin'
    }

    r = requests.post(url=url,data=data)
    print(qq_email,qq_password,r)


while(True):
    t1 = threading.Thread(target=regist())
    t1.start()






