from selenium import webdriver
import time

driver  = webdriver.Chrome("c:/PythonHome/chromedriver.exe")
driver.implicitly_wait(3)#창이 켜질 때가지 기다림<-인터넷 접속 속도/컴퓨터의 사양에 따라/3초/1초도 충분 테스트필요

# y = range(1,11)#한페이지 10개
# pages = range(92,101)# 10개 페이지


name = __file__.split("\\")[-1][:-3]
search_address=f"http://sillok.history.go.kr/manInfo/branchList.do"
driver.get(search_address)
timesleep=0.5

page_number=8
under_page=0

########################################################
for page in range(1,page_number+1):
    third_page=1
    while True:
        try:
            print("*"*20+"third_page"+"*"*20)
            print(third_page)
            print("*"*20+"third_page"+"*"*20)
            url = search_address
            xpath = f'//*[@id="cont_area"]/div/table[3]/tbody/tr[6]/td/ul/li[1]/a'
            #어느왕?

            driver.get(url)
            time.sleep(timesleep)#크롤링 속도에 맞춰주기 위해

            search_res = driver.find_element_by_xpath(xpath)
            page_url=driver.find_element_by_xpath(xpath).get_attribute('href')

            search_res.click()

            ########################################################

            xpath_2 = f'//*[@id="cont_area"]/div/table[3]/tbody/tr[6]/td/ul/li[1]/a'
                        # //*[@id="cont_area"]/div/div[2]/ul[2]/li[1]/ul/li[2]/a
            #몇년/몇월??


            search_res = driver.find_element_by_xpath(xpath_2)
            page_url=driver.find_element_by_xpath(xpath_2).get_attribute('href')

            search_res.click()

            ########################################################


            xpath_3 = f'//*[@id="cont_area"]/div[1]/div[3]/div/dl/dd/ul/li[{third_page}]/a'
                    # //*[@id="cont_area"]/div[1]/div[3]/div/dl/dd/ul/li[2]/a
                    # //*[@id="cont_area"]/div[1]/div[3]/div/dl/dd/ul/li[19]/a
            #몇번째일?
            
            search_res = driver.find_element_by_xpath(xpath_3)
            page_url=driver.find_element_by_xpath(xpath_3).get_attribute('href')

            search_res.click()

            ########################################################

            title1=driver.find_element_by_css_selector('#cont_area > div.cont_in_left.cont_full > div.page_tit.clear2.pl_20 > h3').text
            text1 = driver.find_element_by_css_selector('#cont_area > div.cont_in_left.cont_full > div.ins_view_wrap.clear2 > div.ins_view.ins_view_left.w50_w50 > div > div').text
            
            print(title1)

            with open(f"{name}.txt",'a',encoding='utf-8') as file:
                file.write(title1)
                file.write(",\n")
                file.write(text1)
                file.write(",\n")
            
            third_page+=1
        except:
            print(f"error:{third_page}")
            break
    
driver.quit()


