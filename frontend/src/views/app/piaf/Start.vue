<template>
<div>
	<!-- 감정 카테고리 분류 시작 -->
    <b-row>
        <b-colxx xxs="12" class="mb-4 pl-0 pr-0">
            <glide-component :settings="glideSingleOption">
                <!-- 첫번째 -->
                <div class="pr-3 pl-3 mb-4 glide__slide" style="height:500px">
                    <b-card class="flex-row" no-body>
                        
                    </b-card>
                </div>
                <!-- 첫번째 끝 -->

                <!-- 두번째 시작 -->
                <div class="pr-3 pl-3 mb-4 glide__slide" style="height:500px">
                    <b-card class="flex-row" no-body>
                        
                    </b-card>
                </div>
                <!-- 두번째 끝 -->

                <!-- 세번째 시작 -->
                <div class="pr-3 pl-3 mb-4 glide__slide" style="height:500px">
                    <b-card class="flex-row" no-body>
                        
                    </b-card>
                </div>
                <!-- 세번째 끝 -->

                <!-- 네번째 시작 -->
                <div class="pr-3 pl-3 mb-4 glide__slide" style="height:500px">
                    <b-card class="flex-row" no-body>
                        
                    </b-card>
                </div>
                <!-- 네번째 끝 -->
            </glide-component>
        </b-colxx>
    </b-row>
	<!-- 감정 카테고리 분류 끝 -->

	<!-- 날씨 매칭 추천 시작 -->
    <b-row>
        <b-colxx xxs="12">
            <a href="#" @click.prevent="tempFunction"><h5 class="mb-4 card-title">{{ $t('오늘 같은 날에는 >') }}</h5></a>
        </b-colxx>
        <b-colxx xxs="12" class="mb-4 pl-0 pr-0">
            <glide-component :settings="glideNoControlsSettings">
                <div v-for="(data, index) in dummyData1" :key="index" class="pr-3 pl-3 mb-4 glide__slide">
                    <b-card no-body>
                        <div class="position-relative">
                            <img class="card-img-top" :src="data.src" alt="Card cap" />
                            <!-- <b-badge variant="primary" pill class="position-absolute badge-top-left">NEW</b-badge> -->
                            <!-- <b-badge variant="secondary" pill class="position-absolute badge-top-left-2">TRENDING</b-badge> -->
                        </div>
                        <b-card-body>
                            <h6 class="mb-4">{{ data.title }}</h6>
                            <p class="text-muted text-small mb-0 font-weight-light">{{ data.artist }}</p>
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
            <a href="#" @click.prevent="tempFunction"><h5 class="mb-4 card-title">{{ $t('지금 시간대에 >') }}</h5></a>
        </b-colxx>
        <b-colxx xxs="12" class="mb-4 pl-0 pr-0">
            <glide-component :settings="glideNoControlsSettings">
                <div v-for="(data, index) in dummyData2" :key="index" class="pr-3 pl-3 mb-4 glide__slide">
                    <b-card no-body>
                        <div class="position-relative">
                            <img class="card-img-top" :src="data.src" alt="Card cap" />
                            <!-- <b-badge variant="primary" pill class="position-absolute badge-top-left">NEW</b-badge> -->
                            <!-- <b-badge variant="secondary" pill class="position-absolute badge-top-left-2">TRENDING</b-badge> -->
                        </div>
                        <b-card-body>
                            <h6 class="mb-4">{{ data.title }}</h6>
                            <p class="text-muted text-small mb-0 font-weight-light">{{ data.artist }}</p>
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
            <a href="#" @click.prevent="tempFunction"><h5 class="mb-4 card-title">{{ $t('지금 기분에는 >') }}</h5></a>
        </b-colxx>
        <b-colxx xxs="12" class="mb-4 pl-0 pr-0">
            <glide-component :settings="glideNoControlsSettings">
                <div v-for="(data, index) in dummyData3" :key="index" class="pr-3 pl-3 mb-4 glide__slide">
                    <b-card no-body>
                        <div class="position-relative">
                            <img class="card-img-top" :src="data.src" alt="Card cap" />
                            <!-- <b-badge variant="primary" pill class="position-absolute badge-top-left">NEW</b-badge> -->
                            <!-- <b-badge variant="secondary" pill class="position-absolute badge-top-left-2">TRENDING</b-badge> -->
                        </div>
                        <b-card-body>
                            <h6 class="mb-4">{{ data.title }}</h6>
                            <p class="text-muted text-small mb-0 font-weight-light">{{ data.artist }}</p>
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

export default {
    components: {
        'glide-component': GlideComponent,
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
			dummyData1: [
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
			dummyData2: [
				{
					src: "https://cdnimg.melon.co.kr/cm2/album/images/104/34/250/10434250_20200522151246_500.jpg?efb35e4b6d68454084fe2a58b8d70805/melon/quality/80/optimize",
					title: "돼버릴거야 (feat.휘인 of 마마무) (Prod.기리보이)",
					artist: "딘딘",
				},
				{
					src: "https://cdnimg.melon.co.kr/cm2/album/images/104/72/319/10472319_20200805151615_500.jpg?ab6e9e2acf7e853b6611add34fdb55d7/melon/quality/80/optimize",
					title: "On&On",
					artist: "D2ear",
				},
				{
					src: "https://cdnimg.melon.co.kr/cm2/album/images/104/69/721/10469721_20200730171630_500.jpg?050fafc6d4d4a2d6c865c43a71d8450c/melon/quality/80/optimize",
					title: "잘 살고 있어요",
					artist: "nokdu",
				},
				{
					src: "https://cdnimg.melon.co.kr/cm2/album/images/104/74/356/10474356_20200810183044_500.jpg?c37e9c51256d54058bd45510eb1c06a3/melon/quality/80/optimize",
					title: "0과 1사이",
					artist: "원지 (WONJI)",
				},
				{
					src: "https://cdnimg.melon.co.kr/cm2/album/images/104/74/229/10474229_20200810152829_500.jpg?0e275b2d5e5968ff4997aeb1cac957b3/melon/quality/80/optimize",
					title: "WE (Feat. SOLE)",
					artist: "다희 (DAHEE)",
				},
				{
					src: "https://cdnimg.melon.co.kr/cm2/album/images/103/64/577/10364577_20191213144211_500.jpg?3ed85e910eff03b518e083f012243648/melon/quality/80/optimize",
					title: "나뿐인것같아",
					artist: "비비 (BB)",
				},
			],
			dummyData3: [
				{
					src: "https://cdnimg.melon.co.kr/cm/album/images/103/01/063/10301063_500.jpg?5c1875b59ddea1e468ed869842234382/melon/quality/80/optimize",
					title: "Good Nights",
					artist: "Jeff Draco",
				},
				{
					src: "https://cdnimg.melon.co.kr/cm2/album/images/103/35/933/10335933_500.jpg?04fe10884d7e81b4e19b4e0ee5835e23/melon/quality/80/optimize",
					title: "나를 사랑하지 않는 나에게",
					artist: "폴킴",
				},
				{
					src: "https://cdnimg.melon.co.kr/cm2/album/images/103/31/947/10331947_500.jpg?c6e307f67cf7124ec13127cd60ab569f/melon/quality/80/optimize",
					title: "작별 인사",
					artist: "AKMU (악동뮤지션)",
				},
				{
					src: "https://cdnimg.melon.co.kr/cm2/album/images/103/39/757/10339757_500.jpg?596cca1fa675415009fd4983433dab30/melon/resize/282/quality/80/optimize",
					title: "FLY TO THE SKY 10TH ALBUM [Fly High]",
					artist: "플라이 투 더 스카이",
				},
				{
					src: "https://cdnimg.melon.co.kr/cm2/album/images/103/37/684/10337684_500.jpg?093fc443892f4f23989208172f3b32a7/melon/resize/282/quality/80/optimize",
					title: "이젠 보낼게",
					artist: "어쿠스틱 콜라보",
				},
				{
					src: "https://cdnimg.melon.co.kr/cm2/album/images/103/25/945/10325945_500.jpg?88b2b5bd60d01d4abd53d0fd09295ddb/melon/resize/282/quality/80/optimize",
					title: "Rewind",
					artist: "케이시 (Kassy)",
				},
			]
        }
	},
	methods:{
		tempFunction(){
			alert("페이지 준비중");
		}
	}
}
</script>
