
from urllib.request import urlopen
from urllib.parse import quote
import bs4

# name = __file__.split("\\")[-1][:-3]
name = "공부하는법"
num_per_page = range(1,11)#한페이지 10개
pages = range(1,151)# 10개 페이지
detail_address="D:\private\project\main_project\\"

#1. url 긁어오기
for page in pages:
    url = f"https://kin.naver.com/search/list.nhn?query={quote(name)}&page={page}"
    

    source = urlopen(url).read()
    source_bs4 = bs4.BeautifulSoup(source,"html.parser")
#    urls=[]
    print(f"{page},{url}")
    for num in num_per_page:
        url_under=source_bs4.select(f'#s_content > div.section > ul > li:nth-of-type({num}) > dl > dt > a')[0]["href"]
                                      #s_content > div.section > ul > li:nth-child(1) > dl > dt > a
        # print(f"{page}_{num},{url_under}")
        url_under=url_under.replace("§","%C2%A7")
       # urls.append(url_under)
    # print(urls)
        with open(f"{detail_address}urls_{name}.txt",'a',encoding='utf-8') as file:
                file.write(f"{page}_{num},")
                file.write(url_under+"\n")


