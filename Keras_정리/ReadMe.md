# Keras 예제를 이용한 Keras 사용법 정리

* Reference

  [Kaggle_Introduction to CNN Keras - 0.997 (top 6%)](https://www.kaggle.com/yassineghouzam/introduction-to-cnn-keras-0-997-top-6)

  [케라스 강좌](https://tykimos.github.io/lecture/)

  [케라스를 사용한 신경망 구현](https://datascienceschool.net/view-notebook/51e147088d474fe1bf32e394394eaea7/)

## 케라스 기본

```python
# 0. 사용할 패키지 불러오기
from keras.utils import np_utils
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Activation
# from tensorflow import keras  <= tensorflow 설치만 하면 keras를 사용할 수 있다.
```

```python
# 1. 데이터셋 생성하기
(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train = x_train.reshape(60000, 784).astype('float32') / 255.0  # Normalization
x_test = x_test.reshape(10000, 784).astype('float32') / 255.0    # Normalization
y_train = np_utils.to_categorical(y_train, 10)
y_test = np_utils.to_categorical(y_test, 10)
```

`keras.np_utils.categorical()` 를 이용해 `One-Hot-Encoding` 을 할 수 있다.

```python
# 2. 모델 구성하기
model = Sequential()
model.add(Dense(units=64, input_dim=28*28, activation='relu'))
model.add(Dense(units=10, activation='softmax'))
```

* `Sequential` 모형 클래스 객체 생성
* `add` 메서드로 레이어 추가
  * 입력단부터 순차적 추가
  * 레이어는 출력 뉴런 갯수를 첫번째 인수로 받는다.
  * 최초의 레이어는 `input_dim` 인수로 입력 크기를 설정해야 한다.

```python
# 3. 모델 학습과정 설정하기
from keras.optimizers import SGD
model.compile(loss='categorical_crossentropy', optimizer=SGD(lr=0.2), metrics=['accuracy'])
```

* `compile` 메서드로 모형 완성  
  * `loss` : 비용함수 설정 [`loss`에 입력 가능한 카테고리](https://keras.io/losses/)
  * `optimizer` : 최적화 알고리즘 설정[`optimizer에 입력 가능한 카테고리`](https://keras.io/optimizers/)
  * `metrics` : 트레이닝 단계에서 기록할 성능 기준 설정

```python
# 4. 모델 학습시키기
hist = model.fit(x_train, y_train, epochs=5, batch_size=32, validation_data=(x_test, y_test), verbose=2)
```

* `fit` 메서드로 트레이닝
  * `nb_epoch` : 에포크(epoch) 횟수 설정
  * `batch_size` : 배치크기(batch_size) 설정
  * `verbos` : 학습 중 출력되는 문구 설정. `Jupyter Notebook`을 사용할 때는 `verbose=2` 로 설정하여 진행 막대(progress bar)가 나오지 않도록 설정할 수 있다.

```python
# 5. 학습과정 살펴보기
print('## training loss and acc ##')
print(hist.history['loss'])
print(hist.history['acc'])
```

```python
# 6. 모델 평가하기
loss_and_metrics = model.evaluate(x_test, y_test, batch_size=32)
print('## evaluation loss and_metrics ##')
print(loss_and_metrics)

# 7. 모델 사용하기
xhat = x_test[0:1]
yhat = model.predict(xhat)
print('## yhat ##')
print(yhat)
```

```python
# 만들어진 모형 확인
model.summary()
```

```
Model: "sequential"
_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
dense (Dense)                (None, 15)                11775     
_________________________________________________________________
dense_1 (Dense)              (None, 10)                160       
=================================================================
Total params: 11,935
Trainable params: 11,935
Non-trainable params: 0
_________________________________________________________________
```

```python
# 각 레이어의 특성 확인
l1 = model.layers[0]
l2 = model.layers[1]

print(l1.name, type(l1), l1.output_shape, l1.activation.__name__, l1.count_params())
print(l2.name, type(l1), l2.output_shape, l2.activation.__name__, l2.count_params())
```

```
dense <class 'tensorflow.python.keras.layers.core.dense'> (None, 15) sigmoid 11775
dense_1 <class 'tensorflow.python.keras.layers.core.dense'> (None, 10) sigmoid 160
```

* `from tensorflow import keras` 와 `from keras import ...` 를 사용했을 때 속성이 달라질 수 있다.

## 가중치 정보

트레이닝이 끝난 모형의 가중치 정보는 `get_weights` 메서드로 구할 수 있다. 이 메서드는 신경망 모형에서 사용된 가중치 *w* 값과 *b* 값을 출력한다.

```python
# 첫번째 레이어
w1 = l1.get_weights()
w1[0].shape, w1[1].shape
# ((784, 15), (15,))

# 두번째 레이어
w2 = l2.get_weights()
w2[0].shape, w2[1].shape
((15, 10), (10,))
```

## 모형의 사용

트레이닝이 끝나면 `predict` 메서드로 y값을 출력하거나 출력된 y값을 각 클래스에 대한 판별함수로 가정하고 `predict_classes` 메서드로 분류를 수행할 수 있다.

```python
model.predict(X_test[:1, :])
```

```
array([[0.13069251, 0.05602819, 0.05318496, 0.11021447, 0.1379965 ,
        0.1319567 , 0.06235668, 0.7017868 , 0.06432711, 0.2564229 ]],
      dtype=float32)
```

## 모형의 저장

트레이닝이 끝난 모형은 `save` 메서드로 가중치와 함께 "hdf5" 형식으로 저장하였다가 나중에 `load`명령으로 불러 사용할 수 있다. 

```python
model.save('my_model.hdf5')
del model

from tensorflow.keras.models import load_model

model2 = load_model('my_model.hdf5')
print(model2.predict_classes(X_test[:1, :], verbose=0))
```



