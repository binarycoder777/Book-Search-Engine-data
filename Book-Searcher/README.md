# 小型搜素引擎
描述：现在通过PC、手机、电子阅读器都可以完成阅读行为，网络上“飘荡”着浩瀚的电子书，常常让网络读者不知所措。快速检索电子书成为读者关心的话题。类似google、百度、中搜这样的搜索引擎，多数只是把图书搜索作为其中一项分支功能提供给大众，搜索结果不全面时有发生。因此需要一个专业的图书垂直搜索引擎。从精确搜索电子书，到电子书相关推荐，涵盖方方面面，可以自由查看你喜欢的书籍，形成一一个书籍资料库，给用户阅读书籍带来更多的选择。

## 系统架构
该搜索引擎整体系统架构主要由python数据处理端和java服务端构成。python数据处理端主要任务是从指定的站点爬取书籍信息，然后对数据进行清洗过滤，得到想要的数据后存储到Elasticsearch中，Java服务端使用springboot集成Elasticsearch，并借助于Elasticsearch提供的相关API进行搜索引擎相关功能开发，将接口暴露给web端。用户通过web端进行访问使用该搜索引擎。具体实现架构图如下所示：

## 系统设计

### Java服务端

功能模块说明：

- pom.xml: 管理项目需要的jar包依赖
- main: 存放功能代码
- test: 存放测试代码
- resources:存放项目的配置信息
- Main：项目启动程序
- Config: 项目配置类
- Controller: 交互类
- Entity: 实体类
- Mapper: 数据处理类
- Service: 业务处理类

项目使用技术栈：
服务器端：SpringBoot、SpringData、Elasticsearch
前端：Vue、ElementUI

功能模块实现：
整个java服务端实现了前缀搜索、搜索纠错、模糊搜索、搜索分页、高亮显示、搜索推荐等功能模块。

### python数据处理端：

功能模块说明：

- Items.py: 数据传输实体
- Middlewares.py: 中间件
- Pipelines.py: 数据处理管道
- Settings.py: 项目配置信息
- Spiders: 主要爬虫功能代码
- Book.py:爬虫+数据处理
- Temp.log: 项目日志信息

项目所使用技术栈和算法：Scrapy、Goose、TestRank、PageRank

功能模块实现
整个python数据处理端实现了数据爬取、数据处理、数据存储等功能。


### 实现预览

