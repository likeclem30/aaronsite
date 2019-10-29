import time
from datetime import datetime as dt

hosts_temp = "/Users/Williams/codes/python/webBlocker/hosts"
hosts_path = "/private/etc/hosts"
redirect = "127.0.0.1"

websites_list = ["www.facebook.com","facebook.com","dub119.mail.live.com","www.dub119.mail.live.com"]

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,8) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,16):
        
        with open(hosts_path,"r+") as file:
            content = file.read()
            ##print(content)
            for website in websites_list:
                if website in content:
                    pass
                else:
                    file.write(redirect+" "+website+"\n")

        print("Working hours")
    else:
        with open(hosts_path,'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in websites_list):
                    file.write(line)
            file.truncate()

        print("not working hours. it fun hours")
    time.sleep(5)