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
		<p>{{sort_value}}</p>
		<p>{{sort}}</p>
        <b-tab title="플레이리스트">
          <b-colxx xxs="12" class="pl-3 pr-3">
            <b-card class="mb-0" style="text-align: center;">
              <table  class="table table-sm" style="margin-bottom:0px;">
                  <thead style="font-size: initial;">
                    <th></th>
                    <th @click="changeSortValue('title')" style="cursor:pointer">곡</th>
                    <th @click="changeSortValue('artist')" style="cursor:pointer">가수</th>
                    <th>장르</th>
                    <th>재생</th>
                    <th>삭제</th>
                    <th>상세정보</th>
                    <th @click="changeSortValue('like')" style="cursor:pointer">좋아요</th>
                  </thead>
                  <tbody style="font-size: x-large;">
                    <tr :class="{'flex-row':true}" v-for="(song, index) in playlist" v-bind:key="index">
                      <td style="width:85px;"><img :src="song.img" class="list-thumbnail responsive border-0" /></td>
                      <td class="list-item-heading mb-0 truncate" style="vertical-align: middle;">{{song.name}}</td>
                      <td class="list-item-heading mb-0 truncate" style="vertical-align: middle;">{{song.artist}}</td>
                      <td class="list-item-heading mb-0 truncate" style="vertical-align: middle;">{{song.genre}}</td>
                      <td style="vertical-align: middle;"><div class="glyph-icon simple-icon-control-play"/></td>
                      <td style="vertical-align: middle;"><div class="glyph-icon simple-icon-trash"/></td>
                      <td style="vertical-align: middle;"><div class="glyph-icon simple-icon-magnifier-add" @click="detailSong(song.id)" style="cursor:pointer;"/></td>
                      <td style="vertical-align: middle;"><div class="glyph-icon simple-icon-heart"/></td>
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
		sort_value : "111",
		sort : 'asc',
		playlist: [{ id: 1, name: '선물', artist: '멜로망스', genre: '발라드', img: 'https://cdnimg.melon.co.kr/cm/album/images/100/78/176/10078176_500.jpg?fc3fe8c6bd74c16bce7ffd971a930ffa/melon/resize/282/quality/80/optimize'},
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
		}else{
			if(this.sort =='asc'){
				this.sort = 'desc';
			}else{
				this.sort = 'asc';
			}
		}
		sortList();
	},
	
  },
};
</script>
