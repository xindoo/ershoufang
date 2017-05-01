# -*- coding: utf-8 -*-
import scrapy
import re

class ershoufangSpider(scrapy.Spider):
    name = "ershoufang"
    # start_urls = ["http://bj.lianjia.com/ershoufang/dongcheng/pg1", "http://bj.lianjia.com/ershoufang/xicheng/pg1", "http://bj.lianjia.com/ershoufang/chaoyang/pg1", "http://bj.lianjia.com/ershoufang/haidian/pg1", "http://bj.lianjia.com/ershoufang/fengtai/pg1", "http://bj.lianjia.com/ershoufang/shijingshan/pg1", "http://bj.lianjia.com/ershoufang/tongzhou/pg1", "http://bj.lianjia.com/ershoufang/changping/pg1", "http://bj.lianjia.com/ershoufang/daxing/pg1", "http://bj.lianjia.com/ershoufang/yizhuangkaifaqu/pg1", "http://bj.lianjia.com/ershoufang/shunyi/pg1", "http://bj.lianjia.com/ershoufang/fangshan/pg1", "http://bj.lianjia.com/ershoufang/mentougou/pg1", "http://bj.lianjia.com/ershoufang/pinggu/pg1", "http://bj.lianjia.com/ershoufang/huairou/pg1", "http://bj.lianjia.com/ershoufang/miyun/pg1", "http://bj.lianjia.com/ershoufang/yanqing/pg1", "http://bj.lianjia.com/ershoufang/yanjiao/pg1"]
    start_urls = ["http://bj.lianjia.com/ershoufang/pg1"]
    def parse(self, response):
        houses = response.xpath(".//ul[@class='sellListContent']/li")
        for house in houses:
            attention = ''
            visited = ''
            publishday = ''
            try:
                attention = house.xpath(".//div[@class='followInfo']/text()").re("\d+")[0]
                visited = house.xpath(".//div[@class='followInfo']/text()").re("\d+")[1]
                if u'月' in house.xpath(".//div[@class='followInfo']/text()").extract()[0].split('/')[2]:
                    number = house.xpath(".//div[@class='followInfo']/text()").re("\d+")[2]
                    publishday = '' + int(number)*30

                elif u'年' in house.xpath(".//div[@class='followInfo']/text()").extract()[0].split('/')[2]:
                    number = house.xpath(".//div[@class='followInfo']/text()").re("\d+")[2]
                    publishday = '365'
                else:
                    publishday = house.xpath(".//div[@class='followInfo']/text()").re("\d+")[2]
            except:
                print "These are some ecxeptions"
            else:
                pass

            yield {
                'region': house.xpath(".//div[@class='houseInfo']/a/text()").extract(),
                'url':house.xpath(".//a[@class='img ']/@href").extract(),
                'houseInfo':house.xpath(".//div[@class='houseInfo']/text()").extract(),
                'unitPrice':house.xpath(".//div[@class='unitPrice']/span").re("\d+.\d+"),
                'totalPrice':house.xpath(".//div[@class='totalPrice']/span").re("\d+.\d+"),
                'attention': attention,
                'visited': visited,
                'publishday': publishday
            }
        page = response.xpath("//div[@class='page-box house-lst-page-box'][@page-data]").re("\d+")
        p = re.compile(r'[^\d]+')
        if len(page)>1 and page[0] != page[1]:
            next_page = p.match(response.url).group()+str(int(page[1])+1)
            print next_page+"*********************"
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
