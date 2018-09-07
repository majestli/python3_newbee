import requests

data ={

    "name":"zhanfan",
    "age":22
}
response = requests.get("http://httpbin.org/get",params=data)
print(response.url)
print(response.text)
print(response.content.decode("utf-8"))

