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
			<MyPlayList/>

        </b-tab>

        <b-tab title="좋아요">
        </b-tab>
      </b-tabs>
    </b-colxx>
  </b-row>
</template>

<script>
import MyPlayList from '@/components/User/MyPlayList.vue'
export default {
  components: {
	  MyPlayList
  },
  data() {
    return {
		sort_value : "",
		sort_type : 'asc',
		
    };
  },
  methods: {
	showMoreSong: function() {
      this.moreSong = !this.moreSong;
	},
	detailSong: function(id){
      this.$router.push('/A505/songDetail/'+id)
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
