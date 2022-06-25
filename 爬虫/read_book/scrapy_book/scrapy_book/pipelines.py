# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import pymysql
from itemadapter import ItemAdapter
from scrapy.utils.project import get_project_settings

from scrapy_book.items import ScrapyLinkItem

from scrapy_book.items import ScrapyDocumentItem


class ScrapyBookPipeline:
    def process_item(self, item, spider):
        return item

class MysqlPipeline(object):
    # init是获取settings中的连接参数
    def __init__(self):
        settings = get_project_settings()
        self.host = settings['DB_HOST']
        self.port = settings['DB_PORT']
        self.user = settings['DB_USER']
        self.pwd = settings['DB_PASSWORD']
        self.name = settings['DB_NAME']
        self.charset = settings['DB_CHARSET']
        self.connect()

    # 连接数据库并且获取cursor对象
    def connect(self):
        self.conn = pymysql.connect(host=self.host, port=self.port, user=self.user, password=self.pwd, db=self.name,
                                    charset=self.charset)
        self.cursor = self.conn.cursor()

    # 执行存储过程
    def process_item(self, item, spider):
        if type(item) == ScrapyLinkItem:
            # print(type(item), item)
            sql = 'insert into inner_link(parent_url, childer_url) values ("%s", "%s")' % (
            item['parent_url'], item['childer_url'])
        else:
            sql = 'insert into tb_doc(title, author, create_time, summary, pic, url, site) values ("%s", "%s", "%s", "%s", "%s", "%s", "%s")' % (
        item['title'], item['author'], item['create_time'], item['summary'], item['pic'], item['url'], item['site'])
            print(type(item), item)
        # 执行sql语句
        self.cursor.execute(sql)
        # 提交事务
        self.conn.commit()
        print('success')
        return item

    # 关闭连接
    def close_spider(self, spider):
        self.conn.close()
        self.cursor.close()
