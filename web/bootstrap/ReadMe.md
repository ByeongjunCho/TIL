# Bootstrap

## 1. intro

### 1.1 bootstrap 기초

```html

  <!-- css는 head에 -->
  <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">

</head>
<body>
    .....
    
  <!-- javascript는 body 닫는 테그 바로 위에 -->
  <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
  <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
</body>
</html>
```

* bootstrap 홈페이지에서 링크롤 `html`파일에 입력하면 bootstrap를 사용할 수 있다.

### 1.2 CDN

 ## 2. spacing

> xy-nz

* x: 원하는 요소 ex) m: margin, p: padding
* y: 위치 ex) x: x축, y: y축, t: top, .....
* n: (-)요소
* z: 1~5숫자 ex) 3: 1rem

## 3. color

다양한 요소에 색을 추가할 수 있다. 

```html
<!-- background-color: 특정색 -->
  <div class="bg-primary text-center text-white">.bg-primary</div>
  <div class="bg-warning text-center text-white">.bg-warning</div>
  <div class="bg-danger text-center text-white">.bg-danger</div>
  <div class="bg-dark text-center text-white">.bg-dark</div>
  
  <span class="text-primary">Primary</span>
  <span class="text-white">Primary</span>
  <span class="text-success">Primary</span>
  <span class="text-info">info</span>

  <div class="alert alert-light">alert! alert-light</div>
  <div class="alert alert-primary">alert! alert-primary</div>

  <button class="btn btn-success">bun-succenss</button>
  <button class="btn btn-transpart">btn-transparent</button>
```

다양한 색은 [bootstrap Colors](https://getbootstrap.com/docs/4.3/utilities/colors/) 참조

## 4. Border

```html
<!-- 색상 지정 가능 -->
  <div class="border border-primary bg-light">파란선</div>
  <div class="border border-danger">빨간선</div>
  <!-- top, right, bottom, left 각각 지정 가능 -->
  <div class="border-right">오른쪽 경계선</div>
  <div class="border-left border-warning">왼쪽 노란 경계선</div>
```

[bootstrap border](https://getbootstrap.com/docs/4.3/utilities/borders/) 참조

## 5. display

```html
<img src="bonobono.jpg" alt="보노보노" class="d-block">
  <img src="bonobono.jpg" alt="보노보노">
  <div class="d-inline bg-primary">인라인인라인</div>
  <div class="d-block bg-primary">블럭블럭블럭</div>
  <img src="bonobono.jpg" alt="보노보노" class="d-sm-none">
  <img src="bonobono.jpg" alt="보노보노" class="d-md-none">
  <img src="bonobono.jpg" alt="보노보노" class="d-lg-none">
```

## 6. position

```html
<div class="fixed-top bg-primary text-white">안녕하세요 맨 위 고정(fixed)</div>
  <div class="fixed-bottom bg-primary text-white">안녕하세요 맨 아래 고정(fixed)</div>
  <div class="position-relative mt-5">
    position relative
    <div class="position-absolute">
      position absolute
    </div>

  </div>
```

## 7. components

* bootstrap에는 다양한 form예제를 지원한다.

## 8. gird

### 8.1 container

```html
<h2>컨테이너 밖</h2>
  <!-- container: 마진+패딩 -->
  <div class="container">
    <h2>컨테이너 안</h2>
  </div>
  <!-- container-fluid: 패딩 -->
  <div class="container-fluid">
    <h2>
      fluid 컨테이너
    </h2>
  </div>
  <hr>
```

* container : 마진+패딩을 가지고 있음
* container-fluid : 패딩만 존재

### 8.2 grid 기본

```html
  <div class="container">
    <div class="row">
      <!-- 총 12칸을 3등분, 4칸씩 사용 -->
      <div class="col-4">
        <div class="bg-primary text-center text-white">1/3</div>
      </div>
      <div class="col-4">
        <div class="bg-primary text-info text-center">1/3</div>
      </div>
      <div class="col-4">
        <div class="bg-primary">1/3</div>
      </div>
    </div>
```

* `row`: 내부의 영역을 12칸으로 나누어줌
* `col-x`: x만큼의 구역을 나눠 사용

### 8.3 균등하지 않은 배치

```html
<div class="container">
    <div class="row">
      <div class="col-3 div bg-success text-center text-white">1</div>
      <div class="col-6 div bg-success text-center text-white">2</div>
      <div class="col-5 div bg-success text-center text-white">overflow</div>
    </div>
  </div>
```

* col 클래스에 원하는 영역 크기를 입력하여 공간 차지
* row영역 내부 12칸을 넘어가는 영역을 가지면 다음줄로 이동한다.

```html
<!-- 3. offset -->
  <div class="container">
    <div class="row">
      <div class="col-6 offset-6">
        <div class="bg-primary">오른쪽?</div>
      </div>
    </div>
```

* offset클래스는 col클래스와 함께 사용되면 먼저 적용되어





## 참고

Fontawesome

animate.css