<template>
<div>
    <b-colxx xxs="12" class="px-0">
        <b-colxx xxs="12" class="pl-3 pr-3">
            <b-card class="mb-0" style="text-align: center;">
                <table  class="table table-sm" style="margin-bottom:0px;">
                    <thead style="font-size: initial;">
                        <th id='song' style="cursor:pointer; width: 35%;">곡</th>
                        <th id='artist' style="cursor:pointer; width: 20%;">가수</th>
                        <th id='genre' style="width: 20%;">장르</th>
                        <th id='play' style="width:10%;">재생</th>
                        <th id='like' style="width:10%;">좋아요</th>
                        <th id='addplaylist' style="width:5%;">추가</th>
                    </thead>
                    <tbody>  
                        <tr :class="{'flex-row':true}" v-for="song in logs" v-bind:key="song.id" style="cursor:pointer;">
                        <td class="list-item-heading mb-0 truncate" style="vertical-align: middle; font-size: 0.85rem; width: 35%;" @click="detailSong(song.id)"><img :src="song.img" class="responsive border-0" alt="song_img" width="75px" style="float: left;"/><div style="padding-top:25px; height:75px; padding-left:85px; padding-right:85px;">{{limitString(song.name)}}</div></td>
                        <td class="list-item-heading mb-0 truncate" style="vertical-align: middle; font-size: 0.85rem; width: 20%;" @click="detailSong(song.id)"><a v-for="(member, index) in song.artist" v-bind:key="index">{{member.name}}</a></td>
                        <td class="list-item-heading mb-0 truncate" style="vertical-align: middle; font-size: 0.85rem; width: 20%;" @click="detailSong(song.id)"><a v-for="(genre, index) in song.genres" v-bind:key="index">{{genre.name}}</a>{{song.genre}}</td>
                        <td style="vertical-align: middle; width: 10%;" @click.prevent="addToPlaylistAndPlayNotify(song)"><div class="glyph-icon simple-icon-control-play"/></td>
                        <td :id="song.id" v-if="!checkLikeSong(song.id)" style="vertical-align: middle; width: 10%;" @click="likeSong(song.id)" ><img src="@/assets/img/heart/heart_empty.png" style="width:13px;"/></td>
                        <td :id="song.id" v-if="checkLikeSong(song.id)" style="vertical-align: middle; width: 10%;" @click="likeSong(song.id)" ><img src="@/assets/img/heart/heart_full.png" style="width:13px;"/></td>
                        <td style="vertical-align: middle;">
                        <b-dropdown variant="empty" toggle-class="p-0 m-0" dropleft no-caret style="position:relative;">
                            <template slot="button-content">
                                <div class="glyph-icon simple-icon-playlist text-color" style="font-size: 0.85rem;"/>
                            </template>
                            <b-dropdown-item @click="addToPlaylistAndNotify(song)">현재 재생목록</b-dropdown-item>
                            <b-dropdown-item v-for="(playlist, index) in userPlayList" :key="index" @click="addToUserPlaylist(song, playlist, index)">{{ playlist.name }}</b-dropdown-item>
                        </b-dropdown>
                        </td>
                        </tr>
                    </tbody>
                </table>
            </b-card>
        </b-colxx>
    </b-colxx>
</div>
  
</template>

<script>
import { mapState, mapGetters, mapActions } from 'vuex'
import { adminRoot } from "@/constants/config"
import http from '@/utils/http-common'
import http2 from '@/utils/http-user'
export default {
    data() {
        return {
            logs: [],
            uniqLogs: [],
        }
    },
    methods: {
        ...mapActions(["addToPlaylistAndPlay", "addToPlaylist","likeSong"]),
        limitString(songName) {
            if(songName.length>26){
                return songName.substr(0,22) + "...";
            }else{
                return songName;
            }
        },
        checkLikeSong(songId){
            if(this.user.like_songs){
                for(var i=0;i<this.user.like_songs.length;i++){
                if(this.user.like_songs[i]==songId){
                    return true;
                }
                }
                return false;
            }
            return false;
        },
        detailSong(songId) {
            this.$router.push(`${adminRoot}/songDetail/${songId}`)
        },
        
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
                if (this.playlist[i].id == data.id) {
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
            http2.post(`playlist/${playlist.id}/song/`, {'songs': [data.id]}, this.config)
            .then((value)=> {
                this.$notify('primary', "사용자 재생 목록에 추가 되었습니다.", data.name+" - "+data.artist[0].name, { duration: 4000, permanent: false })
                this.userPlayList[index].song.push(data)
            })
        },

    },

    computed: {
        ...mapState(['user', 'userPlayList', 'playlist']),
        ...mapGetters(['config']),
    
    },
    created() {
        http.get('log/', this.config)
        .then((res) => {
            this.logs = _.uniqBy(res.data.map(obj => obj.song).reverse(), 'id')
            
            
        })
    }

}
</script>

<style>

</style>