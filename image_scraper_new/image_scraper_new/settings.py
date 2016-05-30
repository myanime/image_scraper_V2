# -*- coding: utf-8 -*-

# Scrapy settings for image_scraper_new project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'image_scraper_new'
SPIDER_MODULES = ['image_scraper_new.spiders']
NEWSPIDER_MODULE = 'image_scraper_new.spiders'

FILES_STORE = './files/'
IMAGES_STORE = './pictures/'

ITEM_PIPELINES = {'image_scraper_new.pipelines.RenamePipeline': 1}
#ITEM_PIPELINES = {'scrapy.pipelines.images.ImagesPipeline': 1}
#ITEM_PIPELINES = {'scrapy.contrib.pipeline.images.FilesPipeline':1,}
