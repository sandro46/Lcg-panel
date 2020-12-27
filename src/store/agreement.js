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
    csi_action_data:{
      agreement_id: null,
      csi: {},
      arrest_of_salary: 'N',
      arrest_of_property: 'N',
      arrest_of_accounts: 'N',
      arrest_of_deparure: 'N',
      give_csi_dt: '',
      recall_csi_dt: '',
      stop_actions_csi_dt: '',
      return_ispol_doc_dt: '',
      comment: ''
    },
    payments: [],
    csi_actions: [],
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
    csiActionData(state) {
      return state.csi_action_data
    },
    contacts(state) {
      return state.contacts
    },
    csi_actions(state) {
      return state.csi_actions
    },
    agreement_payments(state) {
      return state.payments
    },
    sum_agreement_payments(state) {
      return state.payments.reduce((accum, item) => accum + item.amount, 0)
    },
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
    setCsiActionAgreement(state, id){
      state.csi_action_data.agreement_id = id
    },
    setContacts(state, payload){
      state.contacts = payload
    },
    setCsiActions(state, payload){
      // debugger
      state.csi_actions = payload
    },
    appendNewContact(state, payload){
      state.contacts.push(payload)
      state.contactData.result = false
      state.contactData.type = false
      state.contactData.comment = ''
      state.contactData.installment_amt = ''
      state.contactData.installment_dt_to = ''
    },
    appendNewCsiAction(state, payload){
      state.csi_actions.push(payload)

      state.csi_action_data.csi = {}
      state.csi_action_data.arrest_of_salary = 'N'
      state.csi_action_data.arrest_of_property = 'N'
      state.csi_action_data.arrest_of_accounts = 'N'
      state.csi_action_data.arrest_of_deparure = 'N'
      state.csi_action_data.give_csi_dt = ''
      state.csi_action_data.recall_csi_dt = ''
      state.csi_action_data.stop_actions_csi_dt = ''
      state.csi_action_data.return_ispol_doc_dt = ''
      state.csi_action_data.comment = ''
    },
    editCsiAction(state, payload){
      let idx = state.csi_actions.findIndex((i, e) => {
        return e.id == payload.id
      })
      state.csi_actions[idx] = payload
    },
    deleteCsiAction(state, id){
      let idx = state.csi_actions.findIndex((i, e) => {
        return e.id == id
      })
      state.csi_actions.splice(idx, 1)
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
          commit('setCsiActions', res.data.csi_actions)
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
    async saveCsiAction({state, commit}, data){
      const res = await ax.post("/csi_actions", state.csi_action_data).catch(function(err) { console.log(err)});
      if(!res.err) {
        commit('appendNewCsiAction', res.data.payload)
        return true;
      }
    },
    async editCsiAction({ commit }, data){
      const res = await ax.put("/csi_actions", data).catch(function(err) { console.log(err)});
      if(!res.err) {
        commit('editCsiAction', res.data.payload)
        return true;
      }
    },
    async deleteCsiAction({ commit }, id){
      const res = await ax.delete(`/csi_actions/${id}`).catch(function(err) { console.log(err)});
      if(!res.err) {
        commit('deleteCsiAction', id)
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