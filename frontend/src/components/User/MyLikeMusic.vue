<template>
<div>
    <h3>곡</h3>
    <b-row>
        <b-colxx cols="2" class="mb-4 pl-3 pr-3" v-for="(song, index) in songs" :key="index" v-if="isLike(song.id)">
            <div>
                <b-card no-body>
                    <div class="position-relative">
                        <a href="#" @click.prevent="search(song.title)">
                            <img class="card-img-top" :src="song.img" alt="Card cap" />
                        </a>
                    </div>
                    <b-card-body>
                        <a href="#" @click.prevent="tempFunction"><h6 class="mb-4 ellipsis">{{ song.name }}</h6></a>
                        <a href="#" @click.prevent="tempFunction"><p class="text-muted mb-0 font-weight-light ellipsis">{{ song.artist[0].name }}</p>
                        </a>
                        <div class="mt-4" style="font-size:x-large;">
                            <span class="glyph-icon simple-icon-control-play mr-3" style="cursor:pointer;" @click="addToPlaylistAndPlay(song)"></span>
                            <span v-if="isLike(song.id)" class="glyph-icon simple-icon-heart mr-3 liked" style="cursor:pointer;" @click="songLike(song.id)"></span>
                            <span v-else class="glyph-icon simple-icon-heart mr-3" style="cursor:pointer;" @click="songLike(song.id)"></span>
                            <b-dropdown variant="empty" toggle-class="p-0 m-0 pt-1 pl-1" no-caret style="position:absolute;">
                                <template slot="button-content">
                                    <span class="glyph-icon simple-icon-playlist text-secondary" style="font-size:x-large; cursor:pointer;"></span>
                                </template>
                                <b-dropdown-item @click="addToPlaylistAndNotify(data)">현재 재생목록</b-dropdown-item>
                                <b-dropdown-item v-for="(playlist, index) in userPlayList" :key="index" @click="addToUserPlaylist(song, playlist, index)">{{ playlist.name }}</b-dropdown-item>
                            </b-dropdown>
                        </div>
                    </b-card-body>
                </b-card>
            </div>
            
        </b-colxx>
    </b-row>
    <hr>
    <h3>앨범</h3>
    <b-row>
    <b-colxx cols="2" class="mb-4 pl-3 pr-3" style="display: inline-flex;" v-for="(album, index) in albums" v-bind:key="index">
            <b-card no-body  style=" cursor:pointer;" >
                <div class="position-relative">
                    <img :src="album.img" class="card-img-top"/>
                </div>
                <b-card-body>
                    <b-row>
                        <b-colxx>
                            <h6 style="font-weight :bold">{{album.name}}</h6>
                            <p><a v-for="(singer, index) in album.artist" v-bind:key="index">{{singer.name}}</a></p>
                            <p v-if="album.genre">장르:<a v-for="(genre, index) in album.genres" v-bind:key="index"> {{genre.name}}</a></p>
                            <p>발매일: {{dateformat(album.released_date)}}</p>
                            <img src="../../assets/img/heart/heart_empty.png" v-if="!checkLikeAlbum(index)" style="width:32px;" @click="likeAlbum(album.id, index)"/>
                            <img src="../../assets/img/heart/heart_full.png" v-if="checkLikeAlbum(index)" style="width:32px;" @click="likeAlbum(album.id, index)"/>
                        </b-colxx>
                    </b-row>
                </b-card-body>
            </b-card>
    </b-colxx>
    </b-row>
</div>
</template>

<script>
import http from '@/utils/http-common'
import http2 from '@/utils/http-user'
import { mapState, mapGetters, mapActions } from 'vuex'
import axios from 'axios'
const youtubeURL = 'https://www.googleapis.com/youtube/v3/search'
const API_KEY = process.env.VUE_APP_YOUTUBE_API_KEY
export default {
    data() {
        return {
            songs: [],
            albums: []
        }
    },
    methods: {
        ...mapActions(["addToPlaylist"]),
        getMusic() {
            for ( var i=0; i < this.user.like_songs.length; i++ ) {
                const song_id = this.user.like_songs[i]
                http.get(`song/${song_id}`)
                .then((res) => {
                    this.songs.push(res.data)
                })
            }

        },
        getAlbum() {
            for ( var i=0; i < this.user.like_albums.length; i++ ) {
                const album_id = this.user.like_albums[i]
                http.get(`album/${album_id}`)
                .then((res) => {
                    this.albums.push(res.data.data)
                })   
            }
        },
        isLike(songId) {
            if (this.user)
                return this.user.like_songs.includes(songId)
            else
                return false

        },
        async songLike(id) {      
                const { data: { liked } } = await http.post(`song/${id}/like/`, '',this.config)
                if (liked) {
                    // this.$notify('primary', "좋아요", this.song.name+" - "+this.song.artist[0].name, { duration: 5000, permanent: false });
                    this.$store.state.user.like_songs.push(Number(id))
                }
                else {
                    // this.$notify('primary', "좋아요 취소", '', { duration: 5000, permanent: false });
                    this.$store.state.user.like_songs = this.$store.state.user.like_songs.filter(song => {
                        return song !== Number(id)
                    })
                }        
        },
        async addToPlaylistAndNotify(data) {
            this.addToPlaylist(data)
            this.$notify('primary', "재생 목록에 추가 되었습니다.", data.name+" - "+data.artist[0].name, { duration: 4000, permanent: false })
        },
        addToUserPlaylist(data, playlist, index) {
            console.log(data)
            console.log(playlist)
            http2
            .post(`playlist/${playlist.id}/song/`, {'songs': [data.id]}, this.config)
            .then((value)=> {
                this.$notify('primary', "사용자 재생 목록에 추가 되었습니다.", data.name+" - "+data.artist[0].name, { duration: 4000, permanent: false })
                this.userPlayList[index].song.push(data)
            })
        },
        dateformat(albumDate) {
            return albumDate.substr(0,4) + "-" + albumDate.substr(4,2) + "-" + albumDate.substr(6,2);
        },
        checkLikeAlbum(index){
            if(this.user){
                for(var i=0;i<this.albums[index].user_like.length;i++){
                if(this.albums[index].user_like[i].id==this.user.id){
                    return true;
                }
                }
                return false;
            }
            return false;
        },
        async fetchYoutubeId(song) {
          const { data } = await axios.get(youtubeURL, {
            params: {
              key: API_KEY,
              part: 'snippet',
              maxResults: 1,
              type: 'video',
              q: song.artist[0].name + ' ' + song.name
            }
          })
          const { items } = data
          const { videoId } = items[0].id
          const reqData = {'src': videoId}
          song['src'] = videoId
          await http.post(`addsrc/${song.id}/`, reqData,'')
        },
        // 한곡 재생
        async addToPlaylistAndPlay(song) {
            this.$store.state.playerControl = "pause"
            if (song['src']) {
                this.playlist.unshift(song)
                this.$store.state.playerControl = "add"
                this.$notify('primary', "재생 중인 곡", song.name+" - "+song.artist[0].name, { duration: 4000, permanent: false })
            } else {
                await this.fetchYoutubeId(song)
                this.playlist.unshift(song)
                this.$store.state.playerControl = "add"
                this.$notify('primary', "재생 중인 곡", song.name+" - "+song.artist[0].name, { duration: 4000, permanent: false })
            }
        },

    },
    computed: {
        ...mapState(['user', 'playlist', 'userPlayList']),
        ...mapGetters(['config'])
    },
    created() {
        this.getMusic()
        this.getAlbum()
    }

}
</script>

<style>

</style>