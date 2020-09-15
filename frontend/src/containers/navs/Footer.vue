<template>
<footer class="page-footer">
    <div class="footer-content">
        <div class="row" style="height:100%; align-items:center;">
            <div class="col-12 col-sm-4">
                <p class="mb-0 text-muted">앨범 사진 들어갈 자리</p>
            </div>
            <div class="col-sm-4">
                <center>
                <p class="mb-0 text-muted">
                    <font size="20px">
                        <span class="glyph-icon iconsminds-back-music" style="cursor:pointer"></span>
                        <span class="glyph-icon iconsminds-play-music" style="padding:0px 20px 0px 20px; cursor:pointer;"></span>
                        <span class="glyph-icon iconsminds-next-music" style="cursor:pointer">  </span>
                    </font>
                </p>
                </center>
            </div>
            <div class="col-sm-4 d-none d-sm-block">
                <p class="mb-0 text-muted float-right">
                    <font size="20px">
                        <span class="glyph-icon simple-icon-playlist" style="cursor:pointer" @click="togglePlaylist"></span>
                    </font>
                </p>
            </div>
        </div>
    </div>
</footer>
</template>
<script>
export default {
    methods:{
        togglePlaylist(){
            this.$store.state.visiblePlaylist = !this.$store.state.visiblePlaylist
        }
    }
}
</script>
