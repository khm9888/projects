from selenium import webdriver
import requests
from bs4 import BeautifulSoup
driver  = webdriver.Chrome("c:/PythonHome/chromedriver.exe")

#  페이지별로 기업 번호 불러오기
num = list(range(1,2))
for i in num:
    try:
        corp_list = []
        driver.get("http://people.incruit.com/resumeguide/pdslist.asp?page=" +f'{i}'+ "&listseq=1&sot=&pds1=1&pds2=11&pds3=&pds4=&schword=&rschword=&lang=&price=&occu_b_group=&occu_m_group=&occu_s_group=&career=&pass=&compty=&rank=&summary=&goodsty=")
        driver.implicitly_wait(5)
        table = driver.find_element_by_class_name('board_Tbl01')
        tbody = table.find_element_by_tag_name("tbody")
        for j in range(0,1):
            rows = tbody.find_elements_by_tag_name("tr")[j]
            body = rows.find_elements_by_tag_name("td.numcol")
            for index, value in enumerate(body):
                corp_list.append(value.text)
    except:
        continue

for i in corp_list:
    print(1)
    # try:
    driver.get("https://people.incruit.com/resumeguide/pdsview.asp?pds1=1&pds2=11&pdsno="+ i +"&listseq=&page=1&sot=0&pass=y")
    # 페이지 소스 가져오기
    # time.sleep(5)
    html = driver.page_source
    soup = BeautifulSoup(html,'lxml')
    resume = list(soup.find_all(class_='cont')[2].find_all('p',string=True))
    print(type(resume))
    print(len(resume))
    # print("resume")
    # print(resume)/
    sentences=[]
    for r in resume:
        k = r.string.split(".")
        for p in k:
            sentences.append(p)
    print(sentences)
    # print(2)
    temp=[]
    for res in sentences:#str
        print(3)
        temp.append(res.replace('\n','').replace('\t','').replace('\r',''))
    file = open("resume.txt",'a',encoding='utf-8')
    print(temp)
    for resum in temp:
        print(4)
        file.write(resum+"\n")
    file.close()
    # except:
    #     continue
driver.quit()