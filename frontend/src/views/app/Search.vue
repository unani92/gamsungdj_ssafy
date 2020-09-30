<template>
<div>
  <b-row>
    <b-colxx xxs="12">
      <h1> '{{keyword}}' 검색 결과</h1>
      <div class="separator mb-5"></div>
    </b-colxx>
  </b-row>
  <b-row>
    <b-colxx xxs="12">
        <template v-if="isArtist">
          <template v-if="!moreArtist">
            <h2>아티스트><a v-if="artists.length>3" @click="showMoreArtist" style="font-size:0.7em; float:right; cursor:pointer">더보기∨</a></h2>
          </template>
          <template v-else>
            <h2>아티스트><a v-if="artists.length>3" @click="showMoreArtist" style="font-size:0.7em; float:right; cursor:pointer">접기∧</a></h2>
          </template>
          <b-colxx xxs="12" class="pl-0 pr-0" style="display: inline-flex;">
            <div class="pr-3 pl-3 mb-4 glide__slide" v-for="(artist, index) in artists.slice(0,3)" :key="index"  @click="detailArtist(artist.id)" style="width:33%">
                <b-card class="flex-row" no-body style=" cursor:pointer;">
                    <div class="w-50 position-relative">
                        <img class="card-img-left" :src="artist.img"/>
                        <!-- <b-badge variant="primary" pill class="position-absolute badge-top-left">NEW</b-badge> -->
                    </div>
                    <div class="w-50">
                        <b-card-body>
                            <h3 class="mb-4 card-subtitle" style="font-weight :bold"><br>{{artist.name}}</h3>
                            <h4 class="mb-4 card-subtitle">활동유형: {{artist.type}}</h4>
                            <h4 class="mb-4 card-subtitle" v-if="artist.member">멤버: {{artist.member}}</h4>
                            <h6 class="mb-4 card-subtitle">데뷔: {{artist.debue}}</h6>
                        </b-card-body>
                    </div>
                </b-card>
            </div>
          </b-colxx>
          <template v-if="moreArtist">
            <div v-for="n in parseInt((artists.length-1)/3)" v-bind:key="n">
              <b-colxx xxs="12" class="pl-0 pr-0" style="display: inline-flex;">
                      <div class="pr-3 pl-3 mb-4 glide__slide" v-for="(artist, index) in artists.slice(n*3,(n+1)*3)" v-bind:key="index" @click="detailArtist(artist.id)" style="width:33%">
                          <b-card class="flex-row" no-body style=" cursor:pointer;">
                              <div class="w-50 position-relative">
                                  <img class="card-img-left" :src="artist.img" />
                                  <!-- <b-badge variant="primary" pill class="position-absolute badge-top-left">NEW</b-badge> -->
                              </div>
                              <div class="w-50">
                                  <b-card-body>
                                      <h3 class="mb-4 card-subtitle" style="font-weight :bold"><br>{{artist.name}}</h3>
                                      <h4 class="mb-4 card-subtitle"><a style="font-size:16px;">활동유형: </a>{{artist.type}}</h4>
                                      <h4 class="mb-4 card-subtitle" v-if="artist.member">멤버: {{artist.member}}</h4>
                                      <h6 class="mb-4 card-subtitle">데뷔: {{artist.released}}</h6>
                                  </b-card-body>
                              </div>
                          </b-card>
                      </div>
              </b-colxx>
            </div>
          </template>
          <br><div class="separator mb-5"></div>
        </template>
    </b-colxx>
  </b-row>
  <b-row>
    <b-colxx xxs="12">
      <template v-if="isSong">
        <h2>곡></h2>
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
                    <tr :class="{'flex-row':true}" v-for="(song, index) in sortSongs.slice((currentPage-1)*5,currentPage*5)" v-bind:key="index" style="cursor:pointer;">
                      <td style="width:85px;"><img :src="song.img" class="list-thumbnail responsive border-0" @click="detailSong(song.id)"/></td>
                      <td class="list-item-heading mb-0 truncate" style="vertical-align: middle;" @click="detailSong(song.id)">{{limitString(song.name)}}</td>
                      <td class="list-item-heading mb-0 truncate" style="vertical-align: middle;" @click="detailSong(song.id)"><a v-for="(member, index) in song.artist" v-bind:key="index">{{member.name}} </a></td>
                      <td class="list-item-heading mb-0 truncate" style="vertical-align: middle;" @click="detailSong(song.id)"><a v-for="(genre, index) in song.genres" v-bind:key="index">{{genre.name}}</a>{{song.genre}}</td>
                      <td style="vertical-align: middle;" @click.prevent="addToPlaylistAndPlay(song)"><div class="glyph-icon simple-icon-control-play"/></td>
                      <td style="vertical-align: middle;" @click.prevent="addToPlayList(song)"><div class="glyph-icon simple-icon-playlist"/></td>
                      <!-- <td style="vertical-align: middle;" @click.prevent="likeSong(song.id)" ><div class="glyph-icon simple-icon-heart" /></td> -->
                      <td v-if="!checkLikeSong((currentPage-1)*5+index)" style="vertical-align: middle;" @click="likeSong(song.id, (currentPage-1)*5+index)" ><img src="../../assets/img/heart/heart_empty.png" style="width:32px;"/></td>
                      <td v-if="checkLikeSong((currentPage-1)*5+index)" style="vertical-align: middle;" @click="likeSong(song.id, (currentPage-1)*5+index)" ><img src="../../assets/img/heart/heart_full.png" style="width:32px;"/></td>
                    </tr>
                  </tbody>
              </table>
              <b-pagination-nav
                align="center"
                :link-gen="linkGen"
                :number-of-pages="endPage"
                v-model="currentPage"
              >
                <template v-slot:next-text>
                  <i class="simple-icon-arrow-right"/>
                </template>
                <template v-slot:prev-text>
                  <i class="simple-icon-arrow-left"/>
                </template>
                <template v-slot:first-text>
                  <i class="simple-icon-control-start"/>
                </template>
                <template v-slot:last-text>
                  <i class="simple-icon-control-end"/>
                </template>
              </b-pagination-nav>
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

const youtubeURL = 'https://www.googleapis.com/youtube/v3/search'
const API_KEY = process.env.VUE_APP_YOUTUBE_API_KEY

export default {
  components: {
    LoginModal,
  },

  created() {
    this.keyword = this.$route.params.keyword;
    http.get("/search/song/"+this.keyword+"/")
      .then((rest) => {
        this.songs = rest.data;
        if(this.songs.length!=0){
          this.isSong=true;
          console.log(Math.ceil(this.songs.length/5))
          this.endPage = Math.ceil(this.songs.length/5);
        }else{
          this.dataCheck+=1;
        }
    })
    http.get("/search/artist/"+this.keyword+"/")
      .then((rest) => {
        this.artists = rest.data;
        if(this.artists.length!=0){
          this.isArtist=true;
        }else{
          this.dataCheck+=1;
        }
    })
    http.get("/search/album/"+this.keyword+"/")
      .then((rest) => {
        this.albums = rest.data;
        if(this.albums.length!=0){
          this.isAlbum=true;
        }else{
          this.dataCheck+=1;
        }
    })
  },
  data () {
    return {
      endPage:1,
      currentPage: 1,
      emptyModal: false,
      dataCheck: 0,
      showLogin: false,
      clickAlbumLike: false,
      sort_value : "",
	  	sort_type : 'asc',
      isArtist: false,
      isSong: false,
      isAlbum: false,
      moreArtist: false,
      moreAlbum: false,
      keyword: '',
      songListSize: 5,
      // currentPage: 1,
      artists: [],
      songs: [],
      albums: [],
    }
  },
  methods: {
    showMoreArtist: function() {
      this.moreArtist = !this.moreArtist;
    },
    showMoreAlbum: function() {
      this.moreAlbum = !this.moreAlbum;
    },
    detailArtist: function(id){
      this.$router.push(`${adminRoot}/ArtistDetail/${id}`)
    },
    detailSong: function(id){
      this.$router.push(`${adminRoot}/songDetail/${id}`)
    },
    detailAlbum: function(id){
      if(!this.clickAlbumLike){
        this.$router.push(`${adminRoot}/albumDetail/${id}`)
      }else{
        this.clickAlbumLike=false;
      }

    },
    async addToPlaylistAndPlay(song) {
      const { data } = await http.get(youtubeURL, {
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
      song['src'] = videoId
      this.playlist.unshift(song)
      this.$store.state.playerControl = 'add'
      this.$notify('primary', "재생 중인 곡", song.name+" - "+song.artist[0].name, { duration: 5000, permanent: false })
    },
    async addToPlayList(song) {
      const { data } = await http.get(youtubeURL, {
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
      song['src'] = videoId
      this.playlist.push(song)
      this.$notify('primary', "재생 목록에 추가 었습니다.", song.name+" - "+song.artist[0].name, { duration: 5000, permanent: false })
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
            this.$notify('primary', "♥ 좋아요", this.albums[index].name, { duration: 5000, permanent: false });
          }else{
            for(var i=0;i<this.albums[index].user_like.length;i++){
              if(this.albums[index].user_like[i].id==this.user.id){
                this.albums[index].user_like.splice(i, 1);
                this.$notify('primary', "♡ 좋아요 취소", this.albums[index].name, { duration: 5000, permanent: false });
                break;
              }
            }
          }
      })
      }else{
        this.showLogin=true;
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
    toMain(){
      this.$router.push(`${adminRoot}/main`);
    },
    linkGen (pageNum) {
      return '#';
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
          if( a.artist[0].name > b.artist[0].name) return 1;
          else if ( a.artist[0].name < b.artist[0].name ) return -1;
          else return 0;
        })
        }else if(this.sort_type=='desc'){
          return this.songs.sort((a, b) => {
            if( a.artist[0].name < b.artist[0].name) return 1;
            else if ( a.artist[0].name > b.artist[0].name ) return -1;
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
  watch : {
    dataCheck: function(){
      if(this.dataCheck==3){
        this.emptyModal = true;
      }
    },
  },
}
</script>
