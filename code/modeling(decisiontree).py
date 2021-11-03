
from google.colab import drive
drive.mount('/content/drive')

import pandas as pd

train = pd.read_csv("/content/drive/MyDrive/Colab Notebooks/메뉴의사결정나무/점심메뉴 추천 서비스 구현을 위한 설문조사(응답).csv", encoding='CP949')

train.head()

feature_name = ['식사타입', '성별', '직업상태', '일행', '식사목적', '대기시간', '식당선택기준', '가격대', '날씨', '식당타입', '식사가치관']
x_train=train[feature_name]

label_name = '식사메뉴'
y_train=train[label_name]

x_train.head()
y_train.head()

from sklearn.tree import DecisionTreeClassifier

model = DecisionTreeClassifier()

model.fit(x_train,y_train)

!pip install graphviz

import graphviz
from sklearn.tree import export_graphviz

tree = export_graphviz(model, feature_names= feature_name,
                       class_names = ['고기류', '한식', '일식', '중식', '분식', '패스트푸드',
                                     '양식', '국밥 및 찌개류', '국수', '찜탕', '카페', '동남아요리'])

graphviz.Source(tree)

!pip install pydotplus

import pydotplus

from sklearn.tree import export_graphviz

from IPython.core.display import Image

from sklearn.tree import export_graphviz

# .dot 파일로 export 해줍니다
export_graphviz(model, out_file='tree.dot')

# 생성된 .dot 파일을 .png로 변환
from subprocess import call
call(['dot', '-Tpng', 'tree.dot', '-o', 'decistion-tree.png', '-Gdpi=600'])

# jupyter notebook에서 .png 직접 출력
from IPython.display import Image
Image(filename = 'decistion-tree.png')

test = pd.read_csv('/content/drive/MyDrive/Colab Notebooks/메뉴의사결정나무/테스트데이터.csv', encoding='CP949')

test.head()

x_test= test[feature_name]

model.predict(x_test)

import sklearn.metrics as mt

y_pred = model.predict(x_test)

test['예측메뉴'] = y_pred

test.head()

print('Train_Accuracy: ', model.score(x_train,y_train),'\n')

accuracy = mt.accuracy_score(y_test, y_pred)
precision = mt.precision_score(y_test, y_pred, average='micro')

accuracy

precision

