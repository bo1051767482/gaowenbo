# # -*- coding: utf-8 -*-
# import scrapy
#
#
# from scrapy_redis.spiders import RedisSpider
#
# class MySpider(RedisSpider):
#     """Spider that reads urls from redis queue (myspider:start_urls)."""
#     name = 'myspider'
#     redis_key = 'MySpider:start_url'
#     allowed_domains=['baidu.com']
#     # def __init__(self, *args, **kwargs):
#     #     # Dynamically define the allowed domains list.
#     #     domain = kwargs.pop('domain', '')
#     #     self.allowed_domains = filter(None, domain.split(','))
#     #     super(MySpider, self).__init__(*args, **kwargs)
#
#     def parse(self, response):
#         yield {
#             'name': response.css('title::text').extract_first(),
#             'url': response.url,
#         }
