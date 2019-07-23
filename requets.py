import requests

payload = {'page':2, 'count':25}

# r = requests.get('https://httpbin.org/get',params=payload)
load = {'username':'corey','password':'text'}
r = requests.post('https://httpbin.org/post',params=load)

#Basic Authentivation
f = requests.get('https://httpbin.org/basic-auth/corey/testing',auth=('corey','testing'))

# print(r.url)
print(f.text)
# print(r.text)
#print(r.json())