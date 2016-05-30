import scrapy
class ImageScraperItem(scrapy.Item):
    image_urls = scrapy.Field()
    images = scrapy.Field()
    file_urls = scrapy.Field()
    files = scrapy.Field()
    my_nice_file_name = scrapy.Field()
