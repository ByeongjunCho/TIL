# CSS 기본

## 1. CSS 기본사항

### 1.1 내부참조

> html 파일 내 `<style>` 태그에 선택자를 작성하는 방법

```html
<!-- 내부참조(embed) head 태그 내에 style 태그 활용 -->
  <style>
    /* 태그 선택자 */
    h1 {
      color: red;
    }
    /* 클래스 선택자 : .클래스명 */
    .blue{
      color: blue;
    }
    .brown{
      color: brown !important;
    }
    h3{
      color: pink;
    }
    /* 아이디 선택자 : #아이디명 */
    #green {
      color: green;
    }
  </style>
</head>

  <!-- 선택자는 우선순위가 있다.
        id > class > tag
        id는 문서에서 반드시 한번만 등장!
        class는 문서에서 여러번 등장!
  -->
```

### 1.2 외부참조

* 외부 <파일명>.css 의 선택자 사용

```html
<!-- 외부파일 링크 link:css-->
<link rel="stylesheet" href="01_style.css">
```

### 1.3 inline 참조

* inline에 선택자 적용하는 방법

```html
  <p style="color: purple;">인라인 CSS활용</p> 
```

### 1.4 선택자 우선순위

```html
<h2 class="blue">선택자</h2>
  <h3 class="blue">태그 선택자</h3> <!-- 클래스 선택자 > 태그 선택자 -->
  <h3 id="green">클래스 선택자</h3> <!-- 아이디 선택자 > 태그 선택자 -->
  <h3 id="green" class="blue">아이디 선택자</h3> <!-- 아이디 선택자 > 클래스 선택자 > 태그 선택자 -->
  <p id="green" style="color: purple;">인라인 CSS활용</p> <!-- inline 선언 > 선택자 선언 -->
  <!-- !important가 CSS 적용이 가장 우선된다.
       하지만 사용에 주의하자(남발하지 말자)
       모두 !important인 경우 다음 우선순위 : inline > id > class 
  -->
  <p id="green" class="brown" style="color: coral;">무슨 색일까요?</p> <!-- brown class가 !important요소가 있으므로 우선된다.-->
```

## 2. 선택자

### 2.1 그룹선택자

* 여러개의 tag를 그룹하여 선택자 지정이 가능하다.

```css
/* 1. 그룹 선택자 */
h1, h2, h3, h4, h5, h6, .darkblue {
  color: darkblue;
}
```

### 2.2 인접 선택자

* 선택자1 + 선택자2{} : 선택자 1바로 다음에 오는 동생 선택자2 선택

```css
/* 인접 선택자 */
.blue + .red + div {
  background-color: purple;
}
```

### 2.3 자식 선택자

* 선택자와 선택자는 ">"로 구분
* 선택자1 > 선택자2 : 선택자 1의 자식요소 선택자2만 선택
* **자식 선택자는 후손 선택자보다 우선한다**

```css
/* 자식 선택자 */
.parent > li {
  color:red;
}
```

### 2.4 후손 선택자

* 후손 선택자는 계층 구조에서 하위에 오는 모든 자손을 선택한다.
* 선택자와 선택자는 공백문자로 구분
* 선택자1 선택자2 : 선택자 1의 후손 중 선택자 2를 선택

```css
/* 후손 선택자 */

.ancestor li {
  font-size: 40px;
}

.ancestor ul li {
  color:blue;
  font-size: 20px;
}
```

## 3. 단위 요소

### 3.1  상대 선택자

`rem` : 최상위 요소, 즉 `html` 요소 크기의 배수

```html
<!doctype html>
<html lang="ko">
  <head>
    <meta charset="utf-8">
    <title>CSS</title>
    <style>
      html { font-size: 16px; }
      body { font-size: 1.5em; }
      .a { font-size: 2.0rem; }
    </style>
  </head>
  <body>
    <p class="a">Lorem Ipsum Dolor</p>
  </body>
</html>
```



`em` :상위 요소 크기의 배수

```html
<!doctype html>
<html lang="ko">
  <head>
    <meta charset="utf-8">
    <title>CSS</title>
    <style>
      html { font-size: 16px; }
      body { font-size: 1.5em; }
      .a { font-size: 2.0em; }
    </style>
  </head>
  <body>
    <p class="a">Lorem Ipsum Dolor</p>
  </body>
</html>
```

`html`은 16px, `body`는 상위 요소인 `html` 16px에 1.5배인 24px다. 여기서 `<a>`는 상위요소 `body`의 2.0em이 되어 최종적으로 `<a>`태그는 `body`태그의 2배인 48px가 될 것이다.

## 4. box 모델

* box 모델은 크게 4가지 영역으로 구분된다
  1. Margin Area
  2. Border Area
  3. Padding Area
  4. Content Area

### 4.1 Margin Area

```css
.margin {
  margin-top: 30px;
  margin-bottom: 30px;
  margin-left: 10px;
  margin-right: 10px;
}
```

### 4.2 Border Area

```css
.border {
  border-width: 2px;
  border-style: dotted;
  border-color: red;
  border-top-color: blue;
  border-radius: 10px;
}
```

### 4.3 Padding Area

```css
.padding {
  padding-top: 30px;
  padding-bottom: 30px;
}
```

### 4.4 Content Area

```css
div {
  width: 100px;
  height: 100px;
  background-color: #aaff22;
}
```



## 5. Display

### 5.1 block

* 항상 div, h1~h6, p, ol, ul, li, hr, table, form 등의 태그는 모든 가로칸을 차지한다.
* block 레벨요소 내에 inline레벨 요소를 포함할 수 있다.

### 5.2 inline

* 새로운 라인에서 시작하지 않으며 중간에 들어갈 수 있다.
* content의 너비만큼 가로폭을 차지한다.
* span,a,strong,img,br,input,select,textarea,button

### 5.3  visible => none, hidden

* `none`: 해당 요소를 표시하지 않는다(공간 자체가 사라진다.)
* `hidden` : 해당 요소를 표시하지 않는다(공간은 남아있다.)

**예제를 돌려보는게 이해하기 쉽다**

## 7. Position

### 7.1 static

* 기본 위치(왼쪽 위부터)

### 7.2 absolute

* 부모 혹은 조상요소를 기준으로 위치(가까운 조상 중 static이 아닌 요소)
* 조상 중 static가 아닌 요소가 없다면 가장 상위 static을 기준으로 움직인다.

### 7.3 fixed

* 브라우저 위치에 따라 변경된다.(위치가 고정됨)

**07_position.html**과 **box_style.html** 을 참조하자. 글로는 모른다.

## 8. float

* inline처럼 자리를 차지하는것이 아닌 

이것도 해보고 판단하자. 