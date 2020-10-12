<template>
  <home-layout>
    <div :class="{'landing-page': true,'show-mobile-menu': showMobileMenu}">

      <div class="main-container">
        <div class="landing-page-nav">
          <headroom style="height:initial;">
            <nav>
              <div class="container d-flex align-items-center justify-content-between">
                <a class="navbar-logo pull-left" @click="scrollTo('#home')" href="javascript:;" style="heigth:90px!important;">
                  <img src="@/assets/logos/home.png" style="width:60px; margin-top:15px;" />
                </a>
                <ul class="navbar-nav d-none d-lg-flex flex-row">
                  <li class="nav-item">
                    <a @click="scrollTo('#features')" href="javascript:;">소개</a>
                  </li>
                  <li class="nav-item">
                    <a @click="scrollTo('#layouts')" href="javascript:;">기능</a>
                  </li>
                  <li class="nav-item">
                    <a @click="scrollTo('#components')" href="javascript:;">뮤직DNA</a>
                  </li>
                  <li class="nav-item">
                    <a :href="adminRoot+'/main'">감성DJ 즐기기</a>
                  </li>
                </ul>
                <span
                  class="mobile-menu-button"
                  @click="showMobileMenu=!showMobileMenu; $event.stopPropagation()"
                >
                  <i class="simple-icon-menu"></i>
                </span>
              </div>
            </nav>
          </headroom>
        </div>

        <div class="content-container" id="home">
          <div class="section home" id="sectionHome">
            <div class="container">
              <div class="row home-row" id="homeRow">
                <div class="col-12 d-block d-md-none">
                  <a :href="adminRoot" target="_blank">
                    <img
                      alt="mobile hero"
                      class="mobile-hero"
                      src="/assets/img/landing-page/home-hero-mobile.png"
                    />
                  </a>
                </div>

                <div class="col-12 col-xl-4 col-lg-5 col-md-6">
                  <div class="home-text">
                    <div>
                      <h1 style="color:white;">감성 DJ</h1>
                      <h3 style="color:white;">감성으로 받는 추천 플레이리스트</h3>
                    </div>
                    
                    <p class="white mt-5 mb-5">
                      즐거움, 사랑, 슬픔
                      <br />
                      <br />당신의 현재 감성은 무엇인가요?
                      <br />
                      <br />감성에 따라 추천 플레이리스트를 들어보세요
                    </p>
                    
                    <a class="btn btn-light btn-xl mr-2 mb-2" :href="adminRoot+'/main'" target="_blank">
                      시작하기 >
                    </a>
                  </div>
                </div>
                <div class="col-12 col-xl-7 offset-xl-1 col-lg-7 col-md-6 d-none d-md-block">
                  <a :href="adminRoot">
                    <img alt="hero" src="/assets/img/landing-page/home-hero.png" />
                  </a>
                </div>
              </div>
            

              <div class="row">
                <a
                  class="btn btn-circle btn-outline-semi-light hero-circle-button"
                  @click="scrollTo('#features')"
                  style="margin-left: 80px;"
                >
                  <i class="simple-icon-arrow-down"></i>
                </a>
              </div>
            </div>
          </div>

          <div class="section">
            <div class="container" id="features">
              <div class="row">
                <div class="col-12 offset-0 col-lg-8 offset-lg-2 text-center">
                  <h1>감성에 따라 달라지는 플레이리스트</h1>
                  <p>
                    가사분석을 통해 노래의 감성을 즐거움, 사랑, 슬픔으로 구분하여 감성별 플레이리스트를 들을 수 있습니다.
                  </p>
                </div>
              </div>

              <div v-for="(feature,i) in main" :key="`feature_${i}`">
                <div v-if="i%2==0" class="row feature-row">
                  <div class="col-12 col-md-6 col-lg-5 d-flex align-items-center">
                    <div class="feature-text-container">
                      <h2>{{feature.title}}</h2>
                      <p v-html="feature.detail"></p>
                    </div>
                  </div>
                  <div class="col-12 col-md-6 col-lg-6 offset-lg-1 offset-md-0 position-relative">
                    <img
                      :alt="feature.title"
                      :src="feature.img"
                      class="feature-image-right feature-image-charts position-relative"
                    />
                  </div>
                </div>
                <div v-if="i%2==1" class="row feature-row">
                  <div class="col-12 col-md-6 col-lg-6 order-2 order-md-1">
                    <img
                      :alt="feature.title"
                      :src="feature.img"
                      class="feature-image-left feature-image-charts"
                    />
                  </div>
                  <div
                    class="col-12 col-md-6 offset-md-0 col-lg-5 offset-lg-1 d-flex align-items-center order-1 order-md-2"
                  >
                    <div class="feature-text-container">
                      <h2>{{feature.title}}</h2>
                      <p v-html="feature.detail"></p>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>

          <div class="section background">
            <div class="container" id="layouts">
              <div class="row">
                <div class="col-12 offset-0 col-lg-8 offset-lg-2 text-center">
                  <h1>시간 &amp; 날씨에 따른 추천 플레이리스트</h1>
                  <p>
                    시간대와 날씨가 듣고자하는 음악의 감성에 영향을 준다는 사실 알고계셨나요?
                    <br />저희는 시간, 날씨에 따라 음악을 추천해줍니다.
                  </p>
                </div>
              </div>

              <div class="row pt-5">
                <div
                  class="col-12 mb-5"
                  v-for="(l,index) in layouts"
                  :key="`layout_${index}`"
                > 
                  <h4 class="text-left mb-3">{{l.title}}</h4>
                  <img class="img-fluid border-radius depth-2 mb-3 semi-rounded" :src="l.img" alt="img"/>
                  
                </div>
              </div>
            </div>
          </div>

          <div class="section mb-0">
            <div class="container" id="components">
              <div class="row mb-5">
                <div class="col-12 offset-0 col-lg-8 offset-lg-2 text-center">
                  <h1>Music DNA</h1>
                  <p>
                    사용자가 듣는 음악의 취향을 분석해줍니다.
                    <br />
                    <br />많은 곡을 들을수록 더 적합한 음악을 추천해 줄 수 있습니다.
                  </p>
                </div>
              </div>
            </div>
            <img class="components-image mb-5 pb-5" src="/assets/img/landing-page/dna1.png" width="90%"/>
            <img class="components-image mb-5 pb-5" src="/assets/img/landing-page/dna2.png" width="90%"/>
          </div>

          

          <div class="section background background-no-bottom mb-0 pb-0">
            <div class="container">
              <div class="row">
                <div class="col-12 offset-0 col-lg-8 offset-lg-2 text-center">
                  <h1>감성 DJ를 즐기고 싶으시면?</h1>
                </div>
                <div class="col-12 offset-0 col-lg-6 offset-lg-3 newsletter-input-container">
                  <div class="text-center mb-3">
                    <a class="btn btn-secondary btn-xl" target="_blank" :href="adminRoot+'/main'">시작하기</a>
                  </div>
                </div>
              </div>
            </div>
          </div>

          <div class="section footer mb-0" id="sectionFooter">
            <div class="container">
              <div class="row footer-row">
                <div class="col-12 text-right">
                  <a
                    class="btn btn-circle btn-outline-semi-light footer-circle-button"
                    @click="scrollTo('#home')"
                    href="javascript:;"
                  >
                    <i class="simple-icon-arrow-up"></i>
                  </a>
                </div>
                <div class="col-12 text-center footer-content">
                  
                </div>
              </div>
            </div>
            <div class="container copyright pt-5 pb-5">
              <div class="row">
                <div class="col-12"></div>
                <div class="col-12 text-center">
                  <p class="mb-0">2020 © 감성DJ by A505 | SSAFY</p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </home-layout>
</template>

<script>
import { headroom } from "vue-headroom";
import VueScrollTo from "vue-scrollto";
import HomeLayout from "@/layouts/HomeLayout";
import GlideComponent from "@/components/Carousel/GlideComponent";
import { adminRoot } from "@/constants/config";
const slideSettings = {
  type: "carousel",
  gap: 30,
  perView: 4,
  hideNav: true,
  peek: { before: 10, after: 10 },
  breakpoints: {
    "600": { perView: 1 },
    "992": { perView: 2 },
    "1200": { perView: 3 }
  }
};

const main = [
  {
    title: "즐거운 노래",
    img: "/assets/img/wordcloud/wc02.png",
    detail:
      "즐거운 감성과 관련된 단어들을 아시나요?<br/> 하늘, 태양, 빛나는 등 즐거운 노래에 자주 등장하는 가사들이 있답니다. <br/>우리는 이러한 가사들을 기반으로 즐거운 노래를 분석하여 제공합니다.<br/> 신나는 감성의 노래를 들어보세요~"
  },
  {
    title: "사랑 노래",
    img: "/assets/img/wordcloud/wc03.png",
    detail:
      "사랑이 시작되는 순간, 설레이는 감정을 느끼고 싶을 때, 어떤 노래를 들으시나요?<br/> 사랑, 그대, 눈빛, 입술.. 설레는 단어들로 사랑이라는 감성을 분석하였습니다.<br/> 설레는 순간에는 사랑노래를 들어보세요."
  },
  {
    title: "슬픈 노래",
    img: "/assets/img/wordcloud/wc01.png",
    detail:
      "사랑으로 슬플 때, 추억으로 슬플 때, 다양한 상황에서 슬픈 감성을 떠올리고 그 감성과 비슷한 노래를 찾아보신 적이 있었나요?<br/> 여기 당신만을 위한 슬픈 감성의 노래가 준비되어있습니다."
  }
];

const layouts = [
  {
    title: "날씨에 따른 음악 추천",
    img: "/assets/img/landing-page/weather.png"
  },
  {
    title: "시간에 따른 음악 추천",
    img: "/assets/img/landing-page/time.png"
  }
];



const scrollOptions = {
  container: "body",
  easing: "ease-in",
  offset: -120,
  force: true,
  x: false,
  y: true
};

export default {
  components: {
    "home-layout": HomeLayout,
    "glide-component": GlideComponent,
    headroom: headroom
  },
  data() {
    return {
      showMobileMenu: false,
      adminRoot,
      slideSettings,
      main,
      layouts,
    };
  },
  methods: {
    onWindowResize() {
      const homeRect = document
        .getElementById("homeRow")
        .getBoundingClientRect();
      const homeSection = document.getElementById("sectionHome");
      homeSection.style.backgroundPositionX = homeRect.x - 320 + "px";
      homeSection.style.width = window.innerWidth;
      const footerSection = document.getElementById("sectionFooter");
      footerSection.style.backgroundPositionX =
      event.target.innerWidth - homeRect.x - 2000 + "px";

      if (event.target.innerWidth >= 992) {
        this.showMobileMenu = false;
      }
    },
    onWindowScroll() {
      this.showMobileMenu = false;
    },
    onWindowClick() {
      this.showMobileMenu = false;
    },

    scrollTo(target) {
      VueScrollTo.scrollTo(target, 200, scrollOptions);
    }
  },
  mounted() {
    
    document.body.classList.add("no-footer");
    window.addEventListener("scroll", this.onWindowScroll);
    window.addEventListener("resize", this.onWindowResize);
    window.addEventListener("click", this.onWindowClick);
  },
  beforeDestroy() {
    document.body.classList.remove("no-footer");
    window.removeEventListener("scroll", this.onWindowScroll);
    window.removeEventListener("resize", this.onWindowResize);
    window.removeEventListener("click", this.onWindowClick);
  }
};
</script>
