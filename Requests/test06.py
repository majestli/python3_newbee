#requests
import requests
data={
    "name":"zhaofan",
    "age":23
}

response = requests.post("http://httpbin.org/post",data=data)
#print(response.text)
print(type(response.status_code),response.status_code)
print(type(response.headers),response.headers)
print(type(response.cookies),response.cookies)
print(type(response.url),response.url)
print(type(response.history),response.history)

