import scrapy
import json
from ..items import ApiPractiseItem



class CoinDataSpider(scrapy.Spider):
    name = "coin_data"
    allowed_domains = ["s3.coinmarketcap.com"]
    start_urls = ["https://s3.coinmarketcap.com/generated/core/crypto/web-search.json"]
    
   

    def parse(self, response):
        resp = json.loads(response.body)
        # print(resp)
        fields = resp["fields"]
        values = resp['values']
        item = ApiPractiseItem()
        for value in values:
            item["id"] = value[0]
            item["name"] = value[1]
            item["symbol"]= value[2]
            item["slug"] = value[3]
            item["type"] = value[4]
            item["rank"] = value[5]
            item["address"] = value[6]
            item["search_socre"] = value[7]
            
        yield item
        
      

