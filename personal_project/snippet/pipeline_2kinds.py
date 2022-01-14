pipe = make_pipeline(MinMaxScaler(), RandomForestClassifier()) # make_pipeline 이건 전처리랑 모델만

pipe=Pipeline([("scaler",MinMaxScaler()),("model",model)])
