/*eslint-disable */
const axios = require('axios')
const config = require('./config.json')


const ax = axios.create({
    baseURL: config.baseURL,
    timeout: 100000,
});

const state = {
    items: [],
}

const getters = {
    customer_phones(state){
        return state.items
    },
}

const mutations = {
    setCustomerPhones(state, payload) {
        state.items = payload
    },
}

const actions = {
    async loadCustomerPhonesByAgreement({commit}, id){
        const res = await ax.get(`/phone?agreement_id=${id}`).catch(function(err) { console.log(err)});
        if(!res.err) {
          commit('setCustomerPhones', res.data.payload)
          return true;
        }
    }
}

export default {
    state,
    getters,
    actions,
    mutations
 }