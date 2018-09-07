
import requests
import  json

if __name__=='__main__':

    req_url='http://fanyi.baidu.com/transapi'
    Frm_Data={"query": 'love','from':'en','to':'zh'}
    translate_result = requests.post(req_url,Frm_Data)
    result=translate_result.json()
    print(result['data'][0]['dst'])

    print(requests.post('http://fanyi.baidu.com/transapi',data={"query": 'love','from':'en','to':'de'}).json()['data'][0]['dst'])
