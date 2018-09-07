from urllib.request import urlretrieve

from bs4 import  BeautifulSoup
import  requests
import  os
if __name__ == '__main__':
    target_url='http://www.shuaia.net/zhengtai/2018-07-17/15016.html'
    filename='正太'+'.jpg'
    headers={

        "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
    }
    img_req = requests.get(url = target_url,headers = headers)
    img_req.encoding = 'utf-8'
    img_html = img_req.text
    img_bf_1 = BeautifulSoup(img_html, 'lxml')
    img_url = img_bf_1.find_all('div', class_='wr-single-content-list')
    print(img_url)
    img_bf_2 = BeautifulSoup(str(img_url), 'lxml')
    img_url = 'http://www.shuaia.net' + img_bf_2.div.img.get('src')
    if 'images' not in os.listdir():
        os.makedirs('images')
    urlretrieve(url = img_url,filename = 'images/' + filename)
    print('下载完成！')
