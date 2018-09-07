from urllib import  request
from urllib import  error


if __name__=='__main__':
    url='http://www.csdn.net/'
    #req=request.Request(url)
    try:
        response=request.urlopen(url)
        html=response.read().decode('utf-8')
        print(html)
    except error.URLError as  e:
        print(e.reason)
