<template>
<div>
	<!-- 감정 카테고리별 추천 음악 시작 -->
    <b-row>
        <b-colxx xxs="12" class="mb-4 pl-0 pr-0">
            <glide-component :settings="glideSingleOption">
                <!-- 카테고리1 시작 -->
                <div class="pr-3 pl-3 mb-4 glide__slide">
                    <b-card class="flex-row" no-body>
						<div class="col-sm-4 main-carousel-bg1">
						</div>
						<div class="col-sm-8">
							<b-row>
								<b-colxx class="mb-2 mt-4" v-for="(data, index) in carouselData1_1" :key="index">
								<b-card class="text-white" no-body @mouseover="showOverlay(index)" @mouseout="hideOverlay(index)">
									<img :src="data.img" class="card-img" />
									<div class="card-img-overlay" :class="'overlayClass'+(index+0)">
                                        <div style="position:absolute; bottom:10%;">
                                            <span class="glyph-icon simple-icon-control-play mr-3" style="font-size:x-large; cursor:pointer;" @click="addToPlaylistAndPlay(data)"></span>
                                            <span class="glyph-icon simple-icon-heart mr-3" style="font-size:x-large; cursor:pointer;"></span>
                                            <span class="glyph-icon simple-icon-playlist mr-3" style="font-size:x-large; cursor:pointer;" @click="addToPlaylist(data)"></span>
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
                                            <span class="glyph-icon simple-icon-heart mr-3" style="font-size:x-large; cursor:pointer;"></span>
                                            <span class="glyph-icon simple-icon-playlist mr-3" style="font-size:x-large; cursor:pointer;" @click="addToPlaylist(data)"></span>
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
						<div class="col-sm-4 main-carousel-bg2">
						</div>
						<div class="col-sm-8">
							<b-row>
								<b-colxx class="mb-2 mt-4" v-for="(data, index) in carouselData2_1" :key="index">
								<b-card class="text-white" no-body  @mouseover="showOverlay(index+10)" @mouseout="hideOverlay(index+10)">
									<img :src="data.img" class="card-img" />
									<div class="card-img-overlay" :class="'overlayClass'+(index+10)">
                                        <div style="position:absolute; bottom:10%;">
                                            <span class="glyph-icon simple-icon-control-play mr-3" style="font-size:x-large; cursor:pointer;" @click="addToPlaylistAndPlay(data)"></span>
                                            <span class="glyph-icon simple-icon-heart mr-3" style="font-size:x-large; cursor:pointer;"></span>
                                            <span class="glyph-icon simple-icon-playlist mr-3" style="font-size:x-large; cursor:pointer;" @click="addToPlaylist(data)"></span>
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
                                            <span class="glyph-icon simple-icon-heart mr-3" style="font-size:x-large; cursor:pointer;"></span>
                                            <span class="glyph-icon simple-icon-playlist mr-3" style="font-size:x-large; cursor:pointer;" @click="addToPlaylist(data)"></span>
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
						<div class="col-sm-4 main-carousel-bg3">
						</div>
						<div class="col-sm-8">
							<b-row>
								<b-colxx class="mb-2 mt-4" v-for="(data, index) in carouselData3_1" :key="index">
								<b-card class="text-white" no-body  @mouseover="showOverlay(index+20)" @mouseout="hideOverlay(index+20)">
									<img :src="data.img" class="card-img" />
									<div class="card-img-overlay" :class="'overlayClass'+(index+20)">
                                        <div style="position:absolute; bottom:10%;">
                                            <span class="glyph-icon simple-icon-control-play mr-3" style="font-size:x-large; cursor:pointer;" @click="addToPlaylistAndPlay(data)"></span>
                                            <span class="glyph-icon simple-icon-heart mr-3" style="font-size:x-large; cursor:pointer;"></span>
                                            <span class="glyph-icon simple-icon-playlist mr-3" style="font-size:x-large; cursor:pointer;" @click="addToPlaylist(data)"></span>
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
                                            <span class="glyph-icon simple-icon-heart mr-3" style="font-size:x-large; cursor:pointer;"></span>
                                            <span class="glyph-icon simple-icon-playlist mr-3" style="font-size:x-large; cursor:pointer;" @click="addToPlaylist(data)"></span>
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
	<!-- 감정 카테고리별 추천 음악 끝 -->

	<!-- 날씨 매칭 추천 시작 -->
    <b-row>
        <b-colxx xxs="12">
            <a href="#" @click.prevent="tempFunction"><h5 class="mb-4 card-title">오늘 같은 날에는 ></h5></a>
        </b-colxx>
        <b-colxx xxs="12" class="mb-4 pl-0 pr-0">
            <glide-component :settings="glideNoControlsSettings">
                <div v-for="(data, index) in dummyData1" :key="index" class="pr-3 pl-3 mb-4 glide__slide">
                    <b-card no-body>
                        <div class="position-relative">
                            <a href="#" @click.prevent="tempFunction"><img class="card-img-top" :src="data.src" alt="Card cap" /></a>
                            <!-- <b-badge variant="primary" pill class="position-absolute badge-top-left">NEW</b-badge> -->
                            <!-- <b-badge variant="secondary" pill class="position-absolute badge-top-left-2">TRENDING</b-badge> -->
                        </div>
                        <b-card-body>
                            <a href="#" @click.prevent="tempFunction"><h6 class="mb-4">{{ data.title }}</h6></a>
                            <a href="#" @click.prevent="tempFunction"><p class="text-muted text-small mb-0 font-weight-light">{{ data.artist }}</p></a>
                        </b-card-body>
                    </b-card>
                </div>
            </glide-component>

        </b-colxx>
    </b-row>
	<!-- 날씨 매칭 추천 끝 -->

	<!-- 시간 매칭 추천 시작 -->
    <b-row>
        <b-colxx xxs="12">
            <a href="#" @click.prevent="tempFunction"><h5 class="mb-4 card-title">이시간에는 ></h5></a>
        </b-colxx>
        <b-colxx xxs="12" class="mb-4 pl-0 pr-0">
            <glide-component :settings="glideNoControlsSettings">
                <div v-for="(data, index) in dummyData2" :key="index" class="pr-3 pl-3 mb-4 glide__slide">
                    <b-card no-body>
                        <div class="position-relative">
                            <a href="#" @click.prevent="tempFunction"><img class="card-img-top" :src="data.src" alt="Card cap" /></a>
                            <!-- <b-badge variant="primary" pill class="position-absolute badge-top-left">NEW</b-badge> -->
                            <!-- <b-badge variant="secondary" pill class="position-absolute badge-top-left-2">TRENDING</b-badge> -->
                        </div>
                        <b-card-body>
                            <a href="#" @click.prevent="tempFunction"><h6 class="mb-4">{{ data.title }}</h6></a>
                            <a href="#" @click.prevent="tempFunction"><p class="text-muted text-small mb-0 font-weight-light">{{ data.artist }}</p></a>
                        </b-card-body>
                    </b-card>
                </div>
            </glide-component>

        </b-colxx>
    </b-row>
	<!-- 시간 매칭 추천 끝 -->

	<!-- 기분 매칭 추천 시작 -->
    <b-row>
        <b-colxx xxs="12">
            <a href="#" @click.prevent="tempFunction"><h5 class="mb-4 card-title">지금 기분에는 ></h5></a>
        </b-colxx>
        <b-colxx xxs="12" class="mb-4 pl-0 pr-0">
            <glide-component :settings="glideNoControlsSettings">
                <div v-for="(data, index) in dummyData3" :key="index" class="pr-3 pl-3 mb-4 glide__slide">
                    <b-card no-body>
                        <div class="position-relative">
                            <a href="#" @click.prevent="tempFunction"><img class="card-img-top" :src="data.src" alt="Card cap" /></a>
                            <!-- <b-badge variant="primary" pill class="position-absolute badge-top-left">Play</b-badge>
                            <b-badge variant="secondary" pill class="position-absolute badge-top-left-2">Add</b-badge> -->
                        </div>
                        <b-card-body>
                            <a href="#" @click.prevent="tempFunction"><h6 class="mb-4">{{ data.title }}</h6></a>
                            <a href="#" @click.prevent="tempFunction"><p class="text-muted text-small mb-0 font-weight-light">{{ data.artist }}</p></a>
                        </b-card-body>
                    </b-card>
                </div>
            </glide-component>

        </b-colxx>
    </b-row>
	<!-- 기분 매칭 추천 끝 -->
</div>
</template>

<script>
import GlideComponent from '../../../components/Carousel/GlideComponent'
import http from '../../../utils/http-common'
import { dummyData1, dummyData2, dummyData3 } from "../../../data/dummyData"
import { mapState } from 'vuex'
import axios from 'axios'

const youtubeURL = 'https://www.googleapis.com/youtube/v3/search'
const API_KEY = process.env.VUE_APP_YOUTUBE_API_KEY

export default {
    components: {
        'glide-component': GlideComponent,
    },
	mounted(){
        http
        .get('sad')
        .then((data) => {
            this.carouselData1_1 = data.data.slice(0, 5)
            this.carouselData1_2 = data.data.slice(5, 10)
		})
		http
		.get('joy')
        .then((data) => {
			this.carouselData2_1 = data.data.slice(0, 5)
            this.carouselData2_2 = data.data.slice(5, 10)
		})
		http
		.get('love')
        .then((data) => {
			this.carouselData3_1 = data.data.slice(0, 5)
            this.carouselData3_2 = data.data.slice(5, 10)
        })
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
			dummyData1 ,
			dummyData2 ,
			dummyData3 ,
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
            'playlist'
        ]),
    },
	methods:{
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
        addToPlaylistAndPlay(data) {
            axios.get(youtubeURL, {
                params: {
                    key: API_KEY,
                    part: 'snippet',
                    maxResults: 1,
                    type: 'video',
                    q: data.artist[0].name + ' ' + data.name
                }
            })
            .then(res => {
                const { items } = res.data
                const { videoId } = items[0].id
                data['src'] = videoId
                this.playlist.unshift(data)
                this.$store.state.playerControl = "add"
                this.$notify('primary', "재생 중인 곡", data.name+" - "+data.artist[0].name, { duration: 5000, permanent: false })
            })
            .catch(err => console.log(err))
        },
        addToPlaylist(data) {
            axios.get(youtubeURL, {
                params: {
                    key: API_KEY,
                    part: 'snippet',
                    maxResults: 1,
                    type: 'video',
                    q: data.artist[0].name + ' ' + data.name
                }
            })
            .then(res => {
                const { items } = res.data
                const { videoId } = items[0].id
                data['src'] = videoId
                this.playlist.push(data)
                this.$notify('primary', "재생 목록에 추가 었습니다.", data.name+" - "+data.artist[0].name, { duration: 5000, permanent: false })
            })
            .catch(err => console.log(err))
        },
	}
}
</script>
<style scoped>
.card-title {
    text-overflow:ellipsis;
    white-space:nowrap;
    word-wrap:normal;
    width:100%;
    overflow:hidden;
}
.card-text {
    text-overflow:ellipsis;
    white-space:nowrap;
    word-wrap:normal;
    width:100%;
    overflow:hidden;
}
.card-img-overlay {
    white-space: nowrap;
    overflow:hidden;
    display:none;
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
