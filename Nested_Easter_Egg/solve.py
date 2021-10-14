import base64
from codecs import encode
import requests

f = open("prerequisites/eastere.gg", "r")
lines = f.readlines()
f.close()
b64 = lines[11].strip()
print("Original : " + b64)
decoded = base64.b64decode(b64).decode()
print("Base 64 decoded : " + decoded)
done = encode(decoded, "rot13")
print("Final : " + done)
r = requests.get("http://127.0.0.1:3000" + done)
print("Status code : " + str(r.status_code))
