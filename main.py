import json
from twisted.internet import defer, reactor
from scrapy.crawler import CrawlerRunner
from doska.spiders import job_spider

runner = CrawlerRunner()


@defer.inlineCallbacks
def crawl():
    yield runner.crawl(job_spider.JobUrlSpider)
    yield runner.crawl(job_spider.JobSpider)
    reactor.stop()


crawl()
reactor.run()
with open('jobs.json', 'w', encoding="utf-8") as json_file:
    json.dump(job_spider.jobs, json_file, indent=4, ensure_ascii=False)
