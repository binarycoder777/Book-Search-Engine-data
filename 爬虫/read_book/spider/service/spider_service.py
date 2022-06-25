import queue

import jieba
from goose3 import Goose
from goose3.text import StopWordsChinese
import requests

from spider.dao import pipeline
from spider.entity.Items import LinkItem

base_url = 'http://www.xz577.com'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'
}
queue = queue.Queue()
queue.put(base_url)



if __name__ == '__main__':
    url = queue.get()
    pipeline.MysqlPipeline.connect()
    # while queue.
    print('end')
