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
                  <img class="card-img-top" :src="artist.img" style="border-top-left-radius:initial; border-top-right-radius:initial"/>
                </div>
                <div xxs="8" style="width:70%;">
                  <h1 class="mb-0 truncate text-xlarge" style="margin-top:3%">{{artist.name}}</h1><br>
                  <h1 class="mb-0 truncate text-large">{{artist.type}}</h1><br>
                  <h3 class="mb-0 truncate" v-if="artist.member">멤버: {{artist.member}}</h3><br>
                  <h3 class="mb-0 truncate">데뷔: {{artist.debue}}</h3><br>
                </div>
        </b-colxx>
    </b-colxx>
    <b-colxx xxs="12">
        <div class="separator mb-5"></div>
      </b-colxx>
  </b-row>
  <b-row>
    <b-colxx xxs="12">
      <template v-if="isSong">
        <template v-if="!moreSong">
          <h2>곡><a v-if="songs.length>5" @click="showMoreSong" style="font-size:0.7em; float:right; cursor:pointer">더보기∨</a></h2>
        </template>
        <template v-else>
          <h2>곡><a v-if="songs.length>5" @click="showMoreSong" style="font-size:0.7em; float:right; cursor:pointer">접기∧</a></h2>
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
                    <tr :class="{'flex-row':true}" v-for="(song, index) in sortSongs.slice(0,songListSize)" v-bind:key="index" style="cursor:pointer;">
                      <td style="width:85px;"><img :src="song.img" class="list-thumbnail responsive border-0" @click="detailSong(song.id)"/></td>
                      <td class="list-item-heading mb-0 truncate" style="vertical-align: middle;" @click="detailSong(song.id)">{{limitString(song.name)}}</td>
                      <td class="list-item-heading mb-0 truncate" style="vertical-align: middle;" @click="detailSong(song.id)"><a v-for="(member, index) in song.artist" v-bind:key="index">{{member.name}}</a></td>
                      <td class="list-item-heading mb-0 truncate" style="vertical-align: middle;" @click="detailSong(song.id)"><a v-for="(genre, index) in song.genres" v-bind:key="index">{{genre.name}}</a>{{song.genre}}</td>
                      <td style="vertical-align: middle;" @click.prevent="addToPlaylistAndPlay(song)"><div class="glyph-icon simple-icon-control-play"/></td>
                      <td style="vertical-align: middle;" @click.prevent="addToPlayList(song)"><div class="glyph-icon simple-icon-playlist"/></td>
                      <!-- <td style="vertical-align: middle;" @click.prevent="likeSong(song.id)" ><div class="glyph-icon simple-icon-heart" /></td> -->
                      <td v-if="!checkLikeSong(index)" style="vertical-align: middle;" @click="likeSong(song.id, index)" ><img src="../../assets/img/heart/heart_empty.png" style="width:32px;"/></td>
                      <td v-if="checkLikeSong(index)" style="vertical-align: middle;" @click="likeSong(song.id, index)" ><img src="../../assets/img/heart/heart_full.png" style="width:32px;"/></td>
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
      <template v-if="isAlbum">
        <template v-if="!moreAlbum">
          <h2>앨범><a v-if="albums.length>5" @click="showMoreAlbum" style="font-size:0.7em; float:right; cursor:pointer">더보기∨</a></h2>
        </template>
        <template v-else>
          <h2>앨범><a v-if="albums.length>5" @click="showMoreAlbum" style="font-size:0.7em; float:right; cursor:pointer">접기∧</a></h2>
        </template>
        <b-colxx xxs="12" class="mb-4 pl-0 pr-3" style="display: inline-flex;">
            <b-card class="mr-3 ml-3" no-body v-for="(album, index) in albums.slice(0,5)" v-bind:key="index" style="width:18%; cursor:pointer;" @click="detailAlbum(album.id)">
                <div class="position-relative">
                    <img :src="album.img" class="card-img-top"/>
                </div>
                <b-card-body>
                    <b-row>
                        <b-colxx>
                            <h4 style="font-weight :bold">{{album.name}}</h4>
                            <h5><a v-for="(singer, index) in album.artist" v-bind:key="index">{{singer.name}}</a></h5>
                            <h6 v-if="album.genre">장르:<a v-for="(genre, index) in album.genres" v-bind:key="index"> {{genre.name}}</a></h6>
                            <h6>발매일: {{dateformat(album.released_date)}}</h6>
                            <img src="../../assets/img/heart/heart_empty.png" v-if="!checkLikeAlbum(index)" style="width:32px;" @click="likeAlbum(album.id, index)"/>
                            <img src="../../assets/img/heart/heart_full.png" v-if="checkLikeAlbum(index)" style="width:32px;" @click="likeAlbum(album.id, index)"/>
                        </b-colxx>
                    </b-row>
                </b-card-body>
            </b-card>
        </b-colxx>
        <template v-if="moreAlbum">
          <b-colxx xxs="12" class="mb-4 pl-0 pr-3" style="display: inline-flex;" v-for="n in parseInt((albums.length-1)/5)" v-bind:key="n">
            <b-card class="mr-3 ml-3" no-body v-for="(album, index) in albums.slice(n*5,(n+1)*5)" v-bind:key="index" style="width:18%; cursor:pointer;" @click="detailAlbum(album.id)">
              <div class="position-relative">
                <img :src="album.img" class="card-img-top"/>
              </div>
              <b-card-body>
                <b-row>
                    <b-colxx xxs="10" class="mb-3">
                        <h4 style="font-weight :bold">{{album.name}}</h4>
                        <h5><a v-for="(singer, index) in album.artist" v-bind:key="index">{{singer.name}}</a></h5>
                        <h6 v-if="album.genre">장르: {{album.genre}}</h6>
                        <h6>발매일: {{dateformat(album.released_date)}}</h6>
                        <img src="../../assets/img/heart/heart_empty.png" v-if="!checkLikeAlbum(index)" style="width:32px;" @click="likeAlbum(album.id, index)"/>
                        <img src="../../assets/img/heart/heart_full.png" v-if="checkLikeAlbum(index)" style="width:32px;" @click="likeAlbum(album.id, index)"/>
                    </b-colxx>
                </b-row>
              </b-card-body>
            </b-card>
          </b-colxx>
        </template>
      </template>
    </b-colxx>
  </b-row>
  <LoginModal :showLogin="showLogin" @hideModal="showLogin=!showLogin"/>
  <b-modal v-model="emptyModal"  hide-header hide-footer
            :hide-backdrop="true"
            :no-close-on-backdrop="true">
        <b-row style="justify-content: center;">
          <h4>'{{keyword}}' 검색 결과가 없습니다.</h4>
        </b-row>
        <b-row class="mt-1" style="justify-content: center;">
          <b-button variant="secondary" @click="toMain()">메인으로</b-button>
        </b-row>
    </b-modal>
  </div>
</template>
<script>
import http from "../../utils/http-common";
import LoginModal from '@/components/User/LoginModal.vue'
import { mapGetters, mapMutations, mapActions, mapState } from "vuex";
import { adminRoot } from "../../constants/config";
export default {
  components: {
    LoginModal,
  },
  created() {
    this.artistID = this.$route.params.artistID;
    http
      .get("/artist/"+this.artistID)
      .then((rest) => {
        this.artist = rest.data.data;
        this.albums = rest.data.albums;
        if(this.albums.length!=0){
          this.isAlbum=true;
        }
        this.songs = rest.data.songs;
        if(this.songs.length!=0){
          this.isSong=true;
        }
      })
  },
  data () {
    return {
      sort_value : "",
	  	sort_type : 'asc',
      isSong: false,
      isAlbum: false,
      moreSong: false,
      moreAlbum: false,
      showLogin: false,
      clickAlbumLike: false,
      songListSize: 5,
      // currentPage: 1,
      artistID: 0,
      artist: {},
      songs: [],
      albums: [],
    }
  },
  methods: {
    showMoreSong: function() {
      this.moreSong = !this.moreSong;
      if (this.songListSize == 5){
        this.songListSize = this.songs.length;
      }else{
        this.songListSize = 5;
      }
    },
    showMoreAlbum: function() {
      this.moreAlbum = !this.moreAlbum;
    },
    detailSong: function(id){
      this.$router.push('/A505/songDetail/'+id)
    },
    detailAlbum: function(id){
      if(!this.clickAlbumLike){
        this.$router.push('/A505/albumDetail/'+id)
      }else{
        this.clickAlbumLike=false;
      }
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
    likeSong: function(id, index) {
      if(this.user){
        http.post(`song/${id}/like/`,'',{
          headers: {
            Authorization: this.$store.state.authorization
          },
        })
        .then((rest) => {
          console.log(rest.data)
          if(rest.data.liked){
            this.songs[index].user_like.push(this.user);
          }else{
            for(var i=0;i<this.songs[index].user_like.length;i++){
              if(this.songs[index].user_like[i].id==this.user.id){
                this.songs[index].user_like.splice(i, 1);
                break;
              }
            }
          }
      })
      }else{
        this.showLogin=true;
      }
    },
    likeAlbum: function(id, index) {
      this.clickAlbumLike = true;
      if(this.user){
        http.post(`album/${id}/like/`,'',{
          headers: {
            Authorization: this.$store.state.authorization
          },
        })
        .then((rest) => {
          console.log(rest.data)
          if(rest.data.liked){
            this.albums[index].user_like.push(this.user);
          }else{
            for(var i=0;i<this.albums[index].user_like.length;i++){
              if(this.albums[index].user_like[i].id==this.user.id){
                this.albums[index].user_like.splice(i, 1);
                break;
              }
            }
          }
      })
      }else{
        this.showLogin=true;
      }
    },
    limitString(songName) {
      if(songName.length>26){
        return songName.substr(0,22) + "...";
      }else{
        return songName;
      }
    },
    dateformat(albumDate) {
      return albumDate.substr(0,4) + "-" + albumDate.substr(4,2) + "-" + albumDate.substr(6,2);
    },
    checkLikeSong(index){
      if(this.user){
        for(var i=0;i<this.songs[index].user_like.length;i++){
          if(this.songs[index].user_like[i].id==this.user.id){
            return true;
          }
        }
        return false;
      }
      return false;
    },
    checkLikeAlbum(index){
       if(this.user){
         for(var i=0;i<this.albums[index].user_like.length;i++){
          if(this.albums[index].user_like[i].id==this.user.id){
            return true;
          }
        }
        return false;
       }
      return false;
    },
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
