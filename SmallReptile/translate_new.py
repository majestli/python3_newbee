from urllib import request, parse
import json

if __name__ == '__main__':
    req_url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'  # 创建连接接口
    # 创建要提交的数据
    Form_Date = {}
    Form_Date['i'] = 'i love you'
    Form_Date['doctype'] = 'json'
    Form_Date['form'] = 'AUTO'
    Form_Date['to'] = 'AUTO'
    Form_Date['smartresult'] = 'dict'
    Form_Date['client'] = 'fanyideskweb'
    Form_Date['salt'] = '1526995097962'
    Form_Date['sign'] = '8e4c4765b52229e1f3ad2e633af89c76'
    Form_Date['version'] = '2.1'
    Form_Date['keyform'] = 'fanyi.web'
    Form_Date['action'] = 'FY_BY_REALTIME'
    Form_Date['typoResult'] = 'false'
    data = parse.urlencode(Form_Date).encode('utf-8')  # 数据转换
    response = request.urlopen(req_url, data)  # 提交数据并解析
    html = response.read().decode('utf-8')  # 服务器返回结果读取
    print(html)
    # 可以看出html是一个json格式
    translate_results = json.loads(html)  # 以json格式载入,解码
    translate_results = translate_results['translateResult'][0][0]['tgt']  # json格式调取
    print(translate_results)  # 输出结果
