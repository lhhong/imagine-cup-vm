import scrapy
import re
from scrapy_splash import SplashRequest
import urllib

class QuotesSpider(scrapy.Spider):
    name = "menstyle"

    def start_requests(self):
        urls = [
            'http://www.menstylefashion.com/lookbooks/',

        ]
        for url in urls:
            ### MAY NOT NEED SPLASH ###
            # yield SplashRequest(url, self.parse,
            #     endpoint='render.html',
            #     args={'wait': 0.5},
            # )

            yield scrapy.Request(url=url, callback=self.parse)

        
    def parse(self, response):
        for link in response.xpath('//div[@class="cb-mask"]/a/@href').extract():
            link = urllib.urlopen(link).geturl()
            yield scrapy.Request(url=link, callback=self.getinfo)

        

    def getinfo(self, response):
    	yield {
            'url': response.url,
    		'image': response.xpath('//div[contains(@class, "tiled-gallery-item")]/a/@href').extract(),
    	}

