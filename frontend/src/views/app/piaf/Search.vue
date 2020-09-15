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
          <h2>아티스트><a href="#" v-if="artists.length==3" style="font-size:0.7em; float:right">더보기</a></h2>
          <b-colxx xxs="12" class="mb-4 pl-0 pr-0" style="display: inline-flex;">
                  <div class="pr-3 pl-3 mb-4 glide__slide" v-for="(artist, index) in artists" v-bind:key="index" style="width:30%">
                      <b-card class="flex-row" no-body>
                          <div class="w-50 position-relative">
                              <img class="card-img-left" :src="artist.img" alt="Card cap" style="height:100%"/>
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
        <h2>곡><a href="#" v-if="albums.length==10" style="font-size:0.7em; float:right">더보기</a></h2>
        <b-card  :class="{'d-flex flex-row':true}" no-body v-for="(song, index) in songs" v-bind:key="index">
          <img :src="song.img" class="list-thumbnail responsive border-0"/>
          <div class="pl-2 d-flex flex-grow-1 min-width-zero">
              <div class="card-body align-self-center d-flex flex-column flex-lg-row justify-content-between min-width-zero align-items-lg-center">
                  <p class="list-item-heading mb-0 truncate">{{song.name}}</p>
                  <p class="mb-0 text-muted text-small w-15 w-sm-100">{{song.artist}}</p>
                  <p class="mb-0 text-muted text-small w-15 w-sm-100">{{song.genre}}</p>
                  <div class="separator mb-5"></div>
              </div>
          </div>
        </b-card>
        <br><div class="separator mb-5"></div>
      </template>
    </b-colxx>
  </b-row>
  <b-row>
    <template v-if="isAlbum">
        <h2>앨범><a href="#" v-if="albums.length==6" style="font-size:0.7em; float:right">더보기</a></h2>
        <b-colxx xxs="12" class="mb-4 pl-0 pr-0" style="display: inline-flex;">
            <b-card @click.prevent="toggleItem($event,data.id)" no-body v-for="(album, index) in albums" v-bind:key="index" style="width:15%;margin-right:3%;">
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
        <template v-else>
          <div class="loading"></div>
        </template>
    
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
      keyword: '선물',
      // currentPage: 1,
      currentPage: 1,
      totalPage: 1,
      page: 1,
      perPage: 4,
      lastPage: 5,
      artists: [{ id: 1, name: '멜로망스', released: '2015.03.10', type: '그룹', img: 'https://cdnimg.melon.co.kr/cm2/artistcrop/images/008/39/732/839732_500.jpg?bfce7f999e6fa8e6d45e1b329a2eeb6f/melon/resize/416/quality/80/optimize'},
      { id: 1, name: '멜로망스1', released: '2015.03.10', type: '그룹', img: 'https://cdnimg.melon.co.kr/cm2/artistcrop/images/008/39/732/839732_500.jpg?bfce7f999e6fa8e6d45e1b329a2eeb6f/melon/resize/416/quality/80/optimize'},
      { id: 1, name: '멜로망스2', released: '2015.03.10', type: '그룹', img: 'https://cdnimg.melon.co.kr/cm2/artistcrop/images/008/39/732/839732_500.jpg?bfce7f999e6fa8e6d45e1b329a2eeb6f/melon/resize/416/quality/80/optimize'},],
      songs: [{ id: 1, name: '선물', artist: '멜로망스', genre: '발라드', img: 'https://cdnimg.melon.co.kr/cm/album/images/100/78/176/10078176_500.jpg?fc3fe8c6bd74c16bce7ffd971a930ffa/melon/resize/282/quality/80/optimize'},
      { id: 1, name: '선물1', artist: '멜로망스', genre: '발라드', img: 'https://cdnimg.melon.co.kr/cm/album/images/100/78/176/10078176_500.jpg?fc3fe8c6bd74c16bce7ffd971a930ffa/melon/resize/282/quality/80/optimize'},
      { id: 1, name: '선물2', artist: '멜로망스', genre: '발라드', img: 'https://cdnimg.melon.co.kr/cm/album/images/100/78/176/10078176_500.jpg?fc3fe8c6bd74c16bce7ffd971a930ffa/melon/resize/282/quality/80/optimize'},
      { id: 1, name: '선물3', artist: '멜로망스', genre: '발라드', img: 'https://cdnimg.melon.co.kr/cm/album/images/100/78/176/10078176_500.jpg?fc3fe8c6bd74c16bce7ffd971a930ffa/melon/resize/282/quality/80/optimize'},
      { id: 1, name: '선물4', artist: '멜로망스', genre: '발라드', img: 'https://cdnimg.melon.co.kr/cm/album/images/100/78/176/10078176_500.jpg?fc3fe8c6bd74c16bce7ffd971a930ffa/melon/resize/282/quality/80/optimize'},
      { id: 1, name: '선물5', artist: '멜로망스', genre: '발라드', img: 'https://cdnimg.melon.co.kr/cm/album/images/100/78/176/10078176_500.jpg?fc3fe8c6bd74c16bce7ffd971a930ffa/melon/resize/282/quality/80/optimize'},],
      albums: [{ id:1, name:"축제", img: "https://cdnimg.melon.co.kr/cm2/album/images/103/48/325/10348325_500.jpg?679a781c2d3687f2aefffaeb310614d5/melon/resize/282/quality/80/optimize", genre:"발라드, 인디음악", artist:"멜로망스"},
      { id:1, name:"축제1", img: "https://cdnimg.melon.co.kr/cm2/album/images/103/48/325/10348325_500.jpg?679a781c2d3687f2aefffaeb310614d5/melon/resize/282/quality/80/optimize", genre:"발라드, 인디음악", artist:"멜로망스"},
      { id:1, name:"축제2", img: "https://cdnimg.melon.co.kr/cm2/album/images/103/48/325/10348325_500.jpg?679a781c2d3687f2aefffaeb310614d5/melon/resize/282/quality/80/optimize", genre:"발라드, 인디음악", artist:"멜로망스"},],
    }
  },
  methods: {
    loadItems() {
        this.isAlbum = false;

        this.total = 6;
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
    changePageSize(perPage) {
      this.page = 1;
      this.perPage = perPage;
    },
    changePage(pageNum) {
      this.page = pageNum;
    }
  },
  mounted() {
    this.loadItems();
  }

}
</script>
