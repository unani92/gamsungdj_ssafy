<template>
  <div id="app-container" :class="getMenuType">
    <topnav id="topnav" />
    <main>
      <div class="container-fluid">
        <slot></slot>
      </div>
    </main>
    <transition name="slide-up">
      <maskLayer id="mask" v-show="this.$store.state.visiblePlaylist" />
    </transition>
    <footer-component id="footer" style="z-index:10;" />
  </div>
</template>

<script>
import Topnav from "../containers/Topnav";
import Mask from "../containers/Mask";
import Footer from "../containers/Footer";
import { mapGetters } from "vuex";

export default {
  components: {
    topnav: Topnav,
    "maskLayer": Mask,
    "footer-component": Footer,
  },
  computed: {
    ...mapGetters(["getMenuType"])
  },
  mounted() {
    setTimeout(() => {
      document.body.classList.add("default-transition");
    }, 100);
  }
}
</script>
<style scope>
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
#mask {
  z-index:10;
}
</style>
