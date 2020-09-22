<template>
  <div class="player">
    <span>
      <img v-if="selectedSong.img" class="cover" :src="selectedSong.img" />
      <img v-else class="cover" src="https://cdn.manzlab.com/news/photo/201808/1459_2985_4311.jpg">
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
  data() {
    return {
      dummyData: [
        {
            icon: 'iconsminds-male',
            title: 'DEVELOPER',
            price: '$11',
            detail: 'User/Month',
            link: '#',
            features: [
                'Number of end products 1',
                'Free updates',
                'Forum support'
            ]
        },
      ],
    } 
  }
}
</script>
