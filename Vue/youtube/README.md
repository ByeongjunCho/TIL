# youtube

## Project setup
```
npm install
```

### Compiles and hot-reloads for development
```
npm run serve
```

### Compiles and minifies for production
```
npm run build
```

### Lints and fixes files
```
npm run lint
```

### Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).



## 구조

```
App
   |---SearchBar
   |
   |---
```

## SearchBar

### 1. 검색어 입력

```html
<!-- App.vue -->
<template>
  <div>
    <h1>유튜브 검색기</h1>
    <input @input="onInput" type="text">
  </div>
</template>

<script>
export default {
    name: 'SearchBar',
    methods: {
        onInput(event) {
            console.log('==SearchBar==')
            console.log(event.target.value)
            // $emit(이벤트이름, 값)
            // 이벤트이름의 이벤트를 발생 시킴(트리거)
            this.$emit('input-change-event', event.target.value)
        }
    }
}
</script>

<style>

</style>
```

* 자식 컴퍼넌트에서 부모로 데이터를 넘겨주기 위해 `.$emit`메서드를 사용한다.
* 이름을 등록하고 부모 컴퍼넌트에서 값을 받아 처리가 가능하다.

```html
<!-- App.vue -->
<template>
  <div id="app">
    
    <search-bar @input-change-event="onInputChange"></search-bar>  <!-- 출력 -->
  </div>
</template>

<script>
import SearchBar from './components/SearchBar.vue' // 1-1. vue파일 불러오기

export default {
  name: 'app',
  components: {
    SearchBar // component 등록
  },
  methods: {
    onInputChange(value) {
      console.log('==App==')
      console.log(value)
    }
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>

```

* Input 태그에 등록된 이벤트 (@input)
* trigger : input 값이 변경되면,
* 인자로 `event`
* `onInput`method 실행

---

* search-bar 컴포넌트에 등록된 이벤트(@input-change-event)
* trigger : `$emit`메서드 실행되면(자식컴포넌트)
* 인자로 `event.target.value`
* `onInputChange`method 실행

### 2. youtube api

* axios를 설치하고 import

```bash
$ npm install axios
```

```javascript
import axiosn from 'axios'
```

* API_KEY와 요청을 보낼 주소를 이용하여 데이터를 요청하고 data에 저장

```html
<!-- App.vue -->
<template>
  <div>
    <h1>유튜브 검색기</h1>
    <input @change="onInput" type="text">
  </div>
</template>

<script>
export default {
    name: 'SearchBar',
    methods: {
        onInput(event) {
            console.log('==SearchBar==')
            console.log(event.target.value)
            // $emit(이벤트이름, 값)
            // 이벤트이름의 이벤트를 발생 시킴(트리거)
            this.$emit('input-change-event', event.target.value) // $emit를 사용해서 데이터를 부모 컴포넌트로 전달한다.
        }
    }
}
</script>

<style>

</style>
```

* 자식 컴포넌트에서 보낸 데이터를 받는 태그를 설정하고 method를 추가한다.

```html
<!-- App.vue -->
<template>
  <div id="app">
    <div class="container">
      
      <search-bar @input-change-event="onInputChange"></search-bar>  <!-- 출력 -->
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import SearchBar from './components/SearchBar.vue' // 1-1. vue파일 불러오기
const API_KEY = process.env.VUE_LOCAL_API_KEY
export default {
  name: 'app',
  components: {
    SearchBar, // component 등록
    VideoList,
    VideoDetail
  },
  data() {
    return {
      videos: [],
      selectVideo: null
    } // SFC에서는 반드시 data는 함수로 작성하고, 오브젝트를 리턴하도록 작성
  },

  methods: {
    onInputChange(value) {
      console.log('==App==')
      console.log(value)
      axios.get('https://www.googleapis.com/youtube/v3/search', {
        params: {
          key: API_KEY,
          part: 'snippet',
          type: 'video',
          q: value
          }
      }).then(response => {
        console.log(response)
        // data의 videos에 저장
        this.videos = response.data.items
      })
      .catch(error => {
        console.log(error)
      })
        
    },
    selectedVideo(video){
      console.log('왔냐')
      this.selectVideo = video
      console.log(this.selectVideo)
    }
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>

```

