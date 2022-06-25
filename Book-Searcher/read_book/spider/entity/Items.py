# 网页数据结构
class DocumentItem():
    title = ''
    author = ''
    create_time = ''
    summary = ''
    pic = ''
    url = ''
    site = ''

    def __init__(self, title, author, create_time, summary, pic, url, site):
        self.title = title
        self.author = author
        self.create_time = create_time
        self.summary = summary
        self.pic = pic
        self.url = url
        self.site = site


# 链接关系
class LinkItem():
    parent_url = ''
    childer_url = ''

    def __init__(self, parent_url, childer_url):
        self.parent_url = parent_url
        self.childer_url = childer_url
