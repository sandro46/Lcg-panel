/*eslint-disable */
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
        csi: [],
    }
}

const getters = {
    ref_customer_phone_type(state){
        return state.ref.phone_type
    },
    ref_process_type(state) {
      return state.ref.process_type
    },
    ref_contact_type(state) {
      return state.ref.contact_type
    },
    ref_contact_result(state) {
      return state.ref.contact_result
    },
    ref_csi(state) {
      return state.ref.csi
    },
}

const mutations = {
    setCustomerPhoneTypes(state, payload) {
        state.ref.phone_type = payload
    },
    setProcessTypes(state, payload){
        state.ref.process_type = payload
    },
    setContactTypes(state, payload){
      state.ref.contact_type = payload
    },
    setContactsResults(state, payload){
      state.ref.contact_result = payload
    },
    setRefCsi(state, payload){
      state.ref.csi = payload
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
    async loadProcessTypes({commit}){
        const res = await ax.get("/get_ref?type=processTypes").catch(function(err) { console.log(err)});
        // debugger;
        if(!res.err) {
          commit('setProcessTypes', res.data.payload)
          return true;
        }
    },
    async loadContactTypes({commit}){
        const res = await ax.get("/get_ref?type=contactTypes").catch(function(err) { console.log(err)});
        // debugger;
        if(!res.err) {
          commit('setContactTypes', res.data.payload)
          return true;
        }
    },
    async loadContactResults({commit}){
        const res = await ax.get("/get_ref?type=contactResults").catch(function(err) { console.log(err)});
        if(!res.err) {
          commit('setContactsResults', res.data.payload)
          return true;
        }
    },
    async loadRefCsi({commit}){
        const res = await ax.get("/get_ref?type=csi").catch(function(err) { console.log(err)});
        if(!res.err) {
          commit('setRefCsi', res.data.payload)
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