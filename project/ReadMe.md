# project

## 01. 영화진흥위원회 오픈 API(주간/주말 박스오피스 데이터) 

`01.ipynb`

- 기본 요청 URL : http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.xml (또는 .json)

|  요청 변수   |      값      |                             설명                             |
| :----------: | :----------: | :----------------------------------------------------------: |
|     key      | 문자열(필수) |                 발급받은키 값을 입력합니다.                  |
|   targetDt   | 문자열(필수) |     조회하고자 하는 날짜를 yyyymmdd 형식으로 입력합니다.     |
|    weekGb    |    문자열    | 주간/주말/주중을 선택 입력합니다 “0” : 주간 (월~일) “1” : 주말 (금~일) (default) “2” : 주중 (월~목) |


```python
# 요청 인터페이스
targetDt = '20190713' #yyyymmdd 날짜정보
weekGb = '0'  # 주간 : 0, 주말 : 1, 주중 : 2
api_url = f'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json?key={key}&targetDt={targetDt}&weekGb={weekGb}'
# 다른 정보는 이레 링크
```

```python
# 응답 구조 Key    
# movieCd 영화 대표코드
# movieNm 영화명
# audiAcc 누적관객수
# 모든 key는 한글로 작성하였다.
```

`boxoffice.csv`

범주 : 영화명, 영화 대표코드, 해당일 누적관객수

[주간/주말 박스오피스 API 서비스](http://www.kobis.or.kr/kobisopenapi/homepg/apiservice/searchServiceInfo.do)



## 02. 영화진흥위원회 오픈 API(영화 상세정보)

`02.ipynb`

- 기본 요청 URL : http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieInfo.xml (또는 .json)

| 요청 변수 |      값      |            설명             |
| :-------: | :----------: | :-------------------------: |
|    key    | 문자열(필수) | 발급받은키 값을 입력합니다. |
|  movieCd  | 문자열(필수) |   영화코드를 지정합니다.    |

```python
movieCd = '20192591'  #
api_url = f'http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieInfo.json?key={key}&movieCd={movieCd}'
response = requests.get(api_url).json()
```

```python
    # movieCd 영화 대표코드
    # movieNm 영화명(국문)
    # movieNmEn 영화명(영문)
    # movieNmOg 영화명(원문)
    # watchGradeNm 관람등급
    # openDt 개봉년도
    # showTm 상영시간
    # genreNm 장르
    # directors.get(peopleNm) 감독명
    # 모든 key는 한글로 작성하였다.
```

`movie.csv`

범주 : 영화 대표코드, 영화명(국문), 영화명(영문), 영화명(원문), 관람등급, 개봉년도, 상영시간, 장르, 감독명

## 3. 영화진흥위원회 오픈 API(영화인 정보)

`03.ipynb`

- 기본 요청 URL : http://www.kobis.or.kr/kobisopenapi/webservice/rest/people/searchPeopleList.xml (또는 .json)

| 요청 변수 |      값      |            설명             |
| :-------: | :----------: | :-------------------------: |
|    key    | 문자열(필수) | 발급받은키 값을 입력합니다. |

```python
key = '39482ee966f81c52351ae45548ec214f'
peopleNm = '브래드 버드'
api_url = f'http://www.kobis.or.kr/kobisopenapi/webservice/rest/people/searchPeopleList.json?key={key}&peopleNm={peopleNm}'

```

```python
# peopleCd 영화인 코드
# peopleNm 영화인명
# repRoleNm 분야
# filmoNames 필모리스트
# 모든 key는 한글로 작성하였다.
```

`director.csv`

범주 : 영화인 코드, 영화인명, 분야, 필모리스트