from selenium import webdriver
import time

driver  = webdriver.Chrome("c:/PythonHome/chromedriver.exe")
driver.implicitly_wait(3)#창이 켜질 때가지 기다림<-인터넷 접속 속도/컴퓨터의 사양에 따라/3초/1초도 충분 테스트필요

# num_per_page = list(str(range(1,21)))
num_per_page = list(range(1,11))
pages = [1]#list(range(1,10))
data_ls = list()
for page in pages:

    for num in num_per_page:
        # print(num)

        url = f'https://kin.naver.com/userinfo/answerList.nhn?u=w6lLUADsTiE2WDOrNVtf1Qxgc3ft9bDXpkXY1Mua2f4%3D&isSearch=true&query=%EC%9E%90%EA%B2%A9%EC%A6%9D&sd=answer&y=0&section=qna&isWorry=false&x=0&page={page}'
        xpath = f'//*[@id="au_board_list"]/tr[{num}]/td[1]/a'

        question_selector = '#content > div.question-content > div > div.c-heading._questionContentsArea.c-heading--default-old > div.c-heading__title > div > div.title'
        question_detail_selector = '#content > div.question-content > div > div.c-heading._questionContentsArea.c-heading--default-old > div.c-heading__content'

        driver.get(url)

        search_res = driver.find_element_by_xpath('//*[@id="au_board_list"]/tr['+f'{num}'+']/td[1]/a')

        search_res.click()

        driver.switch_to_window(driver.window_handles[1])


        question = driver.find_element_by_css_selector(question_selector).text
        print(question)
        question_detail = driver.find_element_by_css_selector(question_detail_selector).text

        answer_num = 1

        while True:

            answer_writer_selector = '#answer_'+f'{answer_num}'+' > div.c-heading-answer > div.c-heading-answer__body > div.c-heading-answer__title > p > a'
            answer_detail_selector = '#answer_'+f'{answer_num}'+' > div._endContents.c-heading-answer__content'

            try :
                answer_writer = driver.find_element_by_css_selector(answer_writer_selector).text
                answer_detail = driver.find_element_by_css_selector(answer_detail_selector).text
            except :
                pass

            if answer_writer == '자격증 따기 님 답변':
                print(answer_writer)
                print(answer_detail)
                break

            answer_num += 1

driver.quit()