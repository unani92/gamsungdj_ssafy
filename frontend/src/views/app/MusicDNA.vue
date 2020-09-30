<template>
    <div>
        <div class="mb-4">
            <h3>{{ user.username }}님은 2010.05.10부터 1,672개의 곡의 음악을 감상하고 있습니다.</h3>
        </div>
        <b-row>
            <b-colxx lg="3" xl="3" class="mb-4">
                <gradient-with-radial-progress-card
                    icon="simple-icon-heart"
                    title="ambience"
                    :detail=favAmbiance
                    :percent=favAmbianceProp
                    :progressText=favAmbianceProp
                />
            </b-colxx>
            <b-colxx lg="3" xl="3" class="mb-4">
                <gradient-with-radial-progress-card
                    icon="simple-icon-star"
                    title="Genre"
                    :detail=favGenre
                    :percent=favGenreProp
                    :progressText=favGenreProp
                />
            </b-colxx>
            <b-colxx lg="3" xl="3" class="mb-4">
                <gradient-with-radial-progress-card
                    icon="simple-icon-user"
                    title="Artist"
                    detail="선호하는 가수는 BTS입니다."
                    :percent="15"
                    progressText="15%"
                />
            </b-colxx>
            <b-colxx lg="3" xl="3" class="mb-4">
                <gradient-with-radial-progress-card
                    icon="simple-icon-clock"
                    title="Time"
                    detail="주로 오후에 감상을 하고 있습니다."
                    :percent="36"
                    progressText="36%"
                />
            </b-colxx>
        </b-row>
        <b-row class="mb-4">
            <b-colxx lg="3" xl="3">
                <b-card class="h-100" title="감성">
                    <div class="dashboard-donut-chart">
                        <doughnut-chart :data="doughnutChartData1" shadow />
                    </div>
                </b-card>
            </b-colxx>

            <b-colxx lg="9" xl="9">
                <b-card title="시간대별 이용 현황">
                    <div class="dashboard-line-chart">
                    <line-chart :data="lineChartData" shadow />
                    </div>
                </b-card>
            </b-colxx>
        </b-row>
        <b-row class="mb-4" >
            <b-colxx lg="3" xl="3">
                <b-card title="장르">
                    <div v-for="(g,index) in genres" :key="index" class="mb-4">
                    <p class="mb-2">
                        {{ g.title }}
                        <span class="float-right text-muted">{{g.status}} / {{g.total}}</span>
                    </p>
                    <b-progress :value="(g.status / g.total) * 100"></b-progress>
                    </div>
                </b-card>
            </b-colxx>


            <b-colxx lg="9" xl="9">
                <b-card>
                    <b-colxx xxs="12" class="pl-0 pr-0">
                        <glide-component :settings="glideNoControlsSettings">
                            <div class="pr-3 pl-3 mt-2 mb-2 glide__slide" v-for="(data, index) in dummyData1" :key="index">
                                <b-card no-body>
                                    <div class="position-relative">
                                        <img class="card-img-top" :src="data.src" alt="Card cap" />
                                    </div>
                                    <b-card-body>
                                        <h6 class="mb-4">{{ data.title }}</h6>
                                        <p class="text-muted text-small mb-0 font-weight-light">{{ data.artist }}</p>
                                    </b-card-body>
                                </b-card>
                            </div>
                        </glide-component>
                    </b-colxx>
                </b-card>
            </b-colxx>
        </b-row>
        <b-row>
            <b-colxx lg="3" xl="3" class="mb-4">
                <b-card title="가수">
                    <vue-perfect-scrollbar
                        class="scroll dashboard-list-with-user"
                        :settings="{ suppressScrollX: true, wheelPropagation: false }"
                    >
                        <div class="d-flex flex-row mb-3 pb-3 border-bottom" v-for="(data, index) in artists" :key="index">
                            <img :src="data.thumb" :alt="data.title" class="img-thumbnail border-0 rounded-circle list-thumbnail align-self-center xsmall" />
                            <div class="pl-3 pr-2">
                                <p class="font-weight-medium mb-0 ">{{ data.title }}</p>
                                <p class="text-muted mb-0 text-small">{{ data.detail }}</p>
                            </div>
                        </div>
                    </vue-perfect-scrollbar>
                </b-card>
            </b-colxx>
            <b-colxx lg="9" xl="9">
                <b-card>
                    <b-colxx xxs="12" class="pl-0 pr-0">
                        <glide-component :settings="glideNoControlsSettings">
                            <div class="pr-3 pl-3 mt-2 mb-2 glide__slide" v-for="(data, index) in dummyData1" :key="index">
                                <b-card no-body>
                                    <div class="position-relative">
                                        <img class="card-img-top" :src="data.src" alt="Card cap" />
                                    </div>
                                    <b-card-body>
                                        <h6 class="mb-4">{{ data.title }}</h6>
                                        <p class="text-muted text-small mb-0 font-weight-light">{{ data.artist }}</p>
                                    </b-card-body>
                                </b-card>
                            </div>
                        </glide-component>
                    </b-colxx>
                </b-card>
            </b-colxx>
        </b-row>
    </div>
</template>

<script>
import GradientWithRadialProgressCard from "../../components/Cards/GradientWithRadialProgressCard"
import GlideComponent from '../../components/Carousel/GlideComponent'
import DoughnutChart from "../../components/Charts/Doughnut"
import { ThemeColors } from '../../utils'
import LineChart from "../../components/Charts/Line"
import http from '../../utils/http-common'
import { mapState, mapGetters } from 'vuex'
const colors = ThemeColors()
export default {
    components: {
        "gradient-with-radial-progress-card": GradientWithRadialProgressCard,
        'glide-component': GlideComponent,
        "doughnut-chart": DoughnutChart,
        "line-chart": LineChart
    },
    computed: {
      ...mapState(['user']),
      ...mapGetters(['config']),
      favGenre() {
        if (this.genres.length) return `가장 좋아하는 장르는 ${this.genres[0].title} 입니다.`
        else return ''
      },
      favGenreProp() {
        if (this.genres.length) return Math.ceil(this.genres[0].status/this.genresCnt * 100)
        else return 0
      },
      favAmbiance() {
        return `가장 선호하는 감정의 음악은 ${this.doughnutChartData1.labels[0]} 입니다.`
      },
      favAmbianceProp() {
        let arr = this.doughnutChartData1.datasets[0].data
        const sum = arr.reduce((a,b) => a+b)
        console.log(sum)
        console.log(arr[0])
        return Math.ceil(arr[0]/sum * 100)
      },
    },
    mounted() {
      this.fetchLog()
    },
    data() {
        return {
            genresCnt: '',
            genres: [],
            // [
            //     {
            //         title: '발라드',
            //         total: 783,
            //         status: 392
            //     },
            // ],
            doughnutChartData1: {
                labels: ['Sad', 'Joy', 'Love'],
                datasets: [
                    {
                    label: '',
                    borderColor: [colors.themeColor3, colors.themeColor2, colors.themeColor1],
                    backgroundColor: [
                        colors.themeColor3_10,
                        colors.themeColor2_10,
                        colors.themeColor1_10
                    ],
                    borderWidth: 2,
                    data: [50, 80, 50]
                    }
                ]
            },
            glideNoControlsSettings: {
                gap: 5,
                perView: 5,
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
            lineChartData: {
                labels: ['00', '02', '04', '06', '08', '10', '12', '14', '16', '18', '20', '22'],
                datasets:
                [
                    {
                        label: '',
                        data: [12, 5, 0, 1, 35, 7, 11, 13,  35, 92, 75, 15],
                        borderColor: colors.themeColor1,
                        pointBackgroundColor: colors.foregroundColor,
                        pointBorderColor: colors.themeColor1,
                        pointHoverBackgroundColor: colors.themeColor1,
                        pointHoverBorderColor: colors.foregroundColor,
                        pointRadius: 6,
                        pointBorderWidth: 2,
                        pointHoverRadius: 10,
                        fill: false
                    }
                ]
            },
            dummyData1:
            [
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
            artists:
            [
                {
                    title: 'Mayra Sibley',
                    detail: '1,524번 감상',
                    thumb: '/assets/img/profiles/l-1.jpg'
                },
                {
                    title: 'Mimi Carreira',
                    detail: '1,054번 감상',
                    thumb: '/assets/img/profiles/l-2.jpg'
                },
                {
                    title: 'Philip Nelms',
                    detail: '643번 감상',
                    thumb: '/assets/img/profiles/l-3.jpg'
                },
                {
                    title: 'Terese Threadgill',
                    detail: '214번 감상',
                    thumb: '/assets/img/profiles/l-4.jpg'
                },
                {
                    title: 'Kathryn Mengel',
                    detail: '27.07.2018 - 11:45',
                    thumb: '/assets/img/profiles/l-5.jpg'
                },
                {
                    title: 'Esperanza Lodge',
                    detail: '24.07.2018 - 15:00',
                    thumb: '/assets/img/profiles/l-2.jpg'
                },
                {
                    title: 'Laree Munsch',
                    detail: '24.05.2018 - 11:00',
                    thumb: '/assets/img/profiles/l-1.jpg'
                }
            ]
        }
    },
    methods: {
      async fetchLog() {
        const { data } = await http.get('log/', this.config)
        const genresArr = []
        const ambianceArr = []
        const artistsArr = []
        data.forEach(obj => {
          const genres = obj.song.genres
          genres.forEach(gerne => genresArr.push(gerne.name))
          const ambiance = obj.song.type
          ambianceArr.push(ambiance)
          const artists = obj.song.artist
          artists.forEach(artist => artistsArr.push(artist.name))
        })

        // genre 통계처리
        this.genresCnt = genresArr.length
        const genreSet = new Set(genresArr)
        genreSet.forEach(genre => {
          let cnt = 0
          for (let elem of genresArr) {
            if (elem === genre) cnt ++
          }
          this.genres.push({
            'title': genre,
            'total': genresArr.length,
            'status': cnt
          })
        })
        this.genres.sort((a,b) => {
          return b['status'] - a['status']
        })

        // ambiance 통계처리
        const ambianceObj = {'sad': 0, 'love': 0, 'joy': 0}
        ambianceArr.forEach(ambiance => ambianceObj[ambiance]++)
        console.log(ambianceObj)
        const sortable = []
        for (let amb in ambianceObj) {
          sortable.push([amb, ambianceObj[amb]])
        }
        sortable.sort((a,b) => b[1] - a[1])
        console.log(sortable)
        const ambiance = []
        const cnt = []
        sortable.forEach(arr => {
          ambiance.push(arr[0])
          cnt.push(arr[1])
        })
        this.doughnutChartData1.labels = ambiance
        this.doughnutChartData1.datasets[0].data = cnt
      }
    }
}
</script>

<style>

</style>
