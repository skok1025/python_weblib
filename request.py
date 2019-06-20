from urllib.parse import urlencode
from urllib.request import urlopen, Request

httpResponse = urlopen('http://www.example.com')
body = httpResponse.read()

print(type(httpResponse))
print(body)

print("===================================")

# post
data ={
    'email':'skok10251@gmail.com',
    'password':'1234',
    'name':'김석현'
}

data = urlencode(data).encode('utf-8')
request = Request('http://www.example.com',data)
httpresponse = urlopen(request)

print(httpresponse.read())
