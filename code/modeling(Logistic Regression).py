# 로지스틱회귀모델

import statsmodels.api as sm

X_train = train[['식사메뉴','식사타입', '성별', '직업상태', '일행', '식사목적', '대기시간', '식당선택기준', '가격대', '날씨', '식당타입', '식사가치관']]
Y_train = train[['만족여부']]

X_train = sm.add_constant(X_train)
logit = sm.Logit(Y_train,X_train).fit()

print(logit.summary())

X_train = train[['식사메뉴', '식사목적', '대기시간', '식당선택기준', '날씨', '식당타입']]
Y_train = train[['만족여부']]

X_train = sm.add_constant(X_train)
logit = sm.Logit(Y_train,X_train).fit()

print(logit.summary())

X_train = train[['식사메뉴', '대기시간', '식당선택기준', '날씨', '식당타입']]
Y_train = train[['만족여부']]

X_train = sm.add_constant(X_train)
logit = sm.Logit(Y_train,X_train).fit()

print(logit.summary())

train['predict'] = logit.predict(X_train)

train.head()

X_test = test[['예측메뉴', '대기시간', '식당선택기준', '날씨', '식당타입']]

X_test = sm.add_constant(X_test)

print(X_test)

Y_pred=logit.predict(X_test)

test['만족여부예측'] = Y_pred

test.head()

