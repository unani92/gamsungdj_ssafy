<template>
  <div class="player">
    <span>
      <img v-show="selectedSong.img" class="cover" :src="selectedSong.img" @click="goSongDetail"/> 
    </span>
    <span class="songInfo" v-if="selectedSong.title">
      <center>
      <h2 style="cursor:pointer" @click="goSongDetail">{{ selectedSong.title }}</h2>
      <h4 class="mt-3" style="cursor:pointer" @click="goArtistDetail">{{ selectedSong.artist }}</h4>
      <div class="mt-5">-</div>
      <!-- <div class="mt-5">{{ selectedSong.currentTime }} / {{ selectedSong.duration }}</div> -->
      <div class="mt-3">
        <div class="post-icon mr-3 d-inline-block">
          <router-link to="#">
            <i class="simple-icon-heart mr-1"></i>
          </router-link>
          <span>{{ playlist[selectedSong.index].like+playlist[selectedSong.index].user_like.length }} Likes</span>
        </div>
        <div class="post-icon mr-3 d-inline-block">
          <router-link to="#">
            <i class="simple-icon-bubble mr-1"></i>
          </router-link>
          <span>{{ selectedSong.comments.length }} Comments</span>
        </div>
      </div>
      </center>
    </span>
  </div>
</template>

<script>
import { mapState } from "vuex"
export default {
  computed: {
    ...mapState([
      'playlist',
      'selectedSong',
    ]),
    player() {
      return this.$refs.youtube.player
    }
  },
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
  methods: {
    goSongDetail() {
      this.$router.push('/A505/songDetail/'+this.playlist[this.selectedSong.index].id)
      this.$store.state.visiblePlaylist = !this.$store.state.visiblePlaylist
    },
    goArtistDetail() {
      this.$router.push('/A505/artistDetail/'+this.playlist[this.selectedSong.index].artist[0].id)
      this.$store.state.visiblePlaylist = !this.$store.state.visiblePlaylist
    }
  }
}
</script>
