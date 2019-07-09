# Startcamp Day1

## Python 기초 문법

1. 저장

   ```python
   # 저장은 = 을 통해서 한다.
   dust = 64 # 숫자(interger)
   name = '홍길동' # 문자열(string)
   is_summer = True # 참/거짓, Boolearn(True/False)
   
   # 리스트 활용법
   my_list = [1, 2, 3, 4, '정지수', '염겨레']
   print(my_list[0]) # => 1
   # 딕셔너리 활용법
   my_dictionary = {'정지수' : '남자', '염겨레': '남자'}
   print(my_dictionary['정지수']) # => '남자'
   
   ```

   

2. 조건

   ```python
   if dust > 150:
       print('매우나쁨')
   elif dust > 80:
       print('나쁨')
   else:
       print('보통')
   ```

   

3. 반복

   ```python
   lunch_box = ['짬뽕', '류산슬덮밥', '돈육제육..']
   # 정해진 리스트 반복
   for menu in lunch_box:
       # menu = lunch_box[0], ..... menu = lunch_box[2]
       print(menu)
   # n번 반복
   for i in range(5):
       print('hello!!')
   ```

4. 내장함수

   > 내장함수는 별도로 import 구문이 필요없다.

   ```python
   print('hi')
   print(max([2, 4, 1])) #=> 4
   print(min([1, 2, 5])) #=> 1
   print(abs(-5)) #=> 5
   print(len([1, 2, 3])) #=> 3
   ```



5. 외장함수

   > 외장함수는 반드시 import가 필요하다.
   >
   > 다만, 파이썬을 설치하면 그냥 불러서 쓸 수 있다.

   ```python
   import random
   numbers = range(1, 46)
   lotto = random.samples(numbers, 6)
   print(sorted(lotto))
   ```
   
   
   
6. 패키지

   > 패키지는 반드시 설치를 필요로 한다.

   *'pip install + 패키지명 '* 으로 설치를 한다.

   ```bash
   $ pip install requests
   ```

   ```python
   import requests
   requests.get(url)
   ```
   
   
   
   ## 파이썬을 통한 크롤링
   
   1. 필수 설치 패키지
   
      * requests : 파이썬으로 요청을 보내는 패키지
      
      * bs4 : 문자열을 html으로 구조화(파싱)를 해주는 패키지
      
        ```bash
        $ pip install requests
        $ pip install bs4
        ```
      
   2. 네이버에서 코스피지수 가져오기
   
      ```python
      # 0. 활용할 페키지를 불러온다.
      import requests
      from bs4 import BeautifulSoup
      # 1. url을 설정한다.
      url = 'https://www.naver.com/sise/'
      # 2. 요청을 보내고, 그 결과의 내용을 text response에 저장한다.
      response = requests.get(url).text
      # 3. html 문서로 변환한다.
      soup = BeautifulSoup(response, 'html.parser')
      # 4. 원하는 값을 선택자(selector)를 활용해서 가져온다.
      kospi = soup.select_one('#KOSPI_now').text
      ```
   
   3. 간단한 인터넷 웹 열기
   
      ```python
      import webbrowser # 인터넷 브라우저를 open할 수 있는 모듈
      
      idols = ['bts', 'iu', 'ian goodfellow']
      
      for idol in idols:
          # string interpolation
          # 문자열 보간법 : f-string / 3.6+  
          webbrowser.open(f'https://search.naver.com/search.naver?&query={idol}')
      ```
   
      
   









## Typora 간단 사용법

* markdown 편집 툴(beta) 다운로드 => 

* '# Startcamp.... ' => 글씨크기 

* '## Python 기초 문법' => 글씨크기 중간

* '1. 불라불라'  => 번호쓰기

* ' ```(~~~) 프로그래밍 언어 ' => 코드 저장

* ctrl + / => 작성한 명령어를 볼수 있다.
* '*숫자'를 하면 순서에 상관없이 다시 숫자를 만들 수 있다.

> 변수명 짓기

+ ex) BeautifulSoup : comel case(낙타) =>  *함수명에 사용* 
+ ex) select_case : snake case(뱀) => *변수명에 주로 사용*