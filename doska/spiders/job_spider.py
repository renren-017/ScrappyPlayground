import scrapy
import csv


class JobUrlSpider(scrapy.Spider):
    name = "urls"
    base_url = "http://resume.doska.kg"

    def start_requests(self):
        open('job_urls.csv', 'w').close()

        urls = ["http://resume.doska.kg/vacancy/&sortby=new",
                  "http://resume.doska.kg/vacancy/&page=2&sortby=new"]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        filename = 'job_urls.csv'
        with open(filename, 'a') as out:
            for job_title in response.css("div.list_full_title"):
                job_url = job_title.css("a.title_url").attrib["href"]
                full_url = self.base_url + job_url
                out.write(full_url+"\n")

