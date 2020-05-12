from keras.models import Sequential
from keras. layers import Dense
import numpy as np

x_train = np.array([1,2,3,4,5,6,7,8,9,10])
y_train = np.array([1,2,3,4,5,6,7,8,9,10])
x_test = np.array([101,102,103,104,105,106,107,108,109,110])
y_test = np.array([101,102,103,104,105,106,106,108,109,110])

model = Sequential()
model.add(Dense(5, input_dim =1 , activation='relu'))
model.add(Dense(3))
model.add(Dense(1, activation='relu'))

model.summary()

 import numpy as np 
넘파이를 땡겨오겠다 np 라고 칭하겠다. 
x = np.array([1,2,3])
넘파이의 배열 형태를 가져오겠는데 1,2,3,이라는 숫자 그룹을 가져오고 넘파이로 하겠다. 
우리가 중점적으로 다루어야하는것들에는 
1.에포=몇번 반복하여서 반복할건지를 결정
2, 노드갯수
3. 레이어깊이=DEEP
4. batch size=몇개씩 끊어서 측정할것이냐를 판단
이 위에 단계들이 우리의 특기가 되는 것이고 이를 하이퍼 파라미터 튜닝이라고 한다.  
우리의 취미는 전처리가 된다 전처리는 아직 배우지 않았으며 차후에 배우게 될것이다.

y=wx+b는 회귀모델 이것을 예측하는 것이다. 

epoch를 반복하면서 결론적으로는 weight값을 알아내는 것이다. 
기계한테 이를 훈련시키는 것이다. 
정제된데이터, 보통은 받은 데이터를 정제 시켜야 한다. 
그래서 구하는 것이 최적의 W값
y=wx+b x를 구하면 그리고 초반에 w를 구하면 predict 하여 y값을 구할 수 있다. 

model=Sequential
Layers= Dense

*딥러닝 케라스의 기본구조*
1. 데이터 준비
2. 모델구성
3. 컴파일, 훈련
4. 평가, 예측
 
