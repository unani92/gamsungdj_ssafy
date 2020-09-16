<template>
  <div id="app-container" :class="getMenuType">
    <topnav />  
    <!-- <sidebar /> -->
    <main>
      <div class="container-fluid">
        <slot></slot>
      </div>
    </main>
    <transition name="slide-up">
      <maskmask id="mask" v-show="this.$store.state.visiblePlaylist" :msg="msg" />
    </transition>
    <footer-component @action="action" />
  </div>
</template>

<script>
// import Sidebar from "../containers/navs/Sidebar";
import Topnav from "../containers/navs/Topnav";
import Mask from "../containers/navs/Mask";
import Footer from "../containers/navs/Footer";
import { mapGetters } from "vuex";

export default {
  components: {
    topnav: Topnav,
    // sidebar: Sidebar,
    "maskmask": Mask,
    "footer-component": Footer,
  },
  data() {
    return {
      show: false,
      msg: ''
    };
  },
  computed: {
    ...mapGetters(["getMenuType"])
  },
  mounted() {
    setTimeout(() => {
      document.body.classList.add("default-transition");
    }, 100);
  },
  methods: {
    action(msg){
      this.msg = msg
    }
  }
};
</script>
<style scope>
#mask{
  position: fixed;
  top:100px;
  width:100%;
  height:80%;
  background-color:black;
}
.slide-up {
    transition: all 0.5s;
}
.slide-up-enter-active {
    transition: all 0.5s ease;
}
.slide-up-leave-active {
    transition: all 0.25s cubic-bezier(1, 0.5, 0.8, 1);
}
.slide-up-enter, .slide-up-leave-active {
    opacity: 0; transform: translateY(100%);
}
</style>
