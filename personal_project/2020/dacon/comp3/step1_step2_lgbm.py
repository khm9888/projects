

############ 1. 라이브러리 가져오기 ###########

import pandas as pd
import numpy as np
import sklearn
from sklearn.preprocessing import LabelEncoder

# print('Pandas : %s'%(pd.__version__))
# print('Numpy : %s'%(np.__version__))
# print('Scikit-Learn : %s'%(sklearn.__version__))

####################### 2. 전처리 ######################

def grap_year(data):
    data = str(data)
    return int(data[:4])

def grap_month(data):
    data = str(data)
    return int(data[4:])

# 날짜 처리
data = pd.read_csv('data/dacon/comp3/201901-202003.csv')
# print("type(data)")
# print(type(data))
data = data.fillna('')
data['year'] = data['REG_YYMM'].apply(lambda x: grap_year(x))#apply?
data['month'] = data['REG_YYMM'].apply(lambda x: grap_month(x))
data = data.drop(['REG_YYMM'], axis=1)

# 데이터 정제
df = data.copy()
df = df.drop(['CARD_CCG_NM', 'HOM_CCG_NM'], axis=1)

columns = ['CARD_SIDO_NM', 'STD_CLSS_NM', 'HOM_SIDO_NM', 'AGE', 'SEX_CTGO_CD', 'FLC', 'year', 'month']
df = df.groupby(columns).sum().reset_index(drop=False)






# name=__file__.split("\\")[-1] #py확장자 포함
# path =__file__[:-len(name)]

data.to_csv("./data/dacon/comp3/preprocess/data.csv")
df.to_csv("./data/dacon/comp3/preprocess/df.csv")
