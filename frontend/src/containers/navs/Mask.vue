<template>
    <!--
        !참고
        https://developers.google.com/youtube/iframe_api_reference#Events 
        https://www.npmjs.com/package/vue-youtube
    -->
    <div class="row aligner">
        <!-- youtube video 시작 -->
        <div class="col-sm-9 aligner" style="height:inherit;">
            <youtube id="youtube" :video-id="videoid" :player-vars="playerVars" @ended="ended" ref="youtube"></youtube>
        </div>
        <!-- youtube video 끝 -->

        <!-- 플레이리스트 시작 -->
        <div class="col-sm-3" style="height:inherit; overflow:auto; overflow-x: hidden; white-space: nowrap;">
            <!-- <vue-perfect-scrollbar :settings="{ suppressScrollX: true, wheelPropagation: false }"> -->
            <b-row>
                <b-colxx xxs="12" class="mt-3">
                    <b-card class="mb-3">
                        <!-- 헤더 시작 -->
                        <h3 style="display:inline-block; margin-top:12px">{{ selectedPlaylistTitle }}</h3><!-- 가로 중앙 정렬 필요 -->
                        <!-- ########## 로그인 시에만 보이는 부분 ##########-->
                        <b-dropdown id="ddown1" text="재생 목록 불러오기" variant="outline-secondary" class="float-right">
                            <b-dropdown-header>나의 재생 목록</b-dropdown-header>
                            <b-dropdown-divider></b-dropdown-divider>
                            <b-dropdown-item v-for="(data, index) in playlistData" :key="index" @click="selectPlaylist(index)">{{ data.title }}</b-dropdown-item>
                        </b-dropdown>
                        <!-- ########## 로그인 시에만 보이는 부분 ##########-->
                        <!-- 헤더 끝 --><hr>

                        <!-- 바디 시작 -->
                        <div class="d-flex flex-row mb-3" v-for="(data, index) in selectedPlaylist" :key="index">
                            <img :src="data.img" :alt="data.title" class="list-thumbnail border-0"
                            @click="playVideo(data.src, index)" style="cursor:pointer" />
                            <div class="pl-3 pt-2 pr-2 pb-2">
                                <p class="list-item-heading">{{ data.title }}</p>
                                <div class="pr-4">
                                    <p class="text-muted mb-1 text-small">{{ data.artist }}</p>
                                </div>
                                <div class="text-primary text-small font-weight-medium d-none d-sm-block">{{ data.artist }}</div>
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
export default {
    props: ['msg'],
    data() {
        return {
            videoid: '',
            playerVars: {
                autoplay: 1
            },
            plying: '',
            selectedPlaylistIndex: '-1',
            selectedPlaylistTitle: '현재 재생 목록',
            selectedPlaylist: '',
            playlistData: [
                {
                    title: "리스트1",
                    playlist:
                    [
                        {
                            img: "https://cdnimg.melon.co.kr/cm2/album/images/104/79/150/10479150_20200821103346_500.jpg?21a0dfff48264f87bb4120d95578e9ee/melon/quality/80/optimize",
                            title: "Dynamite",
                            artist: "방탄소년단",
                            src: "gdZLi9oWNZg"
                        },
                        {
                            img: "https://cdnimg.melon.co.kr/cm2/album/images/104/69/416/10469416_20200730151034_500.jpg?dcdcccfa8cd1bc5dae7b668a5910c277/melon/sharpen/0x1",
                            title: "눈누난나 (NUNU NANA)",
                            artist: "제시(Jessi)",
                            src: "GcIVcAGlXLU"
                        },
                        {
                            img: "https://cdnimg.melon.co.kr/cm2/album/images/104/63/600/10463600_20200720152905_500.jpg?4f47c8ca556045d56c9f2016a866e652/melon/quality/80/optimize",
                            title: "취기를 빌려 (취향저격 그녀 X 산들)",
                            artist: "산들",
                            src: "d2ytH5mymWY"
                        },
                        {
                            img: "https://cdnimg.melon.co.kr/cm2/album/images/104/62/799/10462799_20200717150822_500.jpg?adcaec1a0d99e7a379c098d31dca68da/melon/quality/80/optimize",
                            title: "다시 여기 바닷가",
                            artist: "싹쓰리 (유두래곤, 린다G, 비룡)",
                            src: "ESKfHHtiSjs"
                        },
                        {
                            img: "https://cdnimg.melon.co.kr/cm2/album/images/104/52/351/10452351_20200629152036_500.jpg?40db717ac487b870724b0bab06e4b0d7/melon/quality/80/optimize",
                            title: "마리아 (Maria)",
                            artist: "화사 (Hwa Sa)",
                            src: "tDukIfFzX18"
                        },
                        {
                            img: "https://cdnimg.melon.co.kr/cm2/album/images/104/75/061/10475061_20200812120927_500.jpg?e0e2a4331bb0aa6e525f679804f35f8e/melon/quality/80/optimize",
                            title: "When We Disco (Duet with 선미)",
                            artist: "박진영",
                            src: "zrsBjYukE8s"
                        },
                        {
                            img: "https://cdnimg.melon.co.kr/cm2/album/images/104/51/566/10451566_20200626114914_500.jpg?d94b8ff3526c8b4807aa4f719f1b929a/melon/quality/80/optimize",
                            title: "How You Like That",
                            artist: "BLACKPINK",
                            src: "ioNng23DkIM"
                        },
                        {
                            img: "https://cdnimg.melon.co.kr/cm2/album/images/104/26/648/10426648_20200506153340_500.jpg?0ed92b652a9149e26387233529a32781/melon/quality/80/optimize",
                            title: "에잇(Prod.&Feat. SUGA of BTS)",
                            artist: "아이유",
                            src: "TgOu00Mf3kI"
                        },
                        {
                            img: "https://cdnimg.melon.co.kr/cm2/album/images/104/23/289/10423289_20200427153909_500.jpg?33a9f621c154722d51621a0ba45dd402/melon/quality/80/optimize",
                            title: "Dolphin",
                            artist: "오마이걸 (OH MY GIRL)",
                            src: "SvWidiKtj6U"
                        },
                        {
                            img: "https://cdnimg.melon.co.kr/cm/album/images/021/48/596/2148596_500.jpg/melon/quality/80/optimize",
                            title: "오래된 노래",
                            artist: "스탠딩 에그",
                            src: "H23rF-rlxD4"
                        },
                    ]
                },
                {
                    title: "리스트2",
                    playlist:
                    [
                        {
                            img: "https://cdnimg.melon.co.kr/cm2/album/images/104/79/150/10479150_20200821103346_500.jpg?21a0dfff48264f87bb4120d95578e9ee/melon/quality/80/optimize",
                            title: "Dynamite",
                            artist: "방탄소년단",
                            src: "gdZLi9oWNZg"
                        },
                        {
                            img: "https://cdnimg.melon.co.kr/cm2/album/images/104/63/600/10463600_20200720152905_500.jpg?4f47c8ca556045d56c9f2016a866e652/melon/quality/80/optimize",
                            title: "취기를 빌려 (취향저격 그녀 X 산들)",
                            artist: "산들",
                            src: "d2ytH5mymWY"
                        },
                        {
                            img: "https://cdnimg.melon.co.kr/cm2/album/images/104/62/799/10462799_20200717150822_500.jpg?adcaec1a0d99e7a379c098d31dca68da/melon/quality/80/optimize",
                            title: "다시 여기 바닷가",
                            artist: "싹쓰리 (유두래곤, 린다G, 비룡)",
                            src: "ESKfHHtiSjs"
                        },
                        {
                            img: "https://cdnimg.melon.co.kr/cm2/album/images/104/52/351/10452351_20200629152036_500.jpg?40db717ac487b870724b0bab06e4b0d7/melon/quality/80/optimize",
                            title: "마리아 (Maria)",
                            artist: "화사 (Hwa Sa)",
                            src: "tDukIfFzX18"
                        },
                        {
                            img: "https://cdnimg.melon.co.kr/cm2/album/images/104/75/061/10475061_20200812120927_500.jpg?e0e2a4331bb0aa6e525f679804f35f8e/melon/quality/80/optimize",
                            title: "When We Disco (Duet with 선미)",
                            artist: "박진영",
                            src: "zrsBjYukE8s"
                        },
                        {
                            img: "https://cdnimg.melon.co.kr/cm2/album/images/104/51/566/10451566_20200626114914_500.jpg?d94b8ff3526c8b4807aa4f719f1b929a/melon/quality/80/optimize",
                            title: "How You Like That",
                            artist: "BLACKPINK",
                            src: "ioNng23DkIM"
                        },
                        {
                            img: "https://cdnimg.melon.co.kr/cm2/album/images/104/26/648/10426648_20200506153340_500.jpg?0ed92b652a9149e26387233529a32781/melon/quality/80/optimize",
                            title: "에잇(Prod.&Feat. SUGA of BTS)",
                            artist: "아이유",
                            src: "TgOu00Mf3kI"
                        },
                        {
                            img: "https://cdnimg.melon.co.kr/cm2/album/images/104/23/289/10423289_20200427153909_500.jpg?33a9f621c154722d51621a0ba45dd402/melon/quality/80/optimize",
                            title: "Dolphin",
                            artist: "오마이걸 (OH MY GIRL)",
                            src: "SvWidiKtj6U"
                        },
                        {
                            img: "https://cdnimg.melon.co.kr/cm/album/images/021/48/596/2148596_500.jpg/melon/quality/80/optimize",
                            title: "오래된 노래",
                            artist: "스탠딩 에그",
                            src: "H23rF-rlxD4"
                        },
                    ]
                },
                {
                    title: "리스트3",
                    playlist:
                    [
                        {
                            img: "https://cdnimg.melon.co.kr/cm2/album/images/104/79/150/10479150_20200821103346_500.jpg?21a0dfff48264f87bb4120d95578e9ee/melon/quality/80/optimize",
                            title: "Dynamite",
                            artist: "방탄소년단",
                            src: "gdZLi9oWNZg"
                        },
                        {
                            img: "https://cdnimg.melon.co.kr/cm2/album/images/104/69/416/10469416_20200730151034_500.jpg?dcdcccfa8cd1bc5dae7b668a5910c277/melon/sharpen/0x1",
                            title: "눈누난나 (NUNU NANA)",
                            artist: "제시(Jessi)",
                            src: "GcIVcAGlXLU"
                        },
                        {
                            img: "https://cdnimg.melon.co.kr/cm2/album/images/104/63/600/10463600_20200720152905_500.jpg?4f47c8ca556045d56c9f2016a866e652/melon/quality/80/optimize",
                            title: "취기를 빌려 (취향저격 그녀 X 산들)",
                            artist: "산들",
                            src: "d2ytH5mymWY"
                        },
                        {
                            img: "https://cdnimg.melon.co.kr/cm2/album/images/104/62/799/10462799_20200717150822_500.jpg?adcaec1a0d99e7a379c098d31dca68da/melon/quality/80/optimize",
                            title: "다시 여기 바닷가",
                            artist: "싹쓰리 (유두래곤, 린다G, 비룡)",
                            src: "ESKfHHtiSjs"
                        },
                        {
                            img: "https://cdnimg.melon.co.kr/cm2/album/images/104/52/351/10452351_20200629152036_500.jpg?40db717ac487b870724b0bab06e4b0d7/melon/quality/80/optimize",
                            title: "마리아 (Maria)",
                            artist: "화사 (Hwa Sa)",
                            src: "tDukIfFzX18"
                        },
                        {
                            img: "https://cdnimg.melon.co.kr/cm2/album/images/104/75/061/10475061_20200812120927_500.jpg?e0e2a4331bb0aa6e525f679804f35f8e/melon/quality/80/optimize",
                            title: "When We Disco (Duet with 선미)",
                            artist: "박진영",
                            src: "zrsBjYukE8s"
                        },
                        {
                            img: "https://cdnimg.melon.co.kr/cm2/album/images/104/51/566/10451566_20200626114914_500.jpg?d94b8ff3526c8b4807aa4f719f1b929a/melon/quality/80/optimize",
                            title: "How You Like That",
                            artist: "BLACKPINK",
                            src: "ioNng23DkIM"
                        },
                        {
                            img: "https://cdnimg.melon.co.kr/cm2/album/images/104/26/648/10426648_20200506153340_500.jpg?0ed92b652a9149e26387233529a32781/melon/quality/80/optimize",
                            title: "에잇(Prod.&Feat. SUGA of BTS)",
                            artist: "아이유",
                            src: "TgOu00Mf3kI"
                        },
                        {
                            img: "https://cdnimg.melon.co.kr/cm2/album/images/104/23/289/10423289_20200427153909_500.jpg?33a9f621c154722d51621a0ba45dd402/melon/quality/80/optimize",
                            title: "Dolphin",
                            artist: "오마이걸 (OH MY GIRL)",
                            src: "SvWidiKtj6U"
                        },
                        {
                            img: "https://cdnimg.melon.co.kr/cm/album/images/021/48/596/2148596_500.jpg/melon/quality/80/optimize",
                            title: "오래된 노래",
                            artist: "스탠딩 에그",
                            src: "H23rF-rlxD4"
                        },
                    ]
                }
			],
        }
    },
    computed: {
        player() {
            return this.$refs.youtube.player
        }
    },
    methods: {
        playVideo(videoid, index) {
            this.playing = index
            this.videoid = videoid
            this.$store.state.visiblePlayButton = false
            this.$store.state.visiblePauseButton = true
        },
        play(msg) {
            if(msg === "play") {
                if(this.selectedPlaylist.length == 0) {
                    alert("playist is empty")
                }
                else if(this.videoid === '') {
                    this.playing = 0
                    this.videoid = this.selectedPlaylist[0].src
                    this.player.playVideo()
                }
                else {
                    this.player.playVideo()
                }
            }
            else if(msg === "pause") {
                this.player.pauseVideo()
            }
            else if(msg === "prev") {
                if(this.playing == 0) {
                    this.playing = this.selectedPlaylist.length-1
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
                else {
                    this.playing = this.playing+1
                    this.videoid = this.selectedPlaylist[this.playing].src
                    this.player.playVideo()
                }
            }
        },
        ended() {
            if(this.playing == this.selectedPlaylist.length-1) {
                this.playing = 0
                this.videoid = this.selectedPlaylist[this.playing].src
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
/* #youtube{
    display:none;
} */
.aligner {
  display: flex;
  align-items: center;
  justify-content: center;
  margin: 0px;
}
/* .aligner-list {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  margin: 0px;
} */
</style>