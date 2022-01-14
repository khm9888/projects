from selenium import webdriver
import time

driver  = webdriver.Chrome("c:/PythonHome/chromedriver.exe")
driver.implicitly_wait(3)#창이 켜질 때가지 기다림<-인터넷 접속 속도/컴퓨터의 사양에 따라/3초/1초도 충분 테스트필요

num_per_page = range(1,21)#한페이지 20개
pages = range(1,11)# 10개 페이지

data_ls = list()

for page in pages:
    for num in num_per_page:
        url = f'''https://kin.naver.com/userinfo/answerList.nhn?u=w6lLUADsTiE2WDOrNVtf1Qxgc3ft9bDXpkXY1Mua2f4%3D&isSearch=true
        &query=%EC%9E%90%EA%B2%A9%EC%A6%9D&sd=answer&y=0&section=qna&isWorry=false&x=0&page={page}'''
        xpath = f'//*[@id="au_board_list"]/tr[{num}]/td[1]/a'

        question_selector = '#content > div.question-content > div > div.c-heading._questionContentsArea.c-heading--default-old > div.c-heading__title > div > div.title'
        question_detail_selector = '#content > div.question-content > div > div.c-heading._questionContentsArea.c-heading--default-old > div.c-heading__content'
        # # is ID / 
        driver.get(url)
        time.sleep(2)#크롤링 속도에 맞춰주기 위해

        search_res = driver.find_element_by_xpath(f'//*[@id="au_board_list"]/tr[{num}]/td[1]/a')

        search_res.click()
        time.sleep(2)
        
        driver.switch_to_window(driver.window_handles[1])#전환된 화면을 전환 선택하기 위한 메서드
        time.sleep(1)

        try :
            question = driver.find_element_by_css_selector(question_selector).text#있는거
        except :
            try :
                question = driver.find_element_by_css_selector('#content > div.question-content > div > div.c-heading._questionContentsArea.c-heading--default > div.c-heading__title > div > div').text#이미지 or x
            except :
                question = driver.find_element_by_css_selector('#content > div.question-content > div > div.c-heading._questionContentsArea.c-heading--multiple > div.c-heading__title > div > div').text#이미지 or x
                pass
        question = question+'\n'

        try :
            question_detail = driver.find_element_by_css_selector(question_detail_selector).text#내용 있으면
        except :
            question_detail = 'Null'#없으면 (이미지 같은 경우는 확인해봐야함)
            pass
        question_detail = question_detail+'\n'

        data_ls.append(question)
        data_ls.append(question_detail)

        answer_num = 1

        while True:

            answer_writer_selector = f'#answer_{answer_num} > div.c-heading-answer > div.c-heading-answer__body > div.c-heading-answer__title > p'
            answer_detail_selector = f'#answer_{answer_num} > div._endContents.c-heading-answer__content'
            # print(answer_num)
            try :
                answer_writer = driver.find_element_by_css_selector(answer_writer_selector).text
            except:
                pass
            
            try :
                answer_detail = driver.find_element_by_css_selector(answer_detail_selector).text
            except:
                pass

            if answer_writer == '자격증 따기 님 답변' and answer_writer != '비공개 답변':
                answer_detail = answer_detail[:-74]+'\n'
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
            

        driver.close()
        time.sleep(1)
        driver.switch_to_window(driver.window_handles[0])
        time.sleep(1)
    
driver.quit()

file = open("page11-page20.txt",'a',encoding='utf-8')
for resum in data_ls:
    file.write(resum)
file.close()