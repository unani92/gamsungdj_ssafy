import Vue from 'vue'
import Vuex from 'vuex'
import menu from './modules/menu'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    authorization:sessionStorage.getItem("authorization"),
    user : JSON.parse(sessionStorage.getItem('user')),
    visiblePlaylist: false,
    visiblePlayButton: true,
    visiblePauseButton: false,
    playlist: [],
    userPlayList: JSON.parse(sessionStorage.getItem('userPlayList')),     // 로그인하면 풀림, 유저랑 똑같이 세션에 박아놓겟음
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
    isLoggedin: sessionStorage.getItem('isLoggedin'),
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
      sessionStorage.setItem("user", JSON.stringify(value))
      state.user = value
      state.songLikeList = value.like_songs
      state.albumLikeList = value.like_albums
      sessionStorage.setItem("isLoggedin", true)
      state.isLoggedin = true
    },
    SET_PLAYLIST(state, value) {
      sessionStorage.setItem('userPlayList', JSON.stringify(value))
      state.userPlayList = value
    },
    SET_SONG_LIKE(state, value) {
      state.songLikeList = value
    },
    LOGOUT(state){
      state.authorization=""
      state.user=null
      state.isLoggedin = false
      sessionStorage.removeItem("isLoggedin")
      sessionStorage.removeItem("authorization")
      sessionStorage.removeItem("user")
      sessionStorage.removeItem('userPlayList')
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
    setPlayList({ commit }, value) {
      commit('SET_PLAYLIST', value)
    },
    logout({commit}){
      commit("LOGOUT")
    },



  },
  modules: {
    menu,
  }
})
