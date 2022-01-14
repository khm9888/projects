# coding=UTF-8

from urllib.request import urlopen
from bs4 import BeautifulSoup
from html_table_parser import parser_functions as parser

import pandas as pd

url="http://race.kra.co.kr/raceScore/ScoretableDetailList.do?meet=1&realRcDate=20170723&realRcNo=1"

result = urlopen(url)
html = result.read()
soup = BeautifulSoup(html, 'html.parser')


temp = soup.find_all('table')
# print(temp[2])

p=parser.make2d(temp[2])
df=pd.DataFrame(p[1:],columns=p[0])

print(df)