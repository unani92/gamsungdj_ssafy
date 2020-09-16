import Vue from 'vue'
import Vuex from 'vuex'

import app from '../main'
import menu from './modules/menu'
import user from './modules/user'
import { setCurrentLanguage } from '../utils'
import axios from 'axios'

Vue.use(Vuex)

const baseURL = 'http://localhost:8000/'
export default new Vuex.Store({
  state: {
    authorization:sessionStorage.getItem("authorization"),
    visiblePlaylist: false,
    visiblePlayButton: true,
    visibelPauseButton: false,
  },
  getters: {
    config: (state) => ({headers: { Authorization: state.authorization }}),
  },

  mutations: {
    changeLang(state, payload) {
      app.$i18n.locale = payload
      setCurrentLanguage(payload);
    },
    SET_AUTH(state, value){
      sessionStorage.setItem("authorization", value)
      
      state.authorization = value
    },
    LOGOUT(state){
      state.authorization=""

      sessionStorage.removeItem("authorization")
    },
  },
  actions: {
    setLang({ commit }, payload) {
      commit('changeLang', payload)
    },
    setAuth({commit},value){
      commit('SET_AUTH',value)
    },
    logout({commit}){
      commit("LOGOUT")
    },



  },
  modules: {
    menu,
    user,
  }
})
