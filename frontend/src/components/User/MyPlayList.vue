<template>
<div>
    <b-button @click="showCreatePlayList = !showCreatePlayList" variant="primary">플레이리스트 생성</b-button>
    <!-- 플레이리스트 생성 모달 -->
    <b-modal v-model="showCreatePlayList" id="modalbackdrop" title="플레이리스트 생성"
            :no-close-on-backdrop="true"
            :hide-header-close="true"
            centered>
        <b-row style="justify-content: center;">
            <b-form style="width:100%;">
                <b-form-group id="input-group" label="플레이리스트 이름" label-for="input-name">
                    <b-form-input
                    id="input-name"
                    v-model="name"
                    required
                    placeholder="생성할 플레이리스트 이름을 작성해 주세요."
                    ></b-form-input>
                </b-form-group>
            </b-form>
        </b-row>
        <template slot="modal-footer">
            <b-button variant="primary" :disabled="name.length<1" @click="createPlayList(name)">생성</b-button>
            <b-button variant="secondary" @click="showCreatePlayList = false">취소</b-button>
        </template>
    </b-modal>
   <!-- 플레이 리스트 관리 모달 -->
    <b-modal v-model="showAdmin" id="modalbackdrop"
        :hide-header-close="true"
        :no-close-on-backdrop="true"
        centered
        size="xl">
        <template v-slot:modal-header>
            <div class="d-flex justify-content-between align-items-center" style="width:100%">
                <div class="d-flex align-items-center" v-if="!updateName">
                    <h5 class="m-0">{{adminList.name}} 관리</h5><span @click="updateName=true" class="glyph-icon simple-icon-pencil ml-2"></span>
                </div>
                <div class="d-flex align-items-center" v-else>
                    <b-form-input v-model="adminList.name"/><span @click="updatePlayList" class="glyph-icon simple-icon-pencil ml-2"></span>
                </div>
                <div>
                    <b-button variant="outline-secondary" size="xs" @click="showSearch=true">노래 추가</b-button>
                    <b-button variant="outline-primary" size="xs" @click="deleteSong">노래 삭제</b-button>
                </div>
            </div>
        </template>
        <b-row style="justify-content: center;">
            <table  class="table table-sm" style="margin-bottom:0px; display:block; width:100%;">
                <thead style="font-size: initial; text-align: center;">
                    <th></th>
                    <th id="checkbox" key="checkbox" style="width:5%;"></th>
                    <th id='song' @click="changeSortValue('name')" style="cursor:pointer; width:35%;">곡</th>
                    <th id='artist' @click="changeSortValue('artist')" style="cursor:pointer; width:20%;">가수</th>
                    <th style="width: 20%;">장르</th>
                    <th style="width: 10%;">재생</th>
                    <th style="width: 10%;">좋아요</th>
                </thead>
                <tbody style="display:block; height:480px; overflow: auto; text-align:center; width:100%;">
                    <b-form-group>
                    <b-form-checkbox-group v-model="deleteItems">
                    <tr :class="{'flex-row':true}" v-for="(song, index) in adminList.song" v-bind:key="index" style="cursor:pointer; width: 100%;">
                    <td></td>
                    <td style="width:5%; vertical-align: middle;">
                        <b-form-checkbox :value="song.id" :id="'delete-checkbox-'+song.id"/>
                    </td>
                    <td class="list-item-heading mb-0 truncate" style="vertical-align: middle; width: 35%; font-size: 0.85rem;" @click="addDeleteList(song.id)"><img :src="song.img" class="responsive border-0" alt="song_img" width="75px" style="float: left;"/><div style="padding-top:25px; height:75px; padding-left:85px;">{{limitString(song.name)}}</div></td>
                    <td class="list-item-heading mb-0 truncate" style="vertical-align: middle; width: 20%; font-size: 0.85rem;" @click="addDeleteList(song.id)"><a v-for="(member, index) in song.artist" v-bind:key="index">{{member.name}}</a></td>
                    <td class="list-item-heading mb-0 truncate" style="vertical-align: middle; width: 20%; font-size: 0.85rem;" @click="addDeleteList(song.id)"><a v-for="(genre, index) in song.genres" v-bind:key="index">{{genre.name}}</a>{{song.genre}}</td>
                    <td style="vertical-align: middle; width:10%;" @click.prevent="addToPlaylistAndPlay(song)" ><div class="glyph-icon simple-icon-control-play"/></td>
                    <td v-if="!checkLikeSong(song.id)" style="vertical-align: middle; width:10%;" @click="likeSong(song.id)" ><img src="../../assets/img/heart/heart_empty.png" style="width:15px;"/></td>
                    <td v-if="checkLikeSong(song.id)" style="vertical-align: middle; width:10%;" @click="likeSong(song.id)" ><img src="../../assets/img/heart/heart_full.png" style="width:15px;"/></td>
                    </tr>
                    </b-form-checkbox-group>
                    </b-form-group>
                </tbody>
            </table>
            
        </b-row>
        <template slot="modal-footer">
            <div class="d-flex justify-content-between w-100">
                <b-button variant="primary" @click="deletePlayList(adminList.id)">플레이리스트 삭제</b-button>
                <b-button variant="secondary" @click="hideAdmin">완료</b-button>
            </div>
        </template>
    </b-modal>

    <!-- 곡 추가 모달 -->
    <b-modal v-model="showSearch" id="modalbackdrop" 
        :hide-header-close="true"
        :no-close-on-backdrop="true"
        centered size="xl">
        <template v-slot:modal-header>
            <div class="d-flex justify-content-between align-items-center" style="width:100%">
            <h5>노래 추가</h5>
            <b-input-group class="mr-3" style="width:30%">
                <b-form-input @keypress.native.enter="search" v-model="searchKeyword" style="border-radius: 30px;" placeholder="검색어를 입력하세요"/>
                <b-input-group-append @click="search" style="cursor:pointer; margin-left: -35px; z-index: 10; align-items:center;">
                    <i class="simple-icon-magnifier"></i>
                </b-input-group-append>
            </b-input-group>
            </div>
        </template>
        <!-- 곡 추가 모달 바디 -->
        <b-row style="justify-content: center; min-height:400px;">
            <h5 v-if="searchBodyKeyword">> {{searchBodyKeyword}}에 대한 검색 결과</h5>
            
            <table class="table table-sm" style="margin-bottom:0px; display:block; width:100%;" v-if="searchBodyKeyword">
                <thead style="font-size: initial; width:100%; text-align:center;">
                    <th ></th>
                    <th id="checkbox" key="checkbox" style="width:5%;"></th>
                    <th id='song' @click="changeSortValue('name')" style="cursor:pointer; width:35%;">곡</th>
                    <th id='artist' @click="changeSortValue('artist')" style="cursor:pointer; width:20%;">가수</th>
                    <th style="width:20%">장르</th>
                    <th style="width:10%">재생</th>
                    <th style="width:10%">좋아요</th>
                </thead>
                <tbody style="display:block; height:480px; overflow: auto; text-align:center; width:100%;">
                    <b-form-group>
                    <b-form-checkbox-group v-model="selectedItems">
                    <tr :class="{'flex-row':true}" v-for="(song, index) in searchList" v-bind:key="index" style="cursor:pointer; width:100%;">
                    <td></td>
                    <td style="width:5%; vertical-align: middle;">
                        <b-form-checkbox :value="song.id" :id="'checkbox-'+song.id"/>
                    </td>
                    <td class="list-item-heading mb-0 truncate" style="vertical-align: middle; width: 35%; font-size: 0.85rem;" @click="addSelectList(song.id)"><img :src="song.img" class="responsive border-0" alt="song_img" width="75px" style="float: left;"/><div style="padding-top:25px; height:75px; text-align:left; padding-left:85px;">{{limitString(song.name)}}</div></td>
                    <td class="list-item-heading mb-0 truncate" style="vertical-align: middle; width: 20%; font-size: 0.85rem;" @click="addSelectList(song.id)"><a v-for="(member, index) in song.artist" v-bind:key="index">{{member.name}}</a></td>
                    <td class="list-item-heading mb-0 truncate" style="vertical-align: middle; width: 20%; font-size: 0.85rem;" @click="addSelectList(song.id)"><a v-for="(genre, index) in song.genres" v-bind:key="index">{{genre.name}}</a>{{song.genre}}</td>
                    <td style="vertical-align: middle; width:10%;" @click.prevent="addToPlaylistAndPlay(song)" ><div class="glyph-icon simple-icon-control-play"/></td>
                    <td v-if="!checkLikeSong(song.id)" style="vertical-align: middle; width:10%;" @click="likeSong(song.id)" ><img src="../../assets/img/heart/heart_empty.png" style="width:15px;"/></td>
                    <td v-if="checkLikeSong(song.id)" style="vertical-align: middle; width:10%;" @click="likeSong(song.id)" ><img src="../../assets/img/heart/heart_full.png" style="width:15px;"/></td>
                    </tr>
                    </b-form-checkbox-group>
                    </b-form-group>
                </tbody>
            </table>
        </b-row>
        <template slot="modal-footer">
            <b-button variant="primary" :disabled="selectedItems.length<1" @click="addPlayList">추가</b-button>
            <b-button variant="secondary" @click="hideSearch">취소</b-button>
        </template>
    </b-modal>
    <!-- 플레이 리스트 -->
    <div v-for="playlist in playlists" :key="playlist.id" class="mt-3">
        <div class="d-flex justify-content-between align-items-center px-3">
            <h5>{{playlist.name}}</h5>
            <div>
                <b-button size="xs" variant="outline-secondary" class="mb-2" @click="adminPlayList(playlist.id)">관리</b-button>
                <b-button size="xs" variant="outline-primary" class="ml-1 mb-2">펼치기</b-button>
            </div>
        </div>
        <b-colxx xxs="12" class="px-0">
            <b-colxx xxs="12" class="pl-3 pr-3">
                <b-card class="mb-0" style="text-align: center;">
                    <table  class="table table-sm" style="margin-bottom:0px;">
                        <thead style="font-size: initial;">
                            <th id='song' @click="changeSortValue('name')" style="cursor:pointer; width: 40%;">곡</th>
                            <th id='artist' @click="changeSortValue('artist')" style="cursor:pointer; width: 20%;">가수</th>
                            <th id='genre' style="cursor:pointer; width: 20%;">장르</th>
                            <th id='play' style="width:10%;">재생</th>
                            <th id='like' style="width:10%;">좋아요</th>
                        </thead>
                        <tbody>
                            <tr :class="{'flex-row':true}" v-for="(song, index) in playlist.song" v-bind:key="index" style="cursor:pointer;">
                            <td class="list-item-heading mb-0 truncate" style="vertical-align: middle; font-size: 0.85rem; width: 40%;" @click="detailSong(song.id)"><img :src="song.img" class="responsive border-0" alt="song_img" width="75px" style="float: left;"/><div style="padding-top:25px; height:75px; padding-left:85px; padding-right:85px;">{{limitString(song.name)}}</div></td>
                            <td class="list-item-heading mb-0 truncate" style="vertical-align: middle; font-size: 0.85rem; width: 20%;" @click="detailSong(song.id)"><a v-for="(member, index) in song.artist" v-bind:key="index">{{member.name}}</a></td>
                            <td class="list-item-heading mb-0 truncate" style="vertical-align: middle; font-size: 0.85rem; width: 20%;" @click="detailSong(song.id)"><a v-for="(genre, index) in song.genres" v-bind:key="index">{{genre.name}}</a>{{song.genre}}</td>
                            <td style="vertical-align: middle; width: 10%;" @click.prevent="addToPlaylistAndPlay(song)"><div class="glyph-icon simple-icon-control-play"/></td>
                            <td v-if="!checkLikeSong(song.id)" style="vertical-align: middle; width: 10%;" @click="likeSong(song.id)" ><img src="../../assets/img/heart/heart_empty.png" style="width:13px;"/></td>
                            <td v-if="checkLikeSong(song.id)" style="vertical-align: middle; width: 10%;" @click="likeSong(song.id)" ><img src="../../assets/img/heart/heart_full.png" style="width:13px;"/></td>
                            </tr>
                        </tbody>
                    </table>
                </b-card>
            </b-colxx>
        </b-colxx>
        <hr>
    </div>
    
</div>
  
</template>

<script>
import httpUser from '@/utils/http-user'
import http from '@/utils/http-common'
import { mapState, mapGetters } from 'vuex'
import { adminRoot } from "@/constants/config"
export default {
    
    data() {
        return {
            playlists: [],
            adminList: [],
            name: '',
            showCreatePlayList: false,
            showAdmin: false,
            showSearch: false,
            isSong: false,
            sort_value : "",
            sort_type : 'asc',
            // 관리 모달
            updateName: false,
            deleteItems: [],
            // 곡 추가 모달
            searchKeyword: "",
            searchBodyKeyword: "",
            searchList: [],
            selectedItems: [],
            
        }
    },
    methods: {
        getPlaylist() {
            httpUser.get('playlist/', this.config)
            .then(res => {
                this.playlists = res.data
                
            })
        },
        createPlayList(name) {
            httpUser.post('playlist/', {"name": name}, this.config)
            .then(res => {
                this.playlists.unshift(res.data)
                this.name = ''
            })
        },
        detailSong(id) {
            this.$router.push(`${adminRoot}/songDetail/${id}`)
        },
        adminPlayList(id) {
            this.showAdmin = true
            httpUser.get(`playlist/${id}/`, this.config)
            .then(res => {
                this.adminList = res.data
            })

        },
        
        changeSortValue(value) {
            if(this.sort_value != value){
                this.sort_value=value;
                this.sort_type = 'asc';
            }else{
                if(this.sort_type =='asc'){
                this.sort_type = 'desc';
                }else if(this.sort_type =='desc'){
                this.sort_value = '';
                this.sort_type = 'none';
                }else{
                this.sort_type = 'asc'
                }
            }

            var tag1 = document.getElementById('song');
            var tag2 = document.getElementById('artist');
            if(this.sort_value=='name'){
                tag1.style.color = "#236591";
            }else {
                tag1.style.color = "";
            }

            if(this.sort_value=='artist'){
                tag2.style.color = "#236591";
            }else {
                tag2.style.color = "";
            }
        },
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
        likeSong(id) {

        },
        updatePlayList() {
            httpUser.put(`playlist/${this.adminList.id}/`, {"name": this.adminList.name}, this.config)
            .then((res) => {
                this.adminList = res.data
                this.updateName = false
            })
        },
        deletePlayList(id) {
            if (confirm(`${this.adminList.name}을 삭제하시겠습니까?`) == true) {
                httpUser.delete(`playlist/${this.adminList.id}/`, this.config)
                .then((res) => {
                    this.playlists = res.data
                    this.hideAdmin()
                })
            }   
        },
        addDeleteList(id) {
            var checkbox = document.getElementById("delete-checkbox-"+id)
            checkbox.checked = !checkbox.checked
            if (this.deleteItems.includes(id)) {
                const idx = this.deleteItems.indexOf(id)
                this.deleteItems.splice(idx, 1)
            }
            else {
                this.deleteItems.push(id)
            }
        },
        deleteSong() {
            httpUser.delete(`playlist/${this.adminList.id}/song/`, {data: {"songs":this.deleteItems}, headers: {Authorization: this.authorization}})
            .then((res) => {
                this.adminList = res.data
                this.getPlaylist()
            })
        },
        search() {
            const keyword = this.searchKeyword
            this.searchBodyKeyword = keyword
            console.log("search", keyword)
            http.get(`/search/song/${keyword}/`)
            .then((res) => {
                this.searchList = res.data;
                this.searchKeyword = ""
                if (this.searchList.length!=0) {
                    this.isSong = true
                    
                }
                else {
                    this.isSong = false
                }
            })
        },
        addSelectList(id) {
            var checkbox = document.getElementById("checkbox-"+id)
            checkbox.checked = !checkbox.checked
            if (this.selectedItems.includes(id)) {
                const idx = this.selectedItems.indexOf(id)
                this.selectedItems.splice(idx, 1)
            }
            else {
                this.selectedItems.push(id)
            }          
        },
        addPlayList() {
            httpUser.post(`playlist/${this.adminList.id}/song/`, {"songs":this.selectedItems}, this.config)
            .then((res) => {
                this.adminList = res.data
                this.hideSearch()
                this.getPlaylist()
            })    
        },
        hideAdmin() {
            this.showAdmin = false
            this.adminList = []
            this.deleteItems = []
            this.updateName = false
            this.getPlaylist()
        },
        hideSearch() {
            this.showSearch = false
            this.searchKeyword = ''
            this.searchBodyKeyword = ''
            this.searchList = []
            this.selectedItems = []
            this.isSong = false
        },
    
    },
    computed: {
        ...mapState(['authorization', 'user']),
        ...mapGetters(['config']),
        sortSongs() {
            if(this.sort_value=='name'){
                if(this.sort_type=='asc'){
                return this.songs.sort((a, b) => {
                if( a.name > b.name) return 1;
                else if ( a.name < b.name ) return -1;
                else return 0;
                })
                }else if(this.sort_type=='desc'){
                return this.songs.sort((a, b) => {
                    if( a.name < b.name) return 1;
                    else if ( a.name > b.name ) return -1;
                    else return 0;
                })
                }
            }else if(this.sort_value=='artist'){
                if(this.sort_type=='asc'){
                return this.songs.sort((a, b) => {
                if( a.artist[0].name > b.artist[0].name) return 1;
                else if ( a.artist[0].name < b.artist[0].name ) return -1;
                else return 0;
                })
                }else if(this.sort_type=='desc'){
                return this.songs.sort((a, b) => {
                    if( a.artist[0].name < b.artist[0].name) return 1;
                    else if ( a.artist[0].name > b.artist[0].name ) return -1;
                    else return 0;
                })
                }
            }
            return this.songs.sort((a, b) => {
                return b.id - a.id
            })
        },
    },
    created() {
        this.getPlaylist()
    }

}
</script>

<style>

</style>