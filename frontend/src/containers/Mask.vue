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
                            <youtube id="youtube" :video-id="selectedSong.src" :player-vars="playerVars" @ended="ended(selectedSong.index)" ref="youtube"></youtube>
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

                        <h3 style="display:inline-block; margin-top:12px">재생 목록</h3>
                        <span v-if="this.$store.state.user">
                            <b-dropdown id="ddown1" text="재생 목록 불러오기" variant="outline-secondary" class="float-right">
                                <b-dropdown-header>나의 재생 목록</b-dropdown-header>
                                <b-dropdown-divider></b-dropdown-divider>
                                <b-dropdown-item v-for="(data, index) in playlistData" :key="index" @click="selectPlaylist(index)">{{ data.title }}</b-dropdown-item>
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
import { mapState } from "vuex"
import Switches from "vue-switches"
import http from "../utils/http-common"

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
            playlistData :
            [
                {
                    title: "리스트1",
                    playlist:
                    [
                        {
                            img: "https://cdnimg.melon.co.kr/cm/album/images/101/37/250/10137250_500.jpg?50e1f74970a36bb3b504a76f87981834/melon/quality/80/optimize",
                            name: "2002",
                            artist: [
                                {
                                    name: "Anne-Marie",
                                }
                            ],
                            src: "Il-an3K9pjg"

                        },
                        {
                            img: "https://cdnimg.melon.co.kr/cm2/album/images/104/65/994/10465994_20200723160043_500.jpg?8db1857c022f2f71eedcb170efbcc16d/melon/quality/80/optimize",
                            name: "홀로",
                            artist: [
                                {
                                    name: "이하이",
                                }
                            ],
                            src: "VdeK_VsG9U0"
                            
                        },
                        {
                            img: "https://cdnimg.melon.co.kr/cm2/album/images/104/79/150/10479150_20200821103346_500.jpg?21a0dfff48264f87bb4120d95578e9ee/melon/quality/80/optimize",
                            name: "Dynamite",
                            artist: [
                                {
                                    name: "방탄소년단",
                                }
                            ],
                            src: "gdZLi9oWNZg"
                        },
                        {
                            img: "https://cdnimg.melon.co.kr/cm2/album/images/103/20/500/10320500_500.jpg?415f9d7d32c2914d632a56cd402ccd62/melon/sharpen/0x1",
                            name: "흔들리는 꽃들 속에서 네 샴푸향이 느껴진거야",
                            artist: [
                                {
                                    name: "장범준",
                                }
                            ],
                            src: "689GoEBjMhY"

                        },
                        {
                            img: "https://cdnimg.melon.co.kr/cm/album/images/102/94/603/10294603_500.jpg?0c56b81bdfc97f7c568a95aad6a7614a/melon/quality/80/optimize",
                            name: "오늘도 빛나는 너에게 (To You My Light) (Feat.이라온)",
                            artist: [
                                {
                                    name: "마크툽 (MAKTUB)",
                                }
                            ],
                            src: "dmSUBdk4SY4"

                        },
                        {
                            img: "https://cdnimg.melon.co.kr/cm2/album/images/104/63/600/10463600_20200720152905_500.jpg?4f47c8ca556045d56c9f2016a866e652/melon/quality/80/optimize",
                            name: "취기를 빌려 (취향저격 그녀 X 산들)",
                            artist: [
                                {
                                    name: "산들",
                                }
                            ],
                            src: "d2ytH5mymWY"
                        },
                        {
                            img: "https://cdnimg.melon.co.kr/cm2/album/images/104/52/351/10452351_20200629152036_500.jpg?40db717ac487b870724b0bab06e4b0d7/melon/quality/80/optimize",
                            name: "마리아 (Maria)",
                            artist: [
                                {
                                    name: "화사 (Hwa Sa)",
                                }
                            ],
                            src: "tDukIfFzX18"
                        },
                        {
                            img: "https://cdnimg.melon.co.kr/cm2/album/images/104/75/061/10475061_20200812120927_500.jpg?e0e2a4331bb0aa6e525f679804f35f8e/melon/quality/80/optimize",
                            name: "When We Disco (Duet with 선미)",
                            artist: [
                                {
                                    name: "박진영",
                                }
                            ],
                            src: "zrsBjYukE8s"
                        },
                        {
                            img: "https://cdnimg.melon.co.kr/cm2/album/images/104/51/566/10451566_20200626114914_500.jpg?d94b8ff3526c8b4807aa4f719f1b929a/melon/quality/80/optimize",
                            name: "How You Like That",
                            artist: [
                                {
                                    name: "BLACKPINK",
                                }
                            ],
                            src: "ioNng23DkIM"
                        },
                        {
                            img: "https://cdnimg.melon.co.kr/cm2/album/images/104/26/648/10426648_20200506153340_500.jpg?0ed92b652a9149e26387233529a32781/melon/quality/80/optimize",
                            name: "에잇(Prod.&Feat. SUGA of BTS)",
                            artist: [
                                {
                                    name: "아이유",
                                }
                            ],
                            src: "TgOu00Mf3kI"
                        },
                        {
                            img: "https://cdnimg.melon.co.kr/cm2/album/images/104/23/289/10423289_20200427153909_500.jpg?33a9f621c154722d51621a0ba45dd402/melon/quality/80/optimize",
                            name: "Dolphin",
                            artist: [
                                {
                                    name: "오마이걸 (OH MY GIRL)",
                                }
                            ],
                            src: "SvWidiKtj6U"
                        },
                        {
                            img: "https://cdnimg.melon.co.kr/cm/album/images/021/48/596/2148596_500.jpg/melon/quality/80/optimize",
                            name: "오래된 노래",
                            artist: [
                                {
                                    name:"스탠딩 에그",
                                }
                            ],
                            src: "H23rF-rlxD4"
                        },
                    ]
                },
            ],
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
            'selectedSong'
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
                    this.selectedSong.index = 0
                    this.markPlayingIndex(this.selectedSong.index)
                    this.selectedSong.img = this.playlist[this.selectedSong.index].img
                    this.selectedSong.title = this.playlist[this.selectedSong.index].name
                    this.selectedSong.artist = this.playlist[this.selectedSong.index].artist[0].name
                    this.selectedSong.src = this.playlist[this.selectedSong.index].src
                }
                else{
                    this.player.playVideo()
                }
            }
            else if(state === "pause")
                this.player.pauseVideo()
            else if(state === "prev") {
                if(this.selectedSong.index == 0) {
                    this.unmarkPlayingIndex(this.selectedSong.index)
                    this.selectedSong.index = this.playlist.length-1
                    this.markPlayingIndex(this.selectedSong.index)
                    this.selectedSong.img = this.playlist[this.selectedSong.index].img
                    this.selectedSong.title = this.playlist[this.selectedSong.index].name
                    this.selectedSong.artist = this.playlist[this.selectedSong.index].artist[0].name
                    this.selectedSong.src = this.playlist[this.selectedSong.index].src
                }
                else if(this.selectedSong.src === ''){
                    this.selectedSong.index = 0
                    this.markPlayingIndex(this.selectedSong.index)
                    this.selectedSong.img = this.playlist[this.selectedSong.index].img
                    this.selectedSong.title = this.playlist[this.selectedSong.index].name
                    this.selectedSong.artist = this.playlist[this.selectedSong.index].artist[0].name
                    this.selectedSong.src = this.playlist[this.selectedSong.index].src
                }
                else {
                    this.unmarkPlayingIndex(this.selectedSong.index)
                    this.selectedSong.index = this.selectedSong.index-1
                    this.markPlayingIndex(this.selectedSong.index)
                    this.selectedSong.img = this.playlist[this.selectedSong.index].img
                    this.selectedSong.title = this.playlist[this.selectedSong.index].name
                    this.selectedSong.artist = this.playlist[this.selectedSong.index].artist[0].name
                    this.selectedSong.src = this.playlist[this.selectedSong.index].src
                }
            }
            else if(state === "next") {
                if(this.selectedSong.index == this.playlist.length-1) {
                    this.unmarkPlayingIndex(this.selectedSong.index)
                    this.selectedSong.index = 0
                    this.markPlayingIndex(this.selectedSong.index)
                    this.selectedSong.img = this.playlist[this.selectedSong.index].img
                    this.selectedSong.title = this.playlist[this.selectedSong.index].name
                    this.selectedSong.artist = this.playlist[this.selectedSong.index].artist[0].name
                    this.selectedSong.src = this.playlist[this.selectedSong.index].src
                }
                else if(this.selectedSong.src === ''){
                    this.selectedSong.index = 0
                    this.markPlayingIndex(this.selectedSong.index)
                    this.selectedSong.img = this.playlist[this.selectedSong.index].img
                    this.selectedSong.title = this.playlist[this.selectedSong.index].name
                    this.selectedSong.artist = this.playlist[this.selectedSong.index].artist[0].name
                    this.selectedSong.src = this.playlist[this.selectedSong.index].src
                }
                else {
                    this.unmarkPlayingIndex(this.selectedSong.index)
                    this.selectedSong.index = this.selectedSong.index+1
                    this.markPlayingIndex(this.selectedSong.index)
                    this.selectedSong.img = this.playlist[this.selectedSong.index].img
                    this.selectedSong.title = this.playlist[this.selectedSong.index].name
                    this.selectedSong.artist = this.playlist[this.selectedSong.index].artist[0].name
                    this.selectedSong.src = this.playlist[this.selectedSong.index].src
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
                }
                else {
                    this.unmarkPlayingIndex(this.selectedSong.index)
                    this.selectedSong.index = 0
                    this.markPlayingIndex(this.selectedSong.index)
                    this.selectedSong.img = this.playlist[this.selectedSong.index].img
                    this.selectedSong.title = this.playlist[this.selectedSong.index].name
                    this.selectedSong.artist = this.playlist[this.selectedSong.index].artist[0].name
                    this.selectedSong.src = this.playlist[this.selectedSong.index].src
                }
                this.$store.state.visiblePlayButton = false
                this.$store.state.visiblePauseButton = true
            }
            this.$store.state.playerControl = ''
        }
    },
    methods: {
        selectSong(index, data) {
            if(this.selectedSong.index == -1) {
                this.selectedSong.index = index
                this.markPlayingIndex(this.selectedSong.index)
                this.selectedSong.img = data.img
                this.selectedSong.title = data.name
                this.selectedSong.artist = data.artist[0].name
                this.selectedSong.src = data.src
                this.$store.state.visiblePlayButton = false
                this.$store.state.visiblePauseButton = true
            }
            else {
                this.unmarkPlayingIndex(this.selectedSong.index)
                this.selectedSong.index = index
                this.markPlayingIndex(this.selectedSong.index)
                this.selectedSong.img = data.img
                this.selectedSong.title = data.name
                this.selectedSong.artist = data.artist[0].name
                this.selectedSong.src = data.src
                this.$store.state.visiblePlayButton = false
                this.$store.state.visiblePauseButton = true
            }
        },
        ended(index) {
            http.
            post('log/',
            {
                song: this.playlist[index].id
            }, this.$store.getters.config)
            .then((value) => {
                console.log(value)
            })
            if(this.selectedSong.index >= this.playlist.length-1) {
                this.unmarkPlayingIndex(this.selectedSong.index)
                this.selectedSong.index = 0
                this.markPlayingIndex(this.selectedSong.index)
                this.selectedSong.img = this.playlist[0].img
                this.selectedSong.title = this.playlist[0].name
                this.selectedSong.artist = this.playlist[0].artist[0].name
                this.selectedSong.src = this.playlist[0].src
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
                this.player.playVideo()
            }
        },
        selectPlaylist(index) {
            for(let i=0; i<this.playlistData[index].playlist.length; i++){
                this.playlist.push(this.playlistData[index].playlist[i])
            }
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
                }
                // 마지막 곡일 경우
                else if(index == this.playlist.length-1) {
                    this.playlist = this.playlist.splice(index, 1)
                    this.selectedSong.index = 0
                    this.selectedSong.img = this.playlist[this.selectedSong.index].img
                    this.selectedSong.title = this.playlist[this.selectedSong.index].name
                    this.selectedSong.artist = this.playlist[this.selectedSong.index].artist[0].name
                    this.selectedSong.src = this.playlist[this.selectedSong.index].src
                    this.markPlayingIndex(this.selectedSong.index)
                }
                else {
                    this.playlist = this.playlist.splice(index, 1)
                    this.selectedSong.img = this.playlist[this.selectedSong.index].img
                    this.selectedSong.title = this.playlist[this.selectedSong.index].name
                    this.selectedSong.artist = this.playlist[this.selectedSong.index].artist[0].name
                    this.selectedSong.src = this.playlist[this.selectedSong.index].src
                }
            }
            else {      
                this.playlist = this.playlist.splice(index, 1)
            }
        },
        // youTubePlayerVolumeChange() {   
        //     this.player.setVolume(this.selectedSong.volume);
        // },
        // youTubePlayerCurrentTimeChange() {
        //     this.player.seekTo(this.selectedSong.currentTime * this.selectedSong.duration / 100)
        // },
        // synchronize() {
        //     this.player.getDuration()
        //     .then((value) => this.selectedSong.duration = value)
        //     this.player.getCurrentTime()
        //     .then((value) => this.selectedSong.currentTime = value / this.selectedSong.duration * 100)
        //     this.player.getVolume()
        //     .then((value) => this.selectedSong.volume = value)
        // }
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
