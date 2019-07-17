# 함수의 return

앞서 설명한 것과 마찬가지로 함수는 반환되는 값이 있으며, 이는 어떠한 종류의 객체여도 상관없습니다. 

단, 오직 한 개의 객체만 반환됩니다.

함수가 return 되거나 종료되면, 함수를 호출한 곳으로 돌아갑니다.

시험문제인가봐요

# 함수의 인수

함수는 `인자(parameter)`를 넘겨줄 수 있습니다.

* 인수(arguments) : 함수 호출
* 인자(parameter) : 함수 정의

## 가변 인자 리스트

앞서 설명한 `print()`처럼 정해지지 않은 임의의 숫자의 인자를 받기 위해서는 가변인자를 활용합니다. 

가변인자는 `tuple` 형태로 처리가 되며, `*`로 표현합니다. 

**활용법**

```python
def func(*args):   # 입력이 여러개 들어갈 수 있음
```

## 정의되지 않은 인자들 처리하기

정의되지 않은 인자들은 `dict` 형태로 처리가 되며, `**`로 표현합니다. 

주로 `kwagrs`라는 이름을 사용하며, `**kwargs`를 통해 인자를 받아 처리할 수 있습니다.

**활용법**

```python
def func(**kwargs):
    print(kwargs)
func(사과='apple', 바나나='banana', 고양이='cat')
# {'사과': 'apple', '바나나': 'banana', '고양이': 'cat'}
```

## dictionary를 인자로 넘기기(unpacking arguments list)

`**dict`를 통해 함수에 인자를 넘길 수 있습니다.

```python
my_dict = {'사과': 'apple', '바나나': 'banana', '고양이': 'cat'}
func(**my_dict) # {'사과': 'apple', '바나나': 'banana', '고양이': 'cat'}
# **my_dict => 사과='apple', 바나나='banana', 고양이='cat'
```



## 이름공간 및 스코프(Scope)

파이썬에서 사용되는 이름들은 이름공간(namespce)에 저장되어 있습니다.
그리고, LEGB Rule을 가지고 있습니다. 

변수에서 값을 찾을 때 아래와 같은 순서대로 이름을 찾아나갑니다.
* `L`ocal scope: 정의된 함수
* `E`nclosed scope: 상위 함수 
* `G`lobal scope: 함수 밖의 변수 혹은 import된 모듈
* `B`uilt-in scope: 파이썬안에 내장되어 있는 함수 또는 속성
* 시험문제인가봐요