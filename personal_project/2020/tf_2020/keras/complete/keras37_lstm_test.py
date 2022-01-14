#ensemble 모델을 만드시오.

import numpy as np

#데이터 구성

dataset=np.array(range(1,13))
dataset2=np.array(range(20,70,10))
# print(dataset2)
def split(dataset,time_steps):
    arr=list()
    for i in range(len(dataset)-time_steps+1):
        input_v=dataset[i:i+time_steps]
        # print(input_v)
        arr.append(input_v)
    return arr


x=np.array(split(dataset,3)+split(dataset2,3))
# x2=np.array(split(dataset,3))
# x2=
print(x)

y=np.array(list(range(4,14))+list(range(50,80,10)))
# y=np.array(list(range(4,14))+list(range(50,80,10)))
print(y)

x=x.reshape(x.shape[0],x.shape[1],1)

print(f"x.shape:{x.shape}")
print(f"y.shape:{y.shape}")


x_pre=np.array([[50,60,70]])
x_pre=x_pre.reshape(x_pre.shape[0],x_pre.shape[1],1)
#모델

from keras.models import Sequential
from keras.models import Model
from keras.layers import Dense, LSTM,Input,Concatenate

model = Sequential()


model.add(LSTM(200,activation="relu",input_shape=(3,1),return_sequences=True))
model.add(LSTM(1,return_sequences=True))
model.add(LSTM(1,return_sequences=True))
model.add(LSTM(1,return_sequences=True))
model.add(LSTM(1))
model.add(Dense(1))


model.summary()


# 트레이닝

from keras.callbacks import EarlyStopping


model.compile(loss="mse", optimizer="adam", metrics=["accuracy"])

# early=EarlyStopping(monitor="loss",patience=20,mode="min")

model.fit(x,y,batch_size=1,epochs=1000,verbose=2)#,callbacks=[early])
# model.fit(x,y,batch_size=1,epochs=100,verbose=3)

#검증

loss, acc=model.evaluate(x,y,batch_size=1)

print(f"loss:{loss}")
print(f"acc:{acc}")

y_pre=model.predict(x_pre)

print(f"y_pre : {y_pre}")