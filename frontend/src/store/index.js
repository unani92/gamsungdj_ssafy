import Vue from 'vue'
import Vuex from 'vuex'
import menu from './modules/menu'
import axios from "axios";
import http from "../utils/http-common";
import http2 from "../utils/http-user";

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    authorization:sessionStorage.getItem("authorization"),
    user : JSON.parse(sessionStorage.getItem('user')),
    climate: sessionStorage.getItem('climate'),
    visiblePlaylist: false,
    visiblePlayButton: true,
    visiblePauseButton: false,
    playlist: [],
    userPlayList: JSON.parse(sessionStorage.getItem('userPlayList')),
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
      songID: -1,
      singerID: -1,
    },
    isLoggedin: sessionStorage.getItem('isLoggedin'),
  },
  getters: {
    config: (state) => ({headers: { Authorization: state.authorization }}),
    currentUser: (state) => state.user,
  },

  mutations: {
    SET_CLIMATE(state, value) {
      sessionStorage.setItem('climate', value)
      state.climate = value
    },
    SET_PLIST(state, { command, data }) {
      if (command === 'addAndPlay') {
        state.playerControl = 'add'
        state.playlist.unshift(data)
      } else {
        state.playerControl = ''
        state.playlist.push(data)
      }
    },
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
      state.userPlayList = value
      sessionStorage.setItem("userPlayList", JSON.stringify(value))
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
      sessionStorage.removeItem('climate')
    },
  },
  actions: {
    setClimate({ commit }, value) {
      commit('SET_CLIMATE', value)
    },
    setLang({ commit }, payload) {
      commit('changeLang', payload)
    },
    setAuth({commit},value){
      commit('SET_AUTH',value)
    },
    setUser( { commit }, value) {
      commit('SET_USER', value)
    },
    setPlayList( { commit, getters } ) {
      http2.get('playlist/', getters.config)
      .then((res) => {
        commit('SET_PLAYLIST', res.data)
      })
    },
    logout({commit}){
      commit("LOGOUT")
    },
    async fetchYoutubeId({ commit }, song) {
      const youtubeURL = 'https://www.googleapis.com/youtube/v3/search'
      const API_KEY = process.env.VUE_APP_YOUTUBE_API_KEY
      const { data } = await axios.get(youtubeURL, {
        params: {
          key: API_KEY,
          part: 'snippet',
          maxResults: 1,
          type: 'video',
          q: song.artist[0].name + ' ' + song.name
        }
      })
      const { items } = data
      const { videoId } = items[0].id
      const reqData = {'src': videoId}
      song['src'] = videoId
      await http.post(`addsrc/${song.id}/`, reqData,'')
    },
    async addToPlaylistAndPlay({ commit, dispatch }, data) {
      let value = {
        'command': 'addAndPlay',
        'data': data
      }
      if (data['src']) {
        commit('SET_PLIST', value)
      } else {
        await dispatch('fetchYoutubeId', data)
        commit('SET_PLIST', value)
      }
    },
    async addToPlaylist({ commit, dispatch }, data) {
      let value = {
        'command': '',
        'data': data
        }
      if (data['src']) {
        commit('SET_PLIST', value)
      } else {
        await dispatch('fetchYoutubeId', data)
        commit('SET_PLIST', value)
      }
    }
  },
  modules: {
    menu,
  }
})
