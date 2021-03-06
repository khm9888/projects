# 200624

# LGBM


import numpy as np
import pandas as pd
import warnings
warnings.filterwarnings("ignore")
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split, KFold, cross_val_score, RandomizedSearchCV, GridSearchCV
from sklearn.preprocessing import MinMaxScaler, StandardScaler, RobustScaler
from xgboost import XGBRegressor
from lightgbm import LGBMClassifier, LGBMRegressor
from sklearn.multioutput import MultiOutputRegressor
from sklearn.feature_selection import SelectFromModel
from sklearn.metrics import accuracy_score, r2_score, mean_absolute_error, mean_absolute_error as mae

x_npy = np.load('./dacon/comp1_bio/csv/x_train.npy')
y_npy = np.load('./dacon/comp1_bio/csv/y_train.npy')
x_pred = np.load('./dacon/comp1_bio/csv/x_pred.npy')
print(x_npy.shape, y_npy.shape, x_pred.shape)   # (10000, 176) (10000, 4) (10000, 176)

x_train, x_test, y_train, y_test = train_test_split(x_npy, y_npy, test_size = 0.2, random_state = 66, shuffle = True)
print(x_train.shape)        # (8000, 176)
print(x_test.shape)         # (2000, 176)
print(y_train.shape)        # (8000, 4)
print(y_test.shape)         # (2000, 4)

scaler = RobustScaler()
scaler.fit(x_train)
x_train = scaler.transform(x_train)
x_test = scaler.transform(x_test)
x_pred = scaler.transform(x_pred)

y_train1 = y_train[:, 0]
y_train2 = y_train[:, 1]
y_train3 = y_train[:, 2]
y_train4 = y_train[:, 3]

y_test1 = y_test[:, 0]
y_test2 = y_test[:, 1]
y_test3 = y_test[:, 2]
y_test4 = y_test[:, 3]

model = LGBMRegressor(n_estimators=550,
                      num_leaves=100,
                      max_depth=20,
                      min_child_samples=30,
                      learning_rate=0.04,
                      colsample_bytree=0.5,
                      reg_alpha=1,
                      reg_lambda = 1.1,
                      n_jobs=6)
# 100 / 20 / 30 / 0.05 / 0.5
# score1 : 72.3023
# mae1 : 1.1604
# score2 : 21.5578
# mae2 : 0.6963
# score3 : 25.3974
# mae3 : 2.0771
# score4 : 17.2373
# mae4 : 1.3498

# 100 / 20 / 30 / 0.04 / 0.7
# score1 : 72.2789
# mae1 : 1.1567
# score2 : 22.8805
# mae2 : 0.6918
# score3 : 26.0999
# mae3 : 2.0683
# score4 : 17.5051
# mae4 : 1.3463

# colsample_bytree=0.7
# score1 : 89.5936
# mae1 : 0.6826
# score2 : 59.9237
# mae2 : 0.4980
# score3 : 49.5317
# mae3 : 1.6976
# score4 : 34.7322
# mae4 : 1.1723

# colsample_bytree=0.5 ???????????? kb3
# score1 : 89.8127
# mae1 : 0.6707
# score2 : 60.8751
# mae2 : 0.4913
# score3 : 49.2990
# mae3 : 1.6988
# score4 : 35.3934
# mae4 : 1.1660

model.fit(x_train, y_train1, verbose=False, eval_metric=['mae'],
                eval_set=[(x_test, y_test1)],
                early_stopping_rounds=20)
score1 = model.score(x_test, y_test1)
print("score1 : %.4f" %(score1 * 100.0))
# print(model.feature_importances_)
y_pred_1 = model.predict(x_test)
mae1 = mean_absolute_error(y_test1, y_pred_1)
print('mae1 : %.4f' %(mae1))
y_pred1 = model.predict(x_pred)

model.fit(x_train, y_train2, verbose=False, eval_metric=['mae'],
                eval_set=[(x_test, y_test2)],
                early_stopping_rounds=20)
score2 = model.score(x_test, y_test2)
print("score2 : %.4f" %(score2 * 100.0))
# print(model.feature_importances_)
y_pred_2 = model.predict(x_test)
mae2 = mean_absolute_error(y_test2, y_pred_2)
print('mae2 : %.4f' %(mae2))
y_pred2 = model.predict(x_pred)

model.fit(x_train, y_train3, verbose=False, eval_metric=['mae'],
                eval_set=[(x_test, y_test3)],
                early_stopping_rounds=20)
score3 = model.score(x_test, y_test3)
print("score3 : %.4f" %(score3 * 100.0))
# print(model.feature_importances_)
y_pred_3 = model.predict(x_test)
mae3 = mean_absolute_error(y_test3, y_pred_3)
print('mae3 : %.4f' %(mae3))
y_pred3 = model.predict(x_pred)

model.fit(x_train, y_train4, verbose=False, eval_metric=['mae'],
                eval_set=[(x_test, y_test4)],
                early_stopping_rounds=20)
score4 = model.score(x_test, y_test4)
print("score4 : %.4f" %(score4 * 100.0))
# print(model.feature_importances_)
y_pred_4 = model.predict(x_test)
mae4 = mean_absolute_error(y_test4, y_pred_4)
print('mae4 : %.4f' %(mae4))
y_pred4 = model.predict(x_pred)

y_pred_1=y_pred_1.reshape(1,y_pred_1.shape[0])
y_pred_2=y_pred_2.reshape(1,y_pred_2.shape[0])
y_pred_3=y_pred_3.reshape(1,y_pred_3.shape[0])
y_pred_4=y_pred_4.reshape(1,y_pred_4.shape[0])


y_pre_total = np.concatenate((y_pred_1,y_pred_2,y_pred_3,y_pred_4)).T
mae_result = mae(y_test,y_pre_total)
print(f"mae_result : {mae_result}")

sub = pd.DataFrame({
    'id': np.array(range(10000, 20000)),
    'hhb': y_pred1,
    'hbo2': y_pred2,
    'ca': y_pred3,
    'na': y_pred4
})
print(sub)

''' 4. ?????? '''
name=__file__.split('\\')[-1]
sub.to_csv(f"dacon\comp1_bio\csv\sample_submission_{name}_{str(mae_result)[:4]}.csv", index = False)
