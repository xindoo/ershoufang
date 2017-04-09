import scrapy
from scrapy.http.request import Request

class ershoufangSpider(scrapy.Spider):
    name = "ershoufang"
    start_urls = ["http://bj.lianjia.com/ershoufang/"]

    def parse(self, response):
        houses = response.xpath(".//ul[@class='sellListContent']/li")
        for house in houses:
            yield {
                'region': house.xpath(".//div[@class='houseInfo']/a/text()").extract(),
                # 'url':house.xpath(".//a[@class='img ']/@href").extract(),
                'houseInfo':house.xpath(".//div[@class='houseInfo']/text()").extract(),
                'unitPrice':house.xpath(".//div[@class='unitPrice']/span").re("\d+.\d+"),
                'totalPrice':house.xpath(".//div[@class='totalPrice']/span").re("\d+.\d+")
            }
        page = response.xpath("//div[@class='page-box house-lst-page-box'][@page-data]").re("\d+")
        if None != page and page[0] != page[1]:
            next_page = "http://bj.lianjia.com/ershoufang/pg"+str(int(page[1])+1)
            print next_page+"*********************"
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
