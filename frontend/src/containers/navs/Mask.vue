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
                <b-tab title="Music Player" active title-item-class="w-50 text-center">
                    <div style="display:flex; flex-direction:column; justify-content: center; align-items: center;">
                        <youtube id="youtube" :video-id="videoid" :player-vars="playerVars" @ended="ended" ref="youtube" style="display:none"></youtube>
                    </div>
                    <div style="display:flex; flex-direction:column; justify-content: center; align-items: center;">
                        <img :src="selectedSongImg">
                    </div>
                </b-tab>
                <b-tab title="Music Analyze" title-item-class="w-50 text-center">
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
                        <h3 style="display:inline-block; margin-top:12px">{{ selectedPlaylistTitle }}</h3><!-- 가로 중앙 정렬 필요 -->
                        <b-dropdown id="ddown1" text="재생 목록 불러오기" variant="outline-secondary" class="float-right">
                            <b-dropdown-header>나의 재생 목록</b-dropdown-header>
                            <b-dropdown-divider></b-dropdown-divider>
                            <b-dropdown-item v-for="(data, index) in playlistData" :key="index" @click="selectPlaylist(index)">{{ data.title }}</b-dropdown-item>
                        </b-dropdown>
                        <!-- 헤더 끝 --><hr>

                        <!-- 바디 시작 -->
                        <div class="playlist-item-wrapper" v-for="(data, index) in selectedPlaylist" :key="index">
                            <!-- <div class="d-flex flex-row" style="padding:10px; cursor:pointer; position:absolute;">
                                <music-bar />
                            </div> -->
                            <div class="d-flex flex-row" style="padding:10px; cursor:pointer" @click="playVideo(data.src, index, data.img)">
                                <img :src="data.img" :alt="data.title" class="list-thumbnail border-0" />
                                <div class="pl-3 pt-2 pr-2 pb-2">
                                    <p class="list-item-heading">{{ data.title }}</p>
                                    <div class="pr-4">
                                        <p class="text-muted mb-1 text-small">{{ data.artist }}</p>
                                    </div>
                                    <!-- <div class="text-primary text-small font-weight-medium d-none d-sm-block">{{ data.artist }}</div> -->
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
import MusicBar from "../../components/Playlist/musicbar2"
import { playlistData } from "../../data/playlist"
export default {
    props: ['msg'],
    components:{
        'music-bar': MusicBar,
    },
    data() {
        return {
            videoid: '',
            playerVars: {
                autoplay: 1
            },
            playing: '',
            selectedPlaylistIndex: '-1',
            selectedPlaylistTitle: '재생 목록',
            selectedPlaylist: '',
            selectedSong: {},
            selectedSongImg: '',
            playlistData,
            
        }
    },
    computed: {
        player() {
            return this.$refs.youtube.player
        }
    },
    methods: {
        playVideo(videoid, index, img) {
            this.videoid = videoid
            this.playing = index
            this.$store.state.visiblePlayButton = false
            this.$store.state.visiblePauseButton = true
            this.selectedSongImg = img
            for(let i=0; i<this.selectedPlaylist.length; i++) {
                this.selectedSong[i] = false
            }
            this.selectedSong[index] = true
        },
        play(msg) {
            if(msg === "play") {
                if(this.selectedPlaylist.length == 0){
                    alert("playlist is empty")
                    this.$store.state.visiblePlayButton = true
                    this.$store.state.visiblePauseButton = false
                }
                else if(this.videoid === ''){
                    this.playing = 0;
                    this.videoid = this.selectedPlaylist[this.playing].src
                    this.player.playVideo()
                }
                else
                    this.player.playVideo()
            }
            else if(msg === "pause")
                this.player.pauseVideo()
            else if(msg === "prev") {
                if(this.playing == 0) {
                    this.playing = this.selectedPlaylist[length-1].src
                    this.videoid = this.selectedPlaylist[this.playing].src
                    this.player.playVideo()
                }
                else if(this.videoid === ''){
                    this.playing = 0;
                    this.videoid = this.selectedPlaylist[this.playing].src
                    this.player.playVideo()
                }
                else {
                    this.playing = this.playing-1
                    this.videoid = this.selectedPlaylist[this.playing].src
                    this.player.playVideo()
                }
            }
            else if(msg === "next") {
                if(this.playing == this.selectedPlaylist.length-1) {
                    this.playing = 0
                    this.videoid = this.selectedPlaylist[this.playing].src
                    this.player.playVideo()
                }
                else if(this.videoid === ''){
                    this.playing = 0;
                    this.videoid = this.selectedPlaylist[this.playing].src
                    this.player.playVideo()
                }
                else {
                    this.playing = this.playing+1
                    this.videoid = this.selectedPlaylist[this.playing].src
                    this.player.playVideo()
                }
            }
        },
        ended() {
            if(this.playing >= this.selectedPlaylist.length-1) {
                this.playing = 0
                this.videoid = this.selectedPlaylist[0].src
                this.player.playVideo()
            }
            else {
                this.playing = this.playing+1
                this.videoid = this.selectedPlaylist[this.playing].src
                this.player.playVideo()
            }
        },
        selectPlaylist(index) {
            this.selectedPlaylistIndex = index
            this.selectedPlaylistTitle = this.playlistData[index].title
            this.selectedPlaylist = this.playlistData[index].playlist
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
</style>