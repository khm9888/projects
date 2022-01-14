
####################### 3. 탐색적 자료분석 ######################
# Exploratory Data Analysis

# 입력하세요.

###################### # 4. 변수 선택 및 모델 구축 ######################
# Feature Engineering & Initial Modeling

# feature, target 설정
train_num = df_num.sample(frac=1, random_state=0)
train_features = train_num.drop(['CSTMR_CNT', 'AMT', 'CNT'], axis=1)
train_target = np.log1p(train_num['AMT'])

####################### 5. 모델 학습 및 검증 ######################
# Model Tuning & Evaluation

# 훈련
model = RandomForestRegressor(n_jobs=-1, random_state=0)
model.fit(train_features, train_target)
