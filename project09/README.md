# movie

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

# Project 09

## 1. App.vue

### 1. movie.json 과 genre.json 불러오기

```javascript
export default {
  name: 'app',
  // 1-2. 아래에 등록 후
  components: {
    MovieList,
  },
  data() {
    return {
      // 활용할 데이터를 정의하시오.
      movies: [],
      genres: []
    }
  },
  mounted() {
    // 0. mounted 되었을 때, 
    // 1) 제시된 URL로 요청을 통해 data의 movies 배열에 해당 하는 데이터를 넣으시오. 
    axios.get('https://gist.githubusercontent.com/ByeongjunCho/f2d5cdf167351677499ed0b38fb7fd83/raw/613f666c48791c3d13c90c6e769b3c89fa877ded/movie.json')
    .then(response => {
      console.log(response)
      this.movies = response.data
    })
    // 2) 제시된 URL로 요청을 통해 data의 genres 배열에 해당 하는 데이터를 넣으시오.
    // axios는 위에 호출되어 있으며, node 설치도 완료되어 있습니다.
    axios.get('https://gist.githubusercontent.com/ByeongjunCho/04b2ebc5930728380089ac10318d1a6e/raw/ca600ea207d4951de8ecc3961087f7aacdeba607/genre.json')
    .then(response => {
      console.log(response)
      this.genres = response.data
    })
  },
}
```

* axios를 활용하여 데이터를 받고 movies와 genres에 입력한다.

### 2. 데이터 넘기기

```html
<template>
  <div id="app">
    <div class="container">
      <!-- 1-3. 호출하시오. 
        필요한 경우 props를 데이터를 보내줍니다.
      -->
      <MovieList :movies="movies" :genres="genres" ></MovieList>
    </div>
  </div>
</template>
```

* MovieList.vue 에 props를 설정하고 데이터를 보내준다.

## 2. MovieList.vue

### 1. 영화목록 출력 및 세부영화 정보 보내기

```html
<template>
  <div>
    <h1>영화 목록</h1>
    <h2>장르 선택</h2>
    <!-- 2. 장르 선택(제일 마지막에 구현하시오.)
    2-1. App 컴포넌트로 부터 받은 genres를 반복하여 드롭다운을 완성 해주세요.
    2-2. 드롭다운은 selectedGenreId data와 양방향바인딩(v-model)이 됩니다.
    2-3. 값 변경이 되면, 특정한 함수를 실행 해야합니다.
     -->
    <select class="form-control" v-model="genre" >
      <option value="">전체보기</option>
      <option v-for="g in genres" :value="g" :key="g.id">{{g.name}}</option>
    </select>
      <!-- 1-3. 반복을 통해 호출하시오. 
        필요한 경우 props를 데이터를 보내줍니다.
      -->
      
      <div class="row">
        <MovieListItem v-for="movie in movieFilter" :key="movie.id" :movie="movie"></MovieListItem>
      </div>
      
      
      <!-- (나중에 마지막으로) selectedGenreId 값에 따른 분기를 해야 합니다.

       -->
  </div>
</template>
```

* `v-for`, `v-model`을 이용해 선택한 장르를 genre 에 입력한다.
* 장르별 영화를 출력하기 위해 `movieFilter`를 설정하고 각각의 movie object를 `MovieListItem`에 보내준다.

### 2. 영화 분류를 위한 함수 설정

```javascript
<script>
// 1-1. 저장되어 있는 MovieListItem 컴포넌트를 불러오고,
import MovieListItem from './MovieListItem.vue'

export default {
  name: 'MovieList',
  // 1-2. 아래에 등록 후
  components: {
    MovieListItem,
  },
    // 0. props 데이터를 받이 위하여 설정하시오.
    // genres와 movies 모두 타입은 Array이며, 필수입니다.
  
  props: {
    movies: {
      type: Array,
      required: true
    },
    genres: {
      type: Array,
      required: true
    }
  },
  data () {
    return {
      genre: '',
      // 활용할 데이터를 정의하시오.
    }
  },
  computed: {
    movieFilter() {
      console.log(this.genre)
      if (this.genre !== ''){
        return this.movies.filter(movie=> this.genre.id===movie.genre_id)
      }
      else {
        return this.movies
      }
    }
  }
  // 설정이 완료 되었다면, 상위 컴포넌트에서 값을 넘겨 주세요.
  // 그리고 적절한 곳에 사용하세요.

  // 2-3.에서 이야기하는 특정한 함수는 selectedGenreId의 값이 변경될 때마다 호출 됩니다.
  // 드랍다운에서 장르를 선택하면, 해당 영화들만 보여주도록 구현 예정입니다.
  // 주의할 것은 직접 부모 컴포넌트의 데이터를 변경할 수 없다는 점입니다.
  // 완료 후 
}
</script>
```

* computed에 분류별 영화 출력을 위한 함수 구현
* genre에 장르가 있는 경우 filter method를 사용하여 해당 장르의 영화목록만 출력

## 3. MovieListItem.vue

### 1.  영화 리스트와 상세정보 보기를 위한 설정

```html
<template>
  <div class="col-3 my-3">
    <!-- img 태그에 src와 alt값(영화제목)을 설정하시오 -->
    <img :src="movie.poster_url" class="movie--poster my-3">
    <!-- 영화 제목을 출력하시오. -->
    <h3>{{movie.name}}</h3>
    <!-- 모달을 활용하기 위해서는 data-taget에 모달에서 정의된 id값을 넣어야 합니다. -->
    <button class="btn btn-primary" data-toggle="modal" :data-target="'#movie-' + movie.id">영화 정보 상세보기
    </button>
    
    <!-- 1-3. 호출하시오.
    
      필요한 경우 props를 데이터를 보내줍니다.
      -->
    <MovieListItemModal :movie="movie"></MovieListItemModal>
    
  </div>
</template>
```

* `button`태그에 data-target 속성을 이용하여 해당 id를 설정한다.

### 2. 영화 정보를 받기 위한 export default 설정

```javascript
<script>
export default {
  name: 'MovieListItemModal',
  // 0. props 데이터를 받이 위하여 설정하시오.
  props: {
    movie: {
      type: Object,
      required: true
    },
  },
  // mounted() {
  //   console.log(this.detail)
  // }
  
  // movie 타입은 Object이며, 필수입니다.
  // 설정이 완료 되었다면, 상위 컴포넌트에서 값을 넘겨 주세요.
  // 그리고 적절한 곳에 사용하세요.
}
</script>
```

## 4. MovieListItemModal.vue

### 1. 영화 세부정보 출력

```html
<template>
<!-- vue 콘솔에서 확인하여, 추가 정보들도 출력하세요. -->
<!-- 고유한 모달을 위해 id 속성을 정의하시오. 예) movie-1, movie-2, ... -->
<div class="modal fade" :id="'movie-' + movie.id" tabindex="-1" role="dialog">
  <div class="modal-dialog" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <!-- 영화 제목을 출력하세요. -->
        <h5 class="modal-title">{{movie.name}}</h5>
        <button type="button" class="close" data-dismiss="modal" aria-label="Close">
          <span aria-hidden="true">&times;</span>
        </button>
      </div>
      <div class="modal-body">
        <!-- 영화 설명을 출력하세요. -->
        <img :src="movie.poster_url" alt="" width="300" height="300">
        <p>{{movie.rating}}</p>
        <p>{{movie.description}}</p>
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
      </div>
    </div>
  </div>
</div>
</template>
```

* 영화의 세부정보 object를 넘겨받고 객체를 이용해 영화 세부정보를 출력