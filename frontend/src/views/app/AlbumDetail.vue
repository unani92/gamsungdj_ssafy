<template>
  <div v-if="songs.length">
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
                  <h1 class="mb-0 truncate text-large"><a v-for="(singer, index) in album.artist" v-bind:key="index"><router-link :to="'/A505/artistDetail/'+singer.id" class="text-primary">{{singer.name}}</router-link></a></h1><br>
                  <h3 class="mb-0 truncate " style="display: inline-flex;">장르:<h3 class="ml-1" v-for="(genre, index) in album.genres" v-bind:key="index"> {{genre.name}}</h3></h3><br>
                  <h3 class="mb-0 truncate">발매일: {{album.released_date}}</h3><br>
                  <h1 v-if="!checkLikeAlbum() && this.album.user_like" class="mb-0 truncate mt-5 text-large glyph-icon" style="cursor:pointer;" @click="likeAlbum(album.id)"><img src="../../assets/img/heart/heart_empty.png" style="width:32px;vertical-align:top;"/> {{this.album.like + this.album.user_like.length}}</h1>
                  <h1 v-if="checkLikeAlbum() && this.album.user_like" class="mb-0 truncate mt-5 text-large glyph-icon" style="cursor:pointer;" @click="likeAlbum(album.id)"><img src="../../assets/img/heart/heart_full.png" style="width:32px;vertical-align:top;"/> {{this.album.like + this.album.user_like.length}}</h1>
                  <!-- <h1 class="mb-0 truncate mt-5 ml-5 text-large"><h1 class="glyph-icon simple-icon-control-play pb-0" style="cursor:pointer;"> 재생</h1></h1>
                  <h1 class="mb-0 truncate mt-5 ml-5 text-large"><h1 class="glyph-icon simple-icon-playlist pb-0" style="cursor:pointer;"> 추가</h1></h1> -->
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
        <template v-if="isSong">
          <template v-if="!moreSong">
            <h2>수록곡><a v-if="songs.length>5" @click="showMoreSong" style="font-size:0.7em; float:right; cursor:pointer">더보기∨</a></h2>
          </template>
          <template v-else>
            <h2>수록곡><a v-if="songs.length>5" @click="showMoreSong" style="font-size:0.7em; float:right; cursor:pointer">접기∧</a></h2>
          </template>
           <b-colxx xxs="12" class="pl-0 pr-3">
          <b-colxx xxs="12" class="pl-3 pr-3">
            <b-card class="mb-0" style="text-align: center;">
              <table  class="table table-sm" style="margin-bottom:0px;">
                  <thead style="font-size: initial;">
                    <th></th>
                    <th id='song' @click="changeSortValue('name')" style="cursor:pointer">곡</th>
                    <th id='artist' @click="changeSortValue('artist')" style="cursor:pointer">가수</th>
                    <th>장르</th>
                    <th style="width:10%">재생</th>
                    <th style="width:10%">추가</th>
                    <th style="width:10%">좋아요</th>
                  </thead>
                  <tbody style="font-size: x-large;">
                    <tr v-show="song.id" :class="{'flex-row':true}" v-for="(song, index) in sortSongs.slice(0,songListSize)" v-bind:key="index" style="cursor:pointer;">
                      <td style="width:85px;"><img :src="album.img" class="list-thumbnail responsive border-0" @click="detailSong(song.id)"/></td>
                      <td class="list-item-heading mb-0 truncate" style="vertical-align: middle;" @click="detailSong(song.id)">{{song.name}}</td>
                      <td class="list-item-heading mb-0 truncate" style="vertical-align: middle;" @click="detailSong(song.id)"><a v-for="(singer, index) in song.artist" v-bind:key="index" class="mr-2">{{singer.name}}</a></td>
                      <td class="list-item-heading mb-0 truncate" style="vertical-align: middle;" @click="detailSong(song.id)"><a v-for="(genre, index) in song.genres" v-bind:key="index" class="mr-2">{{genre.name}}</a></td>
                      <td style="vertical-align: middle;" @click.prevent="addToPlaylistAndPlayNotify(song)"><div class="glyph-icon simple-icon-control-play"/></td>
                      <td v-if="!isLoggedin" style="vertical-align: middle;" @click.prevent="addToPlaylistAndNotify(song)"><div class="glyph-icon simple-icon-playlist"/></td>
                      <td v-else style="vertical-align: middle;">
                      <b-dropdown variant="empty" toggle-class="p-0 m-0" no-caret style="position:relative;">
                          <template slot="button-content">
                            <div class="glyph-icon simple-icon-playlist text-color" style="font-size:x-large;"/>
                          </template>
                          <b-dropdown-item @click="addToPlaylistAndNotify(song)">현재 재생목록</b-dropdown-item>
                          <b-dropdown-item v-for="(playlist, index) in userPlayList" :key="index" @click="addToUserPlaylist(song, playlist, index)">{{ playlist.name }}</b-dropdown-item>
                      </b-dropdown>
                      </td>

                      <td v-if="!checkLikeSong(index)" style="vertical-align: middle;" @click="likeSong(song.id, index)" ><img src="../../assets/img/heart/heart_empty.png" style="width:32px;"/></td>
                      <td v-if="checkLikeSong(index)" style="vertical-align: middle;" @click="likeSong(song.id, index)" ><img src="../../assets/img/heart/heart_full.png" style="width:32px;"/></td>
                    </tr>
                    <tr v-show="!song.id" :class="{'flex-row':true}" v-for="(song, index) in sortSongs.slice(0,songListSize)" v-bind:key="index+songListSize" class="card-img-overlay" style="position: relative">
                      <td style="width:85px;opacity:0.5;"><img :src="album.img" class="list-thumbnail responsive border-0" @click="detailSong(song.id)"/></td>
                      <td class="list-item-heading mb-0 truncate" style="vertical-align: middle;;opacity:0.5;" @click="detailSong(song.id)">{{song.name}}</td>
                      <td colspan="2" style="vertical-align: middle;">서비스를 준비중입니다.</td>
                      <td></td>
                      <td></td>
                      <td></td>
                    </tr>
                  </tbody>
              </table>
            </b-card>
          </b-colxx>
        </b-colxx>
        <br><div class="separator mb-5"></div>
        </template>
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
                <a class="mb-0 text-small text-primary" style="cursor:pointer;" @click="checkDelete(cmt.pk, index)">삭제</a>
              </div>
            </div>
          </b-colxx>
        </b-colxx>
        <b-input-group class="comment-contaiener pl-3 pr-3">
          <b-input placeholder="댓글" id="comment"  @keyup.enter="sendComment"/>
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
import http from "../../utils/http-common"
import http2 from "../../utils/http-user"
import LoginModal from '@/components/User/LoginModal.vue'
import { mapGetters, mapMutations, mapActions, mapState } from "vuex"

const youtubeURL = 'https://www.googleapis.com/youtube/v3/search'
const API_KEY = process.env.VUE_APP_YOUTUBE_API_KEY

export default {

  components: {
    LoginModal,
  },
  created() {
    this.albumID = this.$route.params.albumID;
    http
      .get("/album/"+this.albumID)
      .then((rest) => {
        this.album = rest.data.data;
        this.album.released_date = rest.data.data.released_date.substr(0,4) + "-" + rest.data.data.released_date.substr(4,2) + "-" + rest.data.data.released_date.substr(6,2);
        this.songs = rest.data.songs;
        this.likeCount = this.album.like + this.album.user_like.length;
        var namearray =  rest.data.data.songs.split(",");
        for(var i=0; i<this.songs.length;i++){
          if(!this.songs[i]){
            this.songs[i] = {"name": namearray[i]};
          }
        }
      })
    http
      .get("/album/"+this.albumID+"/comment/")
      .then((rest) => {
        this.comment = rest.data.songComment.concat(rest.data.albumComment);
      })
  },
  data () {
    return {
      deleteCheck: false,
      deletePK: 0,
      deleteIndex:-1,
      modifyComment: false,
      modifyPK: 0,
      modifyIndex: -1,
      showAlert: false,
      alertText: "",
      likeCount:0,
      showLogin: false,
      sort_value : "",
	  	sort_type : 'asc',
      isSong: true,
      moreSong: false,
      songListSize: 5,
      albumID: 0,
      songs: [],
      album:[],
      comment:[],
    }
  },
  methods: {
    ...mapActions(["addToPlaylistAndPlay", "addToPlaylist"]),
    async addToPlaylistAndPlayNotify(data) {
      for(let i=0; i<this.playlist.length; i++) {
        if(this.playlist[i].id == data.id) {
          this.$notify('warning', "재생 목록에 이미 포함 된 곡입니다.", data.name+" - "+data.artist[0].name, { duration: 4000, permanent: false })
          return
        }
      }
      this.addToPlaylistAndPlay(data)
      this.$notify('primary', "재생 중인 곡", data.name+" - "+data.artist[0].name, { duration: 4000, permanent: false })
    },
    async addToPlaylistAndNotify(data) {
      for(let i=0; i<this.playlist.length; i++) {
        if(this.playlist[i].id == data.id) {
          this.$notify('warning', "재생 목록에 이미 포함 된 곡입니다.", data.name+" - "+data.artist[0].name, { duration: 4000, permanent: false })
          return
        }
      }
      this.addToPlaylist(data)
      this.$notify('primary', "재생 목록에 추가 되었습니다.", data.name+" - "+data.artist[0].name, { duration: 4000, permanent: false })
    },
    addToUserPlaylist(data, playlist, index) {
      for(let i=0; i<playlist.song.length; i++) {
        if(playlist.song[i].id == data.id) {
          this.$notify('warning', "재생 목록에 이미 포함 된 곡입니다.", data.name+" - "+data.artist[0].name, { duration: 4000, permanent: false })
          return
        }
      }
      http2
      .post(`playlist/${playlist.id}/song/`, {'songs': [data.id]}, this.config)
      .then((value)=> {
        this.$notify('primary', "사용자 재생 목록에 추가 되었습니다.", data.name+" - "+data.artist[0].name, { duration: 4000, permanent: false })
        this.userPlayList[index].song.push(data)
      })
    },
    showMoreSong: function() {
      this.moreSong = !this.moreSong;
      if (this.songListSize == 5){
        this.songListSize = this.songs.length;
      }else{
        this.songListSize = 5;
      }
    },
    detailSong: function(id){
      this.$router.push('/A505/songDetail/'+id)
    },
    changeSortValue(value) {
      if(this.sort_value != value){
        this.sort_value=value;
        this.sort_type = 'asc';
      }else{
        if(this.sort_type =='asc'){
          this.sort_type = 'desc';
        }else if(this.sort_type =='desc'){
          this.sort_value = '';
          this.sort_type = 'none';
        }else{
          this.sort_type = 'asc'
        }
      }

      var tag1 = document.getElementById('song');
      var tag2 = document.getElementById('artist');
      if(this.sort_value=='name'){
        tag1.style.color = "#236591";
      }else {
        tag1.style.color = "";
      }

      if(this.sort_value=='artist'){
        tag2.style.color = "#236591";
      }else {
        tag2.style.color = "";
      }
    },
    checkLikeSong(index){
      if(this.user){
        for(let i=0;i<this.songs[index].user_like.length;i++){
          if(this.songs[index].user_like[i].id===this.user.id){
            return true;
          }
        }
        return false;
      }
      return false;
    },
    likeSong: function(id, index) {
      if(this.user){
        http.post(`song/${id}/like/`,'',{
          headers: {
            Authorization: this.$store.state.authorization
          },
        })
        .then((rest) => {
          if(rest.data.liked){
            this.songs[index].user_like.push(this.user);
            this.$notify('primary', "♥ 좋아요", this.songs[index].name+" - "+this.songs[index].artist[0].name, { duration: 5000, permanent: false });
          }else{
            for(var i=0;i<this.songs[index].user_like.length;i++){
              if(this.songs[index].user_like[i].id==this.user.id){
                this.songs[index].user_like.splice(i, 1);
                this.$notify('primary', "♡ 좋아요 취소", this.songs[index].name+" - "+this.songs[index].artist[0].name, { duration: 5000, permanent: false });
                break;
              }
            }
          }
      })
      }else{
        this.showLogin=true;
      }
    },
    checkLikeAlbum(){
       if(this.user && this.album.user_like){
         for(var i=0;i<this.album.user_like.length;i++){
          if(this.album.user_like[i].id==this.user.id){
            return true;
          }
        }
        return false;
       }
      return false;
    },
    likeAlbum: function(id) {
      if(this.user){
        http.post(`album/${id}/like/`,'',{
          headers: {
            Authorization: this.$store.state.authorization
          },
        })
        .then((rest) => {
          if(rest.data.liked){
            this.album.user_like.push(this.user);
            this.$notify('primary', "♥ 좋아요", this.album.name, { duration: 5000, permanent: false });
          }else{
            for(var i=0;i<this.album.user_like.length;i++){
              if(this.album.user_like[i].id==this.user.id){
                this.album.user_like.splice(i, 1);
                this.$notify('primary', "♡ 좋아요 취소", this.album.name, { duration: 5000, permanent: false });
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
          http.post(`album/${this.albumID}/comment/`,commentForm,{
            headers: {
              Authorization: this.$store.state.authorization
            },

          })
          .then((rest) => {
            var tag = document.getElementById('comment');
            tag.value = "";
            http
            .get("album/"+this.albumID+"/comment/")
            .then((rest) => {
              this.comment = rest.data.songComment.concat(rest.data.albumComment);
            })
          })
        }else{
          var type;
          if(this.comment[this.modifyIndex].song){
            type = "song/";
          }else{
            type = "album/"
          }
          http.put(type+this.modifyPK+"/comment/",commentForm,{
            headers: {
              Authorization: this.$store.state.authorization
            },

          })
          .then((rest) => {
            http
            .get("/album/"+this.albumID+"/comment/")
            .then((rest) => {
              this.ModifyMode(this.modifyPK, this.modifyIndex);
              this.comment = rest.data.songComment.concat(rest.data.albumComment);
            })
          })
        }

      }else{
        this.showLogin=true;
      }
    },
    checkDelete: function(pk, index){
      if(this.modifyComment){
        this.alertText="수정을 취소해주세요.";
        this.showAlert=true;
        return;
      }
      this.deletePK =pk;
      this.deleteIndex = index;
      this.deleteCheck=true;
      this.alertText="댓글을 삭제하시겠습니까?";
      this.showAlert=true;
      return;
    },
    deleteCommet: function(){
      var type;
      if(this.comment[this.deleteIndex].song){
        type = "song/";
      }else{
        type = "album/"
      }

      http.delete(type+this.deletePK+"/comment/",{
        headers: {
          Authorization: this.$store.state.authorization
        },
      })
      .then((rest) => {
        http
        .get("album/"+this.albumID+"/comment/")
          .then((rest) => {
            this.comment = rest.data.songComment.concat(rest.data.albumComment);
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
    focusComment: function(){
      var tag = document.getElementById('commentTitle');
      tag.scrollIntoView(true);
    }
  },
  computed: {
    sortSongs() {
		if(this.sort_value=='name'){
			if(this.sort_type=='asc'){
			return this.songs.sort((a, b) => {
				if( a.name > b.name) return 1;
				else if ( a.name < b.name ) return -1;
				else return 0;
			})
			}else if(this.sort_type=='desc'){
				return this.songs.sort((a, b) => {
					if( a.name < b.name) return 1;
					else if ( a.name > b.name ) return -1;
					else return 0;
				})
			}
		}else if(this.sort_value=='artist'){
			if(this.sort_type=='asc'){
			return this.songs.sort((a, b) => {
				if( a.artist > b.artist) return 1;
				else if ( a.artist < b.artist ) return -1;
				else return 0;
			})
			}else if(this.sort_type=='desc'){
				return this.songs.sort((a, b) => {
					if( a.artist < b.artist) return 1;
					else if ( a.artist > b.artist ) return -1;
					else return 0;
				})
			}
		}
		return this.songs.sort((a, b) => {
			return b.id - a.id
		})

    },
    sortComment() {
      return this.comment.sort((a, b) => {
				if( a.updated_at.substr(0,10)+" "+a.updated_at.substr(11,8) > b.updated_at.substr(0,10)+" "+b.updated_at.substr(11,8) ) return 1;
				else if ( a.updated_at.substr(0,10)+" "+a.updated_at.substr(11,8) < b.updated_at.substr(0,10)+" "+b.updated_at.substr(11,8) ) return -1;
				else return 0;
			})
    },
    ...mapState(['authorization', 'user', 'isLoggedin', 'playlist', 'userPlayList']),
    ...mapGetters(['config'])
  }
}
</script>
