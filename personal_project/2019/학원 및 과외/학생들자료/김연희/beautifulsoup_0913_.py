from urllib.request import urlopen
import bs4
# name_list=["농업","물가","상업","수산업","식생활","풍속","금융"]
name_list=["재정"]


detail_address="D:\private\lecture\python_prac\학원 및 과외\학생들자료\김연희\\"
for name in name_list:
    
######################part1-start#############################

    # urls=[]
    # with open(f"{detail_address}{name}.txt",'r',encoding='utf-8') as file:
    #     lines=file.readlines()
    #     for i,line in enumerate(lines):

    #         url=line.split("^")[-1]
    #         urls.append(url)

    # with open(f"{detail_address}urls_{name}.txt",'w',encoding='utf-8') as file:
    #     for url in urls:
    #         file.write(url)

######################part1-end#############################


######################part2-start#############################
    with open(f"{detail_address}urls_{name}.txt",'r',encoding='utf-8') as file:
        lines=file.readlines()
        for i,line in enumerate(lines):
            url=line
            # i+=2882
            print(i)
            source = urlopen(url).read()
            source_bs4 = bs4.BeautifulSoup(source,"html.parser")

            title1=source_bs4.select('#cont_area > div.cont_in_left.cont_full > div.page_tit.clear2.pl_20 > h3')[0].text
            text1=source_bs4.select('#cont_area > div.cont_in_left.cont_full > div.ins_view_wrap.clear2 > div.ins_view.ins_view_left.w50_w50 > div > div > p')
            with open(f"{detail_address}results_{name}.txt",'a',encoding='utf-8') as file:
                
                file.write(f"{i}\n")
                file.write(title1+"\n")
                for t in text1:
                    
                    file.write(t.text)
                file.write("\n")
            
######################part2-end#############################





# driver  = webdriver.Chrome("c:/PythonHome/chromedriver.exe")
# driver.implicitly_wait(3)#창이 켜질 때가지 기다림<-인터넷 접속 속도/컴퓨터의 사양에 따라/3초/1초도 충분 테스트필요

# name = __file__.split("\\")[-1][:-3]
# search_address=f"http://sillok.history.go.kr/manInfo/branchList.do"

# timesleep=0.5
# under = 10

# for page in range(50,51):
#     for under_page in range(2,under+1):
#         # try:
#         print("*"*20+"page"+"*"*20)
#         print(page)
#         print("*"*20+"page"+"*"*20)
#         url = search_address
#         xpath = f'//*[@id="cont_area"]/div/table[3]/tbody/tr[6]/th/a'   
#         #크롬 f12(개발자도구) 주부식, f12, 엘리먼트옆 클릭하고 식생활 클릭, 오른마우스 copy xpath

#         driver.get(url)
#         time.sleep(timesleep)#크롤링 속도에 맞춰주기 위해

#         search_res = driver.find_element_by_xpath(xpath)
#         page_url=driver.find_element_by_xpath(xpath).get_attribute('href')

#         search_res.click()

#         ########################################################
#         xpath_2 = f'//*[@id="cont_area"]/div[1]/div[4]/span[{under_page}]/a'
        
#                 # //*[@id="cont_area"]/div[1]/ul[2]/li[50]/dl/dt/a
#         # 식생활내에 첫번째줄만 클릭해서 들어간 상태                        

#         search_res = driver.find_element_by_xpath(xpath_2)
#         page_url=driver.find_element_by_xpath(xpath_2).get_attribute('href')

#         search_res.click()
#         ########################################################
        
#         xpath_3 = f'//*[@id="cont_area"]/div[1]/ul[2]/li[{page}]/dl/dt/a'
                    
#         # //*[@id="cont_area"]/div[1]/ul[2]/li[50]/dl/dt/a
#         # 식생활내에 첫번째줄만 클릭해서 들어간 상태                        

#         search_res = driver.find_element_by_xpath(xpath_3)
#         page_url=driver.find_element_by_xpath(xpath_3).get_attribute('href')

#         search_res.click()
#         ########################################################

#         title1=driver.find_element_by_css_selector('#cont_area > div.cont_in_left.cont_full > div.page_tit.clear2.pl_20 > h3').text
#         text1 = driver.find_element_by_css_selector('#cont_area > div.cont_in_left.cont_full > div.ins_view_wrap.clear2 > div.ins_view.ins_view_left.w100_w0 > div > div > p').text

#         print(title1)

#         with open(f"{name}.txt",'a',encoding='utf-8') as file:
#             file.write(title1)
#             file.write(",\n")
#             file.write(text1)
#             file.write(",\n")
#         print(f"error:{page}")
#         break  
# driver.quit()