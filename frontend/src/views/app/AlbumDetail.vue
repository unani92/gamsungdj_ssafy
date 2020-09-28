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
                  <h1 class="mb-0 truncate text-large"><a v-for="(singer, index) in album.artist" v-bind:key="index"><router-link :to="'/A505/artistDetail/'+singer.id" class="text-primary">{{singer.name}}</router-link></a></h1><br>
                  <h3 class="mb-0 truncate " style="display: inline-flex;">장르:<h3 class="ml-1" v-for="(genre, index) in album.genres" v-bind:key="index"> {{genre.name}}</h3></h3><br>
                  <h3 class="mb-0 truncate">발매일: {{album.released_date}}</h3><br>
<<<<<<< HEAD:frontend/src/views/app/piaf/AlbumDetail.vue
                  <h1 v-if="!checkLikeAlbum(album.id)"><img src="../../assets/img/heart/heart_empty.png" style="width:32px; cursor:pointer;" @click="likeAlbum(album.id)"/> {{likeCount}}</h1>
                  <h1 v-if="checkLikeAlbum(album.id)"><img src="../../assets/img/heart/heart_full.png" style="width:32px; cursor:pointer;" @click="likeAlbum(album.id)"/> {{likeCount}}</h1>
=======
                  <h1 v-if="!checkLikeAlbum(album.id)"><img src="../../assets/img/heart/heart_empty.png" style="width:32px; cursor:pointer;" @click="likeAlbum(album.id)"/> {{album.like}}</h1>
                  <h1 v-if="checkLikeAlbum(album.id)"><img src="../../assets/img/heart/heart_full.png" style="width:32px; cursor:pointer;" @click="likeAlbum(album.id)"/> {{album.like}}</h1>
>>>>>>> 1638777662c43961ef9c8ff15b3ea2e14b547380:frontend/src/views/app/AlbumDetail.vue
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
                      <td style="vertical-align: middle;" @click.prevent="playSong(song.id)"><div class="glyph-icon simple-icon-control-play"/></td>
                      <td style="vertical-align: middle;" @click.prevent="addSong(song.id)"><div class="glyph-icon simple-icon-playlist"/></td>
                      <td v-if="!checkLikeSong(song.id)" style="vertical-align: middle;" @click="likeSong(song.id)" ><img src="../../assets/img/heart/heart_empty.png" style="width:32px;"/></td>
                      <td v-if="checkLikeSong(song.id)" style="vertical-align: middle;" @click="likeSong(song.id)" ><img src="../../assets/img/heart/heart_full.png" style="width:32px;"/></td>
                    </tr>
                    <tr v-show="!song.id" :class="{'flex-row':true}" v-for="(song, index) in sortSongs.slice(0,songListSize)" v-bind:key="index" class="card-img-overlay" style="position: relative">
                      <td style="width:85px;opacity:0.5;"><img :src="album.img" class="list-thumbnail responsive border-0" @click="detailSong(song.id)"/></td>
                      <td class="list-item-heading mb-0 truncate" style="vertical-align: middle;;opacity:0.5;" @click="detailSong(song.id)">{{song.name}}</td>
                      <td colspan="2" style="vertical-align: middle;">서비스를 준비중입니다.</td>
                      <td></td>
                      <td></td>
                      <td></td>
                      <!-- <td class="like" style="vertical-align: middle;" @click.prevent="likeSong(song.id)" ><img src="../../assets/img/heart/heart_empty.png" style="width:32px;"/></td>
                      <td class="like" style="vertical-align: middle;" @click.prevent="likeSong(song.id)" ><img src="../../assets/img/heart/heart_full.png" style="width:32px;"/></td> -->
                    </tr>
                  </tbody>
              </table>
            </b-card>
          </b-colxx>
        </b-colxx>
        <br><div class="separator mb-5"></div>
        </template>
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
  },
  data () {
    return {
      likeCount:0,
      showLogin: false,
      sort_value : "",
	  	sort_type : 'asc',
      isSong: true,
      moreSong: false,
      songListSize: 5,
      albumID: 0,
      dummy_album: { id:1, name:"축제", artistId:1, img: "https://cdnimg.melon.co.kr/cm2/album/images/103/48/325/10348325_500.jpg?679a781c2d3687f2aefffaeb310614d5/melon/resize/282/quality/80/optimize", genre:"발라드, 인디음악", artist:"멜로망스"},
      songs: [],
      album:[],
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
    checkLikeAlbum(albumID){
       if(this.user.like_albums){
         for(var i=0;i<this.user.like_albums.length;i++){
          if(this.user.like_albums[i]==albumID){
            return true;
          }
        }
        return false;
       }
      return false;
    },
    likeAlbum: function(id) {
      console.log(this.$store.state.authorization)
      if(this.user.like_albums){
        http.post(`album/${id}/like/`,'',{
          headers: {
            Authorization: this.$store.state.authorization
          },
        })
        .then((rest) => {
          console.log(rest.data)
          if(rest.data.liked){
            this.likeCount+=1;
            this.user.like_albums.push(id);
          }else{
            for(var i=0;i<this.user.like_albums.length;i++){
              if(this.user.like_albums[i]==id){
                this.likeCount-=1;
                this.user.like_albums.splice(i, 1);
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
    ...mapState(['authorization', 'user', 'isLoggedin'])
  },

}
</script>
