

import requests

url = 'https://www.toutiao.com/api/search/content/?aid=24&app_name=web_search&offset=80&format=json&keyword=%E8%A1%97%E6%8B%8D&autoload=true&count=20&en_qc=1&cur_tab=1&from=search_tab&pd=synthesis&timestamp=1562944068510'
headers = {
    'authority' : 'www.toutiao.com',
    'method': 'GET',
    'path': '/api/search/content/?aid=24&app_name=web_search&offset=80&format=json&keyword=%E8%A1%97%E6%8B%8D&autoload=true&count=20&en_qc=1&cur_tab=1&from=search_tab&pd=synthesis&timestamp=1562944068510',
    'scheme': 'https',
    'accept': 'application/json, text/javascript',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'content-type': 'application/x-www-form-urlencoded',
    'cookie': 'tt_webid=6712790477987841540; WEATHER_CITY=%E5%8C%97%E4%BA%AC; tt_webid=6712790477987841540; UM_distinctid=16be6aedc057d-0cc1af96ea765e-e343166-100200-16be6aedc0618f; CNZZDATA1259612802=2047935419-1562942487-%7C1562942487; __tasessionId=6ltd9tuww1562943348343; csrftoken=256f978a59e2b3fae772f6d866f04fa0; s_v_web_id=771ca7f7375ba6d59172cd03eff783f0',
    'referer': 'https://www.toutiao.com/search/?keyword=%E8%A1%97%E6%8B%8D',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest'
}
proxies = {
    'https': '124.160.56.76:59713',

}
result = requests.get(url, headers=headers, proxies=proxies)
print(result.status_code)
print(dir(result))
print(result.connection)
if result.status_code == 200:
    with open('头条图片.txt', 'w', encoding='utf-8') as f:
        f.write(result.text)
