# Beautiful Soup (web site clone or web scraping)
from bs4 import BeautifulSoup # pip install bs4
import urllib.request as ur
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

web_site = ur.urlopen("https://website-url-to-clone")
content = web_site.read()

# print(content)

bs = BeautifulSoup(content, "lxml")

with open("website.html", "w") as file:
  file.write(bs.prettify())

# Search by tags
# print(bs.title)
# print(bs.title.string)
# print(bs.meta)

# Search by attributes
# print(bs.meta["charset"])

# Advance search
# print(bs.find_all("meta"))

# hrefTags = bs.find_all("a")

# for url in hrefTags:
#   print(url["href"])

# Search by class
# header = bs.find("div", {"class": "header"})
# print(header)

# header_a = header.find_all("a")
# for a in header_a:
#   print(a)

# print(header.find("div", {"class": "section-inner"}))
