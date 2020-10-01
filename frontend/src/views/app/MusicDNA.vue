<template>
    <div v-if="genres.length">
        <div class="mb-4">
            <h3>{{ user.username }}님은 {{ new Date().getFullYear() }}.{{ new Date().getMonth() + 1 }}.{{ new Date().getDate() }}까지 {{ genresCnt }}개의 곡의 음악을 감상하고 있습니다.</h3>
        </div>
        <b-row>
            <b-colxx lg="3" xl="3" class="mb-4">
                <gradient-with-radial-progress-card
                    icon="simple-icon-heart"
                    title="ambience"
                    :detail=favAmbiance
                    :percent=Number(favAmbianceProp.slice(0,favAmbianceProp.length-1))
                    :progressText=favAmbianceProp
                />
            </b-colxx>
            <b-colxx lg="3" xl="3" class="mb-4">
                <gradient-with-radial-progress-card
                    icon="simple-icon-star"
                    title="Genre"
                    :detail=favGenre
                    :percent=Number(favGenreProp.slice(0,favGenreProp.length-1))
                    :progressText=favGenreProp
                />
            </b-colxx>
            <b-colxx lg="3" xl="3" class="mb-4">
                <gradient-with-radial-progress-card
                    icon="simple-icon-user"
                    title="Artist"
                    :detail=favArtist
                    :percent=Number(favArtistProp.slice(0,favArtistProp.length-1))
                    :progressText=favArtistProp
                />
            </b-colxx>
            <b-colxx lg="3" xl="3" class="mb-4">
                <gradient-with-radial-progress-card
                    icon="simple-icon-clock"
                    title="Time"
                    :detail=favTime
                    :percent=Number(favTimeProp.slice(0,favTimeProp.length-1))
                    :progressText=favTimeProp
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
                <b-card>
                  <div style="display: flex; justify-content: space-between">
                    <h4>가수</h4>
                    <v-select :options="options" v-model="emo"/>
                  </div>
                    <vue-perfect-scrollbar
                        class="scroll dashboard-list-with-user"
                        :settings="{ suppressScrollX: true, wheelPropagation: false }"
                    >
                        <div class="d-flex flex-row mb-3 pb-3 border-bottom" v-for="(data, index) in artists" :key="index">
                            <img :src="data.thumb" :alt="data.title" class="img-thumbnail border-0 rounded-circle list-thumbnail align-self-center xsmall" />
                            <div class="pl-3 pr-2">
                                <p class="font-weight-medium mb-0 " @click="fetchArtistSong(data.title)" style="cursor:pointer;">{{ data.title }}</p>
                                <p class="text-muted mb-0 text-small">{{ data.detail }}</p>
                            </div>
                        </div>
                    </vue-perfect-scrollbar>
                </b-card>
            </b-colxx>
            <b-colxx lg="9" xl="9" v-if="artistEmotion.length">
                <b-card>
                    <b-colxx xxs="12" class="pl-0 pr-0">
                        <glide-component :settings="glideNoControlsSettings">
                            <div v-for="(data, index) in artistEmotion" :key="index" class="pr-3 pl-3 mb-4 glide__slide">
                              <b-card no-body>
                                <div class="position-relative">
                                    <a href="#" @click.prevent="search(data.name)"><img class="card-img-top" :src="data.img" alt="Card cap" /></a>
                                </div>
                                <b-card-body>
                                  <a href="#" @click.prevent="search(data.name)"><h6 class="mb-4 ellipsis">{{ data.name }}</h6></a>
                                  <a href="#" @click.prevent="search(data.artist)"><p class="text-muted mb-0 font-weight-light ellipsis">{{ data.artist[0].name }}</p></a>
                                  <div class="mt-4" style="font-size:x-large;">
                                    <span class="glyph-icon simple-icon-control-play mr-3" style="cursor:pointer;" @click="addToPlaylistAndPlay(data)"></span>
<!--                                    <span v-if="isLiked(data)" class="glyph-icon simple-icon-heart mr-3" style="cursor:pointer;"></span>-->
                                    <span class="glyph-icon simple-icon-heart mr-3" style="cursor:pointer;"></span>
                                    <span class="glyph-icon simple-icon-playlist mr-3" style="cursor:pointer;" @click="addToPlaylist(data)"></span>
                                  </div>
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
import {_} from 'vue-underscore'
import 'vue-select/dist/vue-select.css';
import vSelect from "vue-select";

const colors = ThemeColors()
export default {
    components: {
        "gradient-with-radial-progress-card": GradientWithRadialProgressCard,
        'glide-component': GlideComponent,
        "doughnut-chart": DoughnutChart,
        "line-chart": LineChart,
        "v-select": vSelect
    },
    computed: {
      ...mapState(['user']),
      ...mapGetters(['config']),
      favGenre() {
        if (this.genres.length) return `가장 좋아하는 장르는 ${this.genres[0].title} 입니다.`
        else return ''
      },
      favGenreProp() {
        if (this.genres.length) return Math.ceil(this.genres[0].status/this.genresCnt * 100) + '%'
        else return 0 + '%'
      },
      favAmbiance() {
        if (this.doughnutChartData1.labels[0])
        return `가장 선호하는 감정의 음악은 ${this.doughnutChartData1.labels[0]} 입니다.`
      },
      favAmbianceProp() {
        let arr = this.doughnutChartData1.datasets[0].data
        if (arr.length) {
          const sum = arr.reduce((a,b) => a+b)
          return Math.ceil(arr[0]/sum * 100) + '%'
        } else {
          return 0 + '%'
        }
      },
      favArtist() {
        if (this.artists.length) return `가장 많이 들은 가수는 ${this.artists[0].title} 입니다.`
        else return ''
      },
      favArtistProp() {
        if (this.artists.length) return Math.ceil(this.a[0].detail/this.artistCnt * 100) + '%'
        else return 0 + '%'
      },
      favTime() {
        if (this.time.length) return `${this.time[0][0]} 시에서 ~ ${Number(this.time[0][0]) + 2} 시 사이에 가장 많이 들었습니다.`
      },
      favTimeProp() {
        if (this.timeSum) return Math.ceil(Number(this.time[0][1] / this.timeSum) * 100) + '%'
        else return 0
      }
    },
    mounted() {
      this.fetchLog()
    },
    data() {
        return {
            artistEmotion: [],
            options: ['sad','joy','love'],
            emo: '',
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
                labels: [],
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
                    data: []
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
                        data: [],
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
            a: [],
            artists: [],
            artistCnt: '',
            // [
            //     {
            //         title: 'Mayra Sibley',
            //         detail: '1,524번 감상',
            //         thumb: '/assets/img/profiles/l-1.jpg'
            //     },
            // ],
            timeSum: '',
            time: []
        }
    },
    methods: {
      async fetchLog() {
        const { data } = await http.get('log/', this.config)
        const genresArr = []
        const ambianceArr = []
        const artistsArr = []
        const timeArr = []
        data.forEach(obj => {
          const genres = obj.song.genres
          genres.forEach(gerne => genresArr.push(gerne.name))
          const ambiance = obj.song.type
          ambianceArr.push(ambiance)
          const artists = obj.song.artist
          artists.forEach(artist => artistsArr.push({
            name: artist.name,
            img: artist.img,
          }))
          timeArr.push(new Date(obj.time).getHours())
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
        const sortable = []
        for (let amb in ambianceObj) {
          sortable.push([amb, ambianceObj[amb]])
        }
        sortable.sort((a,b) => b[1] - a[1])
        const ambiance = []
        const cnt = []
        sortable.forEach(arr => {
          ambiance.push(arr[0])
          cnt.push(arr[1])
        })
        this.emo = ambiance[0]
        this.doughnutChartData1.labels = ambiance
        this.doughnutChartData1.datasets[0].data = cnt

        // artist 통계처리
        this.artistCnt = artistsArr.length
        const artistsSet = _.uniq(artistsArr, 'name')
        artistsSet.forEach(artist => {
          let cnt = 0
          for (let elem of artistsArr) {
            if (elem.name === artist.name) cnt ++
          }
          this.a.push({
            title: artist.name,
            detail: cnt,
            thumb: artist.img
          })
        })
        this.a.sort((a,b) => {
          return b['detail'] - a['detail']
        })
        this.a.forEach(artist => {
          this.artists.push({
            title: artist.title,
            detail: `${artist.detail} 번`,
            thumb: artist.thumb
          })
        })
        // 감상시간 통계처리
        const timeObj = {0:0, 2:0, 4:0, 6:0, 8:0, 10:0, 12:0, 14:0, 16:0, 18:0, 20:0, 22:0}
        timeArr.forEach(time => {
          if (time >=0 && time < 2) timeObj[0]++
          else if (time >=2 && time < 4) timeObj[2]++
          else if (time >=4 && time < 6) timeObj[4]++
          else if (time >=6 && time < 8) timeObj[6]++
          else if (time >=8 && time < 10) timeObj[8]++
          else if (time >=10 && time < 12) timeObj[10]++
          else if (time >=12 && time < 14) timeObj[12]++
          else if (time >=14 && time < 16) timeObj[14]++
          else if (time >=16 && time < 18) timeObj[16]++
          else if (time >=18 && time < 20) timeObj[18]++
          else if (time >=20 && time < 22) timeObj[20]++
          else timeObj['22']++
        })
        const timeSet = []
        const timeSortable = []
        for (let time in timeObj) {
          timeSet.push(timeObj[time])
          timeSortable.push([time, timeObj[time]])
        }
        this.lineChartData.datasets[0].data = timeSet
        timeSortable.sort((a,b) => b[1] - a[1])
        this.time = timeSortable
        let timesum = 0
        for (let i of timeSortable) {
          timesum += i[1]
        }
        this.timeSum = timesum
        // this.fetchArtistSong()
      },
      async fetchArtistSong(artistName) {
        const { data } = await http.get(`musicdna/artist/?emotion=${this.emo}&keyword=${artistName}`, this.config)
        this.artistEmotion = data
      }
    }
}
</script>

<style>

</style>
