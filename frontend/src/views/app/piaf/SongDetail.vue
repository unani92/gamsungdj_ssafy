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
                  <h1 class="mb-0 truncate text-large"><router-link :to="'/app/piaf/artistDetail/'+song.artist[0].id" class="text-primary">{{song.artist[0].name}}</router-link></h1><br>
                  <h2 class="mb-0 truncate">앨범: <router-link :to="'/app/piaf/albumDetail/'+song.album.id" class="text-primary">{{song.album.name}}</router-link></h2><br>
                  <h3 class="mb-0 truncate " style="display: inline-flex;">장르:<h3 class="ml-1" v-for="(genre, index) in song.genres" v-bind:key="index"> {{genre.name}}</h3></h3><br>
                  <h3 class="mb-0 truncate">감정: {{song.type}}</h3>
                  <h1 class="mb-0 truncate glyph-icon simple-icon-heart mt-5 text-large"> {{song.like}}</h1>
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
          <h4 v-for="(row, index) in song.lyric.split('/')" v-bind:key="index">{{row}}</h4>
        </b-colxx>
      </b-colxx>
      <b-colxx xxs="12">

      </b-colxx>
    </b-row>
  </div>
</template>
<script>
import http from "../../../utils/http-common";
export default {
  components: {
  },
  created() {
    this.songID = this.$route.params.songID;
    http
      .get("/song/"+this.songID)
      .then((rest) => {
        this.song = rest.data;
      })
  },
  data () {
    return {
      songID: 0,

      song: [],
    }
  },
  methods: {

  },
  mounted() {
    this.songID = this.$route.params.songID;
  },

}
</script>
