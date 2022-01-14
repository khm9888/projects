from selenium import webdriver
import time

driver  = webdriver.Chrome("c:/PythonHome/chromedriver.exe")
driver.implicitly_wait(3)#창이 켜질 때가지 기다림<-인터넷 접속 속도/컴퓨터의 사양에 따라/3초/1초도 충분 테스트필요

num_per_page = range(1,3)#한페이지 20개
pages = range(1,3)# 10개 페이지

data_ls = list()


expert_address=f"https://kin.naver.com/userinfo/answerList.nhn?u=2Du%2BPM59USNIsD7YIbLhO6mdRDB%2FdEzwO4gVkrfArKo%3D"
driver.get(expert_address)

expert_nick=driver.find_element_by_css_selector('#au_main_profile_box > div.my_personal_inner.my_personal_simple > div.profile_section._profile_section > div > div > a > strong').text
print(expert_nick)

crawling = dict()

word_list=["레시피","법","요리법","맛있게"]

for page in pages:
    for num in num_per_page:
        print(f"num",num)
        url = expert_address+f'''&page={page}'''
        xpath = f'//*[@id="au_board_list"]/tr[{num}]/td[1]/a'

        question_selector = '''#content > div.question-content > div > div.c-heading._questionContentsArea.c-heading--default-old >
         div.c-heading__title > div > div.title'''
        question_detail_selector = '''#content > div.question-content > div > 
        div.c-heading._questionContentsArea.c-heading--default-old > div.c-heading__content'''


       
        driver.get(url)
        time.sleep(1)#크롤링 속도에 맞춰주기 위해

        search_res = driver.find_element_by_xpath(xpath)

        search_res.click()
        time.sleep(1)

        #question_title
        try :
            question = driver.find_element_by_css_selector(question_selector).text#있는거
        except :
            try :
                question = driver.find_element_by_css_selector('#content > div.question-content > div > div.c-heading._questionContentsArea.c-heading--default > div.c-heading__title > div > div').text#이미지 or x
            except :
                question = driver.find_element_by_css_selector('#content > div.question-content > div > div.c-heading._questionContentsArea.c-heading--multiple > div.c-heading__title > div > div').text#이미지 or x
                pass
        question = question+'\n'

        #question_context
        try :
            question_detail = driver.find_element_by_css_selector(question_detail_selector).text#내용 있으면
        except :
            question_detail = 'Null'#없으면 (이미지 같은 경우는 확인해봐야함)
        question_detail = question_detail+'\n'

        data_ls.append(question)

        data_ls.append(question_detail)

        answer_num = 1

        while True:
            if answer_num >= 15:

                break

            answer_writer_selector = f'#answer_{answer_num} > div.c-heading-answer > div.c-heading-answer__body > div > p > a'
            #
            answer_detail_selector = f'#answer_{answer_num} > div._endContents.c-heading-answer__content > div._endContentsText.c-heading-answer__content-user > div'
            # print(answer_num)
            try :
                answer_writer = driver.find_element_by_css_selector(answer_writer_selector).text
            except:
                pass
            
            try :
                answer_detail = driver.find_element_by_css_selector(answer_detail_selector).text
            except:
                pass

            if answer_writer == f'{expert_nick} 님 답변' and answer_writer != '비공개 답변':
                answer_detail = answer_detail+'\n'
                answer_writer = answer_writer+'\n'

                data_ls.append(answer_writer)
                data_ls.append(answer_detail)

                print(f'{num}/20\t{page}-page')
                print(question_detail)
                print(question)
                print()
                print(answer_writer)
                print(answer_detail)
                print()

                break

            answer_num += 1
            

        # driver.close()
        time.sleep(1)
        # driver.switch_to_window(driver.window_handles[0])
        time.sleep(1)
    
driver.quit()

file = open("page11-page20.txt",'a',encoding='utf-8')
for resum in data_ls:
    file.write(resum)
file.close()