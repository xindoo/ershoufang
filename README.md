This project can help you crawl second-hand houses data from (lianjia.com)[lianjia.com]. This project is a scrapy project, Scrapy is an opensource crawling framework,  it's pretty to use. And I use xpath to resolve second-hand houses data from html souce code.

Before you run my code, you must install scrapy on your machine, you can use pip install it very quickly. 
`pip install scrapy` 

Use this command to start it, it will export data into CSV format.
`scrapy crawl ershoufang -o item.csv` 

_ershoufang_ is the name of spider. Actually, there are three spiders in this project ershoufang  yanjiao and ershoufanghz, they correspond to the second-hand houses data spider of Beijing, Beijing Yanjiao, and Hangzhou. You can also create your own spider, just need to change the URL in the file `ershoufang/spider/ershoufang.py` line 8.   

In case of be banned by lianjian, I configured somethings in settings.py. eg. disable cookie, change the bot_name, crawl only one time each minute, use different use_agent(I commented it out), etc. I don't use proxy, because I don't have proxy IP source. 

这个项目可以帮你从链家爬取二手房数据，这是个scrapy项目。scrapy是一个开源的爬虫框架，很容易使用。我用了xpath来解析网页代码里的二手房数据。  

在你开始运行代码前，你必须先在你电脑上安装scrapy，用pip命令很快就可以装好。  
`pip install scrapy` 

用这条命令启动代码，把数据导出成csv格式。 
`scrapy crawl ershoufang -o item.csv` 

_ershoufang_ 是爬虫的名字，其实在这个项目里我有三个爬虫，ershoufang、yanjiao、ershoufanghz， 分别对应北京、燕郊、杭州的二手房数据爬虫。你也可以创建自己的爬虫，只需要改下`ershoufang/spider/ershoufang.py`代码第8行的URL就行。   

为了防止被链家禁掉，我在settings.py 做了一些配置，比如禁掉cookie，改了bot_name, 每分钟只爬一次，用不同的use_agent(配置被我注释掉了)…… 我没用proxy，因为我没proxy ip资源。 