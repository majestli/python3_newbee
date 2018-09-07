from  urllib import  request
from  bs4 import  BeautifulSoup


if __name__=="__main__":
    target_url="http://www.biqukan.com/1_1094/"
    head={}
    head['User-Agent']='Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'
    target_req=request.Request(url=target_url,headers=head)
    target_reponse=request.urlopen(target_req)
    target_html=target_reponse.read().decode('gbk','ignore')

    listmain_soup=BeautifulSoup(target_html,'lxml')

    chapters=listmain_soup.find_all('div',class_='listmain')  #如果传入 class 参数,Beautiful Soup 会搜索每个 class 属性为 title 的 tag 。kwargs 接收字符串

    dowmload_soup=BeautifulSoup(str(chapters),'lxml')
    begin_flag=False
    for child in dowmload_soup.dl.children: ## 它返回的不是一个 list，不过我们可以通过遍历获取所有子节点，它是一个 list 生成器对象
        if child !='\n':
            if child.string ==u"《一念永恒》正文卷":
                begin_flag=True
            if begin_flag == True and child.a !=None:
                dowmload_url="http://www.biqukan.com"+child.a.get('href')
                download_name=child.string
                print(download_name+":"+dowmload_url)
