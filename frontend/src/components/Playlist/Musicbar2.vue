<template>
  <div class="holder">
    <span>Playing</span>
    <div class="clr"></div>
    <div class="bar b1"></div>
    <div class="bar b2"></div>
    <div class="bar b3"></div>
    <div class="bar b4"></div>
    <div class="bar b5"></div>
    <div class="bar b6"></div>
    <div class="bar b7"></div>
    <div class="bar b8"></div>
    <div class="bar b9"></div>
    </div>
</template>

<script>
export default {

}
</script>

<style>
body{
  background: #343233;
}
.holder{
  position: absolute;
  left: 27px;
  top: 20px;
  /* color: #60b044; */
  color: #900604;

}

.holder span{
  margin-left: 0px;
  font: 500 14px 'verdana';
}
.clr{
  clear: both;
}
.bar{
  width: 2px;
  height: 40px;
  background: #900604;
  margin: 2px;
  float: left;
}
.b1{
  -webkit-animation: anim1 500ms linear infinite;
}
@-webkit-keyframes anim1{
  0%  {height: 10px;}
  25% {height: 30px;}
  50% {height: 10px;}
  75% {height: 25px;}
  100%{height: 10px;}
}
.b2{
  -webkit-animation: anim2 750ms linear infinite;
}
@-webkit-keyframes anim2{
  0%  {height: 30px;}
  25% {height: 10px;}
  50% {height: 40px;}
  75% {height: 25px;}
  100%{height: 30px;}
}
.b3{
  -webkit-animation: anim3 750ms linear infinite;
}
@-webkit-keyframes anim3{
  0%  {height: 10px;}
  25% {height: 25px;}
  50% {height: 10px;}
  75% {height: 40px;}
  100%{height: 10px;}
}
.b4{
  -webkit-animation: anim4 650ms linear infinite;
}
@-webkit-keyframes anim4{
  0%  {height: 40px;}
  25% {height: 10px;}
  50% {height: 35px;}
  75% {height: 15px;}
  100%{height: 40px;}
}
.b5{
  -webkit-animation: anim5 750ms linear infinite;
}
@-webkit-keyframes anim5{
  0%  {height: 15px;}
  25% {height: 25px;}
  50% {height: 10px;}
  75% {height: 40px;}
  100%{height: 15px;}
}
.b6{
  -webkit-animation: anim6 700ms linear infinite;
}
@-webkit-keyframes anim6{
  0%  {height: 30px;}
  25% {height: 10px;}
  50% {height: 30px;}
  75% {height: 20px;}
  100%{height: 30px;}
}
.b7{
  -webkit-animation: anim7 750ms linear infinite;
}
@-webkit-keyframes anim7{
  0%  {height: 0px;}
  25% {height: 30px;}
  50% {height: 15px;}
  75% {height: 20px;}
  100%{height: 00px;}
}
.b8{
  -webkit-animation: anim8 650ms linear infinite;
}
@-webkit-keyframes anim8{
  0%  {height: 0px;}
  25% {height: 20px;}
  50% {height: 10px;}
  75% {height: 30px;}
  100%{height: 0px;}
}
.b9{
  -webkit-animation: anim9 550ms linear infinite;
}
@-webkit-keyframes anim9{
  0%  {height: 10px;}
  25% {height: 30px;}
  50% {height: 0px;}
  75% {height: 15px;}
  100%{height: 10px;}
}
</style>