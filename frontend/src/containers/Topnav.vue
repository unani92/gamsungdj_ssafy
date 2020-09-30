<template>
  <nav class="navbar fixed-top">
    <div class="d-flex align-items-center navbar-left"></div>

    <div
      :class="{'search':true, 'mobile-view':isMobileSearch}"
      ref="searchContainer"
      @mouseenter="isSearchOver=true"
      @mouseleave="isSearchOver=false"
    >
      <b-input
        @keypress.native.enter="search"
        v-model="searchKeyword"
      />
      <span class="search-icon"  style="padding:10px" @click="searchClick">
        <i class="simple-icon-magnifier"></i>
      </span>
    </div>

    <div class="navbar-right">
      <div class="d-none d-md-inline-block align-middle mr-3">
        <switches
          id="tool-mode-switch"
          v-model="isDarkActive"
          theme="custom"
          class="vue-switcher-small"
          color="primary"
        />
        <b-tooltip target="tool-mode-switch" placement="left" title="Dark Mode"></b-tooltip>
      </div>

      <!-- logged in -->
      <div class="user d-inline-block" v-if="isLoggedin">
        <b-dropdown
          class="dropdown-menu-right"
          right
          variant="empty"
          toggle-class="p-0"
          menu-class="mt-3"
          no-caret
        >
          <template slot="button-content">
            <span class="name mr-1">{{user.username}}</span>
            <span v-if="user.avatar">
              <img :alt="user.username" :src="imgURL" />
            </span>
            <span v-else>
              <b-avatar></b-avatar>
            </span>
          </template>
          <b-dropdown-item>My Page</b-dropdown-item>
          <b-dropdown-item @click="link">Music DNA</b-dropdown-item>
          <b-dropdown-divider />
          <b-dropdown-item @click="signout">로그아웃</b-dropdown-item>
        </b-dropdown>
      </div>

      <!-- not logged in -->
       <div id="loginFlag" class="user d-inline-block" v-else @click="showLogin = !showLogin" style="cursor: pointer;">
        <span class="name mr-1">로그인을 해주세요</span>
        <span>
          <b-avatar></b-avatar>
        </span>
      </div>
    </div>
    <LoginModal :showLogin="showLogin" @hideModal="showLogin=false"/>
  </nav>
</template>

<script>
import Switches from "vue-switches";
import LoginModal from '@/components/User/LoginModal.vue'
import { mapGetters, mapMutations, mapActions, mapState } from "vuex";
import { MenuIcon, MobileMenuIcon } from "../components/Svg";
import { adminRoot } from "../constants/config";
import { getDirection, setDirection, getThemeColor, setThemeColor } from "../utils";
export default {
  components: {
    "menu-icon": MenuIcon,
    "mobile-menu-icon": MobileMenuIcon,
    switches: Switches,
    LoginModal,
  },
  data() {
    return {
      searchKeyword: "",
      isMobileSearch: false,
      isDarkActive: false,
      adminRoot,
      showLogin: false
    };
  },
  methods: {
    ...mapActions(['logout']),
    search() {
      this.$router.push(`${adminRoot}/search/${this.searchKeyword}`);
      this.searchKeyword = "";
    },
    searchClick() {
      if (window.innerWidth < this.menuHiddenBreakpoint) {
        if (!this.isMobileSearch) {
          this.isMobileSearch = true;
        } else {
          this.search();
          this.isMobileSearch = false;
        }
      } else {
        this.search();
      }
    },
    handleDocumentforMobileSearch() {
      if (!this.isSearchOver) {
        this.isMobileSearch = false;
        this.searchKeyword = "";
      }
    },
    signout() {
      this.logout()
    },
    link() {
      this.$router.push(`${adminRoot}/musicDNA`)
    }
  },
  computed: {
    imgURL: function() { return "http://127.0.0.1:8000/api/accounts/" + this.user.avatar },
    ...mapGetters({
      currentUser: "currentUser",
    }),
    ...mapState(['authorization', 'user', 'isLoggedin'])
  },
  beforeDestroy() {
    document.removeEventListener("click", this.handleDocumentforMobileSearch);
  },
  created() {
    const color = getThemeColor();
    this.isDarkActive = color.indexOf("dark") > -1;
  },
  watch: {
    isDarkActive(val) {
      let color = getThemeColor();
      let isChange = false;
      if (val && color.indexOf("light") > -1) {
        isChange = true;
        color = color.replace("light", "dark");
      } else if (!val && color.indexOf("dark") > -1) {
        isChange = true;
        color = color.replace("dark", "light");
      }
      if (isChange) {
        setThemeColor(color);
        setTimeout(() => {
          window.location.reload();
        }, 500);
      }
    },
    isMobileSearch(val) {
      if (val) {
        document.addEventListener("click", this.handleDocumentforMobileSearch);
      } else {
        document.removeEventListener(
          "click",
          this.handleDocumentforMobileSearch
        );
      }
    },
  }
};
</script>
<style scoped>

</style>
