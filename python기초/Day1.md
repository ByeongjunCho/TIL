# Python 기초

## N진수 생성 및 출력

```python
# n진수를 만들어보고, 출력 해봅시다.
binary_number = 0b10
octal_number = 0o10
decimal_number = 10
hexdecimal_number = 0x10
print(f'''
2진수 : {binary_number},
8진수 : {octal_number},
10진수 : {decimal_number},
16진수 : {hexdecimal_number}
''')
```

```
2진수 : 2,
8진수 : 8,
10진수 : 10,
16진수 : 16
```

### `float`(부동소수점, 실수)

실수는 `float`로 표현된다. 

다만, 실수를 컴퓨터가 표현하는 과정에서 부동소수점을 사용하며, 항상 같은 값으로 일치되지 않는다. (floating point rounding error)

```python
# 실수의 덧셈을 해봅시다.
3.5 + 3.2  # 6.7
# 실수의 뺄셈을 해봅시다.
3.5-3.12  # 0.3799999999999999
# 두 개의 값이 같은지 확인해봅시다.
3.5 - 3.12 == 0.38  # False
```

이는 컴퓨터가 2진수(비트)를 통해 숫자를 표현하는 과정에서 생기는 오류이며, 대부분의 경우는 중요하지 않으나 값을 같은지 비교하는 과정에서 문제가 발생할 수 있다.

* 따라서 다음과 같은 방법으로 처리 할 수 있다. 이외에 다양한 방법이 있음

```python
# 기본적인 처리방법을 알아봅시다.
a = 3.5 - 3.12 # 0.37999999999
b = 0.38
abs(a - b) <= 1e-10 # True

# sys 모듈을 통해 처리하는 방법을 알아봅시다.
import sys
abs(a - b) <= sys.float_info.epsilon  # True
print(sys.float_info.epsilon)  # 2.220446049250313e-16

# python 3.5부터 활용 가능한 math 모듈을 통해 처리하는 법을 알아봅시다.
import math
math.isclose(a, b)  # True
```

### `complex` (복소수)

복소수는 허수부를 `j`로 표현한다. 

```python
a = 3 + 4j
a.real # 실수부
a.imag # 허수부
a.conjugate() # 켤레복소수 (3-4ㅓ)
```

### 이스케이프 문자열

문자열을 활용하는 경우 특수문자 혹은 조작을 하기 위하여 사용되는 것으로 `\`를 활용하여 이를 구분한다. 

| <center>예약문자</center> |   내용(의미)    |
| :-----------------------: | :-------------: |
|            \n             |     줄바꿈      |
|            \t             |       탭        |
|            \r             |   캐리지리턴    |
|            \0             |    널(Null)     |
|           `\\`            |       `\`       |
|            \'             | 단일인용부호(') |
|            \"             | 이중인용부호(") |

```python
# 이스케이프 문자열을 조합하여 프린트해봅시다.
print('엔터!!\n그리고\t탭')
# 엔터!!
# 그리고	탭
```

```python
print('역슬레쉬는 이렇게 써야해요. \\')
# 역슬레쉬는 이렇게 써야해요. \
```

```python
print('따옴표 \'\"')
```

```python
# print를 하는 과정에서도 이스케이프 문자열을 활용 가능합니다.
print('내용을 옆으로 띄어서 표현하고 싶다.', end='\t')
print('탭탭')
# print는 기본적으로 end='\n'
# 내용을 옆으로 띄어서 표현하고 싶다.	탭탭
```

```python
# 물론, end 옵션은 이스케이프 문자열이 아닌 다른 것도 가능합니다.
print('개행문자 말고 다른것도 되는데', end='....')
print('진짜로', end='!!!')
# 개행문자 말고 다른것도 되는데....진짜로!!!
```

### String interpolation 

1) `%-formatting` 

2) [`str.format()` ](https://pyformat.info/)

3) [`f-strings`](https://www.python.org/dev/peps/pep-0498/) : 파이썬 3.6 버전 이후에 지원 되는 사항입니다.

`.format()`는 해당 [링크](https://pyformat.info/)에서 확인바랍니다.

```python
# name 변수에 이름을 입력해봅시다.
name = '홍길동'
# %-formatting을 활용해봅시다.
'Hello, %s' % name
# f-string을 활용해봅시다.
f'Hello, {name}'
```

