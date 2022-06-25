import jieba
import requests
import scrapy
from bs4 import BeautifulSoup
from goose3 import Goose
from goose3.text import StopWordsChinese
from scrapy.spidermiddlewares.httperror import HttpError
from lxml import etree
from scrapy_book.items import ScrapyLinkItem, ScrapyDocumentItem
from twisted.internet.error import DNSLookupError


class BookSpider(scrapy.Spider):
    name = 'book'
    cur_num = 1
    total_num = 100000
    prefix_url = 'http://search.bookask.com/s/kw_java/t_0/pn_'
    base_url = ' http://search.bookask.com'
    allowed_domains = ['search.bookask.com']
    start_urls = ['http://search.bookask.com/s/kw_java/t_0/pn_1.html']
    custom_settings = {
        "DEFAULT_REQUEST_HEADERS": {
            # 'Connection': 'close',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'
        }
    }
    # 初始化，设置中文分词
    g = Goose({'stopwords_class': StopWordsChinese})
    # jieba分词
    jieba.setLogLevel(jieba.logging.INFO)

    def parse(self, response):
        try:
            # 当前爬取链接作为父链接
            cur_url = response.url
            # 获取图片
            pic_selectors = response.xpath("//img[@class='cover lazy']/@src")
            # 获取标题
            title_selectors = response.xpath("//div[@class='am-u-sm-9 con-minheight']/div/h1//text()")
            # 获取作者
            author_selectors = response.xpath("//div[@class='am-u-sm-9 con-minheight']/div[2]//text()")
            # 获取出版社
            pub_selectors = response.xpath("//div[@class='am-u-sm-9 con-minheight']/p/a[1]//text()")
            # 提取页面url
            url_selectors = response.xpath("//div[@class='am-u-sm-9 con-minheight']/div/h1/a//@href")
            # print()
            l = min(min(min(len(pic_selectors), len(title_selectors)), min(len(author_selectors), len(pub_selectors))),len(url_selectors))
            # print('==----',l)
            for i in range(l):
                pic = pic_selectors.get(i)
                # print(pic)
                title = title_selectors[i].extract()
                # print(title)
                author = author_selectors[i].extract()
                # print(author)
                site = pub_selectors[i].extract()
                # print(site)
                url = self.base_url + url_selectors[i].extract()
                # print(url)
                response = requests.get(url)
                html_tree = etree.HTML(response.content.decode('utf-8'))
                res = ''
                summary = html_tree.xpath("//div[@class='book-text-box']//text()")
                if len(summary) > 0:
                    for s in summary:
                        res += s
                    summary = res.strip()
                # print("summary",len(summary))
                # print(summary)
                create_time = html_tree.xpath("//div[@class='book-top-info fr']/h3[3]//text()")
                print(create_time)
                if len(create_time) > 0:
                    create_time = create_time[0]
                # print(create_time)
                # 信息封装数据，交给管道存储到mysql
                web_page = ScrapyDocumentItem(title=title, author=author, create_time=create_time, summary=summary,
                                              pic=pic, url=url, site=site)
                # print(web_page)
                yield web_page
            # 广度优先策略爬取，回调提取到的网页
            self.cur_num = self.cur_num + 1;
            childer_url = self.prefix_url + str(self.cur_num) + '.html';
            print(childer_url+"===================")
            yield scrapy.Request(url=childer_url, callback=self.parse)
        except Exception as e:
            print('\n\nerror:', e)
        print('end')
