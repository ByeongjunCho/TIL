<template>
  <li @click="selectedVideo" class="list-group-item">
    <img :src="video.snippet.thumbnails.high.url" :alt="video.snippet.title">
    <h3>{{video.snippet.title}}</h3>
    <p>{{ video.snippet.description }}</p>
  </li>
  
</template>

<script>

export default {
    name: 'VideoListItem',
    props: {
        video: {
            type: Object,
            required: true
        }
    },
    methods: {
        selectedVideo() {
            // video-select-event
            // 자식컴포넌트에서는 이벤트 발생(값 부모로 전달)
            // console.log(this.video)
            this.$emit('video-select-event', this.video)
        }
    }
}
</script>

<style scoped>
/* scoped : 해당 컴포넌트에서만 사용되는 style */
img {
  width: 360px;
}
li {
    cursor: pointer;
}
li:hover {
    background-color: darkgray;
}
</style>