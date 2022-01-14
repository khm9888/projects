# https://wikidocs.net/book/4706

# ################### 마우스 자동화 - pyautogui 사용법 ######################

# import pyautogui

# # 좌표 객체 얻기 
# position = pyautogui.position()

# # 화면 전체 크기 확인하기
# print(pyautogui.size())

# # x, y 좌표
# print(position.x)
# print(position.y)

# # 마우스 이동 (x 좌표, y 좌표)
# pyautogui.moveTo(500, 500)

# # 마우스 이동 (x 좌표, y 좌표 2초간)
# pyautogui.moveTo(100, 100, 2)  

# # 마우스 이동 ( 현재위치에서 )
# pyautogui.moveRel(200, 300, 2)

# # 마우스 클릭
# pyautogui.click()

# # 2초 간격으로 2번 클릭
# pyautogui.click(clicks= 2, interval=2)

# # 더블 클릭
# pyautogui.doubleClick()

# # 오른쪽 클릭
# pyautogui.click(button='right')

# # 스크롤하기 
# pyautogui.scroll(10)

# # 드래그하기
# pyautogui.drag(0, 300, 1, button='left')

# # https://pyautogui.readthedocs.io/en/latest/mouse.html 


# ################### 키보드 자동화 - pyautogui 사용법 ######################
# import pyautogui 

# pyautogui.write('hello world!') # 괄호 안의 문자를 타이핑 합니다.
# pyautogui.write('hello world!', interval=0.25) # 각 문자를 0.25마다 타이핑합니다.

# import pyautogui 
# import pyperclip

# pyperclip.copy("안녕하세요") # 클립보드에 텍스트를 복사합니다. 
# pyautogui.hotkey('ctrl', 'v') # 붙여넣기 (hotkey 설명은 아래에 있습니다.)

# pyautogui.press('shift') # shift 키를 누릅니다.
# pyautogui.press('ctrl') # ctrl 키를 누릅니다.
 
# pyautogui.keyDown('ctrl') # ctrl 키를 누른 상태를 유지합니다.
# pyautogui.press('c') # c key를 입력합니다. 
# pyautogui.keyUp('ctrl') # ctrl 키를 뗍니다. 

# pyautogui.press(['left', 'left', 'left']) # 왼쪽 방향키를 세번 입력합니다.
# pyautogui.press('left', presses=3) # 왼쪽 방향키를 세번 입력합니다. 
# pyautogui.press('enter', presses=3, interval=3) # enter 키를 3초에 한번씩 세번 입력합니다. 

# pyautogui.hotkey('ctrl', 'c') # ctrl + c 키를 입력합니다. 

# '''

# ['\t', '\n', '\r', ' ', '!', '"', '#', '$', '%', '&', "'", '(',
# ')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7',
# '8', '9', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`',
# 'a', 'b', 'c', 'd', 'e','f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
# 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~',
# 'accept', 'add', 'alt', 'altleft', 'altright', 'apps', 'backspace',
# 'browserback', 'browserfavorites', 'browserforward', 'browserhome',
# 'browserrefresh', 'browsersearch', 'browserstop', 'capslock', 'clear',
# 'convert', 'ctrl', 'ctrlleft', 'ctrlright', 'decimal', 'del', 'delete',
# 'divide', 'down', 'end', 'enter', 'esc', 'escape', 'execute', 'f1', 'f10',
# 'f11', 'f12', 'f13', 'f14', 'f15', 'f16', 'f17', 'f18', 'f19', 'f2', 'f20',
# 'f21', 'f22', 'f23', 'f24', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9',
# 'final', 'fn', 'hanguel', 'hangul', 'hanja', 'help', 'home', 'insert', 'junja',
# 'kana', 'kanji', 'launchapp1', 'launchapp2', 'launchmail',
# 'launchmediaselect', 'left', 'modechange', 'multiply', 'nexttrack',
# 'nonconvert', 'num0', 'num1', 'num2', 'num3', 'num4', 'num5', 'num6',
# 'num7', 'num8', 'num9', 'numlock', 'pagedown', 'pageup', 'pause', 'pgdn',
# 'pgup', 'playpause', 'prevtrack', 'print', 'printscreen', 'prntscrn',
# 'prtsc', 'prtscr', 'return', 'right', 'scrolllock', 'select', 'separator',
# 'shift', 'shiftleft', 'shiftright', 'sleep', 'space', 'stop', 'subtract', 'tab',
# 'up', 'volumedown', 'volumemute', 'volumeup', 'win', 'winleft', 'winright', 'yen',
# 'command', 'option', 'optionleft', 'optionright']

# '''


# ################### 메세지 박스 - pyautogui 사용법 ######################

# import pyautogui as pg

# a = pg.alert(text='내용입니다', title='제목입니다', button='OK')
# print(a)

# import pyautogui as pg

# a = pg.confirm(text='내용입니다', title='제목입니다', buttons=['OK', 'Cancel'])
# print(a)

# import pyautogui as pg

# a = pg.prompt(text='내용입니다', title='제목입니다', default='입력하세요')
# print(a)

# import pyautogui as pg

# a = pg.password(text='내용입니다', title='제목입니다', default='입력하세요', mask='*')
# print(a)

# # ################### 이미지로 좌표찾기 - pyautogui 사용법 ######################

# import pyautogui as pg

# file_dir = 'C:\\Users\\khg98\\Desktop/5.png'

# button5location = pg.locateOnScreen('C:\\Users\\khg98\\Desktop/5.png') # 이미지가 있는 위치를 가져옵니다. 
# print(button5location)

# import pyautogui as pg

# button5location = pg.locateOnScreen(file_dir)
# point = pg.center(button5location) # Box 객체의 중앙 좌표를 리턴합니다. 
# print(point)


# # # ################### 사이트 정보 가져오기 - requests 사용법 ######################

# # import requests

# # response = requests.get('https://www.naver.com/')

# # print(response.status_code)#응답코드를 가져오는 방법
# # print(response.text)

# import requests

# url = 'https://section.blog.naver.com/Search/Post.nhn?pageNo=1&rangeType=ALL&orderBy=sim&keyword=%ED%8C%8C%EC%9D%B4%EC%8D%AC'

# params = {
#     'pageNo' : 1,
#     'rangeType' : 'ALL',
#     'orderBy' : 'sim',
#     'keyword' : '파이썬'
# }

# response = requests.get('https://section.blog.naver.com/Search/Post.nhn', params=params)

# print(response.status_code)
# print(response.url)
# print(response.url==url)

# # ################### 사이트 정보 가져오기 - beautiful 사용법(1) ######################
# import requests
# from bs4 import BeautifulSoup


# from urllib.parse import quote
# keyword = "음식"
# url = f'https://kin.naver.com/search/list.nhn?query={quote(keyword)}'
# print(url)

# response = requests.get(url)


# if response.status_code == 200:
#     html = response.text
#     soup = BeautifulSoup(html, 'html.parser')
#     title = soup.select_one('#s_content > div.section > ul > li:nth-child(1) > dl > dt > a')
#     # 찾은 html에 copy selector 기능을 이용해 봅시다.
#     # Css 선택자를 자동으로 찾아주는 엄청난 기능입니다.
#     # html에 오른쪽 클릭을 한 후 Copy -> Copy Selector 를 선택해 줍니다.
    
#     print(title)
#     print(title.get_text())
# else : 
#     print(response.status_code)

# # ################### 사이트 정보 가져오기 - beautiful 사용법(2) ######################
# import requests
# from bs4 import BeautifulSoup

# from urllib.parse import quote
# keyword = "파이썬"
# url = f'https://kin.naver.com/search/list.nhn?query={quote(keyword)}'

# response = requests.get(url)

# if response.status_code == 200:
#     html = response.text
#     soup = BeautifulSoup(html, 'html.parser')
#     ul = soup.select_one('ul.basic1')
#     print(ul)
# else : 
#     print(response.status_code)
    
    
# import requests
# from bs4 import BeautifulSoup

# from urllib.parse import quote
# keyword = "음식"
# url = f'https://kin.naver.com/search/list.nhn?query={quote(keyword)}'

# response = requests.get(url)

# if response.status_code == 200:
#     html = response.text
#     soup = BeautifulSoup(html, 'html.parser')
#     ul = soup.select_one('ul.basic1')
#     titles = ul.select('li > dl > dt > a')
#     for title in titles:
#         print(title.get_text())
# else : 
#     print(response.status_code)    

# # ################### 사이트 자동화하기 - selenium 사용법 ######################

# https://wikidocs.net/91474

# 향후에 진행해볼 것.

# # ################### 3.0 파이썬 엑셀 다루기 - openpyxl 사용법 ######################

# from openpyxl import Workbook

# folder_dir = 'C:\\Users\\khg98\\Desktop/'

# # 엑셀파일 쓰기
# write_wb = Workbook()

# # 이름이 있는 시트를 생성
# write_ws = write_wb.create_sheet('생성시트')

# # Sheet1에다 입력
# write_ws = write_wb.active
# write_ws['A1'] = '숫자'

# #행 단위로 추가
# write_ws.append([1,2,3])

# #셀 단위로 추가
# write_ws.cell(5, 5, '5행5열')

# write_wb.save(f"{folder_dir}\숫자.xlsx")



# from openpyxl import load_workbook
# folder_dir = 'C:\\Users\\khg98\\Desktop/'


# # data_only=True로 해줘야 수식이 아닌 값으로 받아온다. 
# load_wb = load_workbook(f"{folder_dir}/숫자.xlsx", data_only=True)
# # 시트 이름으로 불러오기 
# load_ws = load_wb['Sheet']

# # 셀 주소로 값 출력
# print(load_ws['B2'].value)

# # 셀 좌표로 값 출력
# print(load_ws.cell(3, 2).value)

# # 지정한 셀의 값 출력

# get_cells = load_ws['B3' : 'B6']
# for row in get_cells:
#     for cell in row:
#         print(f"cell:{cell.value}")

# # 모든 행 단위로 출력

# for row in load_ws.rows:
#     print(row)

# # 모든 열 단위로 출력

# for column in load_ws.columns:
#     print(column)

# # 모든 행과 열 출력

# all_values = []
# for row in load_ws.rows:
#     row_value = []
#     for cell in row:
#         row_value.append(cell.value)
#     all_values.append(row_value)
# print("all_values")
# print(all_values)

# load_ws.cell(3, 3, 51470)
# load_ws.cell(4, 3, 21470)
# load_ws.cell(5, 3, 1470)
# load_ws.cell(6, 3, 6470)
# load_wb.save(f"{folder_dir}/숫자.xlsx")

# # # ################### 웹스크래핑 예제(1) - 네이버금융 실시간 검색 순위 스크래핑 후 엑셀에 저장하기 ######################


# import requests
# from bs4 import BeautifulSoup

# from openpyxl import Workbook

# url = 'https://finance.naver.com/'
# folder_dir = 'C:\\Users\\khg98\\Desktop/'


# response = requests.get(url)
# response.raise_for_status()
# html = response.text
# soup = BeautifulSoup(html, 'html.parser')
# tbody = soup.select_one('#container > div.aside > div.group_aside > div.aside_area.aside_popular > table > tbody')
# trs = tbody.select('tr')
# datas = []
# for tr in trs:
#     name = tr.select_one('th > a').get_text()
#     current_price = tr.select_one('td').get_text() 
#     change_direction = tr['class'][0]
#     change_price = tr.select_one('td > span').get_text()
#     datas.append([name, current_price, change_direction, change_price])


# write_wb = Workbook()
# write_ws = write_wb.create_sheet('결과')
# for data in datas:
#     write_ws.append(data)

# write_wb.save(f'{folder_dir}/파일이름.xlsx')

# # ################### 3.2 웹스크래핑 예제(2) - 네이버금융 실시간 주가 크롤링하기 ######################

import requests
from bs4 import BeautifulSoup

codes = ['096530', '010130'] # 종목코드 리스트
prices = [] # 가격정보가 담길 리스트

for code in codes:
    url = 'https://finance.naver.com/item/main.nhn?code=' + code

    response = requests.get(url)
    response.raise_for_status()
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')

    today = soup.select_one('#chart_area > div.rate_info > div')
    price = today.select_one('.blind')
    # prices.append(price.get_text())
    prices.append(today.get_text())

print(prices)