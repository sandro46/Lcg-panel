import Vue from 'vue'
import Vuex from 'vuex'
import ref from './ref'
import phone from './phone'
import agreement from './agreement'
import loadManager from './loadManager'

Vue.use(Vuex)

export default new Vuex.Store({
    modules: {
      ref,
      phone,
      agreement,
      loadManager
    }
})
  