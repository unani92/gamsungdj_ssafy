<template>
<footer class="page-footer">
    <div class="footer-content">
        <div class="row" style="height:100%; align-items:center;">
            <div class="col-12 col-sm-3">
                <img :src="selectedSong.img" style="height:-webkit-fill-available;"> 
                <span v-if="selectedSong.title">
                    <a class="glyph-icon" style="cursor:pointer;" @click="detailArtist(selectedSong.singerID)">{{ selectedSong.title }}</a> - <a class="glyph-icon" style="cursor:pointer;" @click="detailSong(selectedSong.songID)">{{ selectedSong.artist }}</a>
                </span>
                <p class="mb-0 text-muted">
                </p>
            </div>
            <div class="col-sm-6">
                <center>
                <p class="mb-0 text-muted">
                    <font class="button" size="10px">
                        <span class="glyph-icon simple-icon-control-rewind" @click="action('prev')"></span>
                        <span class="glyph-icon simple-icon-control-play" @click="action('play')" v-show="this.$store.state.visiblePlayButton" style="padding:0px 20px 0px 20px;"></span>
                        <span class="glyph-icon simple-icon-control-pause" @click="action('pause')" v-show="this.$store.state.visiblePauseButton" style="padding:0px 20px 0px 20px;"></span>
                        <span class="glyph-icon simple-icon-control-forward" @click="action('next')"></span>
                    </font>
                </p>
                </center>
            </div>
            <div class="col-sm-3 d-none d-sm-block">
                <p class="mb-0 text-muted float-right">
                    <font size="20px">
                        <span class="glyph-icon simple-icon-playlist" @click="togglePlaylist"></span>
                    </font>
                </p>
            </div>
        </div>
    </div>
</footer>
</template>
<script>
import { mapState } from "vuex"
import { adminRoot } from '../constants/config'
export default {
    computed: {
        ...mapState([
            'selectedSong',
        ]),
    },
    mounted(){
        window.addEventListener("resize", this.handleResize)
    },
    methods:{
        handleResize(e){
            let height = window.innerHeight;
            let height_topnav = document.getElementById('topnav').offsetHeight;
            let height_footer = document.getElementById('footer').offsetHeight;
            let height_mask = height - height_topnav - height_footer;
            document.getElementById('mask').style.height = height_mask+1 + "px";
            document.getElementById('mask').style.top = height_topnav + "px";
        },
        togglePlaylist(){
            if(!this.$store.state.visiblePlaylist){
                let height = window.innerHeight;
                let height_topnav = document.getElementById('topnav').offsetHeight;
                let height_footer = document.getElementById('footer').offsetHeight;
                let height_mask = height - height_topnav - height_footer;
                document.getElementById('mask').style.height = height_mask+1 + "px";
                document.getElementById('mask').style.top = height_topnav + "px";
                if(document.getElementById('lyricArea')){
                    document.getElementById('lyricArea').style.height = height_mask-70 + "px";
                    // document.getElementById('lyricArea').style.top = height_topnav + "px";
                }
                
            }
            this.$store.state.visiblePlaylist = !this.$store.state.visiblePlaylist
        },
        action(msg) {
            if(msg === "play") {
                this.$store.state.visiblePlayButton = false
                this.$store.state.visiblePauseButton = true
            }
            else if(msg === "pause") {
                this.$store.state.visiblePlayButton = true
                this.$store.state.visiblePauseButton = false
            }
            else if(msg === "prev") {
                this.$store.state.visiblePlayButton = false
                this.$store.state.visiblePauseButton = true
            }
            else if(msg === "next") {
                this.$store.state.visiblePlayButton = false
                this.$store.state.visiblePauseButton = true
            }
            this.$store.state.playerControl = msg
        },
        detailArtist: function(id){
            this.$store.state.visiblePlaylist = false;
            this.$router.push(`${adminRoot}/ArtistDetail/${id}`)
        },
        detailSong: function(id){
            this.$store.state.visiblePlaylist = false;
            this.$router.push(`${adminRoot}/songDetail/${id}`)
        },

    }
}
</script>
<style scoped>
.glyph-icon {
    cursor:pointer;
}
</style>