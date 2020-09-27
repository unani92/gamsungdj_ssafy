import Vue from 'vue'
import App from './App'

// BootstrapVue add
import { BootstrapVue, IconsPlugin }from 'bootstrap-vue'
// Router & Store add
import router from './router'
import store from './store'
import { firebaseConfig } from './constants/config'
// Notification Component Add
import Notifications from './components/Common/Notification'
// Breadcrumb Component Add
import Breadcrumb from './components/Common/Breadcrumb'
// RefreshButton Component Add
import RefreshButton from './components/Common/RefreshButton'
// Colxx Component Add
import Colxx from './components/Common/Colxx'
// Perfect Scrollbar Add
import vuePerfectScrollbar from 'vue-perfect-scrollbar'
import contentmenu from 'v-contextmenu'
import VueLineClamp from 'vue-line-clamp'
import VueScrollTo from 'vue-scrollto'
import firebase from 'firebase/app'
import 'firebase/auth'
import GSignInButton from 'vue-google-signin-button'
import VueYoutube from 'vue-youtube'

Vue.use(IconsPlugin)
Vue.use(GSignInButton)
Vue.use(BootstrapVue);
Vue.use(VueYoutube);
Vue.use(Notifications);
Vue.use(require('vue-shortkey'));
Vue.use(contentmenu);
Vue.use(VueScrollTo);
Vue.use(VueLineClamp, {
  importCss: true
});

Vue.component('piaf-breadcrumb', Breadcrumb);
Vue.component('b-refresh-button', RefreshButton);
Vue.component('b-colxx', Colxx);
Vue.component('vue-perfect-scrollbar', vuePerfectScrollbar);

firebase.initializeApp(firebaseConfig);
Vue.config.productionTip = false
export default new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
