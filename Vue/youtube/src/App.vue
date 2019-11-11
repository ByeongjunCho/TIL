<template>
  <div id="app">
    <div class="container">
      
      <search-bar @input-change-event="onInputChange"></search-bar>  <!-- 출력 -->
      <video-detail :video="selectVideo"></video-detail>
      <video-list :videos="videos" @video-select-event="selectedVideo"></video-list>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import SearchBar from './components/SearchBar.vue' // 1-1. vue파일 불러오기
import VideoList from './components/VideoList.vue'
import VideoDetail from './components/VideoDetail.vue'
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
