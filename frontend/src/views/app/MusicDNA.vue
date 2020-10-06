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
              <b-card>
                <div style="display: flex; justify-content: space-between">
                  <h4>장르</h4>
                  <v-select :options="options" v-model="genreEmo"/>
                </div>
                <div v-for="(g,index) in genres" :key="index" class="mb-4">
                <p class="mb-2" style="cursor: pointer;" @click="fetchGenreSong(g.title)">
                  {{ g.title }}
                  <span class="float-right text-muted">{{g.status}} / {{g.total}}</span>
                </p>
                <b-progress :value="(g.status / g.total) * 100"></b-progress>
                </div>
              </b-card>
            </b-colxx>


            <b-colxx lg="9" xl="9" v-if="genreEmotion.length">
                <b-card>
                    <b-colxx xxs="12" class="pl-0 pr-0">
                        <glide-component :settings="glideNoControlsSettings">
                            <div v-for="(data, index) in genreEmotion" :key="index" class="pr-3 pl-3 mb-4 glide__slide">
                              <b-card no-body>
                                <div class="position-relative">
                                    <a href="#" @click.prevent="search(data.id, 'song')"><img class="card-img-top" :src="data.img" alt="Card cap" /></a>
                                </div>
                                <b-card-body>
                                  <a href="#" @click.prevent="search(data.id, 'song')"><h6 class="mb-4 ellipsis">{{ data.name }}</h6></a>
                                  <a href="#" @click.prevent="search(data.artist[0].id , 'artist')"><p class="text-muted mb-0 font-weight-light ellipsis">{{ data.artist[0].name }}</p></a>
                                  <div class="mt-4" style="font-size:large;">
                                    <span class="glyph-icon simple-icon-control-play mr-2" style="cursor:pointer;" @click="addToPlaylistAndPlayNotify(data)"></span>
                                    <span @click="songLike(data, $event)" :id="data.id" v-if="isLiked(data)" class="glyph-icon simple-icon-heart mr-2 liked" style="cursor:pointer;"></span>
                                    <span @click="songLike(data, $event)" :id='data.id' v-else class="glyph-icon simple-icon-heart mr-2" style="cursor:pointer;"></span>
                                    <b-dropdown variant="empty" dropup toggle-class="p-0 m-0" no-caret>
                                      <template slot="button-content">
                                          <span class="glyph-icon simple-icon-playlist text-color" style="font-size:large; cursor:pointer;"></span>
                                      </template>
                                      <b-dropdown-item @click="addToPlaylistAndNotify(data)">현재 재생목록</b-dropdown-item>
                                      <b-dropdown-item v-for="(playlist, index) in userPlayList" :key="index" @click="addToUserPlaylist(data, playlist, index)">{{ playlist.name }}</b-dropdown-item>
                                    </b-dropdown>
                                  </div>
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
                    <v-select :options="options" v-model="artistEmo"/>
                  </div>
                    <vue-perfect-scrollbar
                        class="scroll dashboard-list-with-user"
                        :settings="{ suppressScrollX: true, wheelPropagation: false }"
                    >
                        <div class="d-flex flex-row mb-3 pb-3 border-bottom" v-for="(data, index) in artists" :key="index">
                            <img :src="data.thumb" :alt="data.title" class="img-thumbnail border-0 rounded-circle list-thumbnail align-self-center xsmall" />
                            <div class="pl-3 pr-2">
                                <p class="font-weight-medium mb-0 " @click="fetchArtistSong(data.id)" style="cursor:pointer;">{{ data.title }}</p>
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
                            <a href="#" @click.prevent="search(data.id, 'song')"><img class="card-img-top" :src="data.img" alt="Card cap" /></a>
                        </div>
                        <b-card-body>
                          <a href="#" @click.prevent="search(data.id, 'song')"><h6 class="mb-4 ellipsis">{{ data.name }}</h6></a>
                          <a href="#" @click.prevent="search(data.artist[0].id, 'artist')"><p class="text-muted mb-0 font-weight-light ellipsis">{{ data.artist[0].name }}</p></a>
                          <div class="mt-4" style="font-size:large;">
                            <span class="glyph-icon simple-icon-control-play mr-2" style="cursor:pointer;" @click="addToPlaylistAndPlayNotify(data)"></span>
                            <span @click="songLike(data, $event)" :id="data.id" v-if="isLiked(data)" class="glyph-icon simple-icon-heart mr-2 liked" style="cursor:pointer;"></span>
                            <span @click="songLike(data, $event)" :id='data.id' v-else class="glyph-icon simple-icon-heart mr-2" style="cursor:pointer;"></span>
                            <b-dropdown variant="empty" dropup toggle-class="p-0 m-0" no-caret>
                              <template slot="button-content">
                                  <span class="glyph-icon simple-icon-playlist text-color" style="font-size:large; cursor:pointer;"></span>
                              </template>
                              <b-dropdown-item @click="addToPlaylistAndNotify(data)">현재 재생목록</b-dropdown-item>
                              <b-dropdown-item v-for="(playlist, index) in userPlayList" :key="index" @click="addToUserPlaylist(data, playlist, index)">{{ playlist.name }}</b-dropdown-item>
                            </b-dropdown>
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
import { mapState, mapGetters, mapActions } from 'vuex'
import {_} from 'vue-underscore'
import 'vue-select/dist/vue-select.css';
import vSelect from "vue-select";
import http2 from "../../utils/http-user"

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
      ...mapState([
        'isLoggedin',
        'userPlayList',
        'user',
        'playlist',
      ]),
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
            artistEmo: '',
            genreEmo: '',
            genresCnt: '',
            genres: [],
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
            genreEmotion: [],
            a: [],
            artists: [],
            artistCnt: '',
            timeSum: '',
            time: []
        }
    },
    methods: {
      ...mapActions(['addToPlaylistAndPlay', 'addToPlaylist']),
      async addToPlaylistAndPlayNotify(data) {
          for(let i=0; i<this.playlist.length; i++) {
              if(this.playlist[i].id == data.id) {
                  this.$notify('warning', "재생 목록에 이미 포함 된 곡입니다.", data.name+" - "+data.artist[0].name, { duration: 4000, permanent: false })
                  return
              }
          }
          this.addToPlaylistAndPlay(data)
          this.$notify('primary', "재생 중인 곡", data.name+" - "+data.artist[0].name, { duration: 4000, permanent: false })
      },
      async addToPlaylistAndNotify(data) {
          for(let i=0; i<this.playlist.length; i++) {
              if(this.playlist[i].id == data.id) {
                  this.$notify('warning', "재생 목록에 이미 포함 된 곡입니다.", data.name+" - "+data.artist[0].name, { duration: 4000, permanent: false })
                  return
              }
          }
          this.addToPlaylist(data)
          this.$notify('primary', "재생 목록에 추가 되었습니다.", data.name+" - "+data.artist[0].name, { duration: 4000, permanent: false })
      },
      addToUserPlaylist(data, playlist, index) {
          for(let i=0; i<playlist.song.length; i++) {
              if(playlist.song[i].id == data.id) {
                  this.$notify('warning', "사용자 재생 목록에 이미 포함 된 곡입니다.", data.name+" - "+data.artist[0].name, { duration: 4000, permanent: false })
                  return
              }
          }
          http2
          .post(`playlist/${playlist.id}/song/`, {'songs': [data.id]}, this.config)
          .then((value)=> {
              this.$notify('primary', "사용자 재생 목록에 추가 되었습니다.", data.name+" - "+data.artist[0].name, { duration: 4000, permanent: false })
              this.userPlayList[index].song.push(data)
          })
      },
      search(word, detail){
          this.$router.push(`/A505/${detail}Detail/${word}`)
      },
      isLiked(data) {
        if (this.user) {
          return this.user.like_songs.includes(data.id);
          } else return false
        },
      async songLike(songData, e) {
        if (this.isLoggedin) {
          const { id } = e.target
          const { data: { liked } } = await http.post(`song/${id}/like/`, '',this.config)
          if (liked) {
            this.$notify('primary', "♥ 좋아요", songData.name+" - "+songData.artist[0].name, { duration: 4000, permanent: false });
            this.$store.state.user.like_songs.push(Number(id))
          } else {
            this.$notify('primary', "♡ 좋아요 취소", songData.name+" - "+songData.artist[0].name, { duration: 4000, permanent: false });
            this.$store.state.user.like_songs = this.$store.state.user.like_songs.filter(song => {
              return song !== Number(id)
            })
          }
        }
      },
      async fetchLog() {
        const { data } = await http.get('log/', this.config)
        if (data.length === 0) {
          alert('로그 데이터가 충분히 쌓이지 않았습니다.')
          this.$router.push('/A505')
        }
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
            id: artist.id,
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
        this.artistEmo = ambiance[0]
        this.genreEmo = ambiance[0]
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
            thumb: artist.img,
            id: artist.id
          })
        })
        this.a.sort((a,b) => {
          return b['detail'] - a['detail']
        })
        this.a.forEach(artist => {
          this.artists.push({
            title: artist.title,
            detail: `${artist.detail} 번`,
            thumb: artist.thumb,
            id: artist.id,
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
        await this.fetchArtistSong(this.artists[0]['id'])
        await this.fetchGenreSong(this.genres[0]['title'])
      },
      async fetchArtistSong(artistId) {
        console.log(artistId)
        const { data } = await http.get(`musicdna/artist/?emotion=${this.artistEmo}&keyword=${Number(artistId)}`, this.config)
        this.artistEmotion = data
      },
      async fetchGenreSong(genre) {
        const { data } = await http.get(`musicdna/genre/?emotion=${this.genreEmo}&keyword=${genre}`, this.config)
        this.genreEmotion = data
      }
    }
}
</script>

