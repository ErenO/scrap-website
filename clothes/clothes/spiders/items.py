# -*- coding: utf-8 -*-
import scrapy

class ProductionItem(scrapy.Item):
    img_url = scrapy.Field()
# ScrapingList Residential & Yield Estate for sale
class ListResidentialItem(scrapy.Item):
    image_urls = scrapy.Field()
    images = scrapy.Field()

class ImageItem(scrapy.Item):
    image_urls = scrapy.Field()
    images = scrapy.Field()