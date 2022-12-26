import scrapy
import json
from scrapy.crawler import CrawlerProcess
from doska.spiders import job_spider

process = CrawlerProcess()
process.crawl(job_spider.JobSpider)
process.start()

with open('jobs.json', 'w', encoding="utf-8") as json_file:
    json.dump(job_spider.jobs, json_file, indent=4, ensure_ascii=False)