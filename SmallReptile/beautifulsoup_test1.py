from urllib import request
from  bs4 import  BeautifulSoup

if __name__=="__main__":
    download_url='http://www.biqukan.com/1_1094/5403177.html'
    head={}
    head['User-Agent']='Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'
    download_req=request.Request(url=download_url,headers=head)
    download_response=request.urlopen(download_req)
    download_html=download_response.read().decode('gbk','ignore')

    soup_texts=BeautifulSoup(download_html,'lxml')
    texts=soup_texts.find_all(id='content',class_='showtxt')

    soup_texts=BeautifulSoup(str(texts),'lxml')
    #print(soup_texts.div.text.replace('\xa0',''))
    #beautifulsoup中，对外接口，只有string这个属性值
    #beautifulsoup内部才有text这个属性，只供内部使用 –> 如果你想要用text值，应该调用对应的get_text()
    print(soup_texts.div.get_text("\n","br/").replace("\xa0",""))

   #text是提取文本，string是提取标签的内容。你可以打印print(soup_text.div)看一下结果。
# div标签下还有很多br标签。所以使用string是提取不出来的，需要使用tex

    #print(soup_texts)
