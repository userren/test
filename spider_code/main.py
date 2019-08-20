import spider
import toMySql.mysql_engine
import time
import datetime
import parameters.Py_Json
import re


class Main(object):

    def __init__(self, exchange='SHFE', date=datetime.datetime.now().date()):
        self.exchange = exchange
        self.date = date
        self.url_date = re.sub("[^0-9]", '', str(self.date))
        self.db_obj = toMySql.mysql_engine.MySql(user='root', password="root1",
                                                 database='futuretradedata')
        self.headers = parameters.Py_Json.to_py('../parameters/headers.json')

        self.url = self.get_url()
        print(self.url)
        if self.url:
            self.crawler_obj = spider.Crawler(self.url, headers=self.headers)

    def get_url(self):
        self.db_obj.connect(charset='utf8')
        try:
            sql = "select data_website from crawlerwebsite where exchange='%s'" % self.exchange
            data = self.db_obj.execute(sql, fetch='fetchone')()[0]
            if data:
                data = re.sub(r'pmXXXXXXXX', 'pm%s' % self.url_date, data)
                return data
            else:
                return None
        except Exception as e:
            print(e)
            self.db_obj.close()
        finally:
            self.db_obj.close()


exe = Main(date='2017-06-08')
exe.crawler_obj.start()
# print(exe.crawler_obj.result.content.decode('utf-8'))
try:
    json_result = exe.crawler_obj.result.json()
    if 'o_msg' in json_result.keys() and json_result['o_msg'] == '成交、持仓排名查询成功':
        print('数据获取成功')

        toMySql_list = []
        toMySqlTable_list = []
        sql_list = []
        lastINSTRUMENTID = '123'
        # totoMySql_list = ['日期','rank排名','最左边期货公司名字','成交量','成交量变化',
        # '中间期货公司','持多单量','多单变化','右边期货公司','持空单量','空单变化']
        for item in json_result['o_cursor']:
            if item['INSTRUMENTID'] != lastINSTRUMENTID:
                toMySqlTable_list.append('''create table if not exists %s(\
id int not null auto_increment,\
tradedate date not null,\
rank int not null,\
futurecompany1 varchar(255) not null,\
cj1 int ,\
cj1_cg int,\
futurecompany2 varchar(255) not null,\
cj2 int ,\
cj2_cg int,\
futurecompany3 varchar(255) not null,\
cj3 int ,\
cj3_cg int,\
PRIMARY KEY(id)\
);''' % re.sub(r' ', '', item['INSTRUMENTID']))
            # print('========')
            # print(item['INSTRUMENTID'])
            # print(type(item['INSTRUMENTID']))
            # print(item['CJ1'])
            # print(type(item['CJ1']))
            sql_list.append('drop table if exists %s; ' % re.sub(r' ', '', item['INSTRUMENTID']))
            if item['RANK'] != 999:
                toMySql_str = (exe.date, item['RANK'],
                               re.sub(r' ', '', str(item['PARTICIPANTABBR1'])) if item['PARTICIPANTABBR1'] else '无排名',
                               item['CJ1'],
                               item['CJ1_CHG'],
                               re.sub(r' ', '', str(item['PARTICIPANTABBR2'])) if item['PARTICIPANTABBR2'] else '无排名',
                               item['CJ2'],
                               item['CJ2_CHG'],
                               re.sub(r' ', '', str(item['PARTICIPANTABBR3'])) if item['PARTICIPANTABBR3'] else '无排名',
                               item['CJ3'],
                               item['CJ3_CHG'])
            else:
                toMySql_str = (exe.date, item['RANK'],
                               re.sub(r' ', '', str(item['PARTICIPANTABBR1'])) if item['PARTICIPANTABBR1'] else '总计',
                               item['CJ1'],
                               item['CJ1_CHG'],
                               re.sub(r' ', '', str(item['PARTICIPANTABBR2'])) if item['PARTICIPANTABBR2'] else '总计',
                               item['CJ2'],
                               item['CJ2_CHG'],
                               re.sub(r' ', '', str(item['PARTICIPANTABBR3'])) if item['PARTICIPANTABBR3'] else '总计',
                               item['CJ3'],
                               item['CJ3_CHG'])

            toMySql_list.append('''insert into {0} (tradedate,rank,futurecompany1,cj1,cj1_cg,\
futurecompany2,cj2,cj2_cg,futurecompany3,cj3,cj3_cg) values('{1}',{2},'{3}',{4},{5},'{6}',{7},{8},'{9}',\
{10},{11});'''.format(
                re.sub(r' ', '', item['INSTRUMENTID']), exe.date, toMySql_str[1], toMySql_str[2],
                toMySql_str[3] if type(toMySql_str[3]) is int else 'null',
                toMySql_str[4] if type(toMySql_str[4]) is int else 'null',
                toMySql_str[5],
                toMySql_str[6] if type(toMySql_str[6]) is int else 'null',
                toMySql_str[7] if type(toMySql_str[7]) is int else 'null',
                toMySql_str[8],
                toMySql_str[9] if type(toMySql_str[9]) is int else 'null',
                toMySql_str[10] if type(toMySql_str[10]) is int else 'null')
            )
            # print(item['INSTRUMENTID'])
            # print(toMySql_str)
        # print(type(json_result['o_cursor']))
        data_amount = len(toMySql_list)
        routine_list = toMySqlTable_list+toMySql_list
        exe.db_obj.connect(charset='utf8')
        start_time = time.time()
        exe.db_obj.routine(routine_list)
        all_time = time.time() - start_time
        print('插入数据库耗时：%f' % all_time)
        exe.db_obj.close()
        print('共抓取%d条数据' % data_amount)
except Exception as e:
    print(e)

'''进行数据库存储时应
1、针对每一条语句，首先判断有没有对应的表，若没有则创建相关表
2、若有则进行数据存储
所以优化后应该为
先汇所有品种（数量不是很多）对所有品种进行判断
然后进行数据存储，

'''
