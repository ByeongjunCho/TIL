# Day 4

## Python Dictionary

```python
my_dict = {'apple': '사과', 'banana': '바나나'}

# 1. 일반 반복문
for key in my_dict:
    print(key)
    print(my_dict[key]) # value 접근
    
# 2. key, value
for key, value in my_dict.items():
    print(key, value)
# 3. value
for value in my_dict.values():
    print(value)
    
# 4. key
for key in my_dict.keys():
    print(key)
```

```python
my_dict = {'apple': '사과', 'banana': '바나나'}
my_dict['apple']
# => 사과
my_dict['cat']
# => 오류발생(Key Error)
my_dict.get('apple')
# => 사과
my_dict.get('cat')
# => None
my_dict.get('cat', 'Not Found')
# => 'Not Found'
```





# HTML 문법

## python flask 실행

```python
# 0. flask 패키지 가져오기
from flask import Flask, render_template

# 1. app 설정
app = Flask(__name__)

# 2. 요청 경로(route) + 함수 만들기
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hello/<string:name>')
def hello(name):
    return render_template('hello.html',namee=name)

if __name__ == "__main__":
    app.run(debug=True)

```

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    <!-- jinja2 : 템플릿 엔진 -->
    <!-- {# {%__% } 로직 코드 #}-->
    <!-- {# {{  }} } 출력 코드 #}-->
    <!-- <h1>{{namee}} 안녕?</h1> -->
    {% if namee == '용흠' %}
        <h1>{{namee}} 님 안녕하십니까.</h1>

    {% else %}
        <h2>{{ namee }} ㅎㅇ.</h2>
    {% endif %}
    <SCRIPT language='python'>
    </SCRIPT>
</body>
</html>
```

* `html` 주석 처리를 하여도 <!-- {%__%} 로직 코드-->  를 읽어서 {%__%}사이가 비어 있기 때문에 오류를 출력하게 된다.

* 이를 방지하기 위해 <!-- {#{{ .... }}  #} --> 처럼 주석 처리를 한번 더 해주어야 한다.

* ```html
  <body>
  <!-- {# {%__% } 로직 코드 #}-->
  <!-- {# {{  }} } 출력 코드 #}-->
  <!-- <h1>{{namee}} 안녕?</h1> -->
  </body>
  ```