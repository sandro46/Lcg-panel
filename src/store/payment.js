
const axios = require('axios')
const config = require('./config.json')


const ax = axios.create({
    baseURL: config.baseURL,
    timeout: 100000,
});

const state = {
    ref:{
        phone_type: [],
        contact_type: [],
        contact_result: [],
        process_type: [],
    }
}

const getters = {
    ref_customer_phone_type(state){
        return state.ref.phone_type
    },
}

const mutations = {
    setCustomerPhoneTypes(state, payload) {
        state.ref.phone_type = payload
    },
}

const actions = {
    async loadCustomerPhoneTypes({commit}){
        const res = await ax.get("/get_ref?type=phone_types").catch(function(err) { console.log(err)});
        if(!res.err) {
          commit('setCustomerPhoneTypes', res.data.payload)
          return true;
        }
    },
}

export default {
    state,
    getters,
    actions,
    mutations
 }