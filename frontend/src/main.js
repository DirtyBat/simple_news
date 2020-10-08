// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import axios from 'axios'

import App from './App'
import router from './router'

import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
Vue.use(ElementUI)

import Vuex from 'vuex'
Vue.use(Vuex)

Vue.config.productionTip = false
Vue.config.debug = true

axios.defaults.withCredentials = true
axios.defaults.baseURL = process.env.API_ROOT
Vue.prototype.$axios = axios

const store = new Vuex.Store({
  state: {
    isLogin: false,
    token: "",
  },
  mutations: {
    setLogin(state, isLogin, token) {
      state.isLogin = isLogin;
      state.token = token;
    }
  }
})

/* eslint-disable no-new */
new Vue({
  el: '#app',
  store,
  router,
  components: { App },
  template: '<App/>'
})
