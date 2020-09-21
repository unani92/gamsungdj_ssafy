<template>
  <div>
    <b-row>
      <b-colxx xxs="12">
        <div class="separator mb-5"></div>
      </b-colxx>
    </b-row>
    <b-row>
      <b-colxx xxs="12">
        <b-colxx xxs="12" class="mb-4 pl-3 pr-3" style="display: inline-flex;">
                <div xxs="4" class="card mb-4"  style="width:30%; margin-right:3%">
                  <img class="card-img-top" :src="song.img" style="border-top-left-radius:initial; border-top-right-radius:initial"/>
                </div>
                <div xxs="8" style="width:70%;">
                  <h1 class="mb-0 truncate text-xlarge" style="margin-top:3%">{{song.name}}</h1><br>
                  <h1 class="mb-0 truncate text-large"><router-link :to="'/app/piaf/artistDetail/'+song.artistId" class="text-primary">{{song.artist}}</router-link></h1><br>
                  <h3 class="mb-0 truncate">앨범: <router-link :to="'/app/piaf/albumDetail/'+song.albumId" class="text-primary">{{song.album}}</router-link></h3><br>
                  <h3 class="mb-0 truncate">장르: {{song.genre}}</h3><br>
                  <h3 class="mb-0 truncate">감정: 슬픔</h3>
                </div>
        </b-colxx>
      </b-colxx>
    </b-row>
    <b-row>
      <b-colxx xxs="12">
        <div class="separator mb-5"></div>
      </b-colxx>
    </b-row>
    <b-row>
      <b-colxx xxs="12">
        <h2>가사></h2>
        <b-colxx xxs="12" class="mb-4 pl-3 pr-3">
          <h4 v-for="(lyric, index) in song.lyrics" v-bind:key="index">{{lyric}}</h4>
        </b-colxx>
      </b-colxx>
      <b-colxx xxs="12">

      </b-colxx>
    </b-row>
  </div>
</template>
<script>

export default {
  components: {
  },

  data () {
    return {
      songID: 0,

      song: { id: 1, name: '선물', artist: '멜로망스', artistId:1, genre: '발라드', album:"moonlight", albumId:1, img: 'https://cdnimg.melon.co.kr/cm/album/images/100/78/176/10078176_500.jpg?fc3fe8c6bd74c16bce7ffd971a930ffa/melon/resize/282/quality/80/optimize',
      lyrics:["빛이 들어오면 자연스레 뜨던 눈",
              "그렇게 너의 눈빛을 보곤 사랑에 눈을 떴어",
              "항상 알고 있던 것들도 어딘가",
              "새롭게 바뀐 것 같아",
              "남의 얘기 같던 설레는 일들이",
              "내게 일어나고 있어",
              "나에게만 준비된 선물 같아",
              "자그마한 모든 게 커져만 가",
              "항상 평범했던 일상도 특별해지는 이 순간",
              "별생각 없이 지나치던 것들이",
              "이제는 마냥 내겐 예뻐 보이고",
              "내 맘을 설레게 해",
              "항상 어두웠던 것들도 어딘가",
              "빛나고 있는 것 같아",
              "남의 얘기 같던 설레는 일들이",
              "내게 일어나고 있어",
              "나에게만 준비된 선물 같아",
              "자그마한 모든 게 커져만 가",
              "항상 평범했던 일상도 특별해지는 이 순간",
              "너를 알게 된 뒤 보이는",
              "모든 것들이 너무 예뻐 보여",
              "그렇게 신난 아이처럼",
              "순수한 사람이 된 것 같아",
              "나에게만 준비된 선물 같아",
              "자그마한 모든 게 커져만 가",
              "항상 평범했던 일상도 특별해지는 이 순간",
              "깊은 사랑에 빠진 순간"]},
    }
  },
  methods: {

  },
  mounted() {
    this.songID = this.$route.params.songID;
  },

}
</script>
