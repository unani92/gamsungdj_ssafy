<template>
  <b-row>
    <b-colxx xxs="12">
      	<b-colxx xxs="12" class="mb-5 mt-5">
    		<div class="d-flex flex-row ">
				<img src="/assets/img/profiles/l-1.jpg" alt="thumbnail" class="img-thumbnail card-img mr-5" />
				<b-colxx class=" mr-5 mt-3 ">
					<h1 class="mb-0 text-xlarge">유저명</h1><br>
					<h1 class="mb-0 text-large">이메일</h1><br>
					<h3 class="mb-0 truncate">성별: 여</h3><br>
					<h3 class="mb-0 truncate">나이: 20</h3>
				</b-colxx>
    			<div style="margin-top: auto;">
					<b-button class="mb-1" variant="outline-dark">정보수정</b-button>
    			</div>
        	</div>
     	</b-colxx>
	  
      <b-tabs nav-class="separator-tabs ml-0 mb-5" content-class="tab-content" :no-fade="true">
        <b-tab title="플레이리스트">
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
                    <th @click="changeSortValue('like')" style="width:10%">좋아요</th>
                  </thead>
                  <tbody style="font-size: x-large;">
                    <tr :class="{'flex-row':true}" v-for="(song, index) in sortPlaylist" v-bind:key="index" style="cursor:pointer;">
                      <td style="width:85px;"><img :src="song.img" class="list-thumbnail responsive border-0" @click="detailSong(song.id)"/></td>
                      <td class="list-item-heading mb-0 truncate" style="vertical-align: middle;" @click="detailSong(song.id)">{{song.name}}</td>
                      <td class="list-item-heading mb-0 truncate" style="vertical-align: middle;" @click="detailSong(song.id)">{{song.artist}}</td>
                      <td class="list-item-heading mb-0 truncate" style="vertical-align: middle;" @click="detailSong(song.id)">{{song.genre}}</td>
                      <td style="vertical-align: middle;" @click.prevent="playSong(song.id)"><div class="glyph-icon simple-icon-control-play"/></td>
                      <td style="vertical-align: middle;" @click.prevent="addSong(song.id)"><div class="glyph-icon simple-icon-playlist"/></td>
                      <td style="vertical-align: middle;" @click.prevent="likeSong(song.id)" ><div class="glyph-icon simple-icon-heart" /></td>
                    </tr>
                  </tbody>
              </table>
            </b-card>
          </b-colxx>

        </b-tab>

        <b-tab title="좋아요">
        </b-tab>
      </b-tabs>
    </b-colxx>
  </b-row>
</template>

<script>
export default {
  components: {

  },
  data() {
    return {
		sort_value : "",
		sort_type : 'asc',
		playlist: [{ id: 1, name: '선물', artist: '멜로망스1', genre: '발라드', img: 'https://cdnimg.melon.co.kr/cm/album/images/100/78/176/10078176_500.jpg?fc3fe8c6bd74c16bce7ffd971a930ffa/melon/resize/282/quality/80/optimize'},
		{ id: 2, name: '인사', artist: '멜로망스2', genre: '발라드', img: 'https://cdnimg.melon.co.kr/cm/album/images/103/05/070/10305070_500.jpg?8e4dafd3e69b879fdeb5f6d5e8e6cdda/melon/sharpen/0x1'},
		{ id: 3, name: '유리', artist: '멜로망스3', genre: '발라드', img: 'https://cdnimg.melon.co.kr/cm/album/images/102/27/379/10227379_500.jpg?bb36e84e0109f6b0253b72688988233d/melon/quality/80/optimize'},
		{ id: 4, name: 'Page 0', artist: '멜로망스4', genre: '발라드', img: 'https://cdnimg.melon.co.kr/cm/album/images/101/93/505/10193505_500.jpg?cf087eb8878fbec43435f3ba84e307e5/melon/quality/80/optimize'},
		{ id: 5, name: '좋은 날', artist: '멜로망스5', genre: '발라드', img: 'https://cdnimg.melon.co.kr/cm/album/images/101/91/294/10191294_500.jpg?ceb46dcf7679dd7c58e2941eb93bc624/melon/quality/80/optimize'},
		{ id: 6, name: '선물5', artist: '멜로망스6', genre: '발라드', img: 'https://cdnimg.melon.co.kr/cm/album/images/100/78/176/10078176_500.jpg?fc3fe8c6bd74c16bce7ffd971a930ffa/melon/resize/282/quality/80/optimize'},
		{ id: 7, name: '선물6', artist: '멜로망스7', genre: '발라드', img: 'https://cdnimg.melon.co.kr/cm/album/images/100/78/176/10078176_500.jpg?fc3fe8c6bd74c16bce7ffd971a930ffa/melon/resize/282/quality/80/optimize'},
		{ id: 8, name: '선물7', artist: '멜로망스8', genre: '발라드', img: 'https://cdnimg.melon.co.kr/cm/album/images/100/78/176/10078176_500.jpg?fc3fe8c6bd74c16bce7ffd971a930ffa/melon/resize/282/quality/80/optimize'},
		{ id: 9, name: '선물8', artist: '멜로망스9', genre: '발라드', img: 'https://cdnimg.melon.co.kr/cm/album/images/100/78/176/10078176_500.jpg?fc3fe8c6bd74c16bce7ffd971a930ffa/melon/resize/282/quality/80/optimize'},
		{ id: 10, name: '선물9', artist: '멜로망스10', genre: '발라드', img: 'https://cdnimg.melon.co.kr/cm/album/images/100/78/176/10078176_500.jpg?fc3fe8c6bd74c16bce7ffd971a930ffa/melon/resize/282/quality/80/optimize'},
		{ id: 11, name: '선물10', artist: '멜로망스', genre: '발라드', img: 'https://cdnimg.melon.co.kr/cm/album/images/100/78/176/10078176_500.jpg?fc3fe8c6bd74c16bce7ffd971a930ffa/melon/resize/282/quality/80/optimize'},
		{ id: 12, name: '선물11', artist: '멜로망스', genre: '발라드', img: 'https://cdnimg.melon.co.kr/cm/album/images/100/78/176/10078176_500.jpg?fc3fe8c6bd74c16bce7ffd971a930ffa/melon/resize/282/quality/80/optimize'},
		{ id: 13, name: '선물12', artist: '멜로망스', genre: '발라드', img: 'https://cdnimg.melon.co.kr/cm/album/images/100/78/176/10078176_500.jpg?fc3fe8c6bd74c16bce7ffd971a930ffa/melon/resize/282/quality/80/optimize'},
		{ id: 14, name: '선물13', artist: '멜로망스', genre: '발라드', img: 'https://cdnimg.melon.co.kr/cm/album/images/100/78/176/10078176_500.jpg?fc3fe8c6bd74c16bce7ffd971a930ffa/melon/resize/282/quality/80/optimize'},
		{ id: 15, name: '선물14', artist: '멜로망스', genre: '발라드', img: 'https://cdnimg.melon.co.kr/cm/album/images/100/78/176/10078176_500.jpg?fc3fe8c6bd74c16bce7ffd971a930ffa/melon/resize/282/quality/80/optimize'},],
      
    };
  },
  methods: {
	showMoreSong: function() {
      this.moreSong = !this.moreSong;
	},
	detailSong: function(id){
      this.$router.push('/app/piaf/songDetail/'+id)
	},
	sortList() {
		//this.playlist = _.orderBy(this.playlist, this.sort_value, this.sort)
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
    sortPlaylist() {
		if(this.sort_value=='name'){
			if(this.sort_type=='asc'){
			return this.playlist.sort((a, b) => {
				if( a.name > b.name) return 1;
				else if ( a.name < b.name ) return -1;
				else return 0;
			})
			}else if(this.sort_type=='desc'){
				return this.playlist.sort((a, b) => {
					if( a.name < b.name) return 1;
					else if ( a.name > b.name ) return -1;
					else return 0;
				})
			}
		}else if(this.sort_value=='artist'){
			if(this.sort_type=='asc'){
			return this.playlist.sort((a, b) => {
				if( a.artist > b.artist) return 1;
				else if ( a.artist < b.artist ) return -1;
				else return 0;
			})
			}else if(this.sort_type=='desc'){
				return this.playlist.sort((a, b) => {
					if( a.artist < b.artist) return 1;
					else if ( a.artist > b.artist ) return -1;
					else return 0;
				})
			}
		}
		return this.playlist.sort((a, b) => {
			return a.id - b.id
		})

    },
  }
};
</script>
