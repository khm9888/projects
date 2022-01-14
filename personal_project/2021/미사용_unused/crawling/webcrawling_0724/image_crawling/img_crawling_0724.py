from bs4 import BeautifulSoup as bs
import requests
from urllib.parse import quote_plus
 
baseUrl = 'https://search.naver.com/search.naver?where=image&sm=tab_jum&query='
# plusUrl = input('검색어 입력: ') 
plusUrl = "뱀"
# crawl_num = int(input('크롤링할 갯수 입력(최대 50개): '))
crawl_num = 5
url = baseUrl + quote_plus(plusUrl) # 한글 검색 자동 변환
# print(url)
response = requests.get(url)
# print(response)

response.raise_for_status()
html = response.content
soup = bs(html, "html.parser")
# print("soup")
# print(soup)
# print(len(soup))
urls = list()


imgtags = soup.find_all('img')[1:crawl_num+1]

for tag in imgtags:
    
    imgurl = tag["src"].rsplit("&")[0]
    urls.append(imgurl)

print(urls)
print()

for i in urls:
    print(i)
 
img_dir = r'C:\Users\khg98\Google 드라이브\공부\code\python_code\_202107_project\0724\img_folder/'
 
n = 1
for imgUrl in urls:
    print(n)
    print(imgUrl)
    img = requests.get(imgUrl)
    print(img)
    with open(f'{img_dir}/{n}.jpg','wb') as f: # w - write b - binary
        print(img)
        f.write(img.content)
        n+=1

print('Image Crawling is done.')

