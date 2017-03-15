import scrapy
import re
from scrapy_splash import SplashRequest
import urllib

class QuotesSpider(scrapy.Spider):
    name = "trendspotter"

    def start_requests(self):
        urls = [
            #'https://www.thetrendspotter.net/lookbooks',
            #'https://www.thetrendspotter.net/lookbooks/page/2',
            #'https://www.thetrendspotter.net/lookbooks/page/3',
            #'https://www.thetrendspotter.net/lookbooks/page/4',
            # 'https://www.thetrendspotter.net/lookbooks/page/5',
            # 'https://www.thetrendspotter.net/lookbooks/page/6',
            # 'https://www.thetrendspotter.net/lookbooks/page/7',
            #'https://www.thetrendspotter.net/lookbooks/page/8',
            # 'https://www.thetrendspotter.net/lookbooks/page/9',
            # 'https://www.thetrendspotter.net/lookbooks/page/10',
            # 'https://www.thetrendspotter.net/lookbooks/page/11',
            # 'https://www.thetrendspotter.net/lookbooks/page/12',
            # 'https://www.thetrendspotter.net/lookbooks/page/13',
            # 'https://www.thetrendspotter.net/lookbooks/page/14',
            # 'https://www.thetrendspotter.net/lookbooks/page/15',
            # 'https://www.thetrendspotter.net/lookbooks/page/16',
            # 'https://www.thetrendspotter.net/lookbooks/page/17',
            # 'https://www.thetrendspotter.net/lookbooks/page/18',
            # 'https://www.thetrendspotter.net/lookbooks/page/19',
            # 'https://www.thetrendspotter.net/lookbooks/page/20',
             'https://www.thetrendspotter.net/lookbooks/page/21',
            # 'https://www.thetrendspotter.net/lookbooks/page/22',
            # 'https://www.thetrendspotter.net/lookbooks/page/23',
            # 'https://www.thetrendspotter.net/lookbooks/page/24',
            # 'https://www.thetrendspotter.net/lookbooks/page/25',
            # 'https://www.thetrendspotter.net/lookbooks/page/26',
            # 'https://www.thetrendspotter.net/lookbooks/page/27',
            # 'https://www.thetrendspotter.net/lookbooks/page/28',
            # 'https://www.thetrendspotter.net/lookbooks/page/29',
            # 'https://www.thetrendspotter.net/lookbooks/page/30',
            # 'https://www.thetrendspotter.net/lookbooks/page/31',
            # 'https://www.thetrendspotter.net/lookbooks/page/32',
            # 'https://www.thetrendspotter.net/lookbooks/page/33',
            # 'https://www.thetrendspotter.net/lookbooks/page/34',
            # 'https://www.thetrendspotter.net/lookbooks/page/35',
            # 'https://www.thetrendspotter.net/lookbooks/page/36',
            # 'https://www.thetrendspotter.net/lookbooks/page/37',
            # 'https://www.thetrendspotter.net/lookbooks/page/38',
            # 'https://www.thetrendspotter.net/lookbooks/page/39',
            # 'https://www.thetrendspotter.net/lookbooks/page/40',
            # 'https://www.thetrendspotter.net/lookbooks/page/41',
            # 'https://www.thetrendspotter.net/lookbooks/page/42',
            # 'https://www.thetrendspotter.net/lookbooks/page/43',
            # 'https://www.thetrendspotter.net/lookbooks/page/44',
            # 'https://www.thetrendspotter.net/lookbooks/page/45',
            # 'https://www.thetrendspotter.net/lookbooks/page/46',



        ]
        for url in urls:
            ### MAY NOT NEED SPLASH ###
            # yield SplashRequest(url, self.parse,
            #     endpoint='render.html',
            #     args={'wait': 0.5},
            # )

            yield scrapy.Request(url=url, callback=self.parse)

        
    def parse(self, response):
        for link in response.xpath('//div[@class="lookbook-item"]/a/@href').extract():
            link = urllib.urlopen(link).geturl()
            yield scrapy.Request(url=link, callback=self.getinfo)

        

    def getinfo(self, response):
    	yield {
            'url': response.url,
    		'image': response.xpath('//img[contains(@src, "justified")]/@src').extract(),
    	}

