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

<script>
const axios = require('axios');
// 1-1. 저장되어 있는 MovieList 컴포넌트를 불러오고,
import MovieList from './components/movies/MovieList.vue'


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
