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
                  <h1 class="mb-0 truncate text-large"><a v-for="(singer, index) in song.artist" v-bind:key="index"><router-link :to="'/A505/artistDetail/'+singer.id" class="text-primary mr-3 ">{{singer.name}}</router-link></a></h1><br>
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
        <div class="separator mb-5"></div>
      </b-colxx>
    </b-row>
    <b-row>
      <b-colxx xxs="12">
        <h2>댓글></h2>
        <b-colxx xxs="12" class="mb-1 pl-3 pr-3 mt-1" style="display: inline-flex;" v-for="(cmt, index) in comment" v-bind:key="index">
          <div style="width:16%;" class="mr-2">
            <h4 class="font-weight-medium mb-0" style="text-align:center;">{{cmt.user.username}}</h4>
          </div>
          <div style="width:70%;">
            <h4>{{cmt.content}}</h4>
          </div>
          <div style="margin-left: auto;">
            <p class="text-muted mb-0 text-small">{{cmt.updated_at.substr(0,10)+" "+cmt.updated_at.substr(11,8)}}</p>
            <div style="text-align: end;" v-if="checkComment(cmt.user.id)">
              <a class="mb-0 text-small text-primary" style="cursor:pointer;">수정</a>
              <a class="mb-0 text-small text-primary" style="cursor:pointer;" @click="deleteCommet()">삭제</a>
            </div>
          </div>
        </b-colxx>
        <b-input-group class="comment-contaiener">
          <b-input placeholder="댓글" id="comment" />
          <template v-slot:append>
            <b-button variant="primary" @click="sendComment">
              <span class="d-inline-block">작성</span>
              <i class="simple-icon-arrow-right ml-2"></i>
            </b-button>
          </template>
        </b-input-group>
      </b-colxx>
    </b-row>
    <LoginModal :showLogin="showLogin" @hideModal="showLogin=false"/>
    <b-modal v-model="showAlert" size="sm" hide-header hide-footer
            :hide-backdrop="true"
            :no-close-on-backdrop="true">
        <b-row style="justify-content: center;">
          <h4>댓글을 작성해주세요.</h4>
        </b-row>
        <b-row class="mt-1" style="justify-content: center;">
          <b-button variant="secondary" @click="showAlert=!showAlert">확인</b-button>
        </b-row>
    </b-modal>
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
        this.likeCount = this.song.like + this.song.user_like.length;
      })
    http
      .get("/song/"+this.songID+"/comment/")
      .then((rest) => {
        this.comment = rest.data;
      })
  },
  data () {
    return {
      showAlert: false,
      likeCount:0,
      songID: 0,
      showLogin: false,
      song: [],
      comment: [],
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
            this.likeCount+=1;
          }else{
            for(var i=0;i<this.user.like_songs.length;i++){
              if(this.user.like_songs[i]==id){
                this.user.like_songs.splice(i, 1);
                this.likeCount-=1;
                break;
              }
            }
          }
      })
      }else{
        this.showLogin=true;
      }
    },
    checkComment: function(id) {
      if(this.user.id){
        if(this.user.id == id){
          return true;
        }
      }
      return false;
    },
    sendComment: function(){
      if(this.user.id){
        const commentForm = new FormData();
        if(document.getElementById("comment").value==""){
          this.showAlert=true;
          return;
        }
        commentForm.append("content", document.getElementById("comment").value)
        http.post(`song/${this.songID}/comment/`,commentForm,{
          headers: {
            Authorization: this.$store.state.authorization
          },
          
        })
        .then((rest) => {
          http
          .get("/song/"+this.songID+"/comment/")
          .then((rest) => {
            this.comment = rest.data;
          })
        })
      }else{
        this.showLogin=true;
      }
    },
    deleteCommet: function(){
      http.post(`song/${this.songID}/comment/`,'',{
        headers: {
          Authorization: this.$store.state.authorization
        },
        
      })
      .then((rest) => {
        http
        .get("/song/"+this.songID+"/comment/")
        .then((rest) => {
          this.comment = rest.data;
        })
      })
    }
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
