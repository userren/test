import json

headers = {
'Accept': '*/*',
'Accept-Encoding': 'gzip, deflate',
'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
'Cache-Control': 'max-age=0',
'Connection': 'keep-alive',
'Cookie': 'shfe_cookid=1907272052020e36d66da8cedd51e70dcd8decb22a02; shfe_fbl=1366*768',
'Host': 'www.shfe.com.cn',
'If-Modified-Since': '0',
'Referer': 'http://www.shfe.com.cn/statements/dataview.html?paramid=kx',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'
}


def to_json(data: dict, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f)


def to_py(filename):
    with open(filename, 'r') as f:
        data = json.load(f)
    return data


if __name__ == '__main__':
    # to_json(headers, 'headers.json')
    pass
