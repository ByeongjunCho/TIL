<template>
  <div v-if="video">
    <h3>비디오</h3>
    <iframe :src="videoUrl" width="560" height="315"></iframe>
  </div>
</template>

<script>
export default {
  name: "VideoDetail",
  props: {
      video: {
          type: Object,
          // required: true 초기에 선택이 되어 있지 않으므로 사용할 필요 없음
      }
  },

  computed: {
      videoUrl() {
        return `https://www.youtube.com/embed/${this.video.id.videoId}`
      }
  }
}
</script>

<style>

</style>