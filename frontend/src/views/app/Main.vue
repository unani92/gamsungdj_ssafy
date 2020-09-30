<template>
<div>
	<!-- 감정 카테고리별 음악 추천 시작 -->
    <b-row>
        <b-colxx xxs="12" class="mb-4 pl-0 pr-0">
            <glide-component :settings="glideSingleOption">
                <!-- 카테고리1 시작 -->
                <div class="pr-3 pl-3 mb-4 glide__slide">
                    <b-card class="flex-row" no-body>
						<div class="col-sm-4 main-carousel-bg1" style="font-size:xx-large;">
                            <div class="glyph-icon simple-icon-refresh button-refresh" @click="getSadSong"></div>
						</div>
						<div class="col-sm-8">
							<b-row>
								<b-colxx class="mb-2 mt-4" v-for="(data, index) in carouselData1_1" :key="index">
								<b-card class="text-white" no-body @mouseover="showOverlay(index)" @mouseout="hideOverlay(index)">
									<img :src="data.img" class="card-img" />
									<div class="card-img-overlay" :class="'overlayClass'+(index+0)">
                                        <div style="position:absolute; bottom:10%;">
                                            <span class="glyph-icon simple-icon-control-play mr-3" style="font-size:x-large; cursor:pointer;" @click="addToPlaylistAndPlay(data)"></span>
                                            <span v-if="isLiked(data)" :id="data.id" class="glyph-icon simple-icon-heart mr-3 liked" style="font-size:x-large; cursor:pointer;" @click="songLike"></span>
                                            <span v-else :id="data.id" class="glyph-icon simple-icon-heart mr-3" style="font-size:x-large; cursor:pointer;" @click="songLike"></span>
                                            <span v-if="!isLoggedin" class="glyph-icon simple-icon-playlist mr-3" style="font-size:x-large; cursor:pointer;" @click="addToPlaylist(data)"></span>
                                            <b-dropdown v-else variant="empty" toggle-class="p-0 m-0" no-caret style="position:absolute;">
                                                <template slot="button-content">
                                                    <span class="glyph-icon simple-icon-playlist text-white" style="font-size:x-large; cursor:pointer;"></span>
                                                </template>
                                                <b-dropdown-item @click="addToPlaylist(data)">현재 재생목록</b-dropdown-item>
                                                <b-dropdown-item v-for="(playlist, index) in userPlayList" :key="index" @click="addToUserPlaylist(data, playlist)">{{ playlist.name }}</b-dropdown-item>
                                            </b-dropdown>
                                        </div>
                                        <h5 class="card-title">{{ data.name }}</h5>
										<p class="card-text" v-for="(artist, index) in data.artist" :key="index">{{ artist.name }}</p>
									</div>
								</b-card>
								</b-colxx>
							</b-row>
							<b-row>
								<b-colxx class="mb-4 mt-2" v-for="(data, index) in carouselData1_2" :key="index">
								<b-card class="text-white" no-body @mouseover="showOverlay(index+5)" @mouseout="hideOverlay(index+5)">
									<img :src="data.img" class="card-img" />
									<div class="card-img-overlay" :class="'overlayClass'+(index+5)">
                                        <div style="position:absolute; bottom:10%;">
                                            <span class="glyph-icon simple-icon-control-play mr-3" style="font-size:x-large; cursor:pointer;" @click="addToPlaylistAndPlay(data)"></span>
                                            <span v-if="isLiked(data)" :id="data.id" class="glyph-icon simple-icon-heart mr-3 liked" style="font-size:x-large; cursor:pointer;" @click="songLike"></span>
                                            <span v-else :id="data.id" class="glyph-icon simple-icon-heart mr-3" style="font-size:x-large; cursor:pointer;" @click="songLike"></span>
                                            <span v-if="!isLoggedin" class="glyph-icon simple-icon-playlist mr-3" style="font-size:x-large; cursor:pointer;" @click="addToPlaylist(data)"></span>
                                            <b-dropdown v-else variant="empty" dropup toggle-class="p-0 m-0" no-caret style="position:absolute;">
                                                <template slot="button-content">
                                                    <span class="glyph-icon simple-icon-playlist text-white" style="font-size:x-large; cursor:pointer;"></span>
                                                </template>
                                                <b-dropdown-item @click="addToPlaylist(data)">현재 재생목록</b-dropdown-item>
                                                <b-dropdown-item v-for="(playlist, index) in userPlayList" :key="index" @click="addToUserPlaylist(data, playlist)">{{ playlist.name }}</b-dropdown-item>
                                            </b-dropdown>
                                        </div>
										<h5 class="card-title">{{ data.name }}</h5>
										<p class="card-text" v-for="(artist, index) in data.artist" :key="index">{{ artist.name }}</p>
									</div>
								</b-card>
								</b-colxx>
							</b-row>
						</div>
                    </b-card>
                </div>
                <!-- 카테고리1 끝 -->

                <!-- 카테고리2 시작 -->
				<div class="pr-3 pl-3 mb-4 glide__slide">
                    <b-card class="flex-row" no-body>
						<div class="col-sm-4 main-carousel-bg2" style="font-size:xx-large;">
                            <div class="glyph-icon simple-icon-refresh button-refresh" @click="getJoySong"></div>
						</div>
						<div class="col-sm-8">
							<b-row>
								<b-colxx class="mb-2 mt-4" v-for="(data, index) in carouselData2_1" :key="index">
								<b-card class="text-white" no-body  @mouseover="showOverlay(index+10)" @mouseout="hideOverlay(index+10)">
									<img :src="data.img" class="card-img" />
									<div class="card-img-overlay" :class="'overlayClass'+(index+10)">
                                        <div style="position:absolute; bottom:10%;">
                                            <span class="glyph-icon simple-icon-control-play mr-3" style="font-size:x-large; cursor:pointer;" @click="addToPlaylistAndPlay(data)"></span>
                                            <span v-if="isLiked(data)" :id="data.id" class="glyph-icon simple-icon-heart mr-3 liked" style="font-size:x-large; cursor:pointer;" @click="songLike"></span>
                                            <span v-else :id="data.id" class="glyph-icon simple-icon-heart mr-3" style="font-size:x-large; cursor:pointer;" @click="songLike"></span>
                                            <span v-if="!isLoggedin" class="glyph-icon simple-icon-playlist mr-3" style="font-size:x-large; cursor:pointer;" @click="addToPlaylist(data)"></span>
                                            <b-dropdown v-else variant="empty" toggle-class="p-0 m-0" no-caret style="position:absolute;">
                                                <template slot="button-content">
                                                    <span class="glyph-icon simple-icon-playlist text-white" style="font-size:x-large; cursor:pointer;"></span>
                                                </template>
                                                <b-dropdown-item @click="addToPlaylist(data)">현재 재생목록</b-dropdown-item>
                                                <b-dropdown-item v-for="(playlist, index) in userPlayList" :key="index" @click="addToUserPlaylist(data, playlist)">{{ playlist.name }}</b-dropdown-item>
                                            </b-dropdown>
                                        </div>
                                        <h5 class="card-title">{{ data.name }}</h5>
										<p class="card-text" v-for="(artist, index) in data.artist" :key="index">{{ artist.name }}</p>
									</div>
								</b-card>
								</b-colxx>
							</b-row>
							<b-row>
								<b-colxx class="mb-4 mt-2" v-for="(data, index) in carouselData2_2" :key="index">
								<b-card class="text-white" no-body @mouseover="showOverlay(index+15)" @mouseout="hideOverlay(index+15)">
									<img :src="data.img" class="card-img" />
									<div class="card-img-overlay" :class="'overlayClass'+(index+15)">
                                        <div style="position:absolute; bottom:10%;">
                                            <span class="glyph-icon simple-icon-control-play mr-3" style="font-size:x-large; cursor:pointer;" @click="addToPlaylistAndPlay(data)"></span>
                                            <span v-if="isLiked(data)" :id="data.id" class="glyph-icon simple-icon-heart mr-3 liked" style="font-size:x-large; cursor:pointer;" @click="songLike"></span>
                                            <span v-else :id="data.id" class="glyph-icon simple-icon-heart mr-3" style="font-size:x-large; cursor:pointer;" @click="songLike"></span>
                                            <span v-if="!isLoggedin" class="glyph-icon simple-icon-playlist mr-3" style="font-size:x-large; cursor:pointer;" @click="addToPlaylist(data)"></span>
                                            <b-dropdown v-else variant="empty" dropup toggle-class="p-0 m-0" no-caret style="position:absolute;">
                                                <template slot="button-content">
                                                    <span class="glyph-icon simple-icon-playlist text-white" style="font-size:x-large; cursor:pointer;"></span>
                                                </template>
                                                <b-dropdown-item @click="addToPlaylist(data)">현재 재생목록</b-dropdown-item>
                                                <b-dropdown-item v-for="(playlist, index) in userPlayList" :key="index" @click="addToUserPlaylist(data, playlist)">{{ playlist.name }}</b-dropdown-item>
                                            </b-dropdown>
                                        </div>
                                        <h5 class="card-title">{{ data.name }}</h5>
										<p class="card-text" v-for="(artist, index) in data.artist" :key="index">{{ artist.name }}</p>
									</div>
								</b-card>
								</b-colxx>
							</b-row>
						</div>
                    </b-card>
                </div>
                <!-- 카테고리2 끝 -->

                <!-- 카테고리3 시작 -->
                <div class="pr-3 pl-3 mb-4 glide__slide">
                    <b-card class="flex-row" no-body>
						<div class="col-sm-4 main-carousel-bg3" style="font-size:xx-large;">
                            <div class="glyph-icon simple-icon-refresh button-refresh" @click="getLoveSong"></div>
						</div>
						<div class="col-sm-8">
							<b-row>
								<b-colxx class="mb-2 mt-4" v-for="(data, index) in carouselData3_1" :key="index">
								<b-card class="text-white" no-body  @mouseover="showOverlay(index+20)" @mouseout="hideOverlay(index+20)">
									<img :src="data.img" class="card-img" />
									<div class="card-img-overlay" :class="'overlayClass'+(index+20)">
                                        <div style="position:absolute; bottom:10%;">
                                            <span class="glyph-icon simple-icon-control-play mr-3" style="font-size:x-large; cursor:pointer;" @click="addToPlaylistAndPlay(data)"></span>
                                            <span v-if="isLiked(data)" :id="data.id" class="glyph-icon simple-icon-heart mr-3 liked" style="font-size:x-large; cursor:pointer;" @click="songLike"></span>
                                            <span v-else :id="data.id" class="glyph-icon simple-icon-heart mr-3" style="font-size:x-large; cursor:pointer;" @click="songLike"></span>
                                            <span v-if="!isLoggedin" class="glyph-icon simple-icon-playlist mr-3" style="font-size:x-large; cursor:pointer;" @click="addToPlaylist(data)"></span>
                                            <b-dropdown v-else variant="empty" toggle-class="p-0 m-0" no-caret style="position:absolute;">
                                                <template slot="button-content">
                                                    <span class="glyph-icon simple-icon-playlist text-white" style="font-size:x-large; cursor:pointer;"></span>
                                                </template>
                                                <b-dropdown-item @click="addToPlaylist(data)">현재 재생목록</b-dropdown-item>
                                                <b-dropdown-item v-for="(playlist, index) in userPlayList" :key="index" @click="addToUserPlaylist(data, playlist)">{{ playlist.name }}</b-dropdown-item>
                                            </b-dropdown>
                                        </div>
                                        <h5 class="card-title">{{ data.name }}</h5>
										<p class="card-text" v-for="(artist, index) in data.artist" :key="index">{{ artist.name }}</p>
									</div>
								</b-card>
								</b-colxx>
							</b-row>
							<b-row>
								<b-colxx class="mb-4 mt-2" v-for="(data, index) in carouselData3_2" :key="index">
								<b-card class="text-white" no-body @mouseover="showOverlay(index+25)" @mouseout="hideOverlay(index+25)">
									<img :src="data.img" class="card-img" />
									<div class="card-img-overlay tempclass" :class="'overlayClass'+(index+25)">
                                        <div style="position:absolute; bottom:10%;">
                                            <span class="glyph-icon simple-icon-control-play mr-3" style="font-size:x-large; cursor:pointer;" @click="addToPlaylistAndPlay(data)"></span>
                                            <span v-if="isLiked(data)" :id="data.id" class="glyph-icon simple-icon-heart mr-3 liked" style="font-size:x-large; cursor:pointer;" @click="songLike"></span>
                                            <span v-else :id="data.id" class="glyph-icon simple-icon-heart mr-3" style="font-size:x-large; cursor:pointer;" @click="songLike"></span>
                                            <span v-if="!isLoggedin" class="glyph-icon simple-icon-playlist mr-3" style="font-size:x-large; cursor:pointer;" @click="addToPlaylist(data)"></span>
                                            <b-dropdown v-else variant="empty" dropup toggle-class="p-0 m-0" no-caret style="position:absolute;">
                                                <template slot="button-content">
                                                    <span class="glyph-icon simple-icon-playlist text-white" style="font-size:x-large; cursor:pointer;"></span>
                                                </template>
                                                <b-dropdown-item @click="addToPlaylist(data)">현재 재생목록</b-dropdown-item>
                                                <b-dropdown-item v-for="(playlist, index) in userPlayList" :key="index" @click="addToUserPlaylist(data, playlist, index)">{{ playlist.name }}</b-dropdown-item>
                                            </b-dropdown>
                                        </div>
                                        <h5 class="card-title">{{ data.name }}</h5>
										<p class="card-text" v-for="(artist, index) in data.artist" :key="index">{{ artist.name }}</p>
									</div>
								</b-card>
								</b-colxx>
							</b-row>
						</div>
                    </b-card>
                </div>
                <!-- 카테고리3 끝 -->
            </glide-component>
        </b-colxx>
    </b-row>
	<!-- 감정 카테고리별 음악 추천 끝 -->

	<!-- 날씨 매칭 추천 시작 -->
    <b-row>
        <b-colxx xxs="12">
            <a href="#" @click.prevent=""><h5 class="mb-4 card-title">오늘 같은 날에는 ></h5></a>
        </b-colxx>
        <b-colxx xxs="12" class="mb-4 pl-0 pr-0">
            <glide-component :settings="glideNoControlsSettings">
                <div v-for="(data, index) in dummyData1" :key="index" class="pr-3 pl-3 mb-4 glide__slide">
                    <b-card no-body>
                        <div class="position-relative" @mouseover="showOverlayWeather(index)" @mouseout="hideOverlayWeather(index)">
                            <a href="#" @click.prevent="search(data.title)">
                                <img class="card-img-top" :src="data.src" alt="Card cap" />
                            </a>
                        </div>
                        <b-card-body>
                            <a href="#" @click.prevent="tempFunction"><h6 class="mb-4 ellipsis">{{ data.title }}</h6></a>
                            <a href="#" @click.prevent="tempFunction"><p class="text-muted mb-0 font-weight-light ellipsis">{{ data.artist }}</p>
                            </a>
                            <div class="mt-4" style="font-size:x-large;">
                                <span class="glyph-icon simple-icon-control-play mr-3" style="cursor:pointer;" @click="addToPlaylistAndPlay(data)"></span>
                                <span class="glyph-icon simple-icon-heart mr-3" style="cursor:pointer;"></span>
                                <span class="glyph-icon simple-icon-playlist mr-3" style="cursor:pointer;" @click="addToPlaylist(data)"></span>
                            </div>
                        </b-card-body>
                    </b-card>
                </div>
            </glide-component>

        </b-colxx>
    </b-row>
	<!-- 날씨 매칭 추천 끝 -->

	<!-- 시간 매칭 추천 시작 -->
    <div v-if="timeRecommend">
    <b-row >
        <b-colxx xxs="12">
            <a href="#" @click.prevent=""><h5 class="mb-4 card-title">이시간에는 ></h5></a>
        </b-colxx>
        <b-colxx xxs="12" class="mb-4 pl-0 pr-0">
            <glide-component :settings="glideNoControlsSettings">
                <div v-for="(data, index) in timeRecommend" :key="index" class="pr-3 pl-3 mb-4 glide__slide">
                    <b-card no-body>
                        <div class="position-relative">
                            <a href="#" @click.prevent="search(data.title)"><img class="card-img-top" :src="data.img" alt="Card cap" /></a>
                        </div>
                        <b-card-body>
                            <a href="#" @click.prevent="search(data.title)"><h6 class="mb-4 ellipsis">{{ data.name }}</h6></a>
                            <a href="#" @click.prevent="search(data.artist)"><p class="text-muted mb-0 font-weight-light ellipsis">{{ data.artist[0].name }}</p></a>
                            <div class="mt-4" style="font-size:x-large;">
                                <span class="glyph-icon simple-icon-control-play mr-3" style="cursor:pointer;" @click="addToPlaylistAndPlay(data)"></span>
                                <span class="glyph-icon simple-icon-heart mr-3" style="cursor:pointer;"></span>
                                <span class="glyph-icon simple-icon-playlist mr-3" style="cursor:pointer;" @click="addToPlaylist(data)"></span>
                            </div>
                        </b-card-body>
                    </b-card>
                </div>
            </glide-component>
        </b-colxx>
    </b-row>
    </div>
	<!-- 시간 매칭 추천 끝 -->
</div>
</template>

<script>
import GlideComponent from '../../components/Carousel/GlideComponent'
import http from '../../utils/http-common'
import http2 from '../../utils/http-user'
import { mapState, mapGetters } from 'vuex'
import axios from 'axios'

const youtubeURL = 'https://www.googleapis.com/youtube/v3/search'
const API_KEY = process.env.VUE_APP_YOUTUBE_API_KEY

export default {
    components: {
        'glide-component': GlideComponent,
    },
	mounted(){
        this.getTimeRecommend()
        this.getSadSong()
        this.getJoySong()
        this.getLoveSong()
        // this.getWeather()
    },
    data() {
        return {
            glideSingleOption: {
                gap: 5,
                perView: 1,
                type: "carousel"
            },
            glideNoControlsSettings: {
                gap: 5,
                perView: 6,
                type: "carousel",
                breakpoints: {
                    480: {
                        perView: 1
                    },
                    800: {
                        perView: 2
                    },
                    1200: {
                        perView: 3
                    }
                },
                hideNav: true
            },
            dummyData1:
            [
                {
                    src: "https://cdnimg.melon.co.kr/cm2/album/images/104/79/150/10479150_20200821103346_500.jpg?21a0dfff48264f87bb4120d95578e9ee/melon/quality/80/optimize",
                    title: "Dynamite",
                    artist: "방탄소년단",
                },
                {
                    src: "https://cdnimg.melon.co.kr/cm2/album/images/104/69/416/10469416_20200730151034_500.jpg?dcdcccfa8cd1bc5dae7b668a5910c277/melon/sharpen/0x1",
                    title: "눈누난나 (NUNU NANA)",
                    artist: "제시(Jessi)",
                },
                {
                    src: "https://cdnimg.melon.co.kr/cm2/album/images/104/63/600/10463600_20200720152905_500.jpg?4f47c8ca556045d56c9f2016a866e652/melon/quality/80/optimize",
                    title: "취기를 빌려 (취향저격 그녀 X 산들)",
                    artist: "산들",
                },
                {
                    src: "https://cdnimg.melon.co.kr/cm2/album/images/104/62/799/10462799_20200717150822_500.jpg?adcaec1a0d99e7a379c098d31dca68da/melon/quality/80/optimize",
                    title: "다시 여기 바닷가",
                    artist: "싹쓰리 (유두래곤, 린다G, 비룡)",
                },
                {
                    src: "https://cdnimg.melon.co.kr/cm2/album/images/104/52/351/10452351_20200629152036_500.jpg?40db717ac487b870724b0bab06e4b0d7/melon/quality/80/optimize",
                    title: "마리아 (Maria)",
                    artist: "화사 (Hwa Sa)",
                },
                {
                    src: "https://cdnimg.melon.co.kr/cm2/album/images/104/75/061/10475061_20200812120927_500.jpg?e0e2a4331bb0aa6e525f679804f35f8e/melon/quality/80/optimize",
                    title: "When We Disco (Duet with 선미)",
                    artist: "박진영",
                },
            ],
            timeRecommend: null,
            carouselData1_1: '',
            carouselData1_2: '',
            carouselData2_1: '',
            carouselData2_2: '',
            carouselData3_1: '',
            carouselData3_2: '',
        }
    },
    computed: {
      ...mapState([
        'playlist',
        'songLikeList',
        'isLoggedin',
        'userPlayList'
      ]),
      ...mapGetters(['config'])
    },
	methods: {
        async getTimeRecommend() {
          const { data: { data } } = await http.get('recommend/time/')
          this.timeRecommend = data
        },
        async getSadSong() {
            const { data } = await http.get('sad')
            this.carouselData1_1 = data.slice(0, 5)
            this.carouselData1_2 = data.slice(5, 10)
        },
        async getJoySong() {
            const { data } = await http.get('joy')
            this.carouselData2_1 = data.slice(0, 5)
            this.carouselData2_2 = data.slice(5, 10)
        },
        async getLoveSong() {
            const { data } = await http.get('love')
            this.carouselData3_1 = data.slice(0, 5)
            this.carouselData3_2 = data.slice(5, 10)
        },
        isLiked(data) {
            return this.songLikeList.includes(data.id);
        },
        async songLike(e) {
            console.log("liek")
            if (this.isLoggedin) {
                const { id } = e.target
                const span = document.getElementById(id)
                const { data } = await http.post(`song/${id}/like/`, '',this.config)
                span.classList.toggle('liked')
            }
            else {
                const loginBtn = document.querySelector('#loginFlag')
                loginBtn.click()
            }
        },
		tempFunction() {
			alert("페이지 준비중입니다.");
        },
        showOverlay(index) {
            let el = document.getElementsByClassName('overlayClass'+index)
            for(var i=0; i<el.length; i++){
                el[i].style.display="block"
            }
        },
        hideOverlay(index) {
            let el = document.getElementsByClassName('overlayClass'+index)
            for(var i=0; i<el.length; i++){
                el[i].style.display="none"
            }
        },
        showOverlayWeather(index) {
            let el = document.getElementsByClassName('overlayWeather'+index)
            for(var i=0; i<el.length; i++){
                el[i].style.display="block"
            }
        },
        hideOverlayWeather(index) {
            let el = document.getElementsByClassName('overlayWeather'+index)
            for(var i=0; i<el.length; i++){
                el[i].style.display="none"
            }
        },
        showOverlay(index) {
            let el = document.getElementsByClassName('overlayClass'+index)
            for(var i=0; i<el.length; i++){
                el[i].style.display="block"
            }
        },
        hideOverlay(index) {
            let el = document.getElementsByClassName('overlayClass'+index)
            for(var i=0; i<el.length; i++){
                el[i].style.display="none"
            }
        },
        async fetchYoutubeId(song) {
          const { data } = await axios.get(youtubeURL, {
            params: {
              key: API_KEY,
              part: 'snippet',
              maxResults: 1,
              type: 'video',
              q: song.artist[0].name + ' ' + song.name
            }
          })
          const { items } = data
          const { videoId } = items[0].id
          const reqData = {'src': videoId}
          song['src'] = videoId
          await http.post(`addsrc/${song.id}/`, reqData,'')
        },
        async addToPlaylistAndPlay(data) {
          if (data['src']) {
            this.playlist.unshift(data)
            this.$store.state.playerControl = "add"
            this.$notify('primary', "재생 중인 곡", data.name+" - "+data.artist[0].name, { duration: 4000, permanent: false })
          } else {
            await this.fetchYoutubeId(data)
            this.playlist.unshift(data)
            this.$store.state.playerControl = "add"
            this.$notify('primary', "재생 중인 곡", data.name+" - "+data.artist[0].name, { duration: 4000, permanent: false })
          }
        },
        async addToPlaylist(data) {
            if (data['src']) {
                this.playlist.push(data)
                this.$notify('primary', "재생 목록에 추가 었습니다.", data.name+" - "+data.artist[0].name, { duration: 4000, permanent: false })
            }
            else {
                await this.fetchYoutubeId(data)
                this.playlist.push(data)
                this.$notify('primary', "재생 목록에 추가 었습니다.", data.name+" - "+data.artist[0].name, { duration: 4000, permanent: false })
            }
        },
        addToUserPlaylist(data, playlist, index) {
            http2
            .post(`playlist/${playlist.id}/song/`,{
                'songs': [data.id]
            },this.config)
            .then((value)=> {
                this.$notify('primary', "사용자 재생 목록에 추가 되었습니다.", data.name+" - "+data.artist[0].name, { duration: 4000, permanent: false })
                this.userPlayList[index].song.push(data)
            })
        },
        search(word){
            this.$router.push(`/A505/search/${word}`);
        },
        getWeather(){
            if(navigator.geolocation) {
                var apikey = '28de7356f776313b2637236fb7961f04'
                navigator.geolocation.getCurrentPosition(function(position) {
                    alert(position.coords.latitude + ' ' +position.coords.longitude)
                    http
                    .get('http://api.openweathermap.org/data/2.5/weather?lat='+position.coords.latitude+'&lon='+position.coords.longitude+'&appid='+apikey)
                    .then((value) => {
                        console.log(value)
                    })
                }, function(error) {
                    console.log(error)
                }, {
                    enableHighAccuracy: false,
                    maximumAge: 0,
                    timeout: Infinity
                })
            }
            else {
                console.log('GPS를 지원하지 않습니다')
            }
        }
	}
}
</script>
<style scoped>
.card-title {
    text-overflow: ellipsis;
    white-space: nowrap;
    word-wrap: normal;
    width: 100%;
    overflow: hidden;
}
.card-text {
    text-overflow: ellipsis;
    white-space: nowrap;
    word-wrap: normal;
    width: 100%;
    overflow: hidden;
}
.liked {
  color: red !important;
}
.card-img-overlay {
    display: none;
}
.main-carousel-bg1 {
	background: url('/assets/img/wordcloud/wc01.png') no-repeat;
	background-size: contain;
	background-position: center center;
}
.main-carousel-bg2 {
	background: url('/assets/img/wordcloud/wc02.png') no-repeat;
    background-size: contain;
	background-position: center center;
}
.main-carousel-bg3 {
	background: url('/assets/img/wordcloud/wc03.png') no-repeat;
    background-size: contain;
	background-position: center center;
}
.main-carousel-bg4 {
	background: url('/assets/img/wordcloud/wc04.png') no-repeat;
    background-size: contain;
	background-position: center center;
}
</style>
