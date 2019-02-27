import scrapy
from scrapy.selector import Selector
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.loader.processors import Join, MapCompose, TakeFirst
from scrapy.pipelines.images import ImagesPipeline
from production.items import ProductionItem
from production.items import ImageItem

class ClothesSpider(scrapy.Spider):
    name = "clothes"
    
    def start_requests(self):
        urls = ['https://www.zalando.fr/manteaux-homme/?p=',
               'https://www.zalando.fr/vestes-homme/?p=',
               'https://www.zalando.fr/pulls-gilets-homme/?p=',
               'https://www.zalando.fr/sweatshirts-homme/?p=',
               'https://www.zalando.fr/t-shirts-polos-homme/?p=',
               'https://www.zalando.fr/t-shirts-tops-femme/?p=',
               'https://www.zalando.fr/sweatshirts-femme/?p=',
               'https://www.zalando.fr/pulls-gilets-femme/?p=',
               'https://www.zalando.fr/vestes-femme/?p=',
               'https://www.zalando.fr/manteaux-femme/?p=',
               'https://www.zalando.fr/pantalons-femme/?p=',
               'https://www.zalando.fr/pantalons-homme/?p=',
               'https://www.zalando.fr/shorts-homme/?p=',
               'https://www.zalando.fr/shorts-femme/?p=',
               'https://www.zalando.fr/jeans-femme/?p=',
               'https://www.zalando.fr/jeans-homme/?p=']
        print ('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
        headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0'}
        for url in urls:
            for i in range(1, 30):
                yield scrapy.Request(url + str(i), headers=headers, callback=self.parse)

    def parse(self, response):
#         images = response.selector.xpath('//img').get()
#         print (response.body)
        print ('<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>')
#         images = Selector(response=response).xpath('//img/@src').extract()
#         print (">>>>>>>>>>>>>>>>>>>>")
#         print (images, len(images))
#         print ("<<<<<<<<<<<<<<<<<<<")
        for elem in Selector(response=response).xpath("//img"):
            img_url = elem.xpath("@src").extract_first()
            print (img_url)
            yield ImageItem(image_urls=[img_url])

#         page = response.url.split("/")[-2]
#         filename = 'quotes-%s.html' % page
#         with open(filename, 'wb') as f:
#             f.write(response.body)
#         self.log('Saved file %s' % filename)