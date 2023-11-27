# Scrapy (SEO and web scraping)
import scrapy
from scrapy.crawler import CrawlerProcess

# Spider
class MySpider(scrapy.Spider):
  name = "my_spider"

  urls = (["https://hackstore.lat/page/" + str(page) +"/" for page in range(1, 50)])

  # print(urls)

  start_urls = urls

  def parse(self, response):
    print("Process started...")

    # Rules (using XPATH) - Tools copy XPath completo
    # Get "a" tags from the web site - at the end of XPath //<tag>
    a_elements = response.xpath("/html/body/div[3]/div[2]/div[1]/div[1]//a")
    # print("A elements size", len(a_elements))
    for a in a_elements:
      # print(a)
      title = a.xpath("@title").extract_first()
      href = a.xpath("@href").extract_first()

      # print("Title:", title)
      # print("href:", href)

      with open("lab5.txt", "a") as file:
        file.write("Title: " + title + "\n")
        file.write("href: " + href + "\n\n")

with open("lab5.txt", "w") as file:
  file.write("")
process = CrawlerProcess()
process.crawl(MySpider)
process.start()
