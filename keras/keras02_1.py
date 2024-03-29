from keras.models import Sequential
from keras.layers import Dense
import numpy as np

x_train = np.array([1,2,3,4,5,6,7,8,9,10])
y_train = np.array([1,2,3,4,5,6,7,8,9,10])
x_test = np.array([101,102,103,104,105,106,107,108,109,110])
y_test = np.array([101,102,103,104,105,106,107,108,109,110])

model = Sequential()
model.add(Dense(5, input_dim =1 , activation='relu'))
model.add(Dense(3))
model.add(Dense(1, activation='relu'))

model.summary()
'''
model.compile(loss='mse', optimizer='adam', metrics=['mse'])

model.fit(x_train, y_train, epochs=100, batch size=25 validation_data = (x_test, y_test))
loss, mse = model.evaluate(x_test, y_test, batch size=25)

print("loss : ", loss)
print("mse : ", mse)

y_predict = model.predict(x_test)
print("결과물 : \n", y_predict)
'''