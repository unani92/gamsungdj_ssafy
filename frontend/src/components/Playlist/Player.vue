<template>
  <div class="player">
    <span>
      <img class="cover" :src="selectedSong.img" />
    </span>
    <span>
    <span class="songInfo">
      <center>
      <h2>{{ selectedSong.title }}</h2>
      <h4 class="mt-3">{{ selectedSong.artist }}</h4>
      <div class="mt-5">00:00 / 03:12</div>
      <div class="glyph-icon simple-icon-heart pt-5"> 152</div>
      </center>
    </span>
    </span>
  </div>
</template>

<script>
export default {
  props: ['selectedSong'],
}
</script>

<style>
.player {
  height: 360px;
  width: 640px;
  background-color: #1E2125;
  position: absolute;
  -webkit-touch-callout: none;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  -webkit-transform: translate(-50%, -50%);
}

.cover {
  height: 360px;
  width: 360px;
}
.songInfo {
  position:absolute;
  bottom: 25%;
  display: inline-block;
  width: 270px;
}
</style>