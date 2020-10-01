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
                  <h2 class="mb-0 truncate" v-if="song.album">앨범: <router-link :to="'/A505/albumDetail/'+song.album.id" class="text-primary">{{song.album.name}}</router-link></h2><br>
                  <h3 class="mb-0 truncate " style="display: inline-flex;">장르:<h3 class="ml-1" v-for="(genre, index) in song.genres" v-bind:key="index"> {{genre.name}}</h3></h3><br>
                  <h3 class="mb-0 truncate">감정: {{song.type}}</h3>
                  <h1 v-if="!checkLikeSong() && this.song.user_like" class="mb-0 truncate mt-5 text-large glyph-icon" style="cursor:pointer;" @click="likeSong(song.id)"><img src="../../assets/img/heart/heart_empty.png" style="width:32px;vertical-align:top;"/> {{this.song.like + this.song.user_like.length}}</h1>
                  <h1 v-if="checkLikeSong()" class="mb-0 truncate mt-5 text-large glyph-icon" style="cursor:pointer;" @click="likeSong(song.id)"><img src="../../assets/img/heart/heart_full.png" style="width:32px;vertical-align:top;"/> {{this.song.like + this.song.user_like.length}}</h1>
                  <h1 class="mb-0 truncate mt-5 ml-5 text-large"><h1 class="glyph-icon simple-icon-control-play pb-0" style="cursor:pointer;" @click.prevent="addToPlaylistAndPlay(song)"> 재생</h1></h1>
                  <h1 class="mb-0 truncate mt-5 ml-5 text-large"><h1 class="glyph-icon simple-icon-playlist pb-0" style="cursor:pointer;" @click.prevent="addToPlayList(song)"> 추가</h1></h1>
                  <h1 class="mb-0 truncate mt-5 ml-5 text-large" @click="focusComment"><h1 class="glyph-icon simple-icon-bubble pb-0" style="cursor:pointer;"> {{comment.length}}</h1></h1>
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
        
        <template v-if="!moreLyric">
          <h2>가사><a v-if="lyrics.length>10" @click="showMoreLyric" style="font-size:0.7em; float:right; cursor:pointer">더보기∨</a></h2>
        </template>
        <template v-else>
          <h2>가사><a v-if="lyrics.length>10" @click="showMoreLyric" style="font-size:0.7em; float:right; cursor:pointer">접기∧</a></h2>
        </template>
        <b-colxx xxs="12" class="mb-4 pl-3 pr-3">
          <h4 v-for="(lyric, index) in lyrics.slice(0,lyricSize)" v-bind:key="index">{{lyric}}</h4>
        </b-colxx>
      </b-colxx>
      <b-colxx xxs="12">
        <div class="separator mb-5"></div>
      </b-colxx>
    </b-row>
    <b-row>
      <b-colxx xxs="12">
        <h2 id="commentTitle">댓글></h2>
        <b-colxx xxs="12" class="mb-1 pl-3 pr-3 mt-1"  v-for="(cmt, index) in sortComment" v-bind:key="index">
          <b-colxx xxs="12" style="display: inline-flex;">
            <div style="width:16%;" class="mr-2">
              <h4 v-if="cmt.user" class="font-weight-medium mb-0" style="text-align:center;">{{cmt.user.username}}</h4>
            </div>
            <div style="width:70%;">
              <h4  class="mb-0">{{cmt.content}}</h4>
              <!-- <b-input type="text" :value="cmt.content">{{cmt.content}}</b-input> -->
            </div>
            <div style="margin-left: auto;">
              <p v-if="cmt.updated_at" class="text-muted mb-0 text-small">{{cmt.updated_at.substr(0,10)+" "+cmt.updated_at.substr(11,8)}}</p>
              <div v-if="checkComment(cmt.user.id)" calss="mb-0" style=" text-align:end;">
                <a class="mb-0 text-small text-primary" :id="'modify_text_'+index" style="cursor:pointer;" @click="ModifyMode(cmt.pk, index)">수정</a>
                <a class="mb-0 text-small text-primary" style="cursor:pointer;" @click="checkDelete(cmt.pk)">삭제</a>
              </div>
            </div>
          </b-colxx>
        </b-colxx>
        <b-input-group class="comment-contaiener pl-3 pr-3">
          <b-input placeholder="댓글" id="comment" @keyup.enter="sendComment"/>
          <template v-slot:append>
            <b-button variant="primary" @click="sendComment">
              <span class="d-inline-block" id="commentButton">작성</span>
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
      <h4>{{alertText}}</h4>
    </b-row>
    <b-row class="mt-1" style="justify-content: center;">
       <b-button v-if="deleteCheck" class="mr-3" variant="danger" @click="showAlert=!showAlert;deleteCommet();">삭제</b-button>
        <b-button v-if="deleteCheck" variant="secondary" @click="showAlert=!showAlert;deleteCheck=!deleteCheck">취소</b-button>
        <b-button v-if="!deleteCheck" variant="secondary" @click="showAlert=!showAlert">확인</b-button>
    </b-row>
    </b-modal>
  </div>
</template>
<script>
import http from "../../utils/http-common";
import LoginModal from '@/components/User/LoginModal.vue'
import { mapGetters, mapMutations, mapActions, mapState } from "vuex";
import axios from 'axios'

const youtubeURL = 'https://www.googleapis.com/youtube/v3/search'
const API_KEY = process.env.VUE_APP_YOUTUBE_API_KEY

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
        this.lyrics = this.song.lyric.split('/');
      })
    http
      .get("/song/"+this.songID+"/comment/")
      .then((rest) => {
        this.comment = rest.data;
      })
  },
  data () {
    return {
      deleteCheck: false,
      deletePK: 0,
      modifyComment: false,
      modifyPK: 0,
      modifyIndex: -1,
      showAlert: false,
      alertText: "",
      songID: 0,
      showLogin: false,
      lyricSize: 10,
      moreLyric:false,
      song: [],
      lyrics: [],
      comment: [],
    }
  },
  methods: {
    checkLikeSong(){
      if(this.user && this.song.user_like){
        for(var i=0;i<this.song.user_like.length;i++){
          if(this.song.user_like[i].id==this.user.id){
            return true;
          }
        }
        return false;
      }
      return false;
    },
    likeSong: function(id) {
      console.log(this.$store.state.authorization)
      if(this.user){
        http.post(`song/${id}/like/`,'',{
          headers: {
            Authorization: this.$store.state.authorization
          },
        })
        .then((rest) => {
          console.log(rest.data)
          if(rest.data.liked){
            this.song.user_like.push(this.user);
            this.$notify('primary', "♥ 좋아요", this.song.name+" - "+this.song.artist[0].name, { duration: 5000, permanent: false });
          }else{
            for(var i=0;i<this.song.user_like.length;i++){
              if(this.song.user_like[i].id==this.user.id){
                this.song.user_like.splice(i, 1);
                this.$notify('primary', "♡ 좋아요 취소", this.song.name+" - "+this.song.artist[0].name, { duration: 5000, permanent: false });
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
      if(this.user){
        if(this.user.id == id){
          return true;
        }
      }
      return false;
    },
    sendComment: function(){
      if(this.user){
        const commentForm = new FormData();
        if(document.getElementById("comment").value.trim()==""){
          this.alertText="댓글을 작성해주세요.";
          this.showAlert=true;
          return;
        }
        commentForm.append("content", document.getElementById("comment").value)
        if(!this.modifyComment){
          http.post("song/" + this.songID + "/comment/",commentForm,{
            headers: {
              Authorization: this.$store.state.authorization
            },
            
          })
          .then((rest) => {
            var tag = document.getElementById('comment');
            console.log(tag);
            tag.value = "";
            http
            .get("song/"+this.songID+"/comment/")
            .then((rest) => {
              this.comment = rest.data;
            })  
          })  
        }else{
          http.put('song/'+this.modifyPK+"/comment/",commentForm,{
            headers: {
              Authorization: this.$store.state.authorization
            },
            
          })
          .then((rest) => {
            http
            .get("/song/"+this.songID+"/comment/")
            .then((rest) => {
              this.ModifyMode(this.modifyPK,this.modifyIndex);
              this.comment = rest.data;
            })
          })
        }
      }else{
        this.showLogin=true;
      }
    },
    checkDelete: function(pk){
      if(this.modifyComment){
        this.alertText="수정을 취소해주세요.";
        this.showAlert=true;
        return;
      }
      this.deletePK =pk;
      this.deleteCheck=true;
      this.alertText="댓글을 삭제하시겠습니까?";
      this.showAlert=true;
      return;
    },
    deleteCommet: function(){
      
      http.delete("song/"+this.deletePK+"/comment/",{
        headers: {
          Authorization: this.$store.state.authorization
        },
      })
      .then((rest) => {
        http
        .get("song/"+this.songID+"/comment/")
          .then((rest) => {
            this.comment = rest.data;
          })
      })
    },
    ModifyMode : function(pk, index){
      //$("#modify_format_"+pk).show();
      var tag1 = document.getElementById('comment');
      var tag2 = document.getElementById('modify_text_'+index);
      var tag3 = document.getElementById('commentButton');
      if(tag2.text == "수정"){
        tag1.value=this.comment[index].content;
        tag2.text = "취소";
        tag3.innerHTML = "수정";
        if(this.modifyIndex!=-1){
          var tag4 = document.getElementById('modify_text_'+this.modifyIndex);
          tag4.text = "수정";
        }
        this.modifyComment = true;
        this.modifyPK = pk;
        this.modifyIndex = index;
      }else{
        tag1.value="";
        tag2.text = "수정";
        tag3.innerHTML = "작성";
        this.modifyComment = false;
        this.modifyPK = 0;
        this.modifyIndex = -1;
      }
    },
    showMoreLyric: function(){
      this.moreLyric = !this.moreLyric;
      if(this.moreLyric){
        this.lyricSize = this.lyrics.length;
      }else{
        this.lyricSize = 10;
      }
    },
    focusComment: function(){
      var tag = document.getElementById('commentTitle');
      tag.scrollIntoView(true);
    },
    async fetchYoutubeId(song) {
      const { data } = await axios.get(youtubeURL, {
        params: {
          key: API_KEY,
          part: 'snippet',
          maxResults: 1,
          type: 'video',
          q: song.artist[0].name + ' ' + song.name
        }
      })
      const { items } = data
      const { videoId } = items[0].id
      const reqData = {'src': videoId}
      song['src'] = videoId
      await http.post(`addsrc/${song.id}/`, reqData,'')
    },
    async addToPlaylistAndPlay(song) {
      if (song['src']) {
        this.playlist.unshift(song)
        this.$store.state.playerControl = "add"
        this.$notify('primary', "재생 중인 곡", song.name+" - "+song.artist[0].name, { duration: 4000, permanent: false })
      } else {
        await this.fetchYoutubeId(song)
        this.playlist.unshift(song)
        this.$store.state.playerControl = "add"
        this.$notify('primary', "재생 중인 곡", song.name+" - "+song.artist[0].name, { duration: 4000, permanent: false })
      }
    },
    async addToPlayList(song) {
      if (song['src']) {
          this.playlist.push(song)
          this.$notify('primary', "재생 목록에 추가 었습니다.", song.name+" - "+song.artist[0].name, { duration: 4000, permanent: false })
      }
      else {
          await this.fetchYoutubeId(song)
          this.playlist.push(song)
          this.$notify('primary', "재생 목록에 추가 었습니다.", song.name+" - "+song.artist[0].name, { duration: 4000, permanent: false })
      }
    },
  },
  mounted() {
    this.songID = this.$route.params.songID;
  },
  computed: {
    sortComment() {
      return this.comment.sort((a, b) => {
				if( a.updated_at.substr(0,10)+" "+a.updated_at.substr(11,8) > b.updated_at.substr(0,10)+" "+b.updated_at.substr(11,8) ) return 1;
				else if ( a.updated_at.substr(0,10)+" "+a.updated_at.substr(11,8) < b.updated_at.substr(0,10)+" "+b.updated_at.substr(11,8) ) return -1;
				else return 0;
			})
    },
    ...mapGetters({
      currentUser: "currentUser",
      // menuType: "getMenuType",
      // menuClickCount: "getMenuClickCount",
      // selectedMenuHasSubItems: "getSelectedMenuHasSubItems"
    }),
    ...mapState(['authorization', 'user', 'isLoggedin', 'playlist'])
  },
}
</script>
