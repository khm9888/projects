from selenium import webdriver
import time

driver  = webdriver.Chrome("c:/PythonHome/chromedriver.exe")
driver.implicitly_wait(3)#창이 켜질 때가지 기다림<-인터넷 접속 속도/컴퓨터의 사양에 따라/3초/1초도 충분 테스트필요

num_per_page = range(1,11)#한페이지 10개
pages = range(118,201)# 10개 페이지

search_address=f"https://kin.naver.com/search/list.nhn?query=요리+레시피"
driver.get(search_address)
timesleep=0.2

for page in pages:
    for num in num_per_page:
        page_dict=dict()
        # print(f"num",num)
        url = search_address+f'''&page={page}'''
        xpath = f'//*[@id="s_content"]/div[3]/ul/li[{num}]/dl/dt/a'

        question_selector = '''#content > div.question-content > div > div.c-heading._questionContentsArea.c-heading--default-old >
         div.c-heading__title > div > div.title'''
        question_detail_selector = '''#content > div.question-content > div > div.c-heading._questionContentsArea.c-heading--default-old > div.c-heading__content'''
                                     #content > div.question-content > div > div.c-heading._questionContentsArea.c-heading--multiple-old > div.c-heading__content
        driver.get(url)
        time.sleep(timesleep)#크롤링 속도에 맞춰주기 위해
        search_res = driver.find_element_by_xpath(xpath)

        page_url=driver.find_element_by_xpath(xpath).get_attribute('href')

        search_res.click()
        driver.switch_to.window(driver.window_handles[1])
        time.sleep(timesleep)
        #question_title
        try :
            question = driver.find_element_by_css_selector(question_selector).text#있는거
        except :
            try :
                question = driver.find_element_by_css_selector('#content > div.question-content > div > div.c-heading._questionContentsArea.c-heading--default > div.c-heading__title > div > div').text#이미지 or x
            except :
                try:
                    question = driver.find_element_by_css_selector('#content > div.question-content > div > div.c-heading._questionContentsArea.c-heading--multiple > div.c-heading__title > div > div').text#이미지 or x
                except:
                    question = driver.find_element_by_css_selector(' #content > div.question-content > div > div.c-heading._questionContentsArea.c-heading--multiple-old > div.c-heading__content').text#이미지 or x
        #question_context
        try :
            question_detail = driver.find_element_by_css_selector(question_detail_selector).text#내용 있으면
        except :
            question_detail = 'null' #없으면 (이미지 같은 경우는 확인해봐야함)



        # print("-"*30)
        # print("step1 질문긁어오기")
        # print(question)
        # print(question_detail)
        # print("-"*30)
        page_dict["question"]=question
        page_dict["question_detail"]=question_detail

        cnt=driver.find_element_by_css_selector("#answerArea > div.answer-content__inner > div.c-classify.c-classify--sorting > div.c-classify__title-part > h3 > em").text
        cnt=int(cnt)

        answer_writer_selector = f'#answer_{cnt} > div.c-heading-answer > div.c-heading-answer__body > div > p > a'
                                    #answer_1 > div.c-heading-answer > div.c-heading-answer__body > div.c-heading-answer__title > p > a
        answer_detail_selector = f'#answer_{cnt} > div._endContents.c-heading-answer__content > div._endContentsText.c-heading-answer__content-user'
                                    #answer_2 > div._endContents.c-heading-answer__content > div._endContentsText.c-heading-answer__content-user            

        try :
            answer_writer = driver.find_element_by_css_selector(answer_writer_selector).text
            # print("test")
        except:
            # print("test2")
            if cnt!=1:
                try:
                    answer_writer_selector = f'#answer_{cnt-1} > div.c-heading-answer > div.c-heading-answer__body > div > p > a'
                    answer_writer = driver.find_element_by_css_selector(answer_writer_selector).text
                    # print("test4")
                except:
                    # print("test3")
        
                    answer_writer='null'
            elif cnt==1:
                try:
                    answer_writer_selector = f'#answer_1 > div.c-heading-answer.c-heading-answer--backout > div.c-heading-answer__body > div.c-heading-answer__title > p'
                                                #answer_1 > div.c-heading-answer > div.c-heading-answer__body > div.c-heading-answer__title > p
                    answer_writer = driver.find_element_by_css_selector(answer_writer_selector).text
                except:
                    try:
                        answer_writer_selector = f'#answer_1 > div.c-heading-answer > div.c-heading-answer__body > div.c-heading-answer__title > p'                          
                        answer_writer = driver.find_element_by_css_selector(answer_writer_selector).text  
                    except:
                        answer_writer='null'

                
        try :
            answer_detail = driver.find_element_by_css_selector(answer_detail_selector).text
        except:

            if cnt!=1:
                try:
                    answer_detail_selector = f'#answer_{cnt-1} > div._endContents.c-heading-answer__content > div._endContentsText.c-heading-answer__content-user'        
                    answer_detail = driver.find_element_by_css_selector(answer_detail_selector).text
                except:
                    try:
                        answer_detail_selector = f'#answer_{cnt-1} > div._endContents.c-heading-answer__content > div._endContentsText.c-heading-answer__content-user> div > div'        
                        answer_detail = driver.find_element_by_css_selector(answer_detail_selector).text
                    except:
                        answer_detail ='null'
        if answer_writer=="null":
            page_dict["answer_writer"]=answer_writer
        else:
            page_dict["answer_writer"]=answer_writer[:-len(" 님 답변")]
        page_dict["answer_detail"]=answer_detail
        page_dict["url"]=page_url
        page_dict["index"]=f"{page}_{num}"
        print("-"*20)
        print(f'num:{num}/10\t page:{page}-page')
        for i in page_dict.values():
            print(i)
        print("-"*20)
        print()
        driver.close()
        time.sleep(timesleep)
        driver.switch_to_window(driver.window_handles[0])
        time.sleep(timesleep)
        filenumber=(num+page*10)//100+1
        with open(f"data/crawling_data/a_{filenumber}.txt",'a',encoding='utf-8') as file:
            file.write(str(page_dict))
            file.write(",\n")
driver.quit()


