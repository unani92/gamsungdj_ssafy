<template>
<div>
	<!-- 감정 카테고리별 추천 음악 시작 -->
    <b-row>
        <b-colxx xxs="12" class="mb-4 pl-0 pr-0">
            <glide-component :settings="glideSingleOption">
                <!-- 카테	고리1 시작 -->
                <div class="pr-3 pl-3 mb-4 glide__slide">
                    <b-card class="flex-row" no-body>
						<div class="col-sm-4 main-carousel-bg1">
						</div>
						<div class="col-sm-8">
							<b-row>
								<b-colxx class="mb-2 mt-4" v-for="(data, index) in carouselData1.data.slice(0,5)" :key="index">
								<b-card class="text-white" no-body>
									<img :src="data.img" class="card-img" />
									<div class="card-img-overlay" style="white-space: nowrap; overflow:hidden; text-overflow: ellipsis;">
										<h5 class="card-title">{{ data.name }}</h5>
										<p class="card-text">{{ data.artist[0].name }}</p>
									</div>
								</b-card>
								</b-colxx>
							</b-row>
							<b-row>
								<b-colxx class="mb-4 mt-2" v-for="(data, index) in carouselData1.data.slice(5,10)" :key="index">
								<b-card class="text-white" no-body>
									<img :src="data.img" class="card-img" />
									<div class="card-img-overlay" style="white-space: nowrap; overflow:hidden; text-overflow: ellipsis;">
										<h5 class="card-title">{{ data.name }}</h5>
										<p class="card-text">{{ data.artist[0].name }}</p>
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
								<b-colxx class="mb-2 mt-4" v-for="(data, index) in carouselData2.data.slice(0,5)" :key="index">
								<b-card class="text-white" no-body>
									<img :src="data.img" class="card-img" />
									<div class="card-img-overlay" style="white-space: nowrap; overflow:hidden; text-overflow: ellipsis;">
										<h5 class="card-title">{{ data.name }}</h5>
										<p class="card-text">{{ data.artist[0].name }}</p>
									</div>
								</b-card>
								</b-colxx>
							</b-row>
							<b-row>
								<b-colxx class="mb-4 mt-2" v-for="(data, index) in carouselData2.data.slice(5,10)" :key="index">
								<b-card class="text-white" no-body>
									<img :src="data.img" class="card-img" />
									<div class="card-img-overlay" style="white-space: nowrap; overflow:hidden; text-overflow: ellipsis;">
										<h5 class="card-title">{{ data.name }}</h5>
										<p class="card-text">{{ data.artist[0].name }}</p>
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
								<b-colxx class="mb-2 mt-4" v-for="(data, index) in carouselData3.data.slice(0,5)" :key="index">
								<b-card class="text-white" no-body>
									<img :src="data.img" class="card-img" />
									<div class="card-img-overlay" style="white-space: nowrap; overflow:hidden; text-overflow: ellipsis;">
										<h5 class="card-title">{{ data.name }}</h5>
										<p class="card-text">{{ data.artist[0].name }}</p>
									</div>
								</b-card>
								</b-colxx>
							</b-row>
							<b-row>
								<b-colxx class="mb-4 mt-2" v-for="(data, index) in carouselData3.data.slice(5,10)" :key="index">
								<b-card class="text-white" no-body>
									<img :src="data.img" class="card-img" />
									<div class="card-img-overlay" style="white-space: nowrap; overflow:hidden; text-overflow: ellipsis;">
										<h5 class="card-title">{{ data.name }}</h5>
										<p class="card-text">{{ data.artist[0].name }}</p>
									</div>
								</b-card>
								</b-colxx>
							</b-row>
						</div>
                    </b-card>
                </div>
                <!-- 카테고리3 끝 -->

                <!-- 카테고리4 시작 -->
                <!-- <div class="pr-3 pl-3 mb-4 glide__slide" style="min-height:500px">
                    <b-card class="flex-row" no-body>
                    </b-card>
                </div> -->
                <!-- 카테고리4 끝 -->
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

export default {
    components: {
        'glide-component': GlideComponent,
    },
	created(){
        http
        .get('sad')
        .then((data) => {
			this.carouselData1 = data;
		})
		http
		.get('joy')
        .then((data) => {
			this.carouselData2 = data;
		})
		http
		.get('love')
        .then((data) => {
			this.carouselData3 = data;
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
			carouselData1: '',
			carouselData2: '',
			carouselData3: '',
			
        }
	},
	methods:{
		tempFunction(){
			alert("페이지 준비중입니다.");
		}
	}
}
</script>
<style scoped>
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