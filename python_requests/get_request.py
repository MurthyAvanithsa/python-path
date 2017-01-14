from requests import get

payload = {"q":"python"}
res = get("http://google.com", params=payload)

print res.content