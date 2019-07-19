# control_of_flow

## 조건 표현식(Conditional Expression)


```
true_value if <조건식> else false_value
```

와 같이 표현식을 작성할 수 있다. 이는 보통 다른 언어에서 활용되는 삼항연산자와 동일하다.

```python
# 조건 표현식을 사용해봅시다.
a = int(input("숫자를 입력하세요 : "))
# 여기에 코드를 작성하세요.
print('0보다큼') if a > 0 else print('0보다 작거나 같음')
```

```
숫자를 입력하세요 : 3
0보다큼
```

```python
num = 2
result = '홀수입니다.' if num % 2 else '짝수입니다.'
print(result)
```

## break, continue, else

### break

```python
rice = ["보리", "보리", "보리", "쌀", "보리"]
# 여기에 코드를 작성하세요.
for st in rice:
    print(st)
    if st == "쌀":
        print('잡았다!')
        break
```

```
보리
보리
보리
쌀
잡았다!
```

### continue

```python
# 여기에 코드를 작성하세요.
age = [10, 23, 8, 30, 25, 31]
for a in age:
    if a < 20:
        continue
    print(f'{a}세는 성인입니다.')
```

### else

* `else` 문은 끝까지 반복문을 시행한 이후에 실행됩니다.(`break`를 통해 중간에 종료되지 않은 경우만 실행)

```python
numbers = [1, 5, 10]
# 여기에 코드를 작성하세요.
for num in numbers:
    if num == 3:
        print(Ture)
        break
else:
    print(False)
```

```
False
```

