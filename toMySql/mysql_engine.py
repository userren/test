import pymysql


class MySql(object):

    def __init__(self, **kwargs):

        """
        链接数据库对象，必要的参数：
        host 默认 localhost
        port 默认 3306
        user 默认 root
        password 默认为空
        database 默认None
        用法示例：
        db = MySql(user='root', password="root1",
                  database='futuretradedata')
        db.connect(charset='utf8')
        sql = 'select * from crawlerwebsite'
        data = a.execute(sql, fetch='fetchall')
        print(data())
        db.close()
        ============================
        方法 connect()
        kwargs:
            charset = 'utf8',必选参数
        """

        self.__host = kwargs['host'] if 'host' in kwargs.keys() else 'localhost'
        self.__port = kwargs['port'] if 'port' in kwargs.keys() else 3306
        self.__user = kwargs['user'] if 'user' in kwargs.keys() else 'root'
        self.__password = kwargs['password'] if 'password' in kwargs.keys() else ''
        self.__database = kwargs['database'] if 'database' in kwargs.keys() else None
        self.db = None
        self.db_cursors = None

    def connect(self, **kwargs):
        try:
            self.db = pymysql.connect(host=self.__host, user=self.__user, password=self.__password,
                                      database=self.__database, port=self.__port, charset=kwargs['charset'])
            self.db_cursors = self.db.cursor()
        except Exception as e:
            return e

    def close(self):

        try:
            if self.db_cursors:
                self.db_cursors.close()
            if self.db:
                self.db.close()
            else:
                print('self.db为空,数据库连接关闭失败')
        except Exception as e:
            return e

    def execute(self, sqls, **kwargs):
        """
        :param sqls: 必要参数，数据库执行语句
        :param kwargs: fetch=fetchall or fetchone or None
        :return:
        """
        try:
            self.db_cursors .execute(sqls)
            if kwargs:
                return getattr(self.db_cursors, kwargs['fetch'])
        except Exception as e:
            return e

    def routine(self, task: list):

        try:
            for sql in task:
                self.db_cursors.execute(sql)
        except Exception as e:
            print(e)
            print('发生错误,正在回滚')
            self.db.rollback()
            print('回滚完成')
        else:
            self.db.commit()


if __name__ == '__main__':
    a = MySql(user='root', password="root1",
              database='futuretradedata')
    a.connect(charset='utf8')
    # sql = 'select * from crawlerwebsite'
    # data = a.execute(sql, fetch='fetchall')
    # print(data())
    # sqls = [
    #     '''create table IF NOT EXISTS cu1908(
    #         id int not null auto_increment,
    #     tradedate date not null,
    #     rank1 int not null,
    #     futurecompany1 varchar(255) not null,
    #     cj1 int,
    #     cj1_cg int,
    #     rank2 int not null,
    #     futurecompany2 varchar(255) not null,
    #     cj2 int,
    #     cj2_cg int,
    #     rank3 int not null,
    #     futurecompany3 varchar(255) not null,
    #     cj3 int,
    #     cj3_cg int,
    #     PRIMARY KEY(id));''',
    #     '''create table IF NOT EXISTS cu1909(
    #                 id int not null auto_increment,
    #             tradedate date not null,
    #             rank1 int not null,
    #             futurecompany1 varchar(255) not null,
    #             cj1 int,
    #             cj1_cg int,
    #             rank2 int not null,
    #             futurecompany2 varchar(255) not null,
    #             cj2 int,
    #             cj2_cg int,
    #             rank3 int not null,
    #             futurecompany3 varchar(255) not null,
    #             cj3 int,
    #             cj3_cg int,
    #             PRIMARY KEY(id));''']
    a.close()
