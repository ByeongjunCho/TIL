<template>
  <div>
    <h2>영상 목록</h2>
    <ul class="list-group">
    <video-list-item v-for="video in videos" :video="video" :key="video.id.videoId" @video-select-event="selectedVideo">
    </video-list-item>
    <!-- 부모 컴포넌트에서는 이벤트 listen(v-on)
      -> 원하는 메소드 실행
     -->
    </ul>
  </div>
</template>

<script>
import VideoListItem from './VideoListItem.vue'
export default {
  name: 'VideoList',
  components: {
      VideoListItem
  },
  data() {
      return {
          video: []
      }
  },
  props: {
      videos: {
          type: Array,
          required: true
      }
  },
  methods: {
    selectedVideo(video){
        console.log(video)
      this.$emit('video-select-event', video)
    }
  }
}
</script>

<style>

</style>