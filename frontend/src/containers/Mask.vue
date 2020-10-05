<template>
    <!--
        https://developers.google.com/youtube/iframe_api_reference#Events
        https://www.npmjs.com/package/vue-youtube
        https://codepen.io/OPiMedia/pen/WrzLQw
        vue-perfect-scroll
    -->
    <div class="row aligner">
        <div class="col-sm-9 aligner" style="height:inherit;">
            <b-tabs card no-fade style="height:100%; width:100%;">
                <b-tab title="Player" active title-item-class="w-50 text-center">
                    <div class="player-wrapper">         
                        <div class="float-right">
                            <!-- <input id="YouTube-player-progress" type="range" v-model="selectedSong.currentTime" min="0" max="100" @change="youTubePlayerCurrentTimeChange">
                            <label for="YouTube-player-progress">duration</label>
                            <input id="YouTube-player-volume" type="range" min="0" max="100" v-model="selectedSong.volume" @change="youTubePlayerVolumeChange">
                            <label for="YouTube-player-volume">volume</label> -->
                            <switches v-model="playerToggleFlag" theme="custom" color="primary-inverse"></switches>
                        </div>
                        <div class="player" v-show="playerToggleFlag">
                            <youtube id="youtube" :video-id="selectedSong.src" :player-vars="playerVars" @ended="ended(selectedSong.index)" @error="error()" ref="youtube"></youtube>
                        </div>
                        <player v-show="!playerToggleFlag" />
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

                        <h3 style="display:inline-block; margin-top:12px">재생 목록</h3>
                        <span v-if="this.$store.state.user">
                            <b-dropdown id="ddown1" text="재생 목록 불러오기" variant="outline-secondary" class="float-right">
                                <b-dropdown-header>나의 재생 목록</b-dropdown-header>
                                <b-dropdown-divider></b-dropdown-divider>
                                <b-dropdown-item v-for="(data, index) in userPlayList" :key="index" @click="selectPlaylist(index)">{{ data.name }}</b-dropdown-item>
                            </b-dropdown>
                        </span><hr>

                        <div class="playlist-item-wrapper" v-for="(data, index) in playlist" :key="index">
                            <div class="d-flex flex-row ellipsis " style="padding:10px; cursor:pointer;"
                                @click="selectSong(index, data)"
                                @mouseover="showOverlay(index)"
                                @mouseout="hideOverlay(index)"
                            >

                                <!-- 재생 중인 곡만 보이는 부분 -->
                                <music-bar style="position:relative; left:16px; top:16px; display:none;" :id="'playlist-item-playing'+index" />

                                <!-- 마우스 오버시 보이는 부분 -->
                                <span style="position:absolute; left:85%; float:right; display:none;" :id="'playlist-item-overlay'+index" @click="remove(index)"><font size="6">x</font></span>

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
                    </b-card>
                </b-colxx>
            </b-row>
            <!-- </vue-perfect-scrollbar> -->
        </div>
        <!-- 플레이리스트 끝 -->
    </div>
</template>

<script>
import MusicBar from "../components/Playlist/Musicbar"
import Player from "../components/Playlist/Player"
import Analyze from "../components/Playlist/Analyze"
import Switches from "vue-switches"
import http from "../utils/http-common"
import { mapGetters, mapMutations, mapActions, mapState } from "vuex"


const youtubeURL = 'https://www.googleapis.com/youtube/v3/search'
const API_KEY = process.env.VUE_APP_YOUTUBE_API_KEY

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
                autoplay: 1,
                controls: 1
            },
            playerToggleFlag: false,
        }
    },
    mounted() {
        setInterval(this.synchronize, 1000);
    },
    computed: {
        ...mapState([
            'playlist',
            'playerControl',
            'selectedSong',
            'userPlayList'
        ]),
        player() {
            return this.$refs.youtube.player
        }
    },
    watch: {
        playerControl: function(state) {
            if(state === "play") {
                if(this.playlist.length == 0) {
                    this.$notify('info', "재생 목록이 비어있습니다.", "", "",{ duration: 4000, permanent: false })
                    this.$store.state.visiblePlayButton = true
                    this.$store.state.visiblePauseButton = false
                }
                else if(this.selectedSong.src === ''){
                    this.selectedSong.index = 0
                    this.markPlayingIndex(this.selectedSong.index)
                    this.selectedSong.img = this.playlist[this.selectedSong.index].img
                    this.selectedSong.title = this.playlist[this.selectedSong.index].name
                    this.selectedSong.artist = this.playlist[this.selectedSong.index].artist[0].name
                    this.selectedSong.src = this.playlist[this.selectedSong.index].src
                    this.selectedSong.songID = this.playlist[this.selectedSong.index].id
                    this.selectedSong.singerID = this.playlist[this.selectedSong.index].artist[0].id
                    http
                    .get("/song/"+this.playlist[this.selectedSong.index].id+"/comment/")
                    .then((res) => {
                        this.selectedSong.comments = res.data
                    })
                }
                else{
                    this.player.playVideo()
                }
            }
            else if(state === "pause")
                this.player.pauseVideo()
            else if(state === "prev") {
                if(this.playlist.length == 0) {
                    this.$notify('info', "재생 목록이 비어있습니다.", "", "",{ duration: 5000, permanent: false })
                    this.$store.state.visiblePlayButton = true
                    this.$store.state.visiblePauseButton = false
                }
                else if(this.selectedSong.index == 0) {
                    this.unmarkPlayingIndex(this.selectedSong.index)
                    this.selectedSong.index = this.playlist.length-1
                    this.markPlayingIndex(this.selectedSong.index)
                    this.selectedSong.img = this.playlist[this.selectedSong.index].img
                    this.selectedSong.title = this.playlist[this.selectedSong.index].name
                    this.selectedSong.artist = this.playlist[this.selectedSong.index].artist[0].name
                    this.selectedSong.src = this.playlist[this.selectedSong.index].src
                    this.selectedSong.songID = this.playlist[this.selectedSong.index].id
                    this.selectedSong.singerID = this.playlist[this.selectedSong.index].artist[0].id
                    http
                    .get("/song/"+this.playlist[this.selectedSong.index].id+"/comment/")
                    .then((res) => {
                        this.selectedSong.comments = res.data
                    })
                }
                else if(this.selectedSong.src === ''){
                    this.selectedSong.index = 0
                    this.markPlayingIndex(this.selectedSong.index)
                    this.selectedSong.img = this.playlist[this.selectedSong.index].img
                    this.selectedSong.title = this.playlist[this.selectedSong.index].name
                    this.selectedSong.artist = this.playlist[this.selectedSong.index].artist[0].name
                    this.selectedSong.src = this.playlist[this.selectedSong.index].src
                    this.selectedSong.songID = this.playlist[this.selectedSong.index].id
                    this.selectedSong.singerID = this.playlist[this.selectedSong.index].artist[0].id
                    http
                    .get("/song/"+this.playlist[this.selectedSong.index].id+"/comment/")
                    .then((res) => {
                        this.selectedSong.comments = res.data
                    })
                }
                else {
                    this.unmarkPlayingIndex(this.selectedSong.index)
                    this.selectedSong.index = this.selectedSong.index-1
                    this.markPlayingIndex(this.selectedSong.index)
                    this.selectedSong.img = this.playlist[this.selectedSong.index].img
                    this.selectedSong.title = this.playlist[this.selectedSong.index].name
                    this.selectedSong.artist = this.playlist[this.selectedSong.index].artist[0].name
                    this.selectedSong.src = this.playlist[this.selectedSong.index].src
                    this.selectedSong.songID = this.playlist[this.selectedSong.index].id
                    this.selectedSong.singerID = this.playlist[this.selectedSong.index].artist[0].id
                    http
                    .get("/song/"+this.playlist[this.selectedSong.index].id+"/comment/")
                    .then((res) => {
                        this.selectedSong.comments = res.data
                    })
                }
            }
            else if(state === "next") {
                if(this.playlist.length == 0) {
                    this.$notify('info', "재생 목록이 비어있습니다.", "", "",{ duration: 5000, permanent: false })
                    this.$store.state.visiblePlayButton = true
                    this.$store.state.visiblePauseButton = false
                }
                else if(this.selectedSong.index == this.playlist.length-1) {
                    this.unmarkPlayingIndex(this.selectedSong.index)
                    this.selectedSong.index = 0
                    this.markPlayingIndex(this.selectedSong.index)
                    this.selectedSong.img = this.playlist[this.selectedSong.index].img
                    this.selectedSong.title = this.playlist[this.selectedSong.index].name
                    this.selectedSong.artist = this.playlist[this.selectedSong.index].artist[0].name
                    this.selectedSong.src = this.playlist[this.selectedSong.index].src
                    this.selectedSong.songID = this.playlist[this.selectedSong.index].id
                    this.selectedSong.singerID = this.playlist[this.selectedSong.index].artist[0].id
                    http
                    .get("/song/"+this.playlist[this.selectedSong.index].id+"/comment/")
                    .then((res) => {
                        this.selectedSong.comments = res.data
                    })
                }
                else if(this.selectedSong.src === ''){
                    this.selectedSong.index = 0
                    this.markPlayingIndex(this.selectedSong.index)
                    this.selectedSong.img = this.playlist[this.selectedSong.index].img
                    this.selectedSong.title = this.playlist[this.selectedSong.index].name
                    this.selectedSong.artist = this.playlist[this.selectedSong.index].artist[0].name
                    this.selectedSong.src = this.playlist[this.selectedSong.index].src
                    this.selectedSong.songID = this.playlist[this.selectedSong.index].id
                    this.selectedSong.singerID = this.playlist[this.selectedSong.index].artist[0].id
                    http
                    .get("/song/"+this.playlist[this.selectedSong.index].id+"/comment/")
                    .then((res) => {
                        this.selectedSong.comments = res.data
                    })
                }
                else {
                    this.unmarkPlayingIndex(this.selectedSong.index)
                    this.selectedSong.index = this.selectedSong.index+1
                    this.markPlayingIndex(this.selectedSong.index)
                    this.selectedSong.img = this.playlist[this.selectedSong.index].img
                    this.selectedSong.title = this.playlist[this.selectedSong.index].name
                    this.selectedSong.artist = this.playlist[this.selectedSong.index].artist[0].name
                    this.selectedSong.src = this.playlist[this.selectedSong.index].src
                    this.selectedSong.songID = this.playlist[this.selectedSong.index].id
                    this.selectedSong.singerID = this.playlist[this.selectedSong.index].artist[0].id
                    http
                    .get("/song/"+this.playlist[this.selectedSong.index].id+"/comment/")
                    .then((res) => {
                        this.selectedSong.comments = res.data
                    })
                }
            }
            else if(state === "add") {
                if(this.playlist.length == 1 || this.selectedSong.index == -1) {
                    this.selectedSong.index = 0
                    this.markPlayingIndex(this.selectedSong.index)
                    this.selectedSong.img = this.playlist[this.selectedSong.index].img
                    this.selectedSong.title = this.playlist[this.selectedSong.index].name
                    this.selectedSong.artist = this.playlist[this.selectedSong.index].artist[0].name
                    this.selectedSong.src = this.playlist[this.selectedSong.index].src
                    this.selectedSong.songID = this.playlist[this.selectedSong.index].id
                    this.selectedSong.singerID = this.playlist[this.selectedSong.index].artist[0].id
                    http
                    .get("/song/"+this.playlist[this.selectedSong.index].id+"/comment/")
                    .then((res) => {
                        this.selectedSong.comments = res.data
                    })
                }
                else {
                    this.unmarkPlayingIndex(this.selectedSong.index)
                    this.selectedSong.index = 0
                    this.markPlayingIndex(this.selectedSong.index)
                    this.selectedSong.img = this.playlist[this.selectedSong.index].img
                    this.selectedSong.title = this.playlist[this.selectedSong.index].name
                    this.selectedSong.artist = this.playlist[this.selectedSong.index].artist[0].name
                    this.selectedSong.src = this.playlist[this.selectedSong.index].src
                    this.selectedSong.songID = this.playlist[this.selectedSong.index].id
                    this.selectedSong.singerID = this.playlist[this.selectedSong.index].artist[0].id
                    http
                    .get("/song/"+this.playlist[this.selectedSong.index].id+"/comment/")
                    .then((res) => {
                        this.selectedSong.comments = res.data
                    })
                }
                this.$store.state.visiblePlayButton = false
                this.$store.state.visiblePauseButton = true
            }
            this.$store.state.playerControl = ''
        }
    },
    methods: {
        ...mapActions(["addToPlaylistAndPlay", "addToPlaylist"]),
        selectSong(index, data) {
            console.log(this.playlist)
            if(this.selectedSong.index == -1) {
                this.selectedSong.index = index
                this.markPlayingIndex(this.selectedSong.index)
                this.selectedSong.img = data.img
                this.selectedSong.title = data.name
                this.selectedSong.artist = data.artist[0].name
                this.selectedSong.src = data.src
                this.selectedSong.songID = this.playlist[this.selectedSong.index].id
                this.selectedSong.singerID = this.playlist[this.selectedSong.index].artist[0].id
                this.$store.state.visiblePlayButton = false
                this.$store.state.visiblePauseButton = true
                console.log(this.playlist[this.selectedSong.index].id)
                http
                .get("/song/"+this.playlist[this.selectedSong.index].id+"/comment/")
                .then((res) => {
                    this.selectedSong.comments = res.data
                })
            }
            else {
                this.unmarkPlayingIndex(this.selectedSong.index)
                this.selectedSong.index = index
                this.markPlayingIndex(this.selectedSong.index)
                this.selectedSong.img = data.img
                this.selectedSong.title = data.name
                this.selectedSong.artist = data.artist[0].name
                this.selectedSong.src = data.src
                this.selectedSong.songID = this.playlist[this.selectedSong.index].id
                this.selectedSong.singerID = this.playlist[this.selectedSong.index].artist[0].id
                this.$store.state.visiblePlayButton = false
                this.$store.state.visiblePauseButton = true
                http
                .get("/song/"+this.playlist[this.selectedSong.index].id+"/comment/")
                .then((res) => {
                    this.selectedSong.comments = res.data
                })
            }
        },
        ended(index) {
            http.
            post('log/',
            {
                song: this.playlist[index].id
            }, this.$store.getters.config)
            .then((value) => {
            })
            if(this.selectedSong.index >= this.playlist.length-1) {
                this.unmarkPlayingIndex(this.selectedSong.index)
                this.selectedSong.index = 0
                this.markPlayingIndex(this.selectedSong.index)
                this.selectedSong.img = this.playlist[0].img
                this.selectedSong.title = this.playlist[0].name
                this.selectedSong.artist = this.playlist[0].artist[0].name
                this.selectedSong.src = this.playlist[0].src
                this.selectedSong.songID = this.playlist[this.selectedSong.index].id
                this.selectedSong.singerID = this.playlist[this.selectedSong.index].artist[0].id
                http
                    .get("/song/"+this.playlist[this.selectedSong.index].id+"/comment/")
                    .then((res) => {
                        this.selectedSong.comments = res.data
                    })
                this.player.playVideo()
            }
            else {
                this.unmarkPlayingIndex(this.selectedSong.index)
                this.selectedSong.index = this.selectedSong.index+1
                this.markPlayingIndex(this.selectedSong.index)
                this.selectedSong.img = this.playlist[this.selectedSong.index].img
                this.selectedSong.title = this.playlist[this.selectedSong.index].name
                this.selectedSong.artist = this.playlist[this.selectedSong.index].artist[0].name
                this.selectedSong.src = this.playlist[this.selectedSong.index].src
                this.selectedSong.songID = this.playlist[this.selectedSong.index].id
                this.selectedSong.singerID = this.playlist[this.selectedSong.index].artist[0].id
                http
                    .get("/song/"+this.playlist[this.selectedSong.index].id+"/comment/")
                    .then((res) => {
                        this.selectedSong.comments = res.data
                    })
                this.player.playVideo()
            }
        },
        error() {
            this.$notify('error', "지원하지 않는 곡입니다.", this.selectedSong.title+" - "+this.selectedSong.artist, { duration: 4000, permanent: false })
            this.$store.state.playerControl = "next"
        },
        selectPlaylist(index) {
            L:for(let i=0; i<this.userPlayList[index].song.length; i++) {
                for(let j=0; j<this.playlist.length; j++){
                    if(this.userPlayList[index].song[i].id == this.playlist[j].id) {
                        continue L
                    }
                }
                this.addToPlaylist(this.userPlayList[index].song[i])
            }
            // this.$notify('primary', "재생 목록에 추가 되었습니다.", data.name+" - "+data.artist[0].name, { duration: 4000, permanent: false })
        },
        showOverlay(index) {
            document.getElementById('playlist-item-overlay'+index).style.display = "block"
        },
        hideOverlay(index) {
            document.getElementById('playlist-item-overlay'+index).style.display = "none"
        },
        markPlayingIndex(index) {
            setTimeout(function(){
                document.getElementById('playlist-item-playing'+index).style.display = "block"
            }, 100)
        },
        unmarkPlayingIndex(index) {
            document.getElementById('playlist-item-playing'+index).style.display = "none"
        },
        remove(index) {
            event.stopPropagation();
            // 재생 중인 곡보다 앞번호일 경우
            if(index < this.selectedSong.index) {
                this.playlist = this.playlist.splice(index, 1)
                this.unmarkPlayingIndex(this.selectedSong.index)
                this.markPlayingIndex(this.selectedSong.index-1)
                this.selectedSong.index=this.selectedSong.index-1
                
            }
            // 재생 중인 곡일 경우
            else if(index == this.selectedSong.index) {
                // 한곡만 남은 경우 
                if(index == 0 && this.playlist.length == 1) {
                    this.playlist = this.playlist.splice(index, 1)
                    this.selectedSong.index = -1
                    this.selectedSong.img = ''
                    this.selectedSong.title = ''
                    this.selectedSong.artist = ''
                    this.selectedSong.src = ''
                    this.selectedSong.songID = -1
                    this.selectedSong.singerID = -1
                    this.selectedSong.comments = ''
                }
                // 마지막 곡일 경우
                else if(index == this.playlist.length-1) {
                    this.playlist = this.playlist.splice(index, 1)
                    this.selectedSong.index = 0
                    this.selectedSong.img = this.playlist[this.selectedSong.index].img
                    this.selectedSong.title = this.playlist[this.selectedSong.index].name
                    this.selectedSong.artist = this.playlist[this.selectedSong.index].artist[0].name
                    this.selectedSong.src = this.playlist[this.selectedSong.index].src
                    this.selectedSong.songID = this.playlist[this.selectedSong.index].id
                    this.selectedSong.singerID = this.playlist[this.selectedSong.index].artist[0].id
                    this.markPlayingIndex(this.selectedSong.index)
                    http
                    .get("/song/"+this.playlist[this.selectedSong.index].id+"/comment/")
                    .then((res) => {
                        this.selectedSong.comments = res.data
                    })
                }
                else {
                    this.playlist = this.playlist.splice(index, 1)
                    this.selectedSong.img = this.playlist[this.selectedSong.index].img
                    this.selectedSong.title = this.playlist[this.selectedSong.index].name
                    this.selectedSong.artist = this.playlist[this.selectedSong.index].artist[0].name
                    this.selectedSong.src = this.playlist[this.selectedSong.index].src
                    this.selectedSong.songID = this.playlist[this.selectedSong.index].id
                    this.selectedSong.singerID = this.playlist[this.selectedSong.index].artist[0].id
                    http
                    .get("/song/"+this.playlist[this.selectedSong.index].id+"/comment/")
                    .then((res) => {
                        this.selectedSong.comments = res.data
                    })
                }
            }
            else {      
                this.playlist = this.playlist.splice(index, 1)
            }
        },
        youTubePlayerVolumeChange() {   
            this.player.setVolume(this.selectedSong.volume);
        },
        youTubePlayerCurrentTimeChange() {
            this.player.seekTo(this.selectedSong.currentTime * this.selectedSong.duration / 100)
        },
        synchronize() {
            this.player.getDuration()
            .then((value) => this.selectedSong.duration = value)
            this.player.getCurrentTime()
            .then((value) => this.selectedSong.currentTime = value / this.selectedSong.duration * 100)
            this.player.getVolume()
            .then((value) => this.selectedSong.volume = value)
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
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    -webkit-transform: translate(-50%, -50%);
}
.playlist-item-ellipsis {
    text-overflow:ellipsis;
    white-space:nowrap;
    word-wrap:normal;
    width:100%;
    overflow:hidden;
}
</style>
