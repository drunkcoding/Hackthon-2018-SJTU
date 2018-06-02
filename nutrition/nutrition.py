from crawler import GetResultCrawler
from hackscrap.hackscrap.spiders.nutrition_spider import NutritionSpider


def scrap_nutrition(food=""):
    crawler = GetResultCrawler()
    scrapped_item = crawler.crawl({NutritionSpider: {"food": food}})
    return scrapped_item[0]


'''
if __name__ == "__main__":
    item = scrap_nutrition("sake")
    print(item)
'''

