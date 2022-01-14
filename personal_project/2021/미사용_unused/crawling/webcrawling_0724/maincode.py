# 배당 정보 investing 을 통해서 가져오기

from urllib.request import urlopen
from urllib.parse import quote
import bs4
import requests
# import time


# https://kr.investing.com/equities/americas

#1. url 긁어오기


url = f"https://kr.investing.com/equities/americas"

response = requests.get(url)

html = response.text
# source_bs4 = bs4.BeautifulSoup(source,"html.parser")
print(html)
# source = urlopen(url).read()




# print(f"{url}")

# url_under=source_bs4.select(f'#s_content > div.section > ul > li:nth-of-type({num}) > dl > dt > a')[0]["href"]
