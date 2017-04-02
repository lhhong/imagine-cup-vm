import scrapy
import re
from scrapy_splash import SplashRequest
import urllib
import json

#### TO DO AFTER FINALISING CATEGORIES OF SHOES

AUTOTHROTTLE_ENABLED = False

class QuotesSpider(scrapy.Spider):
	name = "asos_spider"

	def start_requests(self):
		urls = [
			#'http://www.asos.com/men/t-shirts-vests/cat/?cid=7616&pgesize=204',
			# 'http://www.asos.com/men/t-shirts-vests/cat/?cid=7616&pge=1&pgesize=204',
			#'http://www.asos.com/men/t-shirts-vests/cat/?cid=7616&pge=2&pgesize=204',
			# 'http://www.asos.com/men/t-shirts-vests/cat/?cid=7616&pge=3&pgesize=204',
			# 'http://www.asos.com/men/t-shirts-vests/cat/?cid=7616&pge=4&pgesize=204',
			# 'http://www.asos.com/men/t-shirts-vests/cat/?cid=7616&pge=5&pgesize=204',
			#'http://www.asos.com/men/t-shirts-vests/cat/?cid=7616&pge=6&pgesize=204',
			# 'http://www.asos.com/men/t-shirts-vests/cat/?cid=7616&pge=7&pgesize=204',
			# 'http://www.asos.com/men/t-shirts-vests/cat/?cid=7616&pge=8&pgesize=204',
			# 'http://www.asos.com/men/t-shirts-vests/cat/?cid=7616&pge=9&pgesize=204',
			# 'http://www.asos.com/men/t-shirts-vests/cat/?cid=7616&pge=10&pgesize=204',
			# 'http://www.asos.com/men/t-shirts-vests/cat/?cid=7616&pge=11&pgesize=204',
			# 'http://www.asos.com/men/t-shirts-vests/cat/?cid=7616&pge=12&pgesize=204',
			# 'http://www.asos.com/men/t-shirts-vests/cat/?cid=7616&pge=13&pgesize=204',
			# 'http://www.asos.com/men/t-shirts-vests/cat/?cid=7616&pge=14&pgesize=204',
			# 'http://www.asos.com/men/t-shirts-vests/cat/?cid=7616&pge=15&pgesize=204',
			# 'http://www.asos.com/men/t-shirts-vests/cat/?cid=7616&pge=16&pgesize=204',
			# 'http://www.asos.com/men/t-shirts-vests/cat/?cid=7616&pge=17&pgesize=204',
			# 'http://www.asos.com/men/t-shirts-vests/cat/?cid=7616&pge=18&pgesize=204',
			# 'http://www.asos.com/men/t-shirts-vests/cat/?cid=7616&pge=19&pgesize=204',
			# 'http://www.asos.com/men/t-shirts-vests/cat/?cid=7616&pge=20&pgesize=204',
			# 'http://www.asos.com/men/t-shirts-vests/cat/?cid=7616&pge=21&pgesize=204',
			# 'http://www.asos.com/men/t-shirts-vests/cat/?cid=7616&pge=22&pgesize=204',
			# 'http://www.asos.com/men/t-shirts-vests/cat/?cid=7616&pge=23&pgesize=204',
			# 'http://www.asos.com/men/t-shirts-vests/cat/?cid=7616&pge=24&pgesize=204',
			# 'http://www.asos.com/men/t-shirts-vests/cat/?cid=7616&pge=25&pgesize=204',
			# 'http://www.asos.com/men/t-shirts-vests/cat/?cid=7616&pge=26&pgesize=204',
			# 'http://www.asos.com/men/t-shirts-vests/cat/?cid=7616&pge=27&pgesize=204',
			# 'http://www.asos.com/men/t-shirts-vests/cat/?cid=7616&pge=28&pgesize=204',
			 # 'http://www.asos.com/men/t-shirts-vests/cat/?cid=7616&pge=29&pgesize=204',
			
			#'http://www.asos.com/men/jeans/cat/?cid=4208&pgesize=204',
			# 'http://www.asos.com/men/jeans/cat/?cid=4208&pge=1&pgesize=204',
			# 'http://www.asos.com/men/jeans/cat/?cid=4208&pge=2&pgesize=204',
			# 'http://www.asos.com/men/jeans/cat/?cid=4208&pge=3&pgesize=204',
			# 'http://www.asos.com/men/jeans/cat/?cid=4208&pge=4&pgesize=204',
			# 'http://www.asos.com/men/jeans/cat/?cid=4208&pge=5&pgesize=204',
			# 'http://www.asos.com/men/jeans/cat/?cid=4208&pge=6&pgesize=204',
			 # 'http://www.asos.com/men/jeans/cat/?cid=4208&pge=7&pgesize=204',

			#'http://www.asos.com/men/polo-shirts/cat/?cid=4616&pgesize=204',
			# 'http://www.asos.com/men/polo-shirts/cat/?cid=4616&pge=1&pgesize=204',
			# 'http://www.asos.com/men/polo-shirts/cat/?cid=4616&pge=2&pgesize=204',
			# 'http://www.asos.com/men/polo-shirts/cat/?cid=4616&pge=3&pgesize=204',
			# 'http://www.asos.com/men/polo-shirts/cat/?cid=4616&pge=4&pgesize=204',

			# 'http://www.asos.com/men/trousers-chinos/cat/?cid=4910&pgesize=204',
			# 'http://www.asos.com/men/trousers-chinos/cat/?cid=4910&pge=1&pgesize=204',
			# 'http://www.asos.com/men/trousers-chinos/cat/?cid=4910&pge=2&pgesize=204',
			# 'http://www.asos.com/men/trousers-chinos/cat/?cid=4910&pge=3&pgesize=204'

			# 'http://www.asos.com/men/shorts/cat/?cid=7078&pgesize=204',
			# 'http://www.asos.com/men/shorts/cat/?cid=7078&pge=1&pgesize=204',
			# 'http://www.asos.com/men/shorts/cat/?cid=7078&pge=2&pgesize=204',
			 # 'http://www.asos.com/men/shorts/cat/?cid=7078&pge=3&pgesize=204',

		]
		for url in urls:
			### MAY NOT NEED SPLASH ###
			# yield SplashRequest(url, self.parse,
			#     endpoint='render.html',
			#     args={'wait': 0.5},
			# )

			yield scrapy.Request(url=url, callback=self.parse)

		
	def parse(self, response):
		for link in response.css('a.product.product-link::attr(href)').extract():
			link = urllib.urlopen(link).geturl()

			yield scrapy.Request(url=link, callback=self.getinfo)
			# yield SplashRequest(link, self.getinfo,
			#         endpoint='render.html',
			#         args={'wait': 0.5},
			#     )

		

	def getinfo(self, response):
		yield {
			'url': response.url,
			'image': response.css('div.window img::attr(src)').extract_first(),
			'price': json.loads(response.xpath('//script[contains(., "Pages/FullProduct")]/text()').re_first("view\('(\{.*\})',"))['price']['current'],
			'brand': response.css('div.brand-description span a strong::text').extract_first(),
			'title': response.css('title::text').extract_first(),
			'colour': json.loads(response.xpath('//script[contains(., "Pages/FullProduct")]/text()').re_first("view\('(\{.*\})',"))['images'][0]['colour'],
			#'description': response.css('div.product-description span ul li::text').extract() #a list of descriptors
		}

