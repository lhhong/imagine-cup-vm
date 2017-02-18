import scrapy
import re

class QuotesSpider(scrapy.Spider):
    name = "zalora"

    def start_requests(self):
        urls = [
            'https://www.zalora.sg/vans-ap-teamer-fly-v-short-sleeved-t-shirt-black-588363.html',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # page = response.url.split("/")[-2]
        # filename = 'quotes-%s.html' % page
        # with open(filename, 'wb') as f:
        #     f.write(response.body)
        # self.log('Saved file %s' % filename)
        yield {
            'image': response.css('div.l-productImage.box div.productZoom::attr(data-zoom)').extract_first(),
            'colour': response.xpath('.//td[@itemprop="color"]').extract_first(), #but can't extract just the text
        }

        next_page = response.css('li.next a::attr(href)').extract_first()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)