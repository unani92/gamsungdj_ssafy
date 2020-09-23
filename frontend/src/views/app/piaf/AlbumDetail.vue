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
                  <h1 class="mb-0 truncate text-large"><router-link :to="'/app/piaf/artistDetail/'+album.artist[0].id" class="text-primary">{{album.artist[0].name}}</router-link></h1><br>
                  <h3 class="mb-0 truncate " style="display: inline-flex;">장르:<h3 class="ml-1" v-for="(genre, index) in album.genres" v-bind:key="index"> {{genre.name}}</h3></h3><br>
                  <h3 class="mb-0 truncate">발매일: {{album.released_date}}</h3><br>
                  <h1 class="mb-0 truncate glyph-icon simple-icon-heart mt-5 text-large"> {{album.like}}</h1>
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
                    <tr :class="{'flex-row':true}" v-for="(song, index) in sortSongs.slice(0,songListSize)" v-bind:key="index" style="cursor:pointer;">
                      <td style="width:85px;"><img :src="album.img" class="list-thumbnail responsive border-0" @click="detailSong(song.id)"/></td>
                      <td class="list-item-heading mb-0 truncate" style="vertical-align: middle;" @click="detailSong(song.id)">{{song}}</td>
                      <td class="list-item-heading mb-0 truncate" style="vertical-align: middle;" @click="detailSong(song.id)">{{song.artist}}</td>
                      <td class="list-item-heading mb-0 truncate" style="vertical-align: middle;" @click="detailSong(song.id)">{{song.genre}}</td>
                      <td style="vertical-align: middle;" @click.prevent="playSong(song.id)"><div class="glyph-icon simple-icon-control-play"/></td>
                      <td style="vertical-align: middle;" @click.prevent="addSong(song.id)"><div class="glyph-icon simple-icon-playlist"/></td>
                      <td style="vertical-align: middle;" @click.prevent="likeSong(song.id)" ><div class="glyph-icon simple-icon-heart" /></td>
                      <!-- <td class="like" style="vertical-align: middle;" @click.prevent="likeSong(song.id)" ><img src="../../../assets/img/heart/heart_empty.png" style="width:32px;"/></td>
                      <td class="like" style="vertical-align: middle;" @click.prevent="likeSong(song.id)" ><img src="../../../assets/img/heart/heart_full.png" style="width:32px;"/></td> -->
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
  </div>
</template>
<script>
import http from "../../../utils/http-common";
export default {
  
  components: {
  },
  created() {
    this.albumID = this.$route.params.albumID;
    http
      .get("/album/"+this.albumID)
      .then((rest) => {
        this.album = rest.data;
        this.album.released_date = rest.data.released_date.substr(0,4) + "-" + rest.data.released_date.substr(4,2) + "-" + rest.data.released_date.substr(6,2);
        this.songs = rest.data.songs.split(",");
      })
  },
  data () {
    return {
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
      this.$router.push('/app/piaf/songDetail/'+id)
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
			return a.id - b.id
		})

    },
  }

}
</script>
