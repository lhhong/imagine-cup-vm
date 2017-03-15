import scrapy
import re
from scrapy_splash import SplashRequest
import urllib

class QuotesSpider(scrapy.Spider):
    name = "fashionbeans"

    def start_requests(self):
        urls = [
            #'http://www.fashionbeans.com/category/mens-look-books/?season=ss17',
            #'http://www.fashionbeans.com/category/mens-look-books/page/2/?season=ss17',
            # 'http://www.fashionbeans.com/category/mens-look-books/page/3/?season=ss17',
            # 'http://www.fashionbeans.com/category/mens-look-books/page/4/?season=ss17',
             'http://www.fashionbeans.com/category/mens-look-books/page/5/?season=ss17',

        ]
        for url in urls:
            ### MAY NOT NEED SPLASH ###
            # yield SplashRequest(url, self.parse,
            #     endpoint='render.html',
            #     args={'wait': 0.5},
            # )

            yield scrapy.Request(url=url, callback=self.parse)

        
    def parse(self, response):
        for link in response.xpath('//div[@class="fluidArticleContent"]/a/@href').extract():
            link = urllib.urlopen(link).geturl()
            yield scrapy.Request(url=link, callback=self.getinfo)

        

    def getinfo(self, response):
    	yield {
            'url': response.url,
    		'image': response.xpath('//a[contains(@href, "uploads")]/@href').extract(),
    	}

