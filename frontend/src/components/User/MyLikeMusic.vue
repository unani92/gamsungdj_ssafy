<template>
<div>
    <h3>곡</h3>
    <b-row>
        <b-colxx cols="2" class="mb-4 pl-3 pr-3" v-for="(song, index) in songs" :key="index" >
            <div >
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
                            <span class="glyph-icon simple-icon-heart mr-3" style="cursor:pointer;"></span>
                            <span class="glyph-icon simple-icon-playlist mr-3" style="cursor:pointer;" @click="addToPlaylist(song)"></span>
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
import { mapState } from 'vuex'
export default {
    data() {
        return {
            songs: [],
            albums: []
        }
    },
    methods: {
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

    },
    computed: {
        ...mapState(['user'])
    },
    created() {
        this.getMusic()
        this.getAlbum()
    }

}
</script>

<style>

</style>