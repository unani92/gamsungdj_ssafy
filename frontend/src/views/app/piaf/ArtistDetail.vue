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
          <b-colxx xxs="12" class="mb-4 pl-3 pr-3">
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
                      <td class="list-item-heading mb-0 truncate" style="vertical-align: middle;" @click="detailSong(song.id)">{{song.name}}</td>
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
  </b-row>
  <b-row>
    <b-colxx xxs="12">
      <template v-if="isAlbum">
        <template v-if="!moreAlbum">
            <h2>앨범><a v-if="albums.length>5" @click="showMoreAlbum" style="font-size:0.7em; float:right; cursor:pointer">더보기∨</a></h2>
          </template>
          <template v-else>
            <h2>앨범><a v-if="albums.length>5" @click="showMoreAlbum" style="font-size:0.7em; float:right">접기∧</a></h2>
          </template>
          <b-colxx xxs="12" class="pl-0 pr-0">
            <b-colxx xxs="12" class="mb-4 pl-0 pr-3" style="display: inline-flex;">
                <b-card class="mr-3 ml-3" no-body v-for="(album, index) in albums.slice(0,5)" v-bind:key="index" style="width:18%; cursor:pointer;" @click="detailAlbum(album.id)">
                    <div class="position-relative">
                        <img :src="album.img" class="card-img-top"/>
                    </div>
                    <b-card-body style="padding: 1rem;">
                        <b-row>
                            <b-colxx xxs="10" class="mb-3">
                                <h4 style="font-weight :bold">{{album.name}}</h4>
                                <h5>{{album.artist}}</h5>
                                <h6>장르: {{album.genre}}</h6>
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
                    <b-card-body style="padding: 1rem;">
                        <b-row>
                            <b-colxx xxs="10" class="mb-3">
                                <h4 style="font-weight :bold">{{album.name}}</h4>
                                <h5>{{album.artist}}</h5>
                                <h6>장르: {{album.genre}}</h6>
                            </b-colxx>
                        </b-row>
                    </b-card-body>
                  </b-card>
                </b-colxx>
             </template>
          </b-colxx>
          </template>
        <template v-else>
          <div class="loading"></div>
        </template>
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
    this.artistID = this.$route.params.artistID;
    http
      .get("/artist/"+this.artistID)
      .then((rest) => {
        this.artist = rest.data;
      })
  },
  data () {
    return {
      sort_value : "",
	  	sort_type : 'asc',
      isArtist: true,
      isSong: true,
      isAlbum: true,
      moreSong: false,
      moreAlbum: false,

      songListSize: 5,
      // currentPage: 1,
      artistID: 0,
      artist: {},
      songs: [{ id: 1, name: '선물', artist: '멜로망스', genre: '발라드', img: 'https://cdnimg.melon.co.kr/cm/album/images/100/78/176/10078176_500.jpg?fc3fe8c6bd74c16bce7ffd971a930ffa/melon/resize/282/quality/80/optimize'},
      { id: 1, name: '선물1', artist: '멜로망스', genre: '발라드', img: 'https://cdnimg.melon.co.kr/cm/album/images/100/78/176/10078176_500.jpg?fc3fe8c6bd74c16bce7ffd971a930ffa/melon/resize/282/quality/80/optimize'},
      { id: 1, name: '선물2', artist: '멜로망스', genre: '발라드', img: 'https://cdnimg.melon.co.kr/cm/album/images/100/78/176/10078176_500.jpg?fc3fe8c6bd74c16bce7ffd971a930ffa/melon/resize/282/quality/80/optimize'},
      { id: 1, name: '선물3', artist: '멜로망스', genre: '발라드', img: 'https://cdnimg.melon.co.kr/cm/album/images/100/78/176/10078176_500.jpg?fc3fe8c6bd74c16bce7ffd971a930ffa/melon/resize/282/quality/80/optimize'},
      { id: 1, name: '선물4', artist: '멜로망스', genre: '발라드', img: 'https://cdnimg.melon.co.kr/cm/album/images/100/78/176/10078176_500.jpg?fc3fe8c6bd74c16bce7ffd971a930ffa/melon/resize/282/quality/80/optimize'},
      { id: 1, name: '선물5', artist: '멜로망스', genre: '발라드', img: 'https://cdnimg.melon.co.kr/cm/album/images/100/78/176/10078176_500.jpg?fc3fe8c6bd74c16bce7ffd971a930ffa/melon/resize/282/quality/80/optimize'},
      { id: 1, name: '선물6', artist: '멜로망스', genre: '발라드', img: 'https://cdnimg.melon.co.kr/cm/album/images/100/78/176/10078176_500.jpg?fc3fe8c6bd74c16bce7ffd971a930ffa/melon/resize/282/quality/80/optimize'},
      { id: 1, name: '선물7', artist: '멜로망스', genre: '발라드', img: 'https://cdnimg.melon.co.kr/cm/album/images/100/78/176/10078176_500.jpg?fc3fe8c6bd74c16bce7ffd971a930ffa/melon/resize/282/quality/80/optimize'},
      { id: 1, name: '선물8', artist: '멜로망스', genre: '발라드', img: 'https://cdnimg.melon.co.kr/cm/album/images/100/78/176/10078176_500.jpg?fc3fe8c6bd74c16bce7ffd971a930ffa/melon/resize/282/quality/80/optimize'},
      { id: 1, name: '선물9', artist: '멜로망스', genre: '발라드', img: 'https://cdnimg.melon.co.kr/cm/album/images/100/78/176/10078176_500.jpg?fc3fe8c6bd74c16bce7ffd971a930ffa/melon/resize/282/quality/80/optimize'},
      { id: 1, name: '선물10', artist: '멜로망스', genre: '발라드', img: 'https://cdnimg.melon.co.kr/cm/album/images/100/78/176/10078176_500.jpg?fc3fe8c6bd74c16bce7ffd971a930ffa/melon/resize/282/quality/80/optimize'},
      { id: 1, name: '선물11', artist: '멜로망스', genre: '발라드', img: 'https://cdnimg.melon.co.kr/cm/album/images/100/78/176/10078176_500.jpg?fc3fe8c6bd74c16bce7ffd971a930ffa/melon/resize/282/quality/80/optimize'},
      { id: 1, name: '선물12', artist: '멜로망스', genre: '발라드', img: 'https://cdnimg.melon.co.kr/cm/album/images/100/78/176/10078176_500.jpg?fc3fe8c6bd74c16bce7ffd971a930ffa/melon/resize/282/quality/80/optimize'},
      { id: 1, name: '선물13', artist: '멜로망스', genre: '발라드', img: 'https://cdnimg.melon.co.kr/cm/album/images/100/78/176/10078176_500.jpg?fc3fe8c6bd74c16bce7ffd971a930ffa/melon/resize/282/quality/80/optimize'},
      { id: 1, name: '선물14', artist: '멜로망스', genre: '발라드', img: 'https://cdnimg.melon.co.kr/cm/album/images/100/78/176/10078176_500.jpg?fc3fe8c6bd74c16bce7ffd971a930ffa/melon/resize/282/quality/80/optimize'},],
      albums: [{ id:1, name:"축제", img: "https://cdnimg.melon.co.kr/cm2/album/images/103/48/325/10348325_500.jpg?679a781c2d3687f2aefffaeb310614d5/melon/resize/282/quality/80/optimize", genre:"발라드, 인디음악", artist:"멜로망스"},
      { id:1, name:"인사", img: "https://cdnimg.melon.co.kr/cm/album/images/103/05/070/10305070_500.jpg?8e4dafd3e69b879fdeb5f6d5e8e6cdda/melon/sharpen/0x1", genre:"발라드, 인디음악", artist:"멜로망스"},
      { id:1, name:"WHY : 당신이 연인에게 차인 진짜 이유 OST - Part.2", img: "https://cdnimg.melon.co.kr/cm/album/images/102/27/379/10227379_500.jpg?bb36e84e0109f6b0253b72688988233d/melon/quality/80/optimize", genre:"발라드, 인디음악", artist:"멜로망스"},
      { id:1, name:"Page 0", img: "https://cdnimg.melon.co.kr/cm/album/images/101/93/505/10193505_500.jpg?cf087eb8878fbec43435f3ba84e307e5/melon/quality/80/optimize", genre:"발라드, 인디음악", artist:"멜로망스"},
      { id:1, name:"미스터 션샤인 OST Part.5", img: "https://cdnimg.melon.co.kr/cm/album/images/101/91/294/10191294_500.jpg?ceb46dcf7679dd7c58e2941eb93bc624/melon/quality/80/optimize", genre:"발라드, 인디음악", artist:"멜로망스"},
      { id:1, name:"축제5", img: "https://cdnimg.melon.co.kr/cm2/album/images/103/48/325/10348325_500.jpg?679a781c2d3687f2aefffaeb310614d5/melon/resize/282/quality/80/optimize", genre:"발라드, 인디음악", artist:"멜로망스"},
      { id:1, name:"축제6", img: "https://cdnimg.melon.co.kr/cm2/album/images/103/48/325/10348325_500.jpg?679a781c2d3687f2aefffaeb310614d5/melon/resize/282/quality/80/optimize", genre:"발라드, 인디음악", artist:"멜로망스"},
      { id:1, name:"축제7", img: "https://cdnimg.melon.co.kr/cm2/album/images/103/48/325/10348325_500.jpg?679a781c2d3687f2aefffaeb310614d5/melon/resize/282/quality/80/optimize", genre:"발라드, 인디음악", artist:"멜로망스"},
      { id:1, name:"축제8", img: "https://cdnimg.melon.co.kr/cm2/album/images/103/48/325/10348325_500.jpg?679a781c2d3687f2aefffaeb310614d5/melon/resize/282/quality/80/optimize", genre:"발라드, 인디음악", artist:"멜로망스"},
      { id:1, name:"축제9", img: "https://cdnimg.melon.co.kr/cm2/album/images/103/48/325/10348325_500.jpg?679a781c2d3687f2aefffaeb310614d5/melon/resize/282/quality/80/optimize", genre:"발라드, 인디음악", artist:"멜로망스"},
      { id:1, name:"축제9", img: "https://cdnimg.melon.co.kr/cm2/album/images/103/48/325/10348325_500.jpg?679a781c2d3687f2aefffaeb310614d5/melon/resize/282/quality/80/optimize", genre:"발라드, 인디음악", artist:"멜로망스"},],
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
      this.$router.push('/app/piaf/songDetail/'+id)
    },
    detailAlbum: function(id){
      this.$router.push('/app/piaf/albumDetail/'+id)
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
