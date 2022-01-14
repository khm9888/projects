from selenium import webdriver
import time

browser = webdriver.Chrome('D:\downloads\chromedriver_win32/chromedriver')

browser.get('http://www.naver.com')
 
login_bt=browser.find_element_by_class_name('link_login')
# login_bt=browser.find_element_by_class_name('lg_local_btn')
login_bt.click() 
 
# ID를 입력한다
id=browser.find_element_by_id('id')
id.send_keys('khm9888')

# PWD를 입력 한다
id=browser.find_element_by_id('pw')
id.send_keys('goals3068as!')
time.sleep(1)#초 단위로 작동한다.
 
naver_submit=browser.find_element_by_class_name('btn_global')
naver_submit.click()

time.sleep(20)#초 단위로 작동한다.