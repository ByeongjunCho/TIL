# Vue.js

## 0. Vue를 위한 확장프로그램 설치

* Chrome webstore - vue dev tool 설치
* 확장 프로그램 설정에서 파일 url 체크
* 검사 도구에서 Vue 선택

## 1. Vue 개요

### 1. Vue 기초

* Vue.js는 M VM V 구조로 이루어졌다.

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>Document</title>
  <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
</head>
<body>
  {{message}}
  <div id="app">
    {{message}} - {{count}}
  </div>

  <script>
    // m(data)) - vm(app) - v(그려지는것)
    const app = new Vue({
      // 조작할 DOM(V), vue object(VM) mount
      // class, id 선택자를 바탕으로 DOM 설정
      el: '#app', // id가 app인 선택자,
      // data: 항상 기본 object
      // app.message, app.count
      // app.$data.message, app.$data.count
      data: {
        message:'안녕!', // String
        count: 0 // Integer, Array, object....
      },
      methods: {
        // arrow function 쓰면 안됨!
        plus: function() {
          this.count++ // app.plus()
        },
        minus: function() {
          this.count-- // app.minus()
        }
      }
    })
  </script>
</body>
</html>
```

```html
  <!-- javascript -->
  <input id="input" type="text"> 
  <p id="input-value"></p>
  
  <script>
    // javascript로 코딩한 경우
    const input = document.querySelector('#input')
    input.addEventListener('keydown', function(event) {
      console.log(event.target.value)
      const p = document.querySelector('#input-value')
      p.innerText = event.target.value
    })
  </script>
    
  <!-- Vue-->
  <div id="app">
    <input type="text" v-model="message"> 
    <p>
      {{ message }}
    </p>
  </div>
  <script>
    // Vue로 코딩한 경우
    const app = new Vue({
      el: '#app',  
      data: {
        message: ''
      }
    })
  </script>
```

### 2. Vue for, if문

```html
  <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
</head>
<body>
  <div id="app">
    {{todos}}
    <!-- 
    디렉티브
    v-for : 반복문
    v-if : 조건문
    같이 작성을 하게 되면, 매 반복에 if를 체크 
    -->
    <hr>
    <img v-bind:src="logo" alt="">  <!-- vue에서 이미지를 불러오기 위한 Vue접근 -->
    
    <li v-for="todo in todos" v-if="!todo.completed" v-on:click="toggleCompleted(todo)">
      {{ todo.content }}
    </li>
    <li v-else v-on:click="toggleCompleted(todo)">[완료!]</li>
  </div>
  <script>
    const app = new Vue({
      el: '#app',
      data: {
        logo: 'https://avatars2.githubusercontent.com/in/5534?s=128&v=4',
        todos: [
          {
            content: '수업 열심히 듣기',
            completed: true
          },
          {
            content: '밥 먹기',
            completed: false
          },
          {
            content: '롤 하기',
            completed: false
          },
        ]
      },
      methods: {
        toggleCompleted: function(todo){
          console.log(todo)
          todo.completed = !todo.completed
        }
      }

    })
  </script>
</body>
</html>
```

### 3. 실습 : 멍멍이 불러오기

```html
<!DOCTYPE html>
<html lang="ko">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>Document</title>
  <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
  <script src="https://unpkg.com/axios/dist/axios.min.js"></script>
</head>

<body>
  <!-- DOM : #app -->
  <div id="app">
    <!-- button : v-on -->
    <!-- img 속성값 바인딩 -->
    <button id="dog-button" v-on:click="getDog()">댕댕이</button>
    <img v-bind:src="imageUrl" alt="댕댕이">
  </div>

  <script>
    const animals = new Vue({
      el: '#app',
      data: {
        imageUrl: ''
      },
      methods: {
        getDog: function () {
          // 요청 보내서 가지고 오면,
          // imageUrl을 변경
          axios.get('https://dog.ceo/api/breeds/image/random')
            .then(response => { 
              console.log(this) // window : function, vue(app) : arrow function
              this.imageUrl=response.data.message
            })
          // axios.get('https://dog.ceo/api/breeds/image/random')
          // .then(function(response) {
          //   console.log(this)
          //   this.imageUrl=response.data.message
          // })
        }
      }
    })
  </script>
</body>

</html>
```

* 여러개의 이미지를 입력하는 경우

```html
<!DOCTYPE html>
<html lang="ko">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>Document</title>
  <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
  <script src="https://unpkg.com/axios/dist/axios.min.js"></script>
</head>

<body>
  <!-- DOM : #app -->
  <div id="app">
    <!-- button : v-on -->
    <!-- img 속성값 바인딩 -->
    <button id="dog-button" v-on:click="getDog()">댕댕이</button>
    <img v-for="image in images" v-bind:src="image" alt="댕댕이">
  </div>

  <script>
    const animals = new Vue({
      el: '#app',
      data: {
        images: []  // 2-1 배열로 변경
      },
      methods: {
        getDog: function () {
          // 요청 보내서 가지고 오면,
          // imageUrl을 변경
          axios.get('https://dog.ceo/api/breeds/image/random')
            .then(response => { 
              console.log(this) // window : function, vue(app) : arrow function
              this.images.push(response.data.message) // 2-2 배열에 값 넣기로 변경
            })
          // axios.get('https://dog.ceo/api/breeds/image/random')
          // .then(function(response) {
          //   console.log(this)
          //   this.imageUrl=response.data.message
          // })
        }
      }
    })
  </script>
</body>

</html>
```



