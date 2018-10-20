/* eslint-disable no-param-reassign */
import Vue from 'vue';
import Vuex from 'vuex';

import { assert } from './utils/common';


Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    id: null,
    nickname: null,
    jwt: null,
  },
  mutations: {
    stateSetter(state, { field, value }) {
      assert(field);
      state[field] = value;
    },
    initializeAuth(state) {
      const id = localStorage.getItem('id');
      const nickname = localStorage.getItem('nickname');
      const jwt = localStorage.getItem('jwt');
      if (id && nickname && jwt) {
        state.id = id;
        state.nickname = nickname;
        state.jwt = jwt;
      }
    },
  },
  actions: {

  },
});
