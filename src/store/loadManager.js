/*eslint-disable */
const axios = require('axios')
const config = require('./config.json')


const ax = axios.create({
    baseURL: config.VUE_APP_BASE_URL,
    timeout: 300000,
});


const state = {   
    items:[],
    defaultItem: {
        select: 0,
        types: [],
        file: undefined
    },
    loading: true
}

const getters = {
    load_list(state){
      return state.items
    },    
    load_loading(state){
      return state.loading
    },
    loaderDefaultItem(state){
        return state.defaultItem
    }
}

const mutations = {
    setList(state, payload){
        state.items = payload
    },
    setLoaderDefaultItemType(state, payload){
        state.defaultItem.types = payload
    },
    closeLoaderModal(state){
        state.defaultItem.select = 0
        state.defaultItem.file = undefined
    }
}


const actions = {
    async saveLoadData({commit, state}){
        let fd = new FormData();
        fd.append('file', state.defaultItem.file)
        fd.append('type', state.defaultItem.select)

        const res = await ax.post(
            "/loader", 
            fd,
            {
                headers: { 'Content-Type': 'multipart/form-data' }
            }
        ).catch(function(err) { console.log(err)});
        // debugger;
    },
    async loadLoaderItems({commit}){
        const res = await ax.get("/loader").catch(function(err) { console.log(err)});
        // debugger;
        if(!res.err) {
          commit('setList', res.data.payload)
          return true;
        }
    },    
    async loaderLoadRefs({commit}){
        const res = await ax.get("/get_ref?type=loaderTypes").catch(function(err) { console.log(err)});
        // debugger;
        if(!res.err) {
          commit('setLoaderDefaultItemType', res.data.payload)
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