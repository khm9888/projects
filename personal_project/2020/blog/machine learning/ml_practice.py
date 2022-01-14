from sklearn.model_selection import KFold,cross_val_score,GridSearchCV,train_test_split as tts, RandomizedSearchCV
from sklearn.metrics import accuracy_score

from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_breast_cancer
from sklearn.pipeline import Pipeline,make_pipeline
from sklearn.preprocessing import StandardScaler,MinMaxScaler
from sklearn.svm import LinearSVC,SVC


dataset=load_breast_cancer()
print(dataset.keys())
x=dataset.data
y=dataset.target

x_train,x_test,y_train,y_test=tts(x,y,train_size=0.8)


# pipe = make_pipeline(StandardScaler(),RandomForestClassifier())

parameters=[{"bootstrap":[True,False]}]#딕셔너리형태

pipe = Pipeline([("scaler", MinMaxScaler()), ('ensemble', RandomForestClassifier())])

kfold=KFold(5,shuffle=True)

model = GridSearchCV(pipe,parameters,cv=kfold)

model.fit(x_train,y_train)

y_pre = model.predict(x_test)

print(f"최적의 매개변수 = {model.best_estimator_}")
print(f"최종 정답률 = {accuracy_score(y_test,y_pre)}")