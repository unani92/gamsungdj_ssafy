<template>
    <!--
        참고
        https://developers.google.com/youtube/iframe_api_reference#Events 
        https://www.npmjs.com/package/vue-youtube
        
        문제점
        1. 컬러가 정해져 있지 않아서 재생 중인 곡을 선택 했을 때 css 를 변경하면 다시 복구할 수 없음
        2. index 로 접근하기 때문에 재생 중 다른 플레이리스트를 가져왔을 때 문제가 생김
        3. vue-perfect-scrollbar가 안됨
    -->
    <div class="row aligner">
        <div class="col-sm-9 aligner" style="height:inherit;">
            <b-tabs card no-fade style="height:100%; width:100%;">
                <b-tab title="Player" active title-item-class="w-50 text-center">
                    <div class="player-wrapper">
                        <div class="float-right">
                            <switches v-model="playerToggleFlag" theme="custom" color="primary-inverse"></switches>
                        </div>
                        <div class="player" v-show="playerToggleFlag">
                            <youtube id="youtube" :video-id="selectedSong.src" :player-vars="playerVars" @ended="ended" ref="youtube"></youtube>
                        </div>
                        <player v-show="!playerToggleFlag" :selectedSong="selectedSong" />
                    </div>
                </b-tab>
                <b-tab title="Analyze" title-item-class="w-50 text-center">
                        <analyze />
                </b-tab>
            </b-tabs>
        </div>

        <!-- 플레이리스트 시작 -->
        <div class="col-sm-3" style="height:inherit; overflow:auto; overflow-x: hidden; white-space: nowrap;">
            <!-- <vue-perfect-scrollbar :settings="{ suppressScrollX: true, wheelPropagation: false }"> -->
            <b-row>
                <b-colxx xxs="12" class="mt-3">
                    <b-card class="mb-3">
                        <!-- 헤더 시작 -->
                        <h3 style="display:inline-block; margin-top:12px">재생 목록</h3>
                        <span v-if="this.$store.state.user">
                        <b-dropdown id="ddown1" text="재생 목록 불러오기" variant="outline-secondary" class="float-right">
                            <b-dropdown-header>나의 재생 목록</b-dropdown-header>
                            <b-dropdown-divider></b-dropdown-divider>
                            <b-dropdown-item v-for="(data, index) in playlistData" :key="index" @click="selectPlaylist(index)">{{ data.title }}</b-dropdown-item>
                        </b-dropdown>
                        </span>
                        <!-- 헤더 끝 --><hr>

                        <!-- 바디 시작 -->
                        <div class="playlist-item-wrapper" v-for="(data, index) in playlist" :key="index">
                            <!-- 재생 중인 곡 표시 시작-->
                            <!-- <div class="d-flex flex-row" style="padding:10px; cursor:pointer; position:absolute; width:100%">
                                <music-bar />
                            </div> -->
                            <!-- 재생 중인 곡 표시 끝 -->
                            <div class="d-flex flex-row" style="padding:10px; cursor:pointer" @click="selectSong(index, data)">
                                <img :src="data.img" :alt="data.name" class="list-thumbnail border-0" />
                                <div class="pl-3 pt-2 pr-2 pb-2">
                                    <p class="list-item-heading">{{ data.name }}</p>
                                    <div class="pr-4">
                                        <p class="text-muted mb-1 text-small">{{ data.artist[0].name }}</p>
                                    </div>
                                    <!-- <div class="text-primary text-small font-weight-medium d-none d-sm-block">{{ data.artist[0].name }}</div> -->
                                </div>
                            </div>
                        </div>
                        <!-- 바디 끝 -->
                    </b-card>
                </b-colxx>
            </b-row>
            <!-- </vue-perfect-scrollbar> -->
        </div>
        <!-- 플레이리스트 끝 -->
    </div>
</template>

<script>
import MusicBar from "../../components/Playlist/Musicbar"
import Player from "../../components/Playlist/Player"
import Analyze from "../../components/Playlist/Analyze"
import { playlistData } from "../../data/playlist"
import { mapState } from "vuex"
import Switches from "vue-switches";
import http from "../../utils/http-common"

export default {
    props: ['state'],
    components:{
        'music-bar': MusicBar,
        'player': Player,
        'analyze': Analyze,
        switches: Switches
    },
    data() {
        return {
            playerVars: {
                autoplay: 1
            },
            selectedSong: {
                index: '',
                img: '',
                title: '',
                artist: '',
                src: '',
            },
            playlistData,
            playerToggleFlag: false,
        }
    },
    computed: {
        ...mapState([
            'playlist',
            'playerControl'
        ]),
        player() {
            return this.$refs.youtube.player
        }
    },
    watch: {
        playerControl: function(state) {
            if(state === "play") {
                if(this.playlist.length == 0) {
                    this.$notify('info', "재생 목록이 비어있습니다.", "", "",{ duration: 5000, permanent: false })
                    this.$store.state.visiblePlayButton = true
                    this.$store.state.visiblePauseButton = false
                }
                else if(this.selectedSong.src === ''){
                    this.selectedSong.index = 0;
                    this.selectedSong.img = this.playlist[this.selectedSong.index].img
                    this.selectedSong.title = this.playlist[this.selectedSong.index].name
                    this.selectedSong.artist = this.playlist[this.selectedSong.index].artist[0].name
                    this.selectedSong.src = this.playlist[this.selectedSong.index].src
                    this.player.playVideo()
                }
                else{
                    this.player.playVideo()
                }
            }
            else if(state === "pause")
                this.player.pauseVideo()
            else if(state === "prev") {
                if(this.selectedSong.index == 0) {
                    this.selectedSong.index = this.playlist.length-1
                    this.selectedSong.img = this.playlist[this.selectedSong.index].img
                    this.selectedSong.title = this.playlist[this.selectedSong.index].name
                    this.selectedSong.artist = this.playlist[this.selectedSong.index].artist[0].name
                    this.selectedSong.src = this.playlist[this.selectedSong.index].src
                    this.player.playVideo()
                }
                else if(this.selectedSong.src === ''){
                    this.selectedSong.index = 0;
                    this.selectedSong.img = this.playlist[this.selectedSong.index].img
                    this.selectedSong.title = this.playlist[this.selectedSong.index].name
                    this.selectedSong.artist = this.playlist[this.selectedSong.index].artist[0].name
                    this.selectedSong.src = this.playlist[this.selectedSong.index].src
                    this.player.playVideo()
                }
                else {
                    this.selectedSong.index = this.selectedSong.index-1
                    this.selectedSong.img = this.playlist[this.selectedSong.index].img
                    this.selectedSong.title = this.playlist[this.selectedSong.index].name
                    this.selectedSong.artist = this.playlist[this.selectedSong.index].artist[0].name
                    this.selectedSong.src = this.playlist[this.selectedSong.index].src
                    this.player.playVideo()
                }
            }
            else if(state === "next") {
                if(this.selectedSong.index == this.playlist.length-1) {
                    this.selectedSong.index = 0
                    this.selectedSong.img = this.playlist[this.selectedSong.index].img
                    this.selectedSong.title = this.playlist[this.selectedSong.index].name
                    this.selectedSong.artist = this.playlist[this.selectedSong.index].artist[0].name
                    this.selectedSong.src = this.playlist[this.selectedSong.index].src
                    this.player.playVideo()
                }
                else if(this.selectedSong.src === ''){
                    this.selectedSong.index = 0;
                    this.selectedSong.img = this.playlist[this.selectedSong.index].img
                    this.selectedSong.title = this.playlist[this.selectedSong.index].name
                    this.selectedSong.artist = this.playlist[this.selectedSong.index].artist[0].name
                    this.selectedSong.src = this.playlist[this.selectedSong.index].src
                    this.player.playVideo()
                }
                else {
                    this.selectedSong.index = this.selectedSong.index+1
                    this.selectedSong.img = this.playlist[this.selectedSong.index].img
                    this.selectedSong.title = this.playlist[this.selectedSong.index].name
                    this.selectedSong.artist = this.playlist[this.selectedSong.index].artist[0].name
                    this.selectedSong.src = this.playlist[this.selectedSong.index].src
                    this.player.playVideo()
                }
            }
            else if(state === "add") {
                this.selectedSong.index = 0;
                this.selectedSong.img = this.playlist[this.selectedSong.index].img
                this.selectedSong.title = this.playlist[this.selectedSong.index].name
                this.selectedSong.artist = this.playlist[this.selectedSong.index].artist[0].name
                this.selectedSong.src = this.playlist[this.selectedSong.index].src
            }
            this.$store.state.playerControl = ''
        }
    },
    methods: {
        selectSong(index, data) {
            this.selectedSong.index = index
            this.selectedSong.img = data.img
            this.selectedSong.title = data.name
            this.selectedSong.artist = data.artist[0].name
            this.selectedSong.src = data.src
            this.$store.state.visiblePlayButton = false
            this.$store.state.visiblePauseButton = true
        },
        ended() {
            if(this.selectedSong.index >= this.playlist.length-1) {
                this.selectedSong.index = 0
                this.selectedSong.img = this.playlist[0].img
                this.selectedSong.title = this.playlist[0].name
                this.selectedSong.artist = this.playlist[0].artist[0].name
                this.selectedSong.src = this.playlist[0].src
                this.player.playVideo()
            }
            else {
                this.selectedSong.index = this.selectedSong.index+1
                this.selectedSong.img = this.playlist[this.selectedSong.index].img
                this.selectedSong.title = this.playlist[this.selectedSong.index].name
                this.selectedSong.artist = this.playlist[this.selectedSong.index].artist[0].name
                this.selectedSong.src = this.playlist[this.selectedSong.index].src
                this.player.playVideo()
            }
        },
        selectPlaylist(index) {
            for(let i=0; i<this.playlistData[index].playlist.length; i++){
                this.playlist.push(this.playlistData[index].playlist[i])
            }
        }
    }
}
</script>
<style>
.aligner {
    display: flex;
    align-items: center;
    justify-content: center;
    margin: 0px;
}
.playlist-item-wrapper:hover {
    background: rgba(0,0,0,.7);
    opacity: .7;
}
.player-wrapper {
  height: 460px;
  width: 640px;
  position: absolute;
  -webkit-touch-callout: none;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
  top: 55%;
  left: 50%;
  transform: translate(-50%, -50%);
  -webkit-transform: translate(-50%, -50%);
}
</style>