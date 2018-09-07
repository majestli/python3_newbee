from  urllib import  request
from urllib import error
if __name__ == "__main__":
    # websize
    url="http://www.whatismyip.com.tw/"
    #my daili
    proxy={'http':'106.46.136.112:808'}
    # create ProxyHandler
    proxy_support=request.ProxyHandler(proxy)
    # create opener
    opener =request.build_opener(proxy_support)
    # add user angent
    opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36')]
    # install angent
    request.install_opener(opener)
    #user opener
    try:
        response=request.urlopen(url)
        html=response.read().decode('utf-8')
    except error.HTTPError as e:
        print(e.code)
    except error.URLError as  e:
        print(e.reason)
    else:
        print(html)
