<template>
  <div class="player">
    <span>
      <img v-if="selectedSong.img" class="cover" :src="selectedSong.img" /> 
    </span>
    <span>
    <span class="songInfo">
      <center>
      <h2>{{ selectedSong.title }}</h2>
      <h4 class="mt-3">{{ selectedSong.artist }}</h4>
      <div class="mt-5">{{ selectedSong.currentTime }} / {{ selectedSong.duration }}</div>
      <div class="mt-3">
        <div class="post-icon mr-3 d-inline-block">
          <router-link to="#">
            <i class="simple-icon-heart mr-1"></i>
          </router-link>
          <span>{{ selectedSong.like }} Likes</span>
        </div>
        <div class="post-icon mr-3 d-inline-block">
          <router-link to="#">
            <i class="simple-icon-bubble mr-1"></i>
          </router-link>
          <span>{{ selectedSong.comments}} Comments</span>
        </div>
      </div>
      </center>
    </span>
    </span>
  </div>
</template>

<script>
export default {
  props: ['selectedSong'],
  // computed: {
  //   currentTime: function() {
  //     var min = parseInt(this.selectedSong.currentTime/60)
  //     var sec = parseInt(this.selectedSong.currentTime%60)
  //     return min+':'+sec
  //   },
  //   duration: function() {
  //     var min = parseInt(this.selectedSong.duration/60)
  //     var sec = parseInt(this.selectedSong.duration%60)
  //     return min+':'+sec
  //   }
  // }
}
</script>
