# Project

# 1. CSV 파일 읽고 쓰기

## 1.1 CSV 파일 쓰기

```python
# CSV에 입력할 데이터 생성
students = {
    'asdf1': {
        '순번': '01',
        '이름': '김성훈'
    },
    'asdf2': {
        '순번': '02',
        '이름': '김은정'
    }
}
```

```python
# 1. write함수를 이용할 경우
with open('c.csv', 'w', encoding='utf-8') as f:
    f.write('number, name\n') # 범주를 적어준다.
    for number, name in students.items():  # students의 value값인 
        # (순번, 이름)을 (number, name)에 대입하여 작성한다.
        f.write(f'{number}, {name}\n')
```

```
--------c.csv----------
number, name
ㅁㄴㅇㄹ1, {'순번': '01', '이름': '김성훈'}
ㅁㄴㅇㄹ2, {'순번': '02', '이름': '김은정'}
```

```python
# csv 모듈을 이용하는 경우
import csv
with open('b.csv', 'w', encoding='utf-8') as f:
    fieldnames = ['순번', '이름']
    csv_writer = csv.DictWriter(f, fieldnames=fieldnames)
    csv_writer.writeheader()  # 범주이름을 적어준다.
    for item in students.values():  # 값을 작성한다.
        csv_writer.writerow(item)
```

### 다음과 같이 도 가능하다.

```python
students2 = [
    {
        '순번': '01',
        '이름': '김성훈'
    },
    {
        '순번': '02',
        '이름': '김은정'
    }

]
import csv
with open('b.csv', 'w', encoding='utf-8') as f:
    fieldnames = ['순번', '이름']
    csv_writer = csv.DictWriter(f, fieldnames=fieldnames)
    csv_writer.writeheader()    
    for item in students2:
        csv_writer.writerow(item)
```

### b.csv

```
순번,이름

01,김성훈

02,김은정
```

## 1.2 CSV 파일 읽기

```python
import csv
with open('movie.csv', 'r', encoding='utf-8') as f:
    movie = csv.DictReader(f)  # csv 메서드를 이용하여 읽는다.
    for line in movie:
        print(line)
```

```
OrderedDict([('영화 대표코드', '20181181'), ('영화명(국문)', '미션 임파서블: 폴아웃'), ('영화명(영문)', 'Mission:Impossible- Fallout'), ('영화명(원문)', ''), ('관람등급', '15세이상관람가'), ('개봉연도', '20180725'), ('상영시간', '147'), ('장르', '액션'), ('감독명', '크리스토퍼 맥쿼리')])
OrderedDict([('영화 대표코드', '20183361'), ('영화명(국문)', '인크레더블 2'), ('영화명(영문)', 'INCREDIBLES 2'), ('영화명(원문)', ''), ('관람등급', '전체관람가'), ('개봉연도', '20180718'), ('상영시간', '125'), ('장르', '애니메이션'), ('감독명', '브래드 버드')])
.....

```

### 다음과 같이 Dictionary 형태로 출력된다. key를 이용하여 원하는 값을 출력할 수 있다.





