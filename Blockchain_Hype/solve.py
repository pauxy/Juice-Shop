import requests

p = 12027524255478748885956220793734512128733387803682075433653899983955179850988797899869146900809131611153346817050832096022160146366346391812470987105415233
q = 12131072439211271897323671531612440428472427633701410925634549312301964373042085619324197365322416866541017057361365214171711713797974299334871062829803541
e = 65537
phi = (p - 1) * (q - 1)

print("Breaking RSA key ...")
d = pow(e, -1, phi)
f = open("prerequisites/announcement_encrypted.md", "r")
lines = f.readlines()
sentence = ""
print("Decoding announcemment_encrypted.md ...")
for line in lines:
    c = int(line)
    m = pow(c, d, p * q)
    sentence += chr(m)
print("File contents :")
print(sentence)
url = sentence.split("URL: ")
r = requests.get("http://127.0.0.1:3000" + url[1])
print("\nStatus: " + str(r.status_code))
