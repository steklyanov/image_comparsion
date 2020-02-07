import Vue from 'vue'
import Vuex from 'vuex'
// import Axios from 'axios'
import {HTTP} from '../http-common'

Vue.use(Vuex)

export const store = new Vuex.Store({
  state: {
    persons: null,
    current_person: {
      name: null,
      surname: null
    }
  },

  getters: {
    PERSONS: state => {
      return state.persons
    },
    CURRENT_PERSON: state => {
      return state.current_person
    }
  },

  mutations: {
    SET_PERSONS: (state, payload) => {
      state.persons = payload
    },

    ADD_PERSON: (state, payload) => {
      state.persons.push({id: payload.id})
    },

    LIST_PERSON: (state, payload) => {
      console.log(payload)
      state.current_person.name = payload.name
      state.current_person.surname = payload.surname
    },

    DELETE_PERSON: (state, payload) => {
      state.persons.splice(payload.arr_id, 1)
    }
  },

  actions: {
    GET_PERSONS: async (context, payload) => {
      HTTP.get('list/')
        .then(response => {
          context.commit('SET_PERSONS', response.data)
        })
        .catch(e => {
          this.errors.push(e)
        })
    },

    CREATE_PERSON: async (context, payload) => {
      HTTP.post('create/', {
        name: payload.name,
        surname: payload.surname
      })
        .then(response => {
          context.commit('ADD_PERSON', response.data)
        })
        .catch(e => {
          console.log(e)
        })
    },
    GET_PERSON_DATA: async (context, payload) => {
      HTTP.get('details/' + payload.id)
        .then(response => {
          context.commit('LIST_PERSON', response.data)
        })
        .catch(e => {
          console.log(e)
        })
    },
    DELETE_PERSON: async (context, payload) => {
      HTTP.delete('details/' + payload.id + '/delete/')
        .then(response => {
          context.dispatch('GET_PERSONS')
        })
        .catch(e => {
          console.log(e)
        })
    },
    UPLOAD_IMAGE: async (context, payload) => {
      console.log(payload)
      HTTP.put('details/' + payload.id + '/upload/',
        payload.image, {
          headers: { 'Content-Type': 'multipart/form-data' }
        })
        .then(response => {
          console.log(payload)
          console.log(response)
        })
        .catch(e => {
          console.log(payload)
          console.log(e)
        })
    }
  }
})
