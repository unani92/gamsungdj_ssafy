<template>
    <div class="music-bar">
        <span class="bar bar-0">0</span>
        <span class="bar bar-1">1</span>
        <span class="bar bar-2">2</span>
        <span class="bar bar-3">3</span>
        <span class="bar bar-4">4</span>
    </div>
</template>

<script>
export default {

}
</script>

<style>
.music-bar {
  width: 50px;
  height: 50px;
  display: block;
  border-radius: 10px;
  background-color: ffffff;
  position: relative;
  margin: 50px auto;
  border: 1px solid #dddddd;
}

.bar {
  display: block;
  background-color: #00b4ff;
  height: 25px;
  width: 3px;
  text-indent: -9999px;
  position: absolute;
  top: 13px;
  -webkit-animation: bar 0ms -1000ms linear infinite alternate running;
  animation: bar 0ms -1000ms linear infinite alternate running;
}

@-webkit-keyframes bar {
  0% {
    transform: scale(1, 0.25);
  }
  25% {
    transform: scale(1, 0.5);
  }
  50% {
    transform: scale(1, 0.75);
  }
  75% {
    transform: scale(1, 1);
  }
  100% {
    transform: scale(1, 1.25);
  }
}
@keyframes bar {
  0% {
    transform: scale(1, 0.25);
  }
  25% {
    transform: scale(1, 0.5);
  }
  50% {
    transform: scale(1, 0.75);
  }
  75% {
    transform: scale(1, 1);
  }
  100% {
    transform: scale(1, 1.25);
  }
}
.bar-0 {
  left: 3px;
  -webkit-animation-duration: 337ms;
  animation-duration: 337ms;
}

.bar-1 {
  left: 12px;
  -webkit-animation-duration: 321ms;
  animation-duration: 321ms;
}

.bar-2 {
  left: 21px;
  -webkit-animation-duration: 353ms;
  animation-duration: 353ms;
}

.bar-3 {
  left: 30px;
  -webkit-animation-duration: 341ms;
  animation-duration: 341ms;
}

.bar-4 {
  left: 38px;
  -webkit-animation-duration: 327ms;
  animation-duration: 327ms;
}
</style>
