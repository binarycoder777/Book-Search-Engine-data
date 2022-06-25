import pymysql

from spider.entity.Items import ScrapyLinkItem


class MysqlPipeline(object):
    # init是获取settings中的连接参数
    def __init__(self):
        self.host = '47.108.62.43'
        self.port = 3306
        self.user = 'root'
        self.pwd = '87337334'
        self.name = 'Search_Engine'
        self.charset = 'utf8mb4'

    # 连接数据库并且获取cursor对象
    def connect(self):
        self.conn = pymysql.connect(host=self.host, port=self.port, user=self.user, password=self.pwd, db=self.name,
                                    charset=self.charset)
        self.cursor = self.conn.cursor()

    # 添加链接关系
    def addLink(self, item):
        sql = 'insert into inner_link(parent_url, childer_url) values ("%s", "%s")' % (
            item['parent_url'], item['childer_url'])
        self.cursor.execute(sql)
        # 提交事务
        self.conn.commit()

    # 添加文档
    def addDocument(self, item):
        sql = 'insert into tb_document(title, author, create_time, summary, summary_offline, url, site) values ("%s", "%s", "%s", "%s", "%s", "%s", "%s")' % (
            item['title'], item['author'], item['create_time'], item['summary'], item['summary_offline'],
            item['url'], item['site'])
        self.cursor.execute(sql)
        # 提交事务
        self.conn.commit()

    # 关闭连接
    def close(self):
        self.conn.close()
        self.cursor.close()
