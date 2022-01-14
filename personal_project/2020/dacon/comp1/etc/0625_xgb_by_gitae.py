Skip to content
Search or jump to…

Pull requests
Issues
Marketplace
Explore
 
@khm9888 
Learn Git and GitHub without any code!
Using the Hello World guide, you’ll start a branch, write comments, and open a pull request.


Inerial
/
bitcamp
1
01
Code
Issues
Pull requests
Actions
Projects
Wiki
Security
Insights
bitcamp/dacon/comp1/dacon01_mknpy.py /
@Inerial
Inerial 1
Latest commit d4fd4cd 6 hours ago
 History
 1 contributor
224 lines (179 sloc)  8.31 KB
  
import numpy as np
import pandas as pd
import pywt
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler, MinMaxScaler, MaxAbsScaler, RobustScaler

## 데이터 불러오기
train = pd.read_csv('./data/dacon/comp1/train.csv', sep=',', index_col = 0, header = 0)
test = pd.read_csv('./data/dacon/comp1/test.csv', sep=',', index_col = 0, header = 0)


## 데이터 분해 및 columns이름 저장
train_col = train.columns[:-4]
test_col = test.columns
y_train_col = train.columns[-4:]

y_train = train.values[:,-4:]
train = train.values[:,:-4]
test = test.values

# scaler = MinMaxScaler()
# train = scaler.fit_transform(train)
# test = scaler.transform(test)


## NaN값이 있는 train,test값을 다시 데이터 프레임으로 감싸주기
train = pd.DataFrame(train, columns=train_col)
test = pd.DataFrame(test, columns=test_col)


train_src = train.filter(regex='_src$',axis=1).T.interpolate(limit_direction='both').T.values # 선형보간법
# train_damp = 1
# train_damp = 625/train.values[:,0:1]/train.values[:,0:1]*(10**(625/train.values[:,0:1]/train.values[:,0:1] - 1))
train_damp = np.exp(np.pi*(25 - train.values[:,0:1])/3.44)
train_dst = train.filter(regex='_dst$',axis=1).T.interpolate(limit_direction='both').T.values / train_damp# 선형보간법

test_src = test.filter(regex='_src$',axis=1).T.interpolate(limit_direction='both').T.values
# test_damp = 1
# test_damp = 625/test.values[:,0:1]/test.values[:,0:1]*(10**(625/test.values[:,0:1]/test.values[:,0:1] - 1))
test_damp = np.exp(np.pi*(25 - test.values[:,0:1])/3.44)
test_dst = test.filter(regex='_dst$',axis=1).T.interpolate(limit_direction='both').T.values / test_damp




max_test = 0
max_train = 0
train_fu_real = []
train_fu_imag = []
test_fu_real = []
test_fu_imag = []
train_2fu_real = []
train_2fu_imag = []
test_2fu_real = []
test_2fu_imag = []

train_dst_mean = []
test_dst_mean = []

rho_10 = 0
nrho_10 = 0
rho_15 = 0
nrho_15 = 0
rho_20 = 0
nrho_20 = 0
rho_25 = 0
nrho_25 = 0

for i in range(10000):
    tmp_x = 0
    tmp_y = 0
    for j in range(35):
        if train_src[i, j] == 0 and train_dst[i,j] != 0:
            # train_src[i,j] = 1e-10
            train_src[i,j] = train_dst[i,j]
            # train_dst[i,j] = 0

        if test_src[i, j] == 0 and test_dst[i,j] != 0:
            # test_src[i,j] = 1e-10
            test_src[i,j] = test_dst[i,j]
            # test_dst[i,j] = 0

    if train['rho'][i] == 10:
        rho_10 += train_dst[i,:].sum()
        nrho_10 += 1
    if train['rho'][i] == 15:
        rho_15 += train_dst[i,:].sum()
        nrho_15 += 1
    if train['rho'][i] == 20:
        rho_20 += train_dst[i,:].sum()
        nrho_20 += 1
    if train['rho'][i] == 25:
        rho_25 += train_dst[i,:].sum()
        nrho_25 += 1
    plt.plot(range(35), train_src[i])
    plt.show()

    train_fu_real.append(np.fft.fft(train_dst[i]-train_dst[i].mean(), n=60).real)
    train_fu_imag.append(np.fft.fft(train_dst[i]-train_dst[i].mean(), n=60).imag)
    test_fu_real.append(np.fft.fft(test_dst[i]-test_dst[i].mean(), n=60).real)
    test_fu_imag.append(np.fft.fft(test_dst[i]-test_dst[i].mean(), n=60).imag)
    train_dst_mean.append([train_dst[i].mean()])
    test_dst_mean.append([test_dst[i].mean()])

print("==========================")
print(((train_src - train_dst) < 0).sum())
print(((test_src - test_dst) < 0).sum())
print("==========================")

trian_dst_mean = np.array(train_dst_mean)
test_dst_mean = np.array(test_dst_mean)

train_2fu_real = np.fft.fft(train_dst-train_dst_mean).real
train_2fu_imag = np.fft.fft(train_dst-train_dst_mean).imag
test_2fu_real = np.fft.fft(test_dst-test_dst_mean).real
test_2fu_imag = np.fft.fft(test_dst-test_dst_mean).imag    

print(max_train)
print(max_test)
print("RHO")
print(rho_10/nrho_10)
print(rho_15/nrho_15)
print(rho_20/nrho_20)
print(rho_25/nrho_25)

print(((train_src - train_dst) < 0).sum())
print(((test_src - test_dst) < 0).sum())




small = 1e-20



x_train = np.concatenate([train.values[:,0:1]**2,trian_dst_mean, train_damp, train_dst,  train_dst*train_damp, train_src-train_dst, train_src/(train_dst+small), train_fu_real, train_fu_imag] , axis = 1)
x_pred = np.concatenate([test.values[:,0:1]**2,test_dst_mean, test_damp, test_dst,  test_dst*test_damp, test_src-test_dst, test_src/(test_dst+small),test_fu_real,test_fu_imag], axis = 1)


print(x_train.shape)
print(y_train.shape)
print(x_pred.shape)

np.save('./dacon/comp1_bio/csv/x_train.npy', arr=x_train)
np.save('./dacon/comp1_bio/csv/y_train.npy', arr=y_train)
np.save('./dacon/comp1_bio/csv/x_pred.npy', arr=x_pred)

