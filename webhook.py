import requests
from tokenwebhook import tokensncf
r = requests.post(tokensncf, json={'content':str(input())})
print(r.status_code, r.reason)