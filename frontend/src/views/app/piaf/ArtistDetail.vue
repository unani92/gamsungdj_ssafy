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
                  <h3 class="mb-0 truncate">데뷔: {{artist.released}}</h3><br>
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
        <b-colxx xxs="12" class="mb-4 pl-3 pr-3">
          <b-card  :class="{'d-flex flex-row':true}" no-body v-for="(song, index) in songs.slice(0,5)" v-bind:key="index">
            <img :src="song.img" class="list-thumbnail responsive border-0"/>
            <div class="pl-2 d-flex flex-grow-1 min-width-zero">
                <div class="card-body align-self-center d-flex flex-column flex-lg-row justify-content-between min-width-zero align-items-lg-center">
                    <p class="list-item-heading mb-0 truncate">{{song.name}}</p>
                    <p class="mb-0 text-muted text-small w-15 w-sm-100">{{song.artist}}</p>
                    <p class="mb-0 text-muted text-small w-15 w-sm-100">{{song.genre}}</p>
                    <div class="glyph-icon simple-icon-control-play"/>
                    <div class="glyph-icon simple-icon-playlist"/>
                    <div class="glyph-icon simple-icon-magnifier-add" @click="detailSong(song.id)" style="cursor:pointer;"/>
                    <div class="glyph-icon simple-icon-heart"/>
                    <div class="separator mb-5"></div>
                </div>
            </div>
          </b-card>
          <template v-if="moreSong">
            <b-card  :class="{'d-flex flex-row':true}" no-body v-for="(song, index) in songs.slice(5,songs.length)" v-bind:key="index">
              <img :src="song.img" class="list-thumbnail responsive border-0"/>
              <div class="pl-2 d-flex flex-grow-1 min-width-zero">
                  <div class="card-body align-self-center d-flex flex-column flex-lg-row justify-content-between min-width-zero align-items-lg-center">
                      <p class="list-item-heading mb-0 truncate">{{song.name}}</p>
                      <p class="mb-0 text-muted text-small w-15 w-sm-100">{{song.artist}}</p>
                      <p class="mb-0 text-muted text-small w-15 w-sm-100">{{song.genre}}</p>
                      <div class="glyph-icon simple-icon-control-play"/>
                      <div class="glyph-icon simple-icon-playlist"/>
                      <div class="glyph-icon simple-icon-magnifier-add" @click="detailSong(song.id)" style="cursor:pointer;"/>
                      <div class="glyph-icon simple-icon-heart"/>
                      
                      <div class="separator mb-5"></div>
                  </div>
              </div>
            </b-card>
          </template>
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
            <b-colxx xxs="12" class="mb-4 pl-0 pr-0" style="display: inline-flex;">
                <b-card class="mr-3 ml-3" no-body v-for="(album, index) in albums.slice(0,5)" v-bind:key="index" style="width:20%; cursor:pointer;" @click="detailAlbum(album.id)">
                    <div class="position-relative">
                        <img :src="album.img" class="card-img-top" style="width:100%;height:100%"/>
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
                <b-colxx xxs="12" class="mb-4 pl-0 pr-0" style="display: inline-flex;" v-for="n in parseInt((albums.length-1)/5)" v-bind:key="n">
                  <b-card class="mr-3 ml-3" no-body v-for="(album, index) in albums.slice(n*5,(n+1)*5)" v-bind:key="index" style="width:20%; cursor:pointer;" @click="detailAlbum(album.id)">
                    <div class="position-relative">
                      <img :src="album.img" class="card-img-top" style="width:100%;height:100%"/>
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

export default {
  components: {
  },

  data () {
    return {
      isArtist: true,
      isSong: true,
      isAlbum: true,
      moreSong: false,
      moreAlbum: false,
      keyword: '',
      // currentPage: 1,
      artistID: 0,
      artist: { id: 1, name: '멜로망스', released: '2015.03.10', type: '그룹', img: 'https://cdnimg.melon.co.kr/cm2/artistcrop/images/008/39/732/839732_500.jpg?bfce7f999e6fa8e6d45e1b329a2eeb6f/melon/resize/416/quality/80/optimize'},
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
  },
  mounted() {
    this.artistID = this.$route.params.artistID;
  },

}
</script>
