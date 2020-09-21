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
                            <h4 class="mb-4 card-subtitle"><a style="font-size:16px;">활동유형: </a>{{artist.type}}</h4>
                            <h6 class="mb-4 card-subtitle">데뷔: {{artist.released}}</h6>
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
        <template v-else>
          <div class="loading"></div>
        </template>
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
                    <th>곡</th>
                    <th>가수</th>
                    <th>장르</th>
                    <th>재생</th>
                    <th>추가</th>
                    <th>상세정보</th>
                    <th>좋아요</th>
                  </thead>
                  <tbody style="font-size: x-large;">
                    <tr :class="{'flex-row':true}" v-for="(song, index) in songs.slice(0,songListSize)" v-bind:key="index">
                      <td style="width:85px;"><img :src="song.img" class="list-thumbnail responsive border-0" /></td>
                      <td class="list-item-heading mb-0 truncate" style="vertical-align: middle;">{{song.name}}</td>
                      <td class="list-item-heading mb-0 truncate" style="vertical-align: middle;">{{song.artist}}</td>
                      <td class="list-item-heading mb-0 truncate" style="vertical-align: middle;">{{song.genre}}</td>
                      <td style="vertical-align: middle;"><div class="glyph-icon simple-icon-control-play"/></td>
                      <td style="vertical-align: middle;"><div class="glyph-icon simple-icon-playlist"/></td>
                      <td style="vertical-align: middle;"><div class="glyph-icon simple-icon-magnifier-add" @click="detailSong(song.id)" style="cursor:pointer;"/></td>
                      <td style="vertical-align: middle;"><div class="glyph-icon simple-icon-heart"/></td>
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
            <h2>앨범><a v-if="albums.length>5" @click="showMoreAlbum" style="font-size:0.7em; float:right  cursor:pointer">접기∧</a></h2>
          </template>
          <!-- <b-colxx xxs="12" class="pl-0 pr-0" style="display: inline-flex;">
            <div class="pr-3 pl-3 mb-4 glide__slide" v-for="(artist, index) in artists.slice(0,3)" :key="index"  @click="detailArtist(artist.id)" style="width:33%">
                <b-card class="flex-row" no-body style=" cursor:pointer;">
                    <div class="w-50 position-relative">
                        <img class="card-img-left" :src="artist.img"/>
                    </div>
                    <div class="w-50">
                        <b-card-body>
                            <h3 class="mb-4 card-subtitle" style="font-weight :bold"><br>{{artist.name}}</h3>
                            <h4 class="mb-4 card-subtitle"><a style="font-size:16px;">활동유형: </a>{{artist.type}}</h4>
                            <h6 class="mb-4 card-subtitle">데뷔: {{artist.released}}</h6>
                        </b-card-body>
                    </div>
                </b-card>
            </div>
          </b-colxx> -->
            <b-colxx xxs="12" class="mb-4 pl-0 pr-3" style="display: inline-flex;">
                <b-card class="mr-3 ml-3" no-body v-for="(album, index) in albums.slice(0,5)" v-bind:key="index" style="width:18%; cursor:pointer;" @click="detailAlbum(album.id)">
                    <div class="position-relative">
                        <img :src="album.img" class="card-img-top"/>
                    </div>
                    <b-card-body>
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
                    <b-card-body>
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
      isAlbum: false,
      moreArtist: false,
      moreSong: false,
      moreAlbum: false,
      keyword: '',
      songListSize: 5,
      // currentPage: 1,
      artists: [{ id: 1, name: '멜로망스', released: '2015.03.10', type: '그룹', img: 'https://cdnimg.melon.co.kr/cm2/artistcrop/images/008/39/732/839732_500.jpg?bfce7f999e6fa8e6d45e1b329a2eeb6f/melon/resize/416/quality/80/optimize'},
      { id: 1, name: '멜로망스', released: '2015.03.10', type: '그룹', img: 'https://cdnimg.melon.co.kr/cm2/artistcrop/images/008/39/732/839732_500.jpg?bfce7f999e6fa8e6d45e1b329a2eeb6f/melon/resize/416/quality/80/optimize'},
      { id: 1, name: '멜로망스', released: '2015.03.10', type: '그룹', img: 'https://cdnimg.melon.co.kr/cm2/artistcrop/images/008/39/732/839732_500.jpg?bfce7f999e6fa8e6d45e1b329a2eeb6f/melon/resize/416/quality/80/optimize'},
      { id: 1, name: '멜로망스', released: '2015.03.10', type: '그룹', img: 'https://cdnimg.melon.co.kr/cm2/artistcrop/images/008/39/732/839732_500.jpg?bfce7f999e6fa8e6d45e1b329a2eeb6f/melon/resize/416/quality/80/optimize'},
      { id: 1, name: '멜로망스', released: '2015.03.10', type: '그룹', img: 'https://cdnimg.melon.co.kr/cm2/artistcrop/images/008/39/732/839732_500.jpg?bfce7f999e6fa8e6d45e1b329a2eeb6f/melon/resize/416/quality/80/optimize'},],
      songs: [{ id: 1, name: '선물', artist: '멜로망스', genre: '발라드', img: 'https://cdnimg.melon.co.kr/cm/album/images/100/78/176/10078176_500.jpg?fc3fe8c6bd74c16bce7ffd971a930ffa/melon/resize/282/quality/80/optimize'},
      { id: 1, name: '인사', artist: '멜로망스', genre: '발라드', img: 'https://cdnimg.melon.co.kr/cm/album/images/103/05/070/10305070_500.jpg?8e4dafd3e69b879fdeb5f6d5e8e6cdda/melon/sharpen/0x1'},
      { id: 1, name: '유리', artist: '멜로망스', genre: '발라드', img: 'https://cdnimg.melon.co.kr/cm/album/images/102/27/379/10227379_500.jpg?bb36e84e0109f6b0253b72688988233d/melon/quality/80/optimize'},
      { id: 1, name: 'Page 0', artist: '멜로망스', genre: '발라드', img: 'https://cdnimg.melon.co.kr/cm/album/images/101/93/505/10193505_500.jpg?cf087eb8878fbec43435f3ba84e307e5/melon/quality/80/optimize'},
      { id: 1, name: '좋은 날', artist: '멜로망스', genre: '발라드', img: 'https://cdnimg.melon.co.kr/cm/album/images/101/91/294/10191294_500.jpg?ceb46dcf7679dd7c58e2941eb93bc624/melon/quality/80/optimize'},
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
      { id:1, name:"축제8", img: "https://cdnimg.melon.co.kr/cm2/album/images/103/48/325/10348325_500.jpg?679a781c2d3687f2aefffaeb310614d5/melon/resize/282/quality/80/optimize", genre:"발라드, 인디음악", artist:"멜로망스"},],
    }
  },
  methods: {
    loadItems() {
        this.isAlbum = false;
        this.isAlbum = true;
    //   axios
    //     .get(this.apiUrl)
    //     .then(response => {
    //       return response.data;
    //     })
    //     .then(res => {
    //       this.total = res.total;
    //       this.from = res.from;
    //       this.to = res.to;
    //       this.items = res.data.map(x => {
    //         return {
    //           ...x,
    //           img: x.img.replace("/img/", "/img/products/")
    //         };
    //       });
    //       this.perPage = res.per_page;
    //       this.selectedItems = [];
    //       this.lastPage = res.last_page;
    //       this.isLoad = true;
    //     });
    },
    showMoreArtist: function() {
      this.moreArtist = !this.moreArtist;
    },
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
    detailArtist: function(id){
      this.$router.push('/app/piaf/ArtistDetail/'+id)
    },
    detailSong: function(id){
      this.$router.push('/app/piaf/songDetail/'+id)
    },
    detailAlbum: function(id){
      this.$router.push('/app/piaf/albumDetail/'+id)
    },
  },
  mounted() {
    this.loadItems();
    this.keyword = this.$route.params.keyword;
  },

}
</script>
