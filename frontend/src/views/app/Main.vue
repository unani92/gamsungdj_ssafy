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
                                            <span class="glyph-icon simple-icon-control-play mr-3" style="font-size:x-large; cursor:pointer;" @click="addToPlaylistAndPlayNotify(data)"></span>
                                            <span v-if="isLiked(data)" :id="data.id" class="glyph-icon simple-icon-heart mr-3 liked" style="font-size:x-large; cursor:pointer;" @click="songLike"></span>
                                            <span v-else :id="data.id" class="glyph-icon simple-icon-heart mr-3" style="font-size:x-large; cursor:pointer;" @click="songLike"></span>
                                            <span v-if="!isLoggedin" class="glyph-icon simple-icon-playlist mr-3" style="font-size:x-large; cursor:pointer;" @click="addToPlaylistAndNotify(data)"></span>
                                            <b-dropdown v-else variant="empty" toggle-class="p-0 m-0" no-caret style="position:absolute;">
                                                <template slot="button-content">
                                                    <span class="glyph-icon simple-icon-playlist text-white" style="font-size:x-large; cursor:pointer;"></span>
                                                </template>
                                                <b-dropdown-item @click="addToPlaylistAndNotify(data)">현재 재생목록</b-dropdown-item>
                                                <b-dropdown-item v-for="(playlist, index) in userPlayList" :key="index" @click="addToUserPlaylist(data, playlist, index)">{{ playlist.name }}</b-dropdown-item>
                                            </b-dropdown>
                                        </div>
                                        <router-link :to='"songDetail/"+data.id'><h5 class="card-title text-white">{{ data.name }}</h5></router-link>
										<router-link :to='"artistDetail/"+data.artist[index].id'  v-for="(artist, index) in data.artist" :key="index">
                                            <p class="card-text text-white">{{ artist.name }}</p>
										</router-link>
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
                                            <span class="glyph-icon simple-icon-control-play mr-3" style="font-size:x-large; cursor:pointer;" @click="addToPlaylistAndPlayNotify(data)"></span>
                                            <span v-if="isLiked(data)" :id="data.id" class="glyph-icon simple-icon-heart mr-3 liked" style="font-size:x-large; cursor:pointer;" @click="songLike"></span>
                                            <span v-else :id="data.id" class="glyph-icon simple-icon-heart mr-3" style="font-size:x-large; cursor:pointer;" @click="songLike"></span>
                                            <span v-if="!isLoggedin" class="glyph-icon simple-icon-playlist mr-3" style="font-size:x-large; cursor:pointer;" @click="addToPlaylistAndNotify(data)"></span>
                                            <b-dropdown v-else variant="empty" dropup toggle-class="p-0 m-0" no-caret style="position:absolute;">
                                                <template slot="button-content">
                                                    <span class="glyph-icon simple-icon-playlist text-white" style="font-size:x-large; cursor:pointer;"></span>
                                                </template>
                                                <b-dropdown-item @click="addToPlaylistAndNotify(data)">현재 재생목록</b-dropdown-item>
                                                <b-dropdown-item v-for="(playlist, index) in userPlayList" :key="index" @click="addToUserPlaylist(data, playlist, index)">{{ playlist.name }}</b-dropdown-item>
                                            </b-dropdown>
                                        </div>
										<router-link :to='"songDetail/"+data.id'><h5 class="card-title text-white">{{ data.name }}</h5></router-link>
										<router-link :to='"artistDetail/"+data.artist[index].id'  v-for="(artist, index) in data.artist" :key="index">
                                            <p class="card-text text-white">{{ artist.name }}</p>
										</router-link>
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
                                            <span class="glyph-icon simple-icon-control-play mr-3" style="font-size:x-large; cursor:pointer;" @click="addToPlaylistAndPlayNotify(data)"></span>
                                            <span v-if="isLiked(data)" :id="data.id" class="glyph-icon simple-icon-heart mr-3 liked" style="font-size:x-large; cursor:pointer;" @click="songLike"></span>
                                            <span v-else :id="data.id" class="glyph-icon simple-icon-heart mr-3" style="font-size:x-large; cursor:pointer;" @click="songLike"></span>
                                            <span v-if="!isLoggedin" class="glyph-icon simple-icon-playlist mr-3" style="font-size:x-large; cursor:pointer;" @click="addToPlaylistAndNotify(data)"></span>
                                            <b-dropdown v-else variant="empty" toggle-class="p-0 m-0" no-caret style="position:absolute;">
                                                <template slot="button-content">
                                                    <span class="glyph-icon simple-icon-playlist text-white" style="font-size:x-large; cursor:pointer;"></span>
                                                </template>
                                                <b-dropdown-item @click="addToPlaylistAndNotify(data)">현재 재생목록</b-dropdown-item>
                                                <b-dropdown-item v-for="(playlist, index) in userPlayList" :key="index" @click="addToUserPlaylist(data, playlist, index)">{{ playlist.name }}</b-dropdown-item>
                                            </b-dropdown>
                                        </div>
                                        <router-link :to='"songDetail/"+data.id'><h5 class="card-title text-white">{{ data.name }}</h5></router-link>
										<router-link :to='"artistDetail/"+data.artist[index].id'  v-for="(artist, index) in data.artist" :key="index">
                                            <p class="card-text text-white">{{ artist.name }}</p>
										</router-link>
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
                                            <span class="glyph-icon simple-icon-control-play mr-3" style="font-size:x-large; cursor:pointer;" @click="addToPlaylistAndPlayNotify(data)"></span>
                                            <span v-if="isLiked(data)" :id="data.id" class="glyph-icon simple-icon-heart mr-3 liked" style="font-size:x-large; cursor:pointer;" @click="songLike"></span>
                                            <span v-else :id="data.id" class="glyph-icon simple-icon-heart mr-3" style="font-size:x-large; cursor:pointer;" @click="songLike"></span>
                                            <span v-if="!isLoggedin" class="glyph-icon simple-icon-playlist mr-3" style="font-size:x-large; cursor:pointer;" @click="addToPlaylistAndNotify(data)"></span>
                                            <b-dropdown v-else variant="empty" dropup toggle-class="p-0 m-0" no-caret style="position:absolute;">
                                                <template slot="button-content">
                                                    <span class="glyph-icon simple-icon-playlist text-white" style="font-size:x-large; cursor:pointer;"></span>
                                                </template>
                                                <b-dropdown-item @click="addToPlaylistAndNotify(data)">현재 재생목록</b-dropdown-item>
                                                <b-dropdown-item v-for="(playlist, index) in userPlayList" :key="index" @click="addToUserPlaylist(data, playlist, index)">{{ playlist.name }}</b-dropdown-item>
                                            </b-dropdown>
                                        </div>
                                        <router-link :to='"songDetail/"+data.id'><h5 class="card-title text-white">{{ data.name }}</h5></router-link>
										<router-link :to='"artistDetail/"+data.artist[index].id'  v-for="(artist, index) in data.artist" :key="index">
                                            <p class="card-text text-white">{{ artist.name }}</p>
										</router-link>
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
                                            <span class="glyph-icon simple-icon-control-play mr-3" style="font-size:x-large; cursor:pointer;" @click="addToPlaylistAndPlayNotify(data)"></span>
                                            <span v-if="isLiked(data)" :id="data.id" class="glyph-icon simple-icon-heart mr-3 liked" style="font-size:x-large; cursor:pointer;" @click="songLike"></span>
                                            <span v-else :id="data.id" class="glyph-icon simple-icon-heart mr-3" style="font-size:x-large; cursor:pointer;" @click="songLike"></span>
                                            <span v-if="!isLoggedin" class="glyph-icon simple-icon-playlist mr-3" style="font-size:x-large; cursor:pointer;" @click="addToPlaylistAndNotify(data)"></span>
                                            <b-dropdown v-else variant="empty" toggle-class="p-0 m-0" no-caret style="position:absolute;">
                                                <template slot="button-content">
                                                    <span class="glyph-icon simple-icon-playlist text-white" style="font-size:x-large; cursor:pointer;"></span>
                                                </template>
                                                <b-dropdown-item @click="addToPlaylistAndNotify(data)">현재 재생목록</b-dropdown-item>
                                                <b-dropdown-item v-for="(playlist, index) in userPlayList" :key="index" @click="addToUserPlaylist(data, playlist, index)">{{ playlist.name }}</b-dropdown-item>
                                            </b-dropdown>
                                        </div>
                                        <router-link :to='"songDetail/"+data.id'><h5 class="card-title text-white">{{ data.name }}</h5></router-link>
										<router-link :to='"artistDetail/"+data.artist[index].id'  v-for="(artist, index) in data.artist" :key="index">
                                            <p class="card-text text-white">{{ artist.name }}</p>
										</router-link>
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
                                            <span class="glyph-icon simple-icon-control-play mr-3" style="font-size:x-large; cursor:pointer;" @click="addToPlaylistAndPlayNotify(data)"></span>
                                            <span @click="songLike" :id="data.id" v-if="isLiked(data)" class="glyph-icon simple-icon-heart mr-3 liked" style="cursor:pointer; font-size:x-large;"></span>
                                            <span @click="songLike" :id='data.id' v-else class="glyph-icon simple-icon-heart mr-3" style="cursor:pointer; font-size:x-large;"></span>
                                            <span v-if="!isLoggedin" class="glyph-icon simple-icon-playlist mr-3" style="font-size:x-large; cursor:pointer;" @click="addToPlaylistAndNotify(data)"></span>
                                            <b-dropdown v-else variant="empty" dropup toggle-class="p-0 m-0" no-caret style="position:absolute;">
                                                <template slot="button-content">
                                                    <span class="glyph-icon simple-icon-playlist text-white" style="font-size:x-large; cursor:pointer;"></span>
                                                </template>
                                                <b-dropdown-item @click="addToPlaylistAndNotify(data)">현재 재생목록</b-dropdown-item>
                                                <b-dropdown-item v-for="(playlist, index) in userPlayList" :key="index" @click="addToUserPlaylist(data, playlist, index)">{{ playlist.name }}</b-dropdown-item>
                                            </b-dropdown>
                                        </div>
                                        <router-link :to='"songDetail/"+data.id'><h5 class="card-title text-white">{{ data.name }}</h5></router-link>
										<router-link :to='"artistDetail/"+data.artist[index].id'  v-for="(artist, index) in data.artist" :key="index">
                                            <p class="card-text text-white">{{ artist.name }}</p>
										</router-link>
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
    <div v-if="climateRecommend">
    <b-row>
        <b-colxx xxs="12">
            <a href="#" @click.prevent="getWeather"><h5 class="mb-4 card-title">오늘 같은 날에는 ></h5></a>
        </b-colxx>
        <b-colxx xxs="12" class="mb-4 pl-0 pr-0">
            <glide-component :settings="glideNoControlsSettings">
                <div v-for="(data, index) in climateRecommend" :key="index" class="pr-3 pl-3 mb-4 glide__slide">
                    <b-card no-body>
                        <div class="position-relative">
                            <a href="#" @click.prevent="search(data.id, 'song')"><img class="card-img-top" :src="data.img" alt="Card cap" /></a>
                        </div>
                        <b-card-body>
                            <a href="#" @click.prevent="search(data.id, 'song')"><h6 class="mb-4 ellipsis">{{ data.name }}</h6></a>
                            <a href="#" @click.prevent="search(data.artist[0].id, 'artist')"><p class="text-muted mb-0 font-weight-light ellipsis">{{ data.artist[0].name }}</p></a>
                            <div class="mt-4" style="font-size:x-large;">
                                <span class="glyph-icon simple-icon-control-play mr-3" style="font-size:x-large; cursor:pointer;" @click="addToPlaylistAndPlayNotify(data)"></span>
                                <span @click="songLike" :id="data.id" v-if="isLiked(data)" class="glyph-icon simple-icon-heart mr-3 liked" style="cursor:pointer;"></span>
                                <span @click="songLike" :id='data.id' v-else class="glyph-icon simple-icon-heart mr-3" style="cursor:pointer;"></span>
                                <span v-if="!isLoggedin" class="glyph-icon simple-icon-playlist mr-3" style="font-size:x-large; cursor:pointer;" @click="addToPlaylistAndNotify(data)"></span>
                                <b-dropdown v-else variant="empty" dropup toggle-class="p-0 m-0" no-caret>
                                    <template slot="button-content">
                                        <span class="glyph-icon simple-icon-playlist text-color" style="font-size:x-large; cursor:pointer;"></span>
                                    </template>
                                    <b-dropdown-item @click="addToPlaylistAndNotify(data)">현재 재생목록</b-dropdown-item>
                                    <b-dropdown-item v-for="(playlist, index) in userPlayList" :key="index" @click="addToUserPlaylist(data, playlist, index)">{{ playlist.name }}</b-dropdown-item>
                                </b-dropdown>
                            </div>
                        </b-card-body>
                    </b-card>
                </div>
            </glide-component>

        </b-colxx>
    </b-row>
    </div>
	<!-- 날씨 매칭 추천 끝 -->

	<!-- 시간 매칭 추천 시작 -->
    <div v-if="timeRecommend">
    <b-row >
        <b-colxx xxs="12">
            <a href="#" id="timeRecommend" @click.prevent="getTimeRecommend"><h5 class="mb-4 card-title">이시간에는 ></h5></a>
        </b-colxx>
        <b-colxx xxs="12" class="mb-4 pl-0 pr-0">
            <glide-component :settings="glideNoControlsSettings">
                <div v-for="(data, index) in timeRecommend" :key="index" class="pr-3 pl-3 mb-4 glide__slide">
                    <b-card no-body>
                        <div class="position-relative">
                            <a href="#" @click.prevent="search(data.id, 'song')"><img class="card-img-top" :src="data.img" alt="Card cap" /></a>
                        </div>
                        <b-card-body>
                            <a href="#" @click.prevent="search(data.id, 'song')"><h6 class="mb-4 ellipsis">{{ data.name }}</h6></a>
                            <a href="#" @click.prevent="search(data.artist[0].id, 'artist')"><p class="text-muted mb-0 font-weight-light ellipsis">{{ data.artist[0].name }}</p></a>
                            <div class="mt-4" style="font-size:x-large;">
                                <span class="glyph-icon simple-icon-control-play mr-3" style="font-size:x-large; cursor:pointer;" @click="addToPlaylistAndPlayNotify(data)"></span>
                                <span @click="songLike" :id="data.id" v-if="isLiked(data)" class="glyph-icon simple-icon-heart mr-3 liked" style="cursor:pointer;"></span>
                                <span @click="songLike" :id='data.id' v-else class="glyph-icon simple-icon-heart mr-3" style="cursor:pointer;"></span>
                                <span v-if="!isLoggedin" class="glyph-icon simple-icon-playlist mr-3" style="font-size:x-large; cursor:pointer;" @click="addToPlaylistAndNotify(data)"></span>
                                <b-dropdown v-else variant="empty" dropup toggle-class="p-0 m-0" no-caret>
                                    <template slot="button-content">
                                        <span class="glyph-icon simple-icon-playlist text-color" style="font-size:x-large; cursor:pointer;"></span>
                                    </template>
                                    <b-dropdown-item @click="addToPlaylistAndNotify(data)">현재 재생목록</b-dropdown-item>
                                    <b-dropdown-item v-for="(playlist, index) in userPlayList" :key="index" @click="addToUserPlaylist(data, playlist, index)">{{ playlist.name }}</b-dropdown-item>
                                </b-dropdown>
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
import { mapState, mapGetters, mapActions } from 'vuex'
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
        this.getWeather()
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
            timeRecommend: null,
            climateRecommend: null,
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
        'userPlayList',
        'user',
        'climate',
      ]),
      ...mapGetters(['config'])
    },
	methods: {
        ...mapActions(["addToPlaylistAndPlay", "addToPlaylist", "setClimate"]),
        async addToPlaylistAndPlayNotify(data) {
            for(let i=0; i<this.playlist.length; i++) {
                if(this.playlist[i].id == data.id) {
                    this.$notify('warning', "재생 목록에 이미 포함 된 곡입니다.", data.name+" - "+data.artist[0].name, { duration: 4000, permanent: false })
                    return
                }
            }
            this.addToPlaylistAndPlay(data)
            this.$notify('primary', "재생 중인 곡", data.name+" - "+data.artist[0].name, { duration: 4000, permanent: false })
        },
        async addToPlaylistAndNotify(data) {
            for(let i=0; i<this.playlist.length; i++) {
                if(this.playlist[i].id == data.id) {
                    this.$notify('warning', "재생 목록에 이미 포함 된 곡입니다.", data.name+" - "+data.artist[0].name, { duration: 4000, permanent: false })
                    return
                }
            }
            this.addToPlaylist(data)
            this.$notify('primary', "재생 목록에 추가 되었습니다.", data.name+" - "+data.artist[0].name, { duration: 4000, permanent: false })
        },
        addToUserPlaylist(data, playlist, index) {
            for(let i=0; i<playlist.song.length; i++) {
                if(playlist.song[i].id == data.id) {
                    this.$notify('warning', "사용자 재생 목록에 이미 포함 된 곡입니다.", data.name+" - "+data.artist[0].name, { duration: 4000, permanent: false })
                    return
                }
            }
            http2
            .post(`playlist/${playlist.id}/song/`, {'songs': [data.id]}, this.config)
            .then((value)=> {
                this.$notify('primary', "사용자 재생 목록에 추가 되었습니다.", data.name+" - "+data.artist[0].name, { duration: 4000, permanent: false })
                this.userPlayList[index].song.push(data)
            })
        },
        async getTimeRecommend() {
            const { data: { data } } = await http.get('recommend/time/', this.config)
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
            if (this.user)
                return this.user.like_songs.includes(data.id)
            else
                return false
        },
        async songLike(e) {
            if (this.isLoggedin) {
                const { id } = e.target
                const { data: { liked } } = await http.post(`song/${id}/like/`, '',this.config)
                if (liked) {
                    // this.$notify('primary', "좋아요", this.song.name+" - "+this.song.artist[0].name, { duration: 5000, permanent: false });
                    this.$store.state.user.like_songs.push(Number(id))
                }
                else {
                    // this.$notify('primary', "좋아요 취소", '', { duration: 5000, permanent: false });
                    this.$store.state.user.like_songs = this.$store.state.user.like_songs.filter(song => {
                        return song !== Number(id)
                    })
                }
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
        search(word, detail){
            this.$router.push(`/A505/${detail}Detail/${word}`)
        },
        getWeather(){
          if (this.climate === null) {
            if(navigator.geolocation) {
              var apikey = '28de7356f776313b2637236fb7961f04'
              navigator.geolocation.getCurrentPosition(position => {
                // alert(position.coords.latitude + ' ' +position.coords.longitude)
                http
                  .get('http://api.openweathermap.org/data/2.5/weather?lat='+position.coords.latitude+'&lon='+position.coords.longitude+'&appid='+apikey)
                  .then((res) => {
                    let weather = res.data.weather[0].description
                    this.setClimate(weather)
                    weather = weather.split(' ')
                    console.log(weather)
                    if (weather.includes('rain') || weather.includes('thunderstorm')) {
                      http.get('rain/')
                        .then(res => {
                          console.log(res.data)
                        })
                        .catch(e => console.log(e))
                    } else {
                      http.get('recommend/time/')
                        .then(res => {
                        this.climateRecommend = res.data.data
                      })
                    }
                  })
              }, error => {
                console.log(error)
                http.get('recommend/time/')
                  .then(res => {
                  this.climateRecommend = res.data.data
                })
              }, {
                enableHighAccuracy: false,
                maximumAge: 0,
                timeout: Infinity
              })
            }
            else {
              http.get('recommend/time/')
                .then(res => {
                this.climateRecommend = res.data.data
              })
            }
          } else {
            let weather = this.climate.split(' ')
            if (weather.includes('rain') || weather.includes('thunderstorm')) {
              http.get('rain/')
                .then(res => {
                  this.climateRecommend = res.data
                })
                .catch(e => console.log(e))
            } else {
              http.get('recommend/time/')
                .then(res => {
                this.climateRecommend = res.data.data
              })
                .catch(e => console.log(e))
            }
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
