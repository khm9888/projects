import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split as tts
from sklearn.feature_selection import SelectFromModel
from sklearn.metrics import r2_score,mean_absolute_error as mae
from sklearn.model_selection import GridSearchCV
from xgboost import XGBRegressor,plot_importance


#0~1 데이터 전처리, 데이터 입력

train = pd.read_csv("./dacon/comp1_bio/csv/train.csv",index_col=0,header=0,encoding="cp949")
test = pd.read_csv("./dacon/comp1_bio/csv/test.csv",index_col=0,header=0,encoding="cp949")
submission = pd.read_csv("./dacon/comp1_bio/csv/sample_submission.csv",index_col=0,header=0,encoding="cp949")

# for i in range(len()):
    
    
# print(train.shape)#(10000, 75) train,test
# print(test.shape)#(10000, 71) x_predict
# print(submission.shape)#(10000, 4) y_predict


# print(train.isnull().sum())

# train = train.interpolate()#보간법 // 선형보간

# print(dir(train))
# print(train.isnull().sum())


train=train.interpolate(axis=1)
test=test.interpolate(axis=1) #보간법 // 선형보간


# print(test.info())

# train = train.fillna(method="pad",axis=1)
# test = test.fillna(method="pad",axis=1)




test=test.values


# print(train.shape)

x = train.values[:,:-4]
y = train.values[:,-4:]



# print(x.shape)
# print(y.shape)

x_train, x_test, y_train, y_test = tts(x,y,train_size=0.8,
                                                    random_state=66)

# print(x_train.shape)
# print(x_test.shape)
# print(y_train.shape)
# print(y_test.shape)

#2.모델 구성-0

xgb_0 = XGBRegressor()
xgb_1 = XGBRegressor()
xgb_2 = XGBRegressor()
xgb_3 = XGBRegressor()

y_train_0=y_train[:,0]
y_train_1=y_train[:,1]
y_train_2=y_train[:,2]
y_train_3=y_train[:,3]

y_test_0 = y_test[:,0]
y_test_1 = y_test[:,1]
y_test_2 = y_test[:,2]
y_test_3 = y_test[:,3]

xgb_0.fit(x_train,y_train_0)
xgb_1.fit(x_train,y_train_1)
xgb_2.fit(x_train,y_train_2)
xgb_3.fit(x_train,y_train_3)

y_pre_0=xgb_0.predict(x_test)
y_pre_1=xgb_1.predict(x_test)
y_pre_2=xgb_2.predict(x_test)
y_pre_3=xgb_3.predict(x_test)

r2_0= xgb_0.score(x_test,y_test_0)
r2_1= xgb_1.score(x_test,y_test_1)
r2_2= xgb_2.score(x_test,y_test_2)
r2_3= xgb_3.score(x_test,y_test_3)

mae_0= mae(y_test_0,y_pre_0)
mae_1= mae(y_test_1,y_pre_1)
mae_2= mae(y_test_2,y_pre_2)
mae_3= mae(y_test_3,y_pre_3)

# m=list(mae_0,mae_1,mae_2,mae_3)
mae_result = (mae_0+mae_1+mae_2+mae_3)/4

print(f"mae_0 : {mae_0}")
print(f"mae_1 : {mae_1}")
print(f"mae_2 : {mae_2}")
print(f"mae_3 : {mae_3}")

print(f"mae_result : {mae_result}")

print(f"r2_0 : {r2_0}")
print(f"r2_1 : {r2_1}")
print(f"r2_2 : {r2_2}")
print(f"r2_3 : {r2_3}")

##################################################################################
print("----0-----")

thresholds_0 = np.sort(xgb_0.feature_importances_)

max_0=r2_0
idx_max_0=-1

for idx ,thresh in enumerate(thresholds_0):
    selection = SelectFromModel(xgb_0,threshold=thresh,prefit=True)#median +  GridSearch까지 할 것.데이콘 적용해라.
    
    selection_x_train = selection.transform(x_train)
        
    selection_x_test = selection.transform(x_test)
    # print(selection_x_train)

    selection_model =XGBRegressor()
    selection_model.fit(selection_x_train,y_train_0)
    
    y_pre_0 = selection_model.predict(selection_x_test)
    select_r2_0 = r2_score(y_test_0,y_pre_0)
    if select_r2_0>=max_0:
        max_0=select_r2_0
    #     idx_max_0=idx
    # print("-"*30)
    # print("idx")
    # print(idx)
    # print("thresh")
    # print(thresh)
    # print("select_r2_0")
    # print(select_r2_0)
    # print("-"*30)
    
    # print("y_pre")
    # print(y_pre)
print("-"*30)
print("r2_0")
print(idx_max_0)
print(max_0)

# r2_0
# -1
# 0.8481549266897241

##################################################################################
print("----1-----")


thresholds_1 = np.sort(xgb_1.feature_importances_)

max_1=r2_1
idx_max_1=-1

for idx ,thresh in enumerate(thresholds_1):
    selection = SelectFromModel(xgb_1,threshold=thresh,prefit=True)#median +  GridSearch까지 할 것.데이콘 적용해라.
   
    selection_x_train = selection.transform(x_train)
    
    selection_x_test = selection.transform(x_test)
    # print(selection_x_train)

    selection_model =XGBRegressor()
    selection_model.fit(selection_x_train,y_train_1)
    
    y_pre_1 = selection_model.predict(selection_x_test)
    select_r2_1 = r2_score(y_test_1,y_pre_1)
    if select_r2_1>=max_1:
        max_1=select_r2_1
        idx_max_1=idx
    # print("-"*30)
    # print("idx")
    # print(idx)
    # print("thresh")
    # print(thresh)
    # print("select_r2_1")
    # print(select_r2_1)
    # print("-"*30)
    
    # print("y_pre")
    # print(y_pre)

print("-"*30)
print("r2_1")

print(idx_max_1)
print(max_1)

# r2_1
# 38
# 0.34601582660837094

##################################################################################

print("----2-----")


# plot_importance(xgb_2)
# plt.show()

thresholds_2 = np.sort(xgb_2.feature_importances_)

max_2=r2_2
idx_max_2=-1

for idx ,thresh in enumerate(thresholds_2):
    selection = SelectFromModel(xgb_2,threshold=thresh,prefit=True)#median +  GridSearch까지 할 것.데이콘 적용해라.
   
    selection_x_train = selection.transform(x_train)
    
    selection_x_test = selection.transform(x_test)
    # print(selection_x_train)

    selection_model =XGBRegressor()
    selection_model.fit(selection_x_train,y_train_2)
    
    y_pre_2 = selection_model.predict(selection_x_test)
    select_r2_2 = r2_score(y_test_2,y_pre_2)
    if select_r2_2>=max_2:
        max_2=select_r2_2
        idx_max_2=idx
    # print("-"*30)
    # print("idx")
    # print(idx)
    # print("thresh")
    # print(thresh)
    # print("select_r2_2")
    # print(select_r2_2)
    # print("-"*30)
    
    # print("y_pre")
    # print(y_pre)

print("-"*30)
print("r2_2")

print(idx_max_2)
print(max_2)

# r2_2
# 36
# 0.3112930550861994

##################################################################################


##################################################################################

print("----3-----")

# plot_importance(xgb_3)
# plt.show()

thresholds_3 = np.sort(xgb_3.feature_importances_)

max_3=r2_3
idx_max_3=-1

for idx ,thresh in enumerate(thresholds_3):
    selection = SelectFromModel(xgb_3,threshold=thresh,prefit=True)#median +  GridSearch까지 할 것.데이콘 적용해라.
   
    selection_x_train = selection.transform(x_train)
    
    selection_x_test = selection.transform(x_test)
    # print(selection_x_train)

    selection_model =XGBRegressor()
    selection_model.fit(selection_x_train,y_train_3)
    
    y_pre_3 = selection_model.predict(selection_x_test)
    select_r2_3 = r2_score(y_test_3,y_pre_3)
    if select_r2_3>=max_3:
        max_3=select_r2_3
        idx_max_3=idx
    # print("-"*30)
    # print("idx")
    # print(idx)
    # print("thresh")
    # print(thresh)
    # print("select_r2_3")
    # print(select_r2_3)
    # print("-"*30)
    
    # print("y_pre")
    # print(y_pre)

print("-"*30)
print("r2_3")

print(idx_max_3)
print(max_3)

# r2_3
# 12
# 0.2119125826057462


###################################################################################

print("-"*30)
print("r2_0")
print(idx_max_0)
print(max_0)

print("-"*30)
print("r2_1")

print(idx_max_1)
print(max_1)

print("-"*30)
print("r2_2")

print(idx_max_2)
print(max_2)

print("-"*30)
print("r2_3")

print(idx_max_3)
print(max_3)

# from xgboost import XGBRegressor

# r2_0
# -1
# 0.8481549266897241

# r2_1
# 38
# 0.34601582660837094

# r2_2
# 36
# 0.3112930550861994

# r2_3
# 12
# 0.2119125826057462

