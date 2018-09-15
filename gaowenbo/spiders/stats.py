# -*- coding: utf-8 -*-
import scrapy
from scrapy_redis.spiders import RedisSpider
import re
from ..items import StatsItem


class StatsSpider(RedisSpider):
    name = 'stats'
    allowed_domains = ['stats.gov.cn']
    redis_key = "StatsSpider:start_urls"
    # start_urls = ['http://stats.gov.cn/']
    custom_settings = {
        'ITEM_PIPELINES': {'gaowenbo.pipelines.StatsPipeline': 300, }
    }

    def parse(self, response):
        print('第一级页面开始爬取')
        td_list=response.xpath('//tr[@class="provincetr"]/td')
        # print(td_list)
        #删掉3个空白的td
        td_list.pop()
        td_list.pop()
        td_list.pop()
        for td in td_list:
            prov_url=td.xpath('./a/@href').extract_first()
            prov_code_str = re.search(r'\d+', prov_url).group()
            prov_code = prov_code_str + '0000000000'
            prov_name_node=td.xpath('./a')
            prov_name=prov_name_node.xpath('string(.)').extract_first()
            print(prov_code,prov_name)
            if prov_url:
                print(prov_url)
                yield response.follow(prov_url,dont_filter=True,meta={'prov_code':prov_code,'prov_name':prov_name},callback=self.second_parse)

    def second_parse(self, response):
        print('第二级页面开始爬取')
        tr_list=response.xpath('//tr[@class="citytr"]')
        for tr in tr_list:
            prov_code = response.meta['prov_code']
            prov_name = response.meta['prov_name']
            city_url=tr.xpath('./td[1]/a/@href').extract_first()
            city_code=tr.xpath('./td[1]/a/text()').extract_first()
            city_name=tr.xpath('./td[2]/a/text()').extract_first()
            print(prov_code,prov_name,city_code,city_name)

            if city_url:
                print(city_url)
                yield response.follow(city_url,dont_filter=True,meta={'prov_code':prov_code,'prov_name':prov_name,'city_code':city_code,'city_name':city_name},callback=self.third_parse)

    def third_parse(self, response):
        print('第三级页面开始爬取')
        tr_list=response.xpath('//tr[@class="countytr"]')
        for tr in tr_list:
            prov_code = response.meta['prov_code']
            prov_name = response.meta['prov_name']
            city_code = response.meta['city_code']
            city_name = response.meta['city_name']

            county_url=tr.xpath('./td[1]/a/@href').extract_first()
            county_code=tr.xpath('./td[1]/a/text()').extract_first()
            county_name=tr.xpath('./td[2]/a/text()').extract_first()
            print(prov_code, prov_name, city_code, city_name,county_code,county_name)
            if county_url:
                print(county_url)
                yield response.follow(county_url,dont_filter=True,meta={'prov_code':prov_code,'prov_name':prov_name,'city_code':city_code,'city_name':city_name,'county_code':county_code,'county_name':county_name},callback=self.fourth_parse)

    def fourth_parse(self, response):
        print('第四级页面开始爬取')
        tr_list=response.xpath('//tr[@class="towntr"]')
        for tr in tr_list:
            prov_code = response.meta['prov_code']
            prov_name = response.meta['prov_name']
            city_code = response.meta['city_code']
            city_name = response.meta['city_name']
            county_code = response.meta['county_code']
            county_name = response.meta['county_name']

            town_url=tr.xpath('./td[1]/a/@href').extract_first()
            town_code=tr.xpath('./td[1]/a/text()').extract_first()
            town_name=tr.xpath('./td[2]/a/text()').extract_first()
            print(prov_code, prov_name, city_code, city_name,county_code,county_name,town_code,town_name)

            if town_url:
                print(town_url)
                yield response.follow(town_url,dont_filter=True,meta={'prov_code':prov_code,'prov_name':prov_name,'city_code':city_code,'city_name':city_name,'county_code':county_code,'county_name':county_name,'town_code':town_code,'town_name':town_name},callback=self.fifth_parse)

    def fifth_parse(self, response):
        print('第五级页面开始爬取')
        tr_list=response.xpath('//tr[@class="villagetr"]')
        for tr in tr_list:
            stat=StatsItem()
            prov_code=response.meta['prov_code']
            prov_name=response.meta['prov_name']
            city_code=response.meta['city_code']
            city_name=response.meta['city_name']
            county_code=response.meta['county_code']
            county_name=response.meta['county_name']
            town_code=response.meta['town_code']
            town_name=response.meta['town_name']

            village_code=tr.xpath('./td[1]/text()').extract_first()
            village_name=tr.xpath('./td[3]/text()').extract_first()
            print(prov_code, prov_name, city_code, city_name,county_code,county_name,town_code,town_name,village_code,village_name)

            stat['prov_code']=prov_code
            stat['prov_name']=prov_name
            stat['city_code']=city_code
            stat['city_name']=city_name
            stat['county_code']=county_code
            stat['county_name']=county_name
            stat['town_code']=town_code
            stat['town_name']=town_name
            stat['village_code']=village_code
            stat['village_name']=village_name

            yield stat
