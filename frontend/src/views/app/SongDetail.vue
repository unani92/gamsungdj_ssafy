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
                  <h1 class="mb-0 truncate text-large"><a v-for="(singer, index) in song.artist" v-bind:key="index"><router-link :to="'/app/artistDetail/'+singer.id" class="text-primary mr-3 ">{{singer.name}}</router-link></a></h1><br>
                  <h2 class="mb-0 truncate">앨범: <router-link :to="'/app/albumDetail/'+song.album.id" class="text-primary">{{song.album.name}}</router-link></h2><br>
                  <h3 class="mb-0 truncate " style="display: inline-flex;">장르:<h3 class="ml-1" v-for="(genre, index) in song.genres" v-bind:key="index"> {{genre.name}}</h3></h3><br>
                  <h3 class="mb-0 truncate">감정: {{song.type}}</h3>
                  <h1 v-if="!checkLikeSong(song.id)" class="mb-0 truncate mt-5 text-large"><img src="../../assets/img/heart/heart_empty.png" @click="likeSong(song.id)" style="width:32px; cursor:pointer;"/>{{song.like}}</h1>
                  <h1 v-if="checkLikeSong(song.id)" class="mb-0 truncate mt-5 text-large"><img src="../../assets/img/heart/heart_full.png" @click="likeSong(song.id)" style="width:32px; cursor:pointer;"/>{{song.like}}</h1>
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
    <LoginModal :showLogin="showLogin" @hideModal="showLogin=false"/>
  </div>
</template>
<script>
import http from "../../utils/http-common";
import LoginModal from '@/components/User/LoginModal.vue'
import { mapGetters, mapMutations, mapActions, mapState } from "vuex";
export default {
  components: {
    LoginModal,
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
      showLogin: false,
      song: [],
    }
  },
  methods: {
    checkLikeSong(songID){
      if(this.user.like_songs){
        for(var i=0;i<this.user.like_songs.length;i++){
          if(this.user.like_songs[i]==songID){
            return true;
          }
        }
        return false;
      }
      return false;
    },
    likeSong: function(id) {
      console.log(this.$store.state.authorization)
      if(this.user.like_songs){
        http.post(`song/${id}/like/`,'',{
          headers: {
            Authorization: this.$store.state.authorization
          },
        })
        .then((rest) => {
          console.log(rest.data)
          if(rest.data.liked){
            this.user.like_songs.push(id);
          }else{
            for(var i=0;i<this.user.like_songs.length;i++){
              if(this.user.like_songs[i]==id){
                this.user.like_songs.splice(i, 1);
                break;
              }
            }
          }
      })
      }else{
        this.showLogin=true;
      }
    },
  },
  mounted() {
    this.songID = this.$route.params.songID;
  },
  computed: {
    ...mapGetters({
      currentUser: "currentUser",
      // menuType: "getMenuType",
      // menuClickCount: "getMenuClickCount",
      // selectedMenuHasSubItems: "getSelectedMenuHasSubItems"
    }),
    ...mapState(['authorization', 'user', 'isLoggedin'])
  },
}
</script>
