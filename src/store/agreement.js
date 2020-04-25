/*eslint-disable */
const axios = require('axios')
const config = require('./config.json')

const ax = axios.create({
    baseURL: config.baseURL,
    timeout: 100000,
});



const state = {   
    items:[],
    contacts: [],
    contactData: {
      result: false,
      type: false,
      comment: '',
      agreement_id: null,
      phone_id: null,
      new_phone: null,
      new_phone_type: null,
      installment_amt: '',
      installment_dt_to: ''
    },
    payments: [],
    csi: {},
    loading: true
}

const getters = {
    agreement_list: (state) => (search) => {
      if (search.length == 0)
        return state.items
      return state.items.filter(i => i.agreement_no == search || i.customer.inn == search || i.id == search || i.customer.f == search )
    },    
    agreement_loading(state){
      return state.loading
    },  
    all_customer_agreements: (state) => (id) => {
      let a = state.items.find(agreement => agreement.id == id)
      if(!a) return []
      return state.items.filter(agreement => agreement.customer.id == a.customer.id)
    },
    agreement_Card: (state) => (id) => {
      return state.items.find(agreement => agreement.id == id)
    },
    contactData(state) {
      return state.contactData
    },
    contacts(state) {
      return state.contacts
    },
    agreement_payments(state) {
      return state.payments
    }
}

const mutations = {
    loading(state, is){
        state.loading = is
    },
    setList(state, payload){
        state.items = payload
        this.commit("loading", false)
    },
    addAgreement(state, payload){
      // debugger
      let a = payload[0]
      let i = state.items.findIndex(agreement => agreement.id === a.id)
      if (i > -1) {
        state.items.splice(i, 1);
        // state.items[i] = a
      }
      state.items.push(a)
      
    },
    addManyAgreement(state, payload){
      for (let a in payload) {
        let i = state.items.findIndex(agreement => agreement.id === a.id)
        if (i == -1) {
          state.items.push(payload[a])
        }
      }
    },
    setContactAgreement(state, id){
      state.contactData.agreement_id = id
    },
    setContacts(state, payload){
      // debugger
      state.contacts = payload
    },
    appendNewContact(state, payload){
      state.contacts.push(payload)
      state.contactData = {
        result: false,
        type: false,
        comment: '',
        installment_amt: '',
        installment_dt_to: ''
      }
    },
    setAgreementPayments(state, payload){
      state.payments = payload
    }
}
  
const actions = {
    async loadAgreementItems({commit}){
        const res = await ax.get("/agreement").catch(function(err) { console.log(err)});
        if(!res.err) {
          commit('setList', res.data.payload)
          return true;
        }
    },    
    async searchAgreementByString({commit}, search){
      const res = await ax.get(`/agreement?search_by_string=${search}`).catch(function(err) { console.log(err)});
      commit('addManyAgreement', res.data.payload)
    },
    async getAgreementByID({commit}, id){
        const res = await ax.get(`/agreement/${id}`).catch(function(err) { console.log(err)});
        // debugger;
        if(!res.err) {
          commit('addAgreement', res.data.payload)
          commit('setContacts', res.data.contacts)
          return true;
        }
    },
    async getAgreementPaymentsByAgreementID({commit}, agreement_id){
        const res = await ax.get(`/payment?agreement_id=${agreement_id}`).catch(function(err) { console.log(err)});
        if(!res.err) {
          commit('setAgreementPayments', res.data.payload)
          return true;
        }
    },
    async saveContactData({state, commit}){
        const res = await ax.post("/contact", state.contactData).catch(function(err) { console.log(err)});
        // debugger;
        if(!res.err) {
          commit('appendNewContact', res.data.payload)
          return true;
        }
    },
  async changeAgreement({ state, commit }, id){
    let agreement = this.getters.agreement_Card(id)
    // debugger
    const res = await ax.put(`/agreement/${agreement.id}`, {agreement}).catch(function(err) { console.log(err)});
    if(!res.err) {
      return true;
    }
    return true
  },
    // async changeProcType({state, commit}, id){
    //     let agreement = this.getters.agreement_Card(id)
    //     const res = await ax.put(`/agreement/${id}`, {agreement}).catch(function(err) { console.log(err)});
    //     // debugger;
    //     if(!res.err) {
    //       return true;
    //     }
    // },
}

export default {
  state,
  getters,
  actions,
  mutations
}