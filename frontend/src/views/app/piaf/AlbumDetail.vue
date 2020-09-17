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
                  <img class="card-img-top" :src="album.img" style="border-top-left-radius:initial; border-top-right-radius:initial"/>
                </div>
                <div xxs="8" style="width:70%;">
                  <h1 class="mb-0 truncate text-xlarge" style="margin-top:3%">{{album.name}}</h1><br>
                  <h1 class="mb-0 truncate text-large"><router-link :to="'/app/piaf/artistDetail/'+album.artistId" style="color: ghostwhite;">{{album.artist}}</router-link></h1><br>
                  <h3 class="mb-0 truncate">장르: {{album.genre}}</h3><br>
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
        <template v-if="isSong">
          <template v-if="!moreSong">
            <h2>수록곡><a v-if="songs.length>5" @click="showMoreSong" style="font-size:0.7em; float:right; cursor:pointer">더보기∨</a></h2>
          </template>
          <template v-else>
            <h2>수록곡><a v-if="songs.length>5" @click="showMoreSong" style="font-size:0.7em; float:right; cursor:pointer">접기∧</a></h2>
          </template>
          <b-card  :class="{'d-flex flex-row':true}" no-body v-for="(song, index) in songs.slice(0,5)" v-bind:key="index">
            <img :src="song.img" class="list-thumbnail responsive border-0"/>
            <div class="pl-2 d-flex flex-grow-1 min-width-zero">
                <div class="card-body align-self-center d-flex flex-column flex-lg-row justify-content-between min-width-zero align-items-lg-center">
                    <p class="list-item-heading mb-0 truncate">{{song.name}}</p>
                    <p class="mb-0 text-muted text-small w-15 w-sm-100">{{song.artist}}</p>
                    <p class="mb-0 text-muted text-small w-15 w-sm-100">{{song.genre}}</p>
                    <div class="glyph-icon simple-icon-control-play"/>
                    <div class="glyph-icon simple-icon-playlist"/>
                    <div class="glyph-icon simple-icon-magnifier-add" @click="detailSong(song.id)" style="cursor:pointer;"/>
                    <div class="glyph-icon simple-icon-heart"/>
                    <div class="separator mb-5"></div>
                </div>
            </div>
          </b-card>
          <template v-if="moreSong">
            <b-card  :class="{'d-flex flex-row':true}" no-body v-for="(song, index) in songs.slice(5,songs.length)" v-bind:key="index">
              <img :src="song.img" class="list-thumbnail responsive border-0"/>
              <div class="pl-2 d-flex flex-grow-1 min-width-zero">
                  <div class="card-body align-self-center d-flex flex-column flex-lg-row justify-content-between min-width-zero align-items-lg-center">
                      <p class="list-item-heading mb-0 truncate">{{song.name}}</p>
                      <p class="mb-0 text-muted text-small w-15 w-sm-100">{{song.artist}}</p>
                      <p class="mb-0 text-muted text-small w-15 w-sm-100">{{song.genre}}</p>
                      <div class="glyph-icon simple-icon-control-play"/>
                      <div class="glyph-icon simple-icon-playlist"/>
                      <div class="glyph-icon simple-icon-magnifier-add" @click="detailSong(song.id)" style="cursor:pointer;"/>
                      <div class="glyph-icon simple-icon-heart"/>
                      
                      <div class="separator mb-5"></div>
                  </div>
              </div>
            </b-card>
          </template>
          <br><div class="separator mb-5"></div>
        </template>
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
      isSong: true,
      moreSong: false,
      albumID: 0,
      album: { id:1, name:"축제", artistId:1, img: "https://cdnimg.melon.co.kr/cm2/album/images/103/48/325/10348325_500.jpg?679a781c2d3687f2aefffaeb310614d5/melon/resize/282/quality/80/optimize", genre:"발라드, 인디음악", artist:"멜로망스"},
      songs: [{ id: 1, name: '선물', artist: '멜로망스', genre: '발라드', img: 'https://cdnimg.melon.co.kr/cm/album/images/100/78/176/10078176_500.jpg?fc3fe8c6bd74c16bce7ffd971a930ffa/melon/resize/282/quality/80/optimize'},
      ],
    }
  },
  methods: {
    showMoreSong: function() {
      this.moreSong = !this.moreSong;
    },
    detailSong: function(id){
      this.$router.push('/app/piaf/songDetail/'+id)
    },

  },
  mounted() {
    this.albumID = this.$route.params.albumID;
  },

}
</script>
