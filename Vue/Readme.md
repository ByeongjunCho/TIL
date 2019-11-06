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

* 같은 라인에서는 for문이 if 문보다 우선순위가 높음

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
  <title>Document</title>
</head>
<body>
  <div id="app">
    <p>{{message}}</p>
    <!-- 반복문 돌려서 이름 출력 -->
    <!-- 같은 라인에서는 for문이 if 문보다 우선순위가 높다. -->
    <li v-for="member in members" v-if="member.gender === 'M'">
      {{member.name}} ?
    </li>
    <li v-else>{{member.name}}</li>
    <!-- v-model 
      data 내에 초기화가 반드시 필요!
    -->
    <input type="text" v-model="userText">
    <p>사용자가 입력 중 .. {{userText}}</p>
    <!-- 속성값 : v-bind -->
    <img v-bind:src="url" alt="" width="300" height="300">
    <img :src="url" alt="" width="300" height="300">
    <!-- 이벤트 -->
    <button v-on:click="countUp">+++++</button>
    <p>{{ counter }}</p>
    <button @click="countDown">------</button>
  </div>
  <script>
    const app = new Vue({
      el: '#app',
      data: { // app.$data
        url: 'https://image.chosun.com/sitedata/image/201705/08/2017050801699_0.jpg',
        message: 'Hello',  // app.message
        members: [
          {name: '김', gender: 'M'},
          {name: '박', gender: 'F'},
          {name: '석', gender: 'M'}
        ],
        userText: '',
        counter: 0
      },
      methods: {
        countUp: function() {
          this.counter++
          console.log(this.counter)
        },
        countDown: function(){
          this.counter--
          console.log(this.counter)
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

## 2. Vue 심화

### 1. 예제

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
  <title>Document</title>
</head>
<body>
  <div id="app">
    <p>{{message}}</p>
    <!-- 반복문 돌려서 이름 출력 -->
    <!-- 같은 라인에서는 for문이 if 문보다 우선순위가 높다. -->
    <!-- *반복문 시행시 항강 key를 유니크하게 설정하자 -->

    <li v-for="member in members" v-if="member.gender === 'M'" :key="member.id">
      {{member.name}} ?
    </li>
    <li v-else>{{member.name}}</li>
    <!-- v-model 
      data 내에 초기화가 반드시 필요!
    -->
    <input type="text" v-model="userText">
    <p>사용자가 입력 중 .. {{userText}}</p>
    <!-- 속성값 : v-bind -->
    <img v-bind:src="url" alt="" width="300" height="300">
    <img :src="url" alt="" width="300" height="300">
    <!-- 이벤트 -->
    <button v-on:click="countUp">+++++</button>
    <p>{{ counter }}</p>
    <button @click="countDown">------</button>
    <!-- computed vs methods -->
    <h2>methods : {{dateMethods()}}</h2>  <!-- 함수를 실행, 모든 data 변경시마다 계속 호출 -->
    <h2>computed : {{dateComputed}}</h2>  <!-- 함수의 실행 결과를 계산된(computed) 변수의 값으로 저장 -->
    <!-- v-text -->
    <h3 v-text="message"></h3>
    <h3>{{message}}</h3>
    <!-- html -->
    {{myTag}}
    <span v-html="myTag"></span>
    <!-- v-show -->
    <p v-show="false">이것은 보임?</p> <!-- 랜더링은 하는데, css로 보이지 않게함.(개발자도구 확인) -->
    <p v-if="false">호우 호우호우</p> <!--랜더링 자체를 하지 않음-->
  </div>
  <script>
    const app = new Vue({
      el: '#app',
      data: { // app.$data
        url: 'https://image.chosun.com/sitedata/image/201705/08/2017050801699_0.jpg',
        message: 'Hello',  // app.message
        myTag: '<h2>신기하당</h2>',
        members: [
          {id: 1, name: '김', gender: 'M'},
          {id: 2, name: '박', gender: 'F'},
          {id: 3, name: '석', gender: 'M'}
        ],
        userText: '',
        counter: 0
      },
      methods: {
        countUp: function() {
          this.counter++
          console.log(this.counter)
        },
        countDown: function(){
          this.counter--
          console.log(this.counter)
        },
        dateMethods() {
          return new Date()
        }
      },
      computed: {
        dateComputed() {
          return new Date()
        }
      },
      mounted: function(){
        console.log('처음 실행시 함수를 설정합니다!')
      },
      watch: {
        message: {
          handler: function() {
            console.log('메시지 값이 변경되면 함수를 실행합니다')
          },
          // deep: true // nested object(중첩된 오브젝트의 변경사항 추적)
        }
      }
    })
  </script>
</body>
</html>
```

### 2. v-model

```html
<!-- v-model 
      data 내에 초기화가 반드시 필요!
    -->
    <input type="text" v-model="userText">

<script>
    ....
    const app = new Vue({
        data: {
            userText: ''
        }
    })
</script>
```

### 3. v-bind

* 속성값을 직접 입력할 수는 없고 `v-bind`를 사용해야 한다.
* v-bind:속성 혹은 :속성    으로 약어 사용이 가능하다.

```html
<!-- 속성값 : v-bind -->
    <img v-bind:src="url" alt="" width="300" height="300">
    <img :src="url" alt="" width="300" height="300">
<script>
    ....
    const app = new Vue({
        data: {
            url: '......'
        }
    })
</script>
```

### 4. 이벤트

```html
<!-- 이벤트 -->
    <button v-on:click="countUp">+++++</button>
    <p>{{ counter }}</p>
    <button @click="countDown">------</button>

    const app = new Vue({
        data: {
            url: '......'
        },
		methods: {
			countUp: function(){....}
		}
    })
```

### 5. compute vs methods

```html
<!-- computed vs methods -->
    <h2>methods : {{dateMethods()}}</h2>  <!-- 함수를 실행, 모든 data 변경시마다 계속 호출 -->
    <h2>computed : {{dateComputed}}</h2>  <!-- 함수의 실행 결과를 계산된(computed) 변수의 값으로 저장 -->

    const app = new Vue({
        data: {
            url: '......'
        },
		methods: {
			countUp: function(){....}
		}
		computed: {
        dateComputed() {
          return new Date()
        }
      },
    })
```

## 3. 폼 입력 바인딩

### 1. v-model

* 입력되는 데이터는 Vue data에 저장하는 습관이 좋다.

```html
<input v-model.trim="message" type="text">
<input v-model.number="number" type="number">
```

* v-model.trim : 앞뒤로 공백 제거
* v-model.number : integer로 형변환하여 저장한다(default는 문자)

```html
<select v-model="select" name="" id="">
      <option value="꼬부기">꼬부기</option>
      <option value="이상해씨">이상해씨</option>
      <option value="파이리">파이리</option>
</select>
```

* 오브젝트 내의 값도 변경이 가능하다.

```html
<select v-model="jiwoo.pokemon" name="" id="">
      <option value="꼬부기">꼬부기</option>
      <option value="이상해씨">이상해씨</option>
      <option value="파이리">파이리</option>
</select>

data: {
        jiwoo: {
          pokemon: ''
        },
```

* select에도 v-model을 활용할 수 있다.

```html
<input v-model="checked" type="checkbox" name="" id="">
```

* input radio에도 사용이 가능하다.

```html
<input v-model="type" value="물" type="radio" name="" id="water">
<label for="water">물</label>
<input v-model="type" value="불" type="radio" name="" id="fire">
<label for="water">불</label>
<input v-model="type" value="풀" type="radio" name="" id="green">
<label for="water">풀</label>
```

### 2. 컴포넌트

* 반복되는 내용을 편리하게 사용 가능

```html
<div id="app">
    <h1>오늘의 할일</h1>
    <todo-list category="취업준비"></todo-list>
    <todo-list category="싸피"></todo-list>
    <todo-list category="개인"></todo-list>
  

  <script>
    // 컴포넌트 선언부  
    Vue.component('todo-list', {
      template: `<div class="todo-list">
        <h2>{{category}}</h2>
        <input v-model="newTodo" type="text">
        <button v-on:click="addTodo">할일 추가</button>
        {{todos}}
        <!-- 할일 목록 나열 -->
        <li v-for="todo in todos" :key="todo.id">{{todo.content}} <button v-on:click="removeTodo(todo.id)">일 삭제</button>
        </li>
      </div>`,
      props: {
        category: {
          type: String,
          required: true
        }
      },// 하위컴퍼넌트로 데이터 전송
      data: function () {
        return {
          todos: [],
          newTodo: ''
        }
      },
      methods: {
        addTodo() {
          this.todos.push({
            id: Date.now(),
            content: this.newTodo
          })
          this.newTodo = ''
        },
        removeTodo(id) {
          this.todos = this.todos.filter(todo => {
            return !(todo.id === id)
          })
        },
      },

    })
  </script>
  </div>
  <script>
    // 루트 오브젝트
    const app = new Vue({
      el: '#app',
    })
  </script>
```

* 모든 컴포넌트 인스턴스는 격리되어 있어서 하위 컴포넌트가 상위 컴포넌트를 직접 참조할 수 없다.
* 그래서 props 옵션을 이용해 하위 컴포넌트로 데이터를 전달해야 한다.

## 4. javascript 모듈화

* javascript는 모듈 개념이 없다. 그래서 모듈화를 위해 wbepack 모듈 번들러를 사용해서 모듈환경을 구성한다.
* node.js 의 페키지 관리자는 npm이다.

### 1. vue 파일

```bash
$ npm init
```

* 비어있는 `package.json`생성

```bash
$ npm install vue
$ npm install webpack webpack-cli -D
```

* webpack은 개발환경에서 모듈 번들러로 활용하기 위한 것이므로 `-D`옵션을 해 `package.json`에서 `devDependices`에 추가

* 다음 명령어를 실행하면 관리하는 패키지를 `package.json`파일에 작성한다.

```bash
$ npm install vue-loader vue-template-compiler -D
```

* vue-loader: vue 파일을 불러오는 역할
* vue-template-compiler: 해석하는 역할

```bash
$ npm install vue-style-loader css-loader -D
```

* vue-style-loader : vue의 style
* css-loader: webpack css 불러오는 로더

```bash
$ npm install -g @vue/cli
$ vue create {프로젝트이름}
```

