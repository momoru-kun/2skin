import Vue from 'vue'
import Vuex from 'vuex'
import cart from './modules/cart'
import notification from './modules/notifications'
Vue.use(Vuex)

export default new Vuex.Store({
  modules: {cart, notification}
})
