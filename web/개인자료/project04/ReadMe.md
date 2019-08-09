# Project04

## 01_layout

### nav

```html
<nav class="navbar navbar-expand-lg navbar-light bg-light sticky-top">
    <a class="navbar-brand" href="#">영화 추천 시스템</a>
    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav"
      aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse justify-content-end" id="navbarNav">
      <ul class="navbar-nav">
        <li class="nav-item active">
          <a class="nav-link" href="#">Home <span class="sr-only">(current)</span></a>
        </li>
        <li class="nav-item">
          <a class="nav-link disabled font2" href="#">친구평점보러가기</a>
        </li>
        <li class="nav-item">
          <a class="nav-link disabled" href="#">Login</a>
        </li>
      </ul>
    </div>
  </nav>
```

* `bootstrap`의 `nav` 를 수정하여 사용
* 가장 최상단인 `nav` 태그에 `sticky-top`를 적용하여 최상단에 고정
* `item`영역에 `justify-content-end`클래스를 적용하여 오른쪽으로 고정

### header/footer

```html
  <header class="d-flex justify-content-center align-items-center">
    <h2 class="font1">당신에게 어울리는 영화를 추천해드립니다.</h2>
  </header>
  <footer class="fixed-bottom px-5 d-flex justify-content-between bg-light align-items-center">
    <div class="d-flex font2">조병준</div>
    <a href="#">처음으로</a>
  </footer>
```

```css
body {
  height: 10000px;
}

header {
  height: 350px;
  width: 100%;
  background-image: url("images/how.jpg");
}

footer {
  height: 50px;
}

.font1 {
  font-family: 'Nanum Brush Script', cursive;
}

.font2 {
  font-family: 'Single Day', cursive;
}
```

* header에 배경화면을 지정하고 글자를 중앙으로 이동
* `footer` 를 바닥으로 고정시키기 위해 `fixed-bottom`클래스를 적용하고 의 내용을 왼쪽 및 오른쪽으로 이동시키기 위해  `justify-content-center` 사용
* footer 오른쪽에 상단으로 가는 하이퍼링크 버튼 생성
* 

## 02_movie

```html
<div class="container d-flex justify-content-center">
    <div class="row">
      <div class="col-12 col-sm-6 col-md-4 col-lg-3">
        <div class="card my-3">
          <img src="images/174903.jpg" class="card-img-top" alt="엑시트" data-target="#EXIT" data-toggle="modal">
          <div class="card-body">
            <h4 class="card-title">엑시트</h4>

            <div class="degreebox bg-primary text-light">9.07</div>
            <hr>
            <p class="card-text my-0">코미디 <div class=my-0>2019-07-31</div>
            </p>
            <a href="https://movie.naver.com/movie/bi/mi/basic.nhn?code=174903" target="_blank"
              class="btn btn-info">영화정보 보러가기</a>
          </div>
        </div>
      </div>
    .......
```

```css
.subtitle {
  text-align: center;
}

h3 > hr {
  width: 70px;
  text-align: center;
  background: red;
}

.degreebox {
  width: 40px;
  height: 30px;
  border-radius: 10%;
  text-align: center;
  line-height: 30px;
}
```

* `bootstrap Card` 컴퍼넌트 사용
* `col-12 col-sm-6 col-md-4 col-lg-3` 를 적용하여 화면 크기에 대응
* bootstrap `btn` 클래스로 영화정보 링크버튼 설정

### detail_view

```html
<!-- Modal -->
  <!-- 엑시트 -->
  <div class="modal fade" id="EXIT" role="dialog">
    <div class="modal-dialog modal-lg">
      <!-- Modal content-->
      <div class="modal-content">
        <div class="modal-header justify-content-between">
          <h4 class="modal-title">엑시트/EXIT</h4>
          <button type="button" class="close" data-dismiss="modal">X</button>
          
        </div>
        <div class="modal-body justify-content-center">
          <img src="images/nabduk.jpg"  width="100%" height="auto"  alt="납득이">
          <p>12세이상관람가</p>
          <p>누적관객수 : 2962455</p>
          <hr>
          <p>대학교 산악 동아리 에이스 출신이......</p>
        </div>
        <div class="modal-footer">
          <button type="button" class="btn btn-default" data-dismiss="modal">Close</button>
        </div>
      </div>
    </div>
  </div>
....
<div class="container d-flex justify-content-center">
    <div class="row">
      <div class="col-12 col-sm-6 col-md-4 col-lg-3">
        <div class="card my-3">
            <!-- 추가된 부분 -->
          <img src="images/174903.jpg" class="card-img-top" alt="엑시트" data-target="#EXIT" data-toggle="modal">
            <!-- -->
          <div class="card-body">
            <h4 class="card-title">엑시트</h4>

            <div class="degreebox bg-primary text-light">9.07</div>
            <hr>
            <p class="card-text my-0">코미디 <div class=my-0>2019-07-31</div>
            </p>
            <a href="https://movie.naver.com/movie/bi/mi/basic.nhn?code=174903" target="_blank"
              class="btn btn-info">영화정보 보러가기</a>
          </div>
        </div>
      </div>
```

* `bootstrap`에서 제공하는 `modal` 컴퍼넌트를 사용
* `modal`을 작성하고 `image`태그에 `data-target` 과 `data-toggle` 속성을 추가하여 `modal` 적용

# 결과



![완성 이미지](C:\Users\student\Desktop\프로젝트 및 과제 정리\project04\images\완성 이미지.png)