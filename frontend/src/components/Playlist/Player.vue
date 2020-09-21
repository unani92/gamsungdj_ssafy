<template>


<!-- Inspired By This Dribble post https://dribbble.com/shots/2321025-Music-Player-Freebie <3 <3 <3-->
<div class="player">
    <!-- <img class="cover" src="http://images.genius.com/2216a21a5494b153cb4c24005370d031.700x700x1.jpg" alt="Cover"/> -->
    <div class="icons">
        <div class="fa fa-heart"></div>
        <div class="fa fa-random"></div>
    </div>
    <div class="info">
        <p class="title">Leave Your Lover</p>
        <p class="artist">Artist - Echos</p>
        <p class="album">Album - Echos</p>
    </div>
    <div class="line"></div>
    <div class="playtime"></div>
    <div class="played"><img class="forward" src="data:image/svg+xml;utf8;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iaXNvLTg4NTktMSI/Pgo8IS0tIEdlbmVyYXRvcjogQWRvYmUgSWxsdXN0cmF0b3IgMTYuMC4wLCBTVkcgRXhwb3J0IFBsdWctSW4gLiBTVkcgVmVyc2lvbjogNi4wMCBCdWlsZCAwKSAgLS0+CjwhRE9DVFlQRSBzdmcgUFVCTElDICItLy9XM0MvL0RURCBTVkcgMS4xLy9FTiIgImh0dHA6Ly93d3cudzMub3JnL0dyYXBoaWNzL1NWRy8xLjEvRFREL3N2ZzExLmR0ZCI+CjxzdmcgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB4bWxuczp4bGluaz0iaHR0cDovL3d3dy53My5vcmcvMTk5OS94bGluayIgdmVyc2lvbj0iMS4xIiBpZD0iQ2FwYV8xIiB4PSIwcHgiIHk9IjBweCIgd2lkdGg9IjEyOHB4IiBoZWlnaHQ9IjEyOHB4IiB2aWV3Qm94PSIwIDAgNDM5LjM1NyA0MzkuMzU3IiBzdHlsZT0iZW5hYmxlLWJhY2tncm91bmQ6bmV3IDAgMCA0MzkuMzU3IDQzOS4zNTc7IiB4bWw6c3BhY2U9InByZXNlcnZlIj4KPGc+Cgk8cGF0aCBkPSJNMzYwLjQyNyw1LjgzM2MtMy42MTMtMy42MTctNy44OTgtNS40MjQtMTIuODQ3LTUuNDI0aC0zNi41NDVjLTQuOTQ1LDAtOS4yMzMsMS44MDctMTIuODQ3LDUuNDI0ICAgYy0zLjYxNCwzLjYyMS01LjQyOCw3LjkwMi01LjQyOCwxMi44NXYxOTMuNTc0Yy0wLjk0OC0yLjA5MS0yLjE5LTMuOTAxLTMuNzE3LTUuNDI0TDg2LjM0Myw0LjEyNSAgIGMtMy42MTctMy42MTctNi42NjMtNC44NTYtOS4xMzYtMy43MTNjLTIuNDc0LDEuMTQzLTMuNzExLDQuMTg5LTMuNzExLDkuMTM3djQyMC4yNjJjMCw0Ljk0OCwxLjIzNyw3Ljk5NCwzLjcxMSw5LjEzOCAgIGMyLjQ3MywxLjE0LDUuNTE5LTAuMSw5LjEzNi0zLjcyNEwyODkuMDQ4LDIzMi41MmMxLjUyOS0xLjcxMSwyLjc2NS0zLjUyMSwzLjcyLTUuNDI0VjQyMC42NmMwLDQuOTQ4LDEuODEsOS4yMzksNS40MjEsMTIuODQ3ICAgYzMuNjIsMy42Miw3LjkwNCw1LjQyOCwxMi44NDcsNS40MjhoMzYuNTUyYzQuOTQ4LDAsOS4yMzYtMS44MDgsMTIuODQ3LTUuNDI4YzMuNjE0LTMuNjA3LDUuNDI4LTcuODk4LDUuNDI4LTEyLjg0N1YxOC42ODMgICBDMzY1Ljg1NCwxMy43MywzNjQuMDM3LDkuNDUsMzYwLjQyNyw1LjgzM3oiIGZpbGw9IiNGRkZGRkYiLz4KPC9nPgo8Zz4KPC9nPgo8Zz4KPC9nPgo8Zz4KPC9nPgo8Zz4KPC9nPgo8Zz4KPC9nPgo8Zz4KPC9nPgo8Zz4KPC9nPgo8Zz4KPC9nPgo8Zz4KPC9nPgo8Zz4KPC9nPgo8Zz4KPC9nPgo8Zz4KPC9nPgo8Zz4KPC9nPgo8Zz4KPC9nPgo8Zz4KPC9nPgo8L3N2Zz4K"/></div><img class="backward" src="data:image/svg+xml;utf8;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iaXNvLTg4NTktMSI/Pgo8IS0tIEdlbmVyYXRvcjogQWRvYmUgSWxsdXN0cmF0b3IgMTYuMC4wLCBTVkcgRXhwb3J0IFBsdWctSW4gLiBTVkcgVmVyc2lvbjogNi4wMCBCdWlsZCAwKSAgLS0+CjwhRE9DVFlQRSBzdmcgUFVCTElDICItLy9XM0MvL0RURCBTVkcgMS4xLy9FTiIgImh0dHA6Ly93d3cudzMub3JnL0dyYXBoaWNzL1NWRy8xLjEvRFREL3N2ZzExLmR0ZCI+CjxzdmcgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB4bWxuczp4bGluaz0iaHR0cDovL3d3dy53My5vcmcvMTk5OS94bGluayIgdmVyc2lvbj0iMS4xIiBpZD0iQ2FwYV8xIiB4PSIwcHgiIHk9IjBweCIgd2lkdGg9IjEyOHB4IiBoZWlnaHQ9IjEyOHB4IiB2aWV3Qm94PSIwIDAgNDM5LjM2MiA0MzkuMzYyIiBzdHlsZT0iZW5hYmxlLWJhY2tncm91bmQ6bmV3IDAgMCA0MzkuMzYyIDQzOS4zNjI7IiB4bWw6c3BhY2U9InByZXNlcnZlIj4KPGc+Cgk8cGF0aCBkPSJNMzYyLjE0NiwwLjQxMmMtMi40NzEtMS4xNDMtNS41MTcsMC4wOTQtOS4xMzgsMy43MDlMMTUwLjMwOCwyMDYuODI4Yy0xLjcxOCwxLjUyNC0yLjk1NSwzLjMzMy0zLjcxNSw1LjQyNFYxOC42NzkgICBjMC00Ljk1Mi0xLjgwOS05LjIzNC01LjQyNC0xMi44NWMtMy42MTctMy42MTctNy45LTUuNDI2LTEyLjg0Ny01LjQyNkg5MS43NzVjLTQuOTUyLDAtOS4yMzMsMS44MDktMTIuODUsNS40MjYgICBDNzUuMzA4LDkuNDQ4LDczLjUsMTMuNzMsNzMuNSwxOC42Nzl2NDAxLjk4NmMwLDQuOTQ4LDEuODA3LDkuMjM2LDUuNDI0LDEyLjg0N2MzLjYyMSwzLjYyLDcuOTAyLDUuNDI4LDEyLjg1LDUuNDI4aDM2LjU0MyAgIGM0Ljk0NywwLDkuMjI5LTEuODA4LDEyLjg0Ny01LjQyOGMzLjYxNS0zLjYxLDUuNDI0LTcuODk4LDUuNDI0LTEyLjg0N1YyMjcuMDk3YzAuNzYzLDEuOTAzLDIsMy43MTcsMy43MTUsNS40MjVsMjAyLjcwNSwyMDIuNzEyICAgYzMuNjIxLDMuNjE3LDYuNjY3LDQuODU5LDkuMTM4LDMuNzJjMi40NzgtMS4xNDQsMy43MTYtNC4xODksMy43MTYtOS4xMzhWOS41NDdDMzY1Ljg2Miw0LjU5OSwzNjQuNjI0LDEuNTUzLDM2Mi4xNDYsMC40MTJ6IiBmaWxsPSIjRkZGRkZGIi8+CjwvZz4KPGc+CjwvZz4KPGc+CjwvZz4KPGc+CjwvZz4KPGc+CjwvZz4KPGc+CjwvZz4KPGc+CjwvZz4KPGc+CjwvZz4KPGc+CjwvZz4KPGc+CjwvZz4KPGc+CjwvZz4KPGc+CjwvZz4KPGc+CjwvZz4KPGc+CjwvZz4KPGc+CjwvZz4KPGc+CjwvZz4KPC9zdmc+Cg=="/>
    <div class="fa fa-volume-up fa-2x"></div>
    <p class="songtime">4:20</p>
    <p class="timeleft">1:44</p>
    <svg id="Capa_1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" version="1.1" x="0px" y="0px" viewbox="0 0 512 512" style="enable-background:new 0 0 512 512;" xml:space="preserve" width="512px" height="512px">
        <path d="M256,0C114.617,0,0,114.615,0,256s114.617,256,256,256s256-114.615,256-256S397.383,0,256,0z M344.48,269.57l-128,80  c-2.59,1.617-5.535,2.43-8.48,2.43c-2.668,0-5.34-0.664-7.758-2.008C195.156,347.172,192,341.82,192,336V176  c0-5.82,3.156-11.172,8.242-13.992c5.086-2.836,11.305-2.664,16.238,0.422l128,80c4.676,2.93,7.52,8.055,7.52,13.57  S349.156,266.641,344.48,269.57z" fill="#72e6cf"></path>
    </svg>
</div>

</template>

<script>
export default {

}
</script>

<style scoped>
body {
  height: 700px;
  width: 100vw;
  display: -webkit-box;
  display: flex;
  -webkit-box-align: center;
          align-items: center;
  -webkit-box-pack: center;
          justify-content: center;
}
.player {
  width: 800px;
  height: 529px;
  background: #6b6d83;
  box-shadow: 0px 24px 54px -12px #5e6178;
  position: absolute;
  left: 50%;
  -webkit-transform: translateX(-400px);
          transform: translateX(-400px);
  top: 20%;
}
.player .cover {
  width: 230px;
  position: absolute;
  left: 50%;
  -webkit-transform: translateX(-115px);
          transform: translateX(-115px);
  top: -40px;
  box-shadow: 5px 20px 50px 0px rgba(17,17,17,0.4);
}
.player .icons {
  position: absolute;
  right: 40px;
  top: 40px;
}
.player .icons .fa {
  color: #72e6cf;
  margin-left: 15px;
  font-size: 20px;
}
.player .info {
  position: absolute;
  top: 240px;
  left: 20%;
  color: #fff;
  font-family: Open Sans;
  letter-spacing: 1px;
}
.player .info .title {
  font-size: 2em;
  margin: 0;
}
.player .info .artist {
  color: #bdbdbd;
}
.player .line {
  height: 3px;
  width: 100%;
  background-color: #525363;
  position: absolute;
  top: 400px;
}
.player .playtime {
  background-color: rgba(114,230,207,0.3);
  height: 5px;
  width: 100%;
  position: absolute;
  bottom: 0px;
}
.player .played {
  background-color: #72e6cf;
  height: 5px;
  width: 300px;
  position: absolute;
  bottom: 0px;
}
.player svg {
  width: 85px;
  background-color: #fff;
  border-radius: 50%;
  height: 85px;
  position: absolute;
  left: 50%;
  -webkit-transform: translateX(-42.5px);
          transform: translateX(-42.5px);
  bottom: 25px;
  box-shadow: 0px 0px 40px 0px rgba(0,0,0,0.4);
}
.player .forward {
  width: 30px;
  position: absolute;
  bottom: 55px;
  right: -70%;
}
.player .backward {
  width: 30px;
  position: absolute;
  bottom: 55px;
  left: 36%;
}
.player .fa.fa-volume-up {
  color: #fff;
  position: absolute;
  bottom: 53px;
  right: 28%;
}
.player p.songtime {
  color: #fff;
  position: absolute;
  right: 20px;
  bottom: 45px;
}
.player p.timeleft {
  color: #fff;
  position: absolute;
  left: 20px;
  bottom: 45px;
}
.player .fa.fa-heart.liked {
  color: #ff749f;
}

</style>