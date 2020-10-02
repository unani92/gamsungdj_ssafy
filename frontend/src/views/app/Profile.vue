<template>
  <b-row>
	<UpdateForm :showUpdate="showUpdate" @hideModal="showUpdate=false"/>
    <b-colxx xxs="12">
      	<b-colxx xxs="12" class="mb-5 mt-5">
    		<div class="d-flex flex-row ">
				<img :src="imgURL" alt="profile" class="card-img mr-5"/>
				<b-colxx class=" mr-5 mt-3 ">
					<h1 class="mb-0 text-xlarge">{{user.username}}</h1><br>
					<p class="mb-0">{{user.email}}</p><br>
					<h5 class="mb-0 truncate">성별: {{genders[user.gender]}}</h5><br>
					<h5 class="mb-0 truncate">나이: {{ages[user.age]}}</h5>
				</b-colxx>
    			<div style="margin-top: auto;">
					<b-button class="mb-1" variant="outline-dark" @click="showUpdate=true">정보수정</b-button>
    			</div>
        	</div>
     	</b-colxx>
	  
      <b-tabs nav-class="separator-tabs ml-0 mb-5" content-class="tab-content" :no-fade="true">
        <b-tab title="플레이리스트">
			<MyPlayList/>

        </b-tab>

        <b-tab title="좋아요">
			<MyLikeMusic/>
        </b-tab>
      </b-tabs>
    </b-colxx>
  </b-row>
</template>

<script>
import MyPlayList from '@/components/User/MyPlayList.vue'
import MyLikeMusic from '@/components/User/MyLikeMusic.vue'
import UpdateForm from '@/components/User/UpdateForm.vue'
import httpUser from '@/utils/http-user'
import { mapState, mapActions, mapGetters } from 'vuex'
export default {
  components: {
	  MyPlayList,
	  MyLikeMusic,
	  UpdateForm
  },
  data() {
    return {
		showUpdate: false,
		sort_value : "",
		sort_type : 'asc',
		genders: {
			"M" : "남성",
			"F" : "여성"
		},
		ages : {
			"0" : "10세 이하",
			"1" : "10대",
			"2" : "20대",
			"3" : "30대",
			"4" : "40대",
			"5" : "50세 이상"
		}
		
    };
  },
  methods: {
	...mapActions(['setUser', 'setPlayList']),
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
	...mapState(['user']),
	...mapGetters(['config']),
	imgURL: function() { return "http://127.0.0.1:8000/api/accounts/" + this.user.avatar },
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
  },
  created() {
	  httpUser.get('', this.config)
	  .then((res) => {
		  this.setUser(res.data.data)
	  })
	  this.setPlayList()

  }
};
</script>

<style scoped>
.card-img {
	width: 200px;
	height: 200px;
}
</style>
