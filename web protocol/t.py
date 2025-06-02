import requests,os,time
while True:
    if (requests.get("https://mohalaxy.pythonanywhere.com/").text)=="no":
        os.system("shutdown -i 0 -t 0")
    time.sleep(500)