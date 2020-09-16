<template>
    <div class="row aligner">

        <!-- youtube video 시작 -->
        <div class="col-sm-7 aligner">
            <youtube :video-id="videoid" :player-vars="playerVars" ref="youtube"></youtube>
        </div>
        <!-- youtube video 끝 -->

        <!-- 플레이리스트 시작 -->
        <div class="col-sm-5">
            <h1>Play List</h1>
            <vue-perfect-scrollbar
            class="scroll dashboard-list-with-thumbs"
            :settings="{ suppressScrollX: true, wheelPropagation: false }"
            >
                <!-- 리스트 아이템 시작 -->
                <div class="d-flex flex-row mb-3" v-for="(data, index) in playlistData" :key="index">
                    <img :src="data.img" :alt="data.title" class="list-thumbnail border-0"
                    @click="playVideo(data.src)" style="cursor:pointer" />
                    <b-badge pill class="position-absolute badge-top-left"> playing </b-badge>
                    <div class="pl-3 pt-2 pr-2 pb-2">
                        <p class="list-item-heading">{{ data.title }}</p>
                        <div class="pr-4">
                            <p class="text-muted mb-1 text-small">{{ data.artist }}</p>
                        </div>
                        <div class="text-primary text-small font-weight-medium d-none d-sm-block">{{ data.artist }}</div>
                    </div>
                </div>
                <!-- 리스트 아이템 끝 -->
            </vue-perfect-scrollbar>
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
            playlistData: [
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
			],

        }
    },
    computed: {
        player() {
            return this.$refs.youtube.player
        }
    },
    watch: {
        msg : function() {
            if(this.msg === "play") {
                this.player.playVideo()
            }
            else if(this.msg === "prev") {
                
            }
            else if(this.msg === "next") {

            }
        }
    },
    methods: {
        playVideo(videoid) {
            this.videoid = videoid;
            this.play
        },
        play() {
            this.player.playVideo()
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
.aligner-list {
  display: flex;
  flex-direction: column;
  /* align-items: center; */
  justify-content: center;
  margin: 0px;
}
</style>