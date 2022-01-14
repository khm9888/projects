import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split as tts
from sklearn.metrics import r2_score,mean_absolute_error as mae
# from sklearn.preprocessing import StandardScaler
# from keras.models import Sequential,Model
# from keras.layers import Dense,Input,Dropout,LSTM
from sklearn.model_selection import GridSearchCV


#0~1 데이터 전처리, 데이터 입력

train = pd.read_csv("./dacon/comp1_bio/train.csv",index_col=0,header=0,encoding="cp949")
test = pd.read_csv("./dacon/comp1_bio/test.csv",index_col=0,header=0,encoding="cp949")
submission = pd.read_csv("./dacon/comp1_bio/csv/sample_submission.csv",index_col=0,header=0,encoding="cp949")


train=train.transpose()
test=test.transpose()
train=train.interpolate()
test=test.interpolate() #보간법 // 선형보간
train=train.transpose()
test=test.transpose()

test=test.values

x = train.values[:,:-4]
y = train.values[:,-4:]

x_train, x_test, y_train, y_test = tts(x,y,train_size=0.7,
                                                    random_state=66)
###################################################################################

# parameters = {
#     "n_estimators" : np.arange(100,301,100),
#     "learning_rate" : np.arange(0.01,0.03,0.01),
#     "colsample_bytree":np.arange(0.6,1,0.1),
#     "colsample_bylevel":np.arange(0.6,1,0.1),
#     "max_depth" : [4,5,6]
# }


# parameters_0 = {
#     # "n_estimators" : np.arange(2000),
#     # "learning_rate" : np.arange(0.2,0.27,0.01),
#     # "colsample_bytree":np.arange(0.3,0.6,0.1),
#     # "colsample_bylevel":np.arange(0.3,0.7,0.1),
#     "max_depth" : [6,7,8,9]
# }
# #2.모델 구성-xgb
# from xgboost import XGBRegressor,plot_importance
# '''
# XGBRegressor(base_score=0.5, booster='gbtree', colsample_bylevel=1,
#              colsample_bynode=1, colsample_bytree=1, gamma=0, gpu_id=-1,
#              importance_type='gain', interaction_constraints='',
#              learning_rate=0.300000012, max_delta_step=0, max_depth=6,
#              min_child_weight=1, missing=nan, monotone_constraints='()',
#              n_estimators=100, n_jobs=0, num_parallel_tree=1, random_state=0,
#              reg_alpha=0, reg_lambda=1, scale_pos_weight=1, subsample=1,
#              tree_method='exact', validate_parameters=1, verbosity=None)
# '''
# # xgb_0 = XGBRegressor(n_estimators=parameters_0["n_estimators"][0]//10)
# xgb_0 = XGBRegressor()

# y_train_0=y_train[:,0]
# y_test_0=y_test[:,0]

# xgb_0.fit(x_train,y_train_0,verbose=0)

# xgb_0 = GridSearchCV(xgb_0,parameters_0,cv=5,n_jobs=-1)
# xgb_0.fit(x_train,y_train_0,verbose=0)
# y_pre_0=xgb_0.predict(x_test)
# r2_0= xgb_0.score(x_test,y_test_0)
# mae_0= mae(y_test_0,y_pre_0)

# # m=list(mae_0,mae_1,mae_2,mae_3)

# print("__file__")
# print(__file__)
# # print(xgb_0.best_estimator_)
# # mae_result = (mae_0+mae_1+mae_2+mae_3)/4
# # r2_result = (r2_0+r2_1+r2_2+r2_3)/4
# print("-"*20)
# print(xgb_0.best_params_)
# print(f"mae_0 : {mae_0}")

# print(f"r2_0 : {r2_0}")

# '''
# #0번
# {}
# mae_0 : 0.9071001841982206
# r2_0 : 0.8365277416752172
# {'n_estimators': 2000}
# {'learning_rate': 0.2}
# {"colsample_bytree":1}
# {"colsample_bylevel":1}
# {'max_depth': 7}

# '''

###################################################################################

# # parameters = {
# #     "n_estimators" : np.arange(100,301,100),
# #     "learning_rate" : np.arange(0.01,0.03,0.01),
# #     "colsample_bytree":np.arange(0.6,1,0.1),
# #     "colsample_bylevel":np.arange(0.6,1,0.1),
# #     "max_depth" : [4,5,6]
# # }


# parameters_1 = {
#     # "n_estimators" : np.arange(200,500),
#     # "learning_rate" : np.arange(0.05,0.12,0.01),
#     # "colsample_bytree":np.arange(0.6,1,0.1),
#     # "colsample_bylevel":np.arange(0.3,1,0.1),
#     # "max_depth" : [3,4,5,6,7,8,9]
# }
# #2.모델 구성-xgb
# from xgboost import XGBRegressor,plot_importance
# '''
# XGBRegressor(base_score=0.5, booster='gbtree', colsample_bylevel=1,
#              colsample_bynode=1, colsample_bytree=1, gamma=0, gpu_id=-1,
#              importance_type='gain', interaction_constraints='',
#              learning_rate=0.300000012, max_delta_step=0, max_depth=6,
#              min_child_weight=1, missing=nan, monotone_constraints='()',
#              n_estimators=100, n_jobs=0, num_parallel_tree=1, random_state=0,
#              reg_alpha=0, reg_lambda=1, scale_pos_weight=1, subsample=1,
#              tree_method='exact', validate_parameters=1, verbosity=None)
# '''
# # xgb_1 = XGBRegressor(n_estimators=parameters_1["n_estimators"][0]//10)
# xgb_1 = XGBRegressor()

# y_train_1=y_train[:,1]
# y_test_1=y_test[:,1]

# xgb_1.fit(x_train,y_train_1,verbose=0)

# xgb_1 = GridSearchCV(xgb_1,parameters_1,cv=5,n_jobs=-1)
# xgb_1.fit(x_train,y_train_1,verbose=0)
# y_pre_1=xgb_1.predict(x_test)
# r2_1= xgb_1.score(x_test,y_test_1)
# mae_1= mae(y_test_1,y_pre_1)

# # m=list(mae_1,mae_1,mae_2,mae_3)

# print("__file__")
# print(__file__)
# # print(xgb_1.best_estimator_)
# # mae_result = (mae_1+mae_1+mae_2+mae_3)/4
# # r2_result = (r2_1+r2_1+r2_2+r2_3)/4
# print("-"*20)
# print(xgb_1.best_params_)
# print(f"mae_1 : {mae_1}")
# print(f"r2_1 : {r2_1}")

# '''
# #1번
# {}
# mae_1 : 0.6723148023001353
# r2_1 : 0.28821972499626336
# {'learning_rate': 0.1}
# "colsample_bytree": 1
# {'max_depth': 4}
# mae_1 : 0.6773021589930852
# r2_1 : 0.28896014718449714


# '''


###################################################################################

# # parameters = {
# #     "n_estimators" : np.arange(100,301,100),
# #     "learning_rate" : np.arange(0.1,0.4,0.01),
# #     "colsample_bytree":np.arange(0.6,1,0.1),
# #     "colsample_bylevel":np.arange(0.6,1,0.1),
# #     "max_depth" : [4,5,6]
# # }


# parameters_2 = {
#     # "n_estimators" : np.arange(200,500),
#     # "learning_rate" : np.arange(0.12,0.17,0.01),
#     # "colsample_bytree":np.arange(0.6,1,0.1),
#     # "colsample_bytree":np.array([0.8,0.5,0.4]),
#     # "colsample_bylevel":np.arange(0.3,1,0.1),
#     # "max_depth" : [3,4,5,6,7,8,9]
# }
# #2.모델 구성-xgb
# from xgboost import XGBRegressor,plot_importance
# '''
# XGBRegressor(base_score=0.5, booster='gbtree', colsample_bylevel=1,
#              colsample_bynode=1, colsample_bytree=1, gamma=0, gpu_id=-1,
#              importance_type='gain', interaction_constraints='',
#              learning_rate=0.300000012, max_delta_step=0, max_depth=6,
#              min_child_weight=1, missing=nan, monotone_constraints='()',
#              n_estimators=100, n_jobs=0, num_parallel_tree=1, random_state=0,
#              reg_alpha=0, reg_lambda=1, scale_pos_weight=1, subsample=1,
#              tree_method='exact', validate_parameters=1, verbosity=None)
# '''
# # xgb_2 = XGBRegressor(n_estimators=parameters_2["n_estimators"][0]//10)
# xgb_2 = XGBRegressor()

# y_train_2=y_train[:,2]
# y_test_2=y_test[:,2]

# xgb_2.fit(x_train,y_train_2,verbose=0)

# xgb_2 = GridSearchCV(xgb_2,parameters_2,cv=5,n_jobs=-1)
# xgb_2.fit(x_train,y_train_2,verbose=0)
# y_pre_2=xgb_2.predict(x_test)
# r2_2= xgb_2.score(x_test,y_test_2)
# mae_2= mae(y_test_2,y_pre_2)

# # m=list(mae_2,mae_2,mae_2,mae_3)

# print("__file__")
# print(__file__)
# # print(xgb_2.best_estimator_)
# # mae_result = (mae_2+mae_2+mae_2+mae_3)/4
# # r2_result = (r2_2+r2_2+r2_2+r2_3)/4
# print("-"*20)
# print(xgb_2.best_params_)
# print(f"mae_2 : {mae_2}")
# print(f"r2_2 : {r2_2}")

# '''
# #2번
# {}
# mae_2 : 2.0735658199532825
# r2_2 : 0.22964412524252453
# {'learning_rate': 0.12}
# {'colsample_bytree': 0.8}
# {'colsample_bylevel': 0.4}
# {'max_depth': 3}

# '''

###################################################################################

# parameters = {
#     "n_estimators" : np.arange(100,301,100),
#     "learning_rate" : np.arange(0.1,0.4,0.1),
#     "colsample_bytree":np.arange(0.6,1,0.1),
#     "colsample_bylevel":np.arange(0.6,1,0.1),
#     "max_depth" : [4,5,6]
# }


parameters_3 = {
    # "n_estimators" : np.arange(200,500),
    # "learning_rate" : np.arange(0.12,0.17,0.01),
    # "colsample_bytree":np.arange(0.6,1,0.1),
    # "colsample_bytree":np.array([0.8,0.5,0.4]),
    # "colsample_bylevel":np.arange(0.3,1,0.1),
    # "colsample_bylevel":np.array([0.9,0.95,1]),
    "max_depth" : [3,4,5,6,7,8,9]
}
#2.모델 구성-xgb
from xgboost import XGBRegressor,plot_importance
'''
XGBRegressor(base_score=0.5, booster='gbtree', colsample_bylevel=1,
             colsample_bynode=1, colsample_bytree=1, gamma=0, gpu_id=-1,
             importance_type='gain', interaction_constraints='',
             learning_rate=0.300000012, max_delta_step=0, max_depth=6,
             min_child_weight=1, missing=nan, monotone_constraints='()',
             n_estimators=100, n_jobs=0, num_parallel_tree=1, random_state=0,
             reg_alpha=0, reg_lambda=1, scale_pos_weight=1, subsample=1,
             tree_method='exact', validate_parameters=1, verbosity=None)
'''
# xgb_3 = XGBRegressor(n_estimators=parameters_3["n_estimators"][0]//10)
xgb_3 = XGBRegressor()

y_train_3=y_train[:,3]
y_test_3=y_test[:,3]

xgb_3.fit(x_train,y_train_3,verbose=0)

xgb_3 = GridSearchCV(xgb_3,parameters_3,cv=5,n_jobs=-1)
xgb_3.fit(x_train,y_train_3,verbose=0)
y_pre_3=xgb_3.predict(x_test)
r2_3= xgb_3.score(x_test,y_test_3)
mae_3= mae(y_test_3,y_pre_3)

# m=list(mae_3,mae_3,mae_3,mae_3)

print("__file__")
print(__file__)
# print(xgb_3.best_estimator_)
# mae_result = (mae_3+mae_3+mae_3+mae_3)/4
# r2_result = (r2_3+r2_3+r2_3+r2_3)/4
print("-"*20)
print(xgb_3.best_params_)
print(f"mae_3 : {mae_3}")
print(f"r2_3 : {r2_3}")

'''
#3번
{}
{'learning_rate': 0.13}
{'colsample_bytree': 0.8}
{'colsample_bylevel': 0.9}
{'max_depth': 4}
'''