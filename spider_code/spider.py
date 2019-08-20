
import requests
import datetime
# from bs4 import BeautifulSoup


class Crawler(object):
    """
    抓取上海期货交易数据，单个网页，网页使用Ajex异步加载
    """
    def __init__(self, url, **kwargs):
        """
        :param url:
        :param kwargs:
            headers:请求头，建议使用
            date:获取某日的交易数据 例如2019-7-28
        """
        self.__result = None
        self.url = url
        self.headers = None if 'headers' not in kwargs.keys() else kwargs['headers']
        self.date = datetime.datetime.now().date() if 'date' not in kwargs.keys() else kwargs['date']
        self.sleep = False
        self.result = None

    def start(self):
        # 发送请求
        self.__result = requests.get(self.url, headers=self.headers)
        if self.__result.status_code == 200:
            print('数据%s获取成功' % self.url)
            try:
                self.result = self.__result
            except Exception as e:
                print(e)
        else:
            print(self.__result.reason)

    def date_analyse(self):
        """获得格式化的数据，再本任务中获取字典形式的数据"""
        pass

    def to_database(self):
        pass


def main():
    request_url = 'http://www.shfe.com.cn/data/dailydata/kx/pm20190725.dat'
    headers = {
        'Referer': 'http://www.shfe.com.cn/statements/dataview.html?paramid=kx',
        'If-Modified-Since': '0',
        'Cookie': 'shfe_cookid=190318204720166e4722ce67d4b67dcebbe3a7d26600; shfe_fbl=1366*768',
        'Connection': 'Connection',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:67.0) Gecko/20100101 Firefox/67.0',
        'Accept': '*/*'
    }
    result = requests.get(request_url, headers=headers)
    # print(result.headers)
    # print(result.content.decode('utf-8'))
    with open('../result/数据.txt', 'w', encoding='utf-8') as f:
        f.write(result.content.decode('utf-8'))
    # print(type(result))  # <class 'requests.models.Response'>
    result = result.json()['o_cursor']
    print(len(result))
    result_list = []

    for item in result:
        print(item)


if __name__ == '__main__':
    # main()
    # print(datetime.datetime.now().date())
    pass