#RPA

# https://www.youtube.com/watch?v=exgO1LFl9x8&t=0s

# print("test")

from openpyxl import Workbook
wb = Workbook() #워크북 생성
ws = wb.active #활성화된 sheet 가져옴
ws.title = "NadoSheet"
wb.save("sample.xlsx")
wb.close()