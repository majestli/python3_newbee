import urllib.request
import  chardet

if __name__ == "__main__":

    response =urllib.request.urlopen("http://fanyi.baidu.com")
    html = response.read()
    charset=chardet.detect(html)
    print(charset)
    html=html.decode("utf-8")
    #html=html.decoe(charset)
    print(html)
