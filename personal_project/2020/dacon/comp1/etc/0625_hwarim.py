import numpy as np
import pandas as pd
import pywt
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler, MinMaxScaler, MaxAbsScaler, RobustScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
from lightgbm import LGBMRegressor
from sklearn.multioutput import MultiOutputRegressor
from sklearn.decomposition import PCA



x = np.load('./dacon/comp1_bio/csv/x_train.npy')
y = np.load('./dacon/comp1_bio/csv/y_train.npy')
x_pred = np.load('./dacon/comp1_bio/csv/x_pred.npy')

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=30)

model = MultiOutputRegressor(LGBMRegressor(n_estimators=1000, learning_rate=0.05, max_depth=-1, colsample_bytree=0.8, num_leaves=31))

model.fit(x_train,y_train)


score = model.score(x_test,y_test)

print("R2:",score)

# thresholds = np.sort(model.feature_importances_) # 오름차순 정렬(feature_importances정렬)
# print(thresholds)

# models=[]
# res = np.array([])
# for thresh in thresholds: 
#     selection = SelectFromModel(model, threshold=thresh, prefit=True)  
#     select_x_train = selection.transform(x_train)
#     select_x_test = selection.transform(x_test)

#     model2 = LGBMRegressor(n_estimators=500, learning_rate=0.1, n_jobs=-1)
#     model2.fit(select_x_train, y_train, verbose=False, eval_metric=['logloss','rmse'],
#                 eval_set=[(select_x_train, y_train), (select_x_test, y_test)],
#                 early_stopping_rounds=20)
    
#     y_pred = model2.predict(select_x_test)
#     select_test = selection.transform(test)
    
#     score = r2_score(y_test,y_pred)
#     mae = mean_absolute_error(y_test,y_pred)
#     print("r2:",score)
#     print("mae:",mae)
   
print("r2:",score)
y_predict = model.predict(x_test)
mae = mean_absolute_error(y_test,y_predict)
print("mae:",mae)

result = model.predict(x_pred)
a = np.arange(10000,20000)
#np.arange--수열 만들때
submission = result
submission = pd.DataFrame(submission, a)
name=__file__.split("\\")[-1][:-3]
submission.to_csv(f"./dacon/comp1_bio/csv/{name}_{str(mae)[:5]}.csv", header = ["hhb", "hbo2", "ca", "na"], index = True, index_label="id" )