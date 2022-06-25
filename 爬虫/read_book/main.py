# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import pymysql
from itemadapter import ItemAdapter
from scrapy.utils.project import get_project_settings


if __name__ == '__main__':
    DB_HOST = '47.108.62.43'
    DB_PORT = 3306
    DB_USER = 'root'
    DB_PASSWORD = '87337334'
    DB_NAME = 'Search_Engine'
    DB_CHARSET = 'utf8mb4'
    conn = pymysql.connect(host=DB_HOST, port=DB_PORT, user=DB_USER, password=DB_PASSWORD, db=DB_NAME,
                                charset=DB_CHARSET)
    cursor = conn.cursor()
    sql = 'insert into tb_document(title, author, create_time, summary, summary_offline, url, site) values ("%s", "%s", "%s", "%s", "%s", "%s", "%s")' % (
        'datetime.datetime(2021, 10, 1, 7, 57, 39)', 'Spring教程,Spring手册', 'summary', 'summary_offline', 'url',
        'Spring教程,Spring手册')
    cursor.execute(sql)
    # 提交事务
    conn.commit()
    conn.close()
    cursor.close()
