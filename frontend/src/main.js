import Vue from 'vue'
import App from './App'

// BootstrapVue add
import { BootstrapVue, IconsPlugin }from 'bootstrap-vue'
// Router & Store add
import router from './router'
import store from './store'
// Notification Component Add
import Notifications from './components/Common/Notification'
// RefreshButton Component Add
import RefreshButton from './components/Common/RefreshButton'
// Colxx Component Add
import Colxx from './components/Common/Colxx'
// Perfect Scrollbar Add
import vuePerfectScrollbar from 'vue-perfect-scrollbar'
import contentmenu from 'v-contextmenu'
import VueLineClamp from 'vue-line-clamp'
import VueScrollTo from 'vue-scrollto'
import GSignInButton from 'vue-google-signin-button'
import VueYoutube from 'vue-youtube'
import VueLodash from 'vue-lodash'
import lodash from 'lodash'
import { library } from '@fortawesome/fontawesome-svg-core'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
import { faHeart as emptyHeart } from '@fortawesome/free-regular-svg-icons'
import { faHeart as fillHeart } from '@fortawesome/free-solid-svg-icons'

library.add(emptyHeart, fillHeart)

Vue.use(VueLodash)
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
import vuetify from 'vuetify'
Vue.use(vuetify)
Vue.component('b-refresh-button', RefreshButton);
Vue.component('b-colxx', Colxx);
Vue.component('vue-perfect-scrollbar', vuePerfectScrollbar);
Vue.component('font-awesome-icon', FontAwesomeIcon)
Vue.config.productionTip = false

export default new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
