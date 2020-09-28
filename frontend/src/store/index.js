import Vue from 'vue'
import Vuex from 'vuex'
import menu from './modules/menu'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    authorization:sessionStorage.getItem("authorization"),
    user : sessionStorage.getItem('user'),
    visiblePlaylist: false,
    visiblePlayButton: true,
    visiblePauseButton: false,
    playlist: [],
    songLikeList: [],
    albumLikeList: [],
    playerControl: '',
    selectedSong: {
      index: -1,
      img: '',
      title: '',
      artist: '',
      src: '',
      lyric: '',
      currentTime: '',
      duration: '',
      volume: '',
      like: '',
      comment: '',
    },
    isLoggedin: false,
  },
  getters: {
    config: (state) => ({headers: { Authorization: state.authorization }}),
    currentUser: (state) => state.user,
  },

  mutations: {
    SET_AUTH(state, value){
      sessionStorage.setItem("authorization", value)
      state.authorization = value
    },
    SET_USER(state, value) {
      sessionStorage.setItem("user", value)
      state.user = value
      state.songLikeList = value.like_songs
      state.albumLikeList = value.like_albums
      state.isLoggedin = true
    },
    SET_SONG_LIKE(state, value) {
      state.songLikeList = value
    },
    LOGOUT(state){
      state.authorization=""
      state.user=[]
      state.isLoggedin = false
      sessionStorage.removeItem("authorization")
      sessionStorage.removeItem("user")
    },
  },
  actions: {
    setLang({ commit }, payload) {
      commit('changeLang', payload)
    },
    setAuth({commit},value){
      commit('SET_AUTH',value)
    },
    setUser( { commit }, value) {
      commit('SET_USER', value)
    },
    logout({commit}){
      commit("LOGOUT")
    },



  },
  modules: {
    menu,
  }
})
