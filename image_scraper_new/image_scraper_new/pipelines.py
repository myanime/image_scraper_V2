import scrapy
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem
import random

class ImageScraperNewPipeline(object):
    def process_item(self, item, spider):
        return item

class RenamePipeline(ImagesPipeline):

    def set_filename(self, response):
        my_number = random.randrange(1,100,1)
        #Adds a name passed in from the spider plus a random number
        return 'full/{0}'.format(response.meta['my_nice_file_name']) + '-picture' + str(my_number) +'.jpg'

    def get_media_requests(self, item, info):
        for image_url in item['image_urls']:
            yield scrapy.Request(image_url, meta={'my_nice_file_name': item['my_nice_file_name']})

    def get_images(self, response, request, info):
        for key, image, buf in super(RenamePipeline, self).get_images(response, request, info):
            key = self.set_filename(response)
        yield key, image, buf
