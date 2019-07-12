# Day 3

# List실습

```python
# 3. map : 첫번째 인자의 함수를 두번째 인자를 반복하며 적용.
# 반복가능한 객체에 함수를 각각 적용.
map = (함수, 반복 가능한 객체)

# 2. list comprehension
prices = [int(x) for x in prices]
```

## HTML/CSS

### HTML

`HTML` 은 HyperText Markup Language의 약자로 웹 문서를 구조화 하는데 사용되는 언어이다.

1. HTML의 기본 구조

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
           <h1>안녕?안녕?안녕?</h1>
   </body>
   </html>
   
   ```

   * `<head>` `</head>` 는 문서의 정보를 담고 있다.
   * `<body>` `</body>` 는 문서의 본문을 담고 있다.

2. 태크의 종류

   1. 기본적으로 태그는 `여는태그` 와 `닫는태그`로 구성된다

      ```html
      <h1>
          제목1
      </h1>
      ```

      

   2. `닫은태그` 가 없는 경우도 있다(self-closing tag)

      ```html
      <img src="__"/>
      ```

   3. 태그의 구성

      ```html
      <img src="__" width="300" height="300"/>
      <a href="https://google.com" class="blue"></a>
      ```

      * 태그별로 공통적으로 가질 수 있는 속성 : `id`, `class`, `style`
      * 각 태그별로 가질 수 있는 속성이 추가적으로 있다.
        * img - `src`, `width`, `height`
        * a - `href`

### CSS

CSS는 Cascading Style Sheets의 약자로, HTML을 꾸며주는 역할을 한다.

HTML을 꾸며주기 위하여, `선택자(selector)` 를 통해 특정한 element를 지정하여야 한다.

1. 선택자

   * 태그 선택자

     ```html
     p {
         color: red;
     }
     ```

     

   * class 선택자

     ```html
     .blue{
         color : blue;
     }
     ```

     

   * id 선택자

     ```html
     #pink {
         color: pink;
     }
     ```

   선택자 우선순위는 id선택자 > class선택자 > 태그선택자 순서로 적용된다.



# Flask

### 기본 활용법

`Flask` 는 파이썬 기반의 micro framework이다.

1. 설치

   ```bash
   $ pip install flask
   ```

2. 기본 코드

   ```python
   from flask import Flask
   app = Flask(__name__)
   
   @app.route('./')
   def hello():
       return 'Hello!'
   if __name__ == '__main__':
       app.run(debug=True)
   ```

3. 서버 실행

   ```bash
   $ flask run
   ```

   * 기본적으로 `flask run` 명령어는 `app.py` 파일을 실행시킨다. 만약 다른 파일명으로 만들었다면, 옵션을 추가해야 한다.
   * 마지막 두 줄을 작성해놓았다면, 아래와 같이 실행도 가능하다.

   ```bash
   $ python app.py
   ```



## Variable routing

요청 오는 url을 변수화하여 값을 사용할 수 있다.

```python
@app.route('/hi/<string:name>')
def hi(name):
    return f'{name}아 안녕?'
```

## Rendering Template

`HTML` 파일을 만들어 활용할 수 있다. 기본적으로 `templates` 폴더에 파일을 만들어야 한다.

```
app.py
tempaltes/
	hi.html
	lunch.html
	index.html
```

```python
from flask import Flask, render_template
# ...
@app.route('/hi')
def hi():
    return render_template('hi.html')
```

`HTML` 파일에서 변수의 값을 출력하고자 한다면, 키워드 인자로 그 값을 넘겨줘야 한다.

```python
return render_template('app.html', name=name)
```

그리고 출력을 위해서는 `{{ }}` 사용한다.

```jinja2
<h1>{{name }} 안녕? </h1>
```



## Flask Template Engine - jinja2

Flask는 기본적으로 Template을 만들 때 `jinja2` 언어를 사용한다. 기본 문법은 다음과 같다.

1. 값 출력

   ```jinja2
   <h1> {{name}}, 안녕? </h1>
   ```

2. 조건문

   ```jinja2
   {% if name == '용흠' %}
   	<h1>반장님 안녕하세요</h1>
   {% else %}
   	<h2>ㅎㅇ</h2>
   {% endif %}
   ```

3. 반복문

   ```jinja2
   {% for menu in menu_list %}
   	<li> {{ menu }}</li>
   {% endfor %}
   ```


## Form data

HTML에서 사용자로부터 정보를 받기 위해서는 `form` 탬그를 활용한다.

### form 태그 기본 구조

```html
<!-- templates/ping.html -->
<form action="/pong">
    <input type="text" name="say">
    <input type="radio" name="gender" value="M">남자
    <input type="radio" name="gender" value="F">여자
    <input type="submit" value="전송">
</form>
```

* form 태그는 `action` 속성으로 해당 폼이 전송될 `url`을 지정해야 한다.
* form 태그 내에는 `input` 태그들을 정의하여, 사용자에게 받을 정보를(설문지를 만든다.)만들어놓는다.
* `input` 태그에는 어떤 종류의 입력을 받을지(`type`)와 어떤 변수에 담아서 보낼지(`name`) 정의한다.

### Flask에서 사용자 정보 받기

1. 사용자가 입력할 수 있는 `form` 보내주기

   ```python
   # app.py
   @app.route('/ping')
   def ping():
       return render_template('ping.html')
   ```

   ```html
   <!-- templates/ping.html -->
   <form action="/pong">
       <input type="text" name="say">
       <input type="submit" value="전송">
   </form>
   ```

   

2. 정보 받아서 활용하기

   ```python
   # app.py
   from flask import Flask, render_template, request   # form에서 정보를 받는 모듈
   
   # ...
   
   @app.route('/pong')
   def pong():
       say = request.args.get('say')
       return render_template('pong.html', say_template=say)
   ```

   ```html
   <!-- templates/pong.html -->
   <h1>
        {{ say_template }}~~~
   </h1>
   ```

   * `request.args` 는 일종의 `dictionary` 이고, `key` 는 `input` 에 정의한 `name` 이고 사용자가 입력한 값은 `value` 이다.



## PDF정리 HTML이란?

`HTML`은 웹페이지를 만들기 위한 언어로 웹브라우저 위에서 동작하는 언어로 웹페이지를 기술하기 위한 **마크업 언어**이다.

### 1) HTML태그의 형식

**<태그명 속성명1="속성값1" 속성명2="속성값2"> 정보 </태그명>**

* **태그(Element, 요소)**는 컨텐츠를 감싸서 그 정보의 성격과 의미를 정의한다.
* **속성(Attribute)**은 태그의 부가적인 정보가 들어온다.

### 2) HTML 문서의 구조

* HTML 문서는 파일의 확장자가 `html` 혹은 `htm`으로 끝난다.

* 최상위 태그로 <html>을 사용한다. 그 하위에 <head> 태그와 <body> 태그를 컨텐츠로 가지고 있다.

* <head> 태그는 문서를 설명하는 태그로 제목이나 키워드와 같은 정보를 담는다.

* <body> 태그에는 문서의 내용이 위치한다.

```html
<!DOCTYPE html>
<html lang="ko">
    <head>
        <meta charset="utf-8">
        <title>첫번째 HTML</title>
    </head>
    <body>
    </body>
</html>
```

* 다양한 태그 도움말은 [SSAFY 수업자료 google drive : HTML](https://drive.google.com/drive/folders/1MjFf60qUfw3-vsAp475cp3XcgfdvoQ1a)에서 확인 가능하다.

## 2. CSS란?

HTML이 정보를 표현한다면 CSS는 HTML을 시각적으로 꾸며주는 역할을 한다.

HTML5에서는 **HTML는 정보의 구조화**, **CSS는 styling의 정의**라는 본연의 임무에 충실한 명확한 구분이 이루어졌다.

### 1) HTML에서 CSS 사용하기

**a. inline 방식**

```html
<!DOCTYPE html>
<html lang="ko">
    <head>
        <meta charset="utf-8">
        <title>첫번째 HTML</title>
    </head>
    <body>
        <p style="font-size:20pt;color:blue">스타일이 지정된 문단이다.</p>
    </body>
</html>
```

* 우선순위 : `id` > `class` > `tag`

* HTML 태그에 스타일을 직접 기술하는 방식
* CSS 선언이 분명해서 style tag 방식에 비해 엘리먼트에 영향을 주고 있는 CSS를 추적하기가 쉽다.
* 코드가 많아지고, 의미와 디자인의 분리라는 CSS의 취지와 벗어난다.

**b. style tag 방식**

```html
<!DOCTYPE html>
<html lang="ko">
    <head>
        <meta charset="utf-8">
        <title>첫번째 HTML</title>
        <style>
            /* 태그 선택자 */
            p {
                color: blue;
                text-aligh: center;
            }
            
            /* 클래스 선택자 */
            .red{
                color : red;
            }
            
            /* 아이디 선택자 */
            # pink{
                color : pink;
            }
        </style>
    </head>
    <body>
        <h2 id="pink">안녕하세요.</h2>  
        <p>스타일이 inline형식으로 지정된 문단이다.</p>
        <p class="red">나는 빨간색이고 싶어요.</p>
    </body>
</html><!DOCTYPE html>
<html lang="ko">
    <head>
        <meta charset="utf-8">
        <title>첫번째 HTML</title>
    </head>
    <body>
        <p>
            스타일이 tag방식으로 지정된 문단이다.
        </p>
    </body>
</html>
```



* style 태그에 기술하는 방식
* inline 방식 대비 경제적으로 코디할 수 있다.
* 의미와 디자인의 분리라는 CSS의 취지와 부합하다.

**c. 외부 파일 방식 **

```html
/* style.css */
p { background-color: red}
```



* CSS를 별도의 파일로 분리해서 링크하는 방식

* 문법적으로는 style tag와 동일

* 파일의 교체로 디자인을 변경할 수 있다는 점에서 유지보수가 편리하다.

### 2) CSS의 형식

> 선택하는 대상 + { 꾸며주는 법; }
>
> p { font-size: 15px; }

**a. 선택자**

**요소 선택자(type)**

* 특정 태그명을 가진 엘리먼트 전체를 제어하기 위해서 사용
* css 선택자에서는 태그의 이름을 사용함

**클래스 선택자(class)**

* class 속성은 일련의 태그를 그룹핑해서 하나처럼 제어하기 위해서 사용
* class 속성에는 공백으로 구분된 여러개의 class 가 표시될 수 있음

**아이디 선택자(id)**

* id 속성은 전체 문서에서 하나의 태그를 식별하기 위해서만 사용됨
* 우선순위가 가장 높음
* css 선택자에서는 #을 사용해서 id 임을 표시



## 다양한 HTML 사용요소

```html
<body>
    <a href="https://google.com"> 구글로 가즈아!</a>
    <iframe width="300" height="100" src="https://www.youtube.com/embed/A7KxKh1IBeg" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

</body>
```

* `<a>` : 하이퍼링크를 걸어줄 수 있음
* `youtube` 의 공유 속성을 이용하여 동영상 참조가 가능하다.

  

  

### 참고사항

[HTML example page](https://startbootstrap.com/)

[Github page](https://pages.github.com/)






vs code : open in browser