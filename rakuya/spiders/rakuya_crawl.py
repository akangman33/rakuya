# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class RakuyaCrawlSpider(CrawlSpider):
    name = 'rakuya_crawl'
    allowed_domains = ['rakuya.com.tw']
    start_urls = ['https://www.rakuya.com.tw/search/rent_search/index?con=eJyrVkrOLKlUsopWMlCK1VFKySwuyEkE8pVyMotLlHSU8pOyMvNSQPJBIPni1MSi5AwQF6wtthYAibYUPw&upd=1']

    rules = (
        Rule(LinkExtractor(allow=r'https://www\.rakuya\.com\.tw/rent_item/info\?ehid\=.*'), callback='parse_item', follow=True),
        Rule(LinkExtractor(allow=r'https://www\.rakuya\.com\.tw/search/rent_search/.*\&page\=\d+')),
    )

    def parse_item(self, response):
        i = {}
        i['title'] = response.xpath('.//div[@class = "title-3"]/h2/span[@class = "title"]/text()').extract_first()
        i['address'] = response.xpath('.//div[@class = "block__title"]/h1[@class = "txt__address"]/text()').extract()[1]
        i['type'] = response.xpath('.//div[@class = "block__info-sub"]/div[1]/ul/li/span[contains(text(),"類型")]/../span[2]/text()').extract_first()
        i['structure'] = response.xpath('.//div[@class = "block__info-sub"]/div[1]/ul/li/span[contains(text(),"格局")]/../span[2]/text()').extract_first()
        i['floor'] = response.xpath('.//div[@class = "block__info-sub"]/div[1]/ul/li/span[contains(text(),"樓層/樓高")]/../span[2]/text()').extract_first()
        i['legal_use'] = response.xpath('.//div[@class = "block__info-sub"]/div[1]/ul/li/span[contains(text(),"法定用途")]/../span[2]/text()').extract_first()
        i['house_age'] = response.xpath('.//div[@class = "block__info-sub"]/div[1]/ul/li/span[contains(text(),"屋齡")]/../span[2]/text()').extract_first()
        i['pings'] = response.xpath('.//div[@class = "block__info-sub"]/div[1]/ul/li/span[contains(text(),"使用坪數")]/../span[2]/text()').extract_first()
        i['oriented'] = response.xpath('.//div[@class = "block__info-sub"]/div[1]/ul/li/span[contains(text(),"朝向")]/../span[2]/text()').extract_first()
        i['material'] = response.xpath('.//div[@class = "block__info-sub"]/div[1]/ul/li/span[contains(text(),"隔間材質")]/../span[2]/text()').extract_first()
        i['property'] = response.xpath('.//div[@class = "block__info-sub"]/div[1]/ul/li/span[contains(text(),"產權登記")]/../span[2]/text()').extract_first()
        i['environment'] = response.xpath('.//div[@class = "block__info-sub"]/div[1]/ul/li/span[contains(text(),"物件環境")]/../span[2]/text()').extract_first()
        i['short_lease'] = response.xpath('.//div[@class = "block__info-sub"]/div[2]/ul/li/span[contains(text(),"短期租賃")]/../span[2]/text()').extract_first()
        i['cook'] = response.xpath('.//div[@class = "block__info-sub"]/div[2]/ul/li/span[contains(text(),"開伙")]/../span[2]/text()').extract_first()
        i['moveable_day'] = response.xpath('.//div[@class = "block__info-sub"]/div[2]/ul/li/span[contains(text(),"可遷入日")]/../span[2]/text()').extract_first()
        i['pet'] = response.xpath('.//div[@class = "block__info-sub"]/div[2]/ul/li/span[contains(text(),"飼養寵物")]/../span[2]/text()').extract_first()
        i['rent'] = response.xpath('.//div[@class = "block__info-sub"]/div[2]/ul/li/span[contains(text(),"租金內含")]/../span[2]/text()').extract_first()
        i['gender'] = response.xpath('.//div[@class = "block__info-sub"]/div[2]/ul/li/span[contains(text(),"性別要求")]/../span[2]/text()').extract_first()
        i['deposit'] = response.xpath('.//div[@class = "block__info-sub"]/div[2]/ul/li/span[contains(text(),"押金")]/../span[2]/text()').extract_first()
        i['identity'] = response.xpath('.//div[@class = "block__info-sub"]/div[2]/ul/li/span[contains(text(),"身分要求")]/../span[2]/text()').extract_first()
        i['landlord_living'] = response.xpath('.//div[@class = "block__info-sub"]/div[2]/ul/li/span[contains(text(),"房東同住")]/../span[2]/text()').extract_first()
        i['parking'] = response.xpath('.//div[@class = "block__info-sub"]/div[3]/ul/li/span[contains(text(),"車位")]/../span[2]/text()').extract_first()
        i['school'] = ",".join(response.xpath('.//div[@class = "block__map"]/div/h4[contains(text(),"鄰近學校")]/../ul/li/text()').extract())
        i['market'] = ",".join(response.xpath('.//div[@class = "block__map"]/div/h4[contains(text(),"鄰近市場")]/../ul/li/text()').extract())
        i['park'] = ",".join(response.xpath('.//div[@class = "block__map"]/div/h4[contains(text(),"鄰近公園")]/../ul/li/text()').extract())
        i['traffic'] = ",".join(response.xpath('.//div[@class = "block__map"]/div/h4[contains(text(),"鄰近交通")]/../ul/li/text()').extract())

        print(i, '**************'*10)
        return i
