import multiprocessing as mp
from .crawler import GetResultCrawler
from .hackscrap.hackscrap.spiders.nutrition_spider import NutritionSpider


def _crawl(queue, food):
    crawler = GetResultCrawler()
    scrapped_item = crawler.crawl({NutritionSpider: {"food": food}})
    queue.put(scrapped_item[0])


def scrap_nutrition(food=""):
    q = mp.Queue()
    p = mp.Process(target=_crawl, args=(q, food))
    p.start()
    retval = q.get()
    p.join()

    return retval

'''
if __name__ == "__main__":
    item = scrap_nutrition("sake")
    print(item)
'''

