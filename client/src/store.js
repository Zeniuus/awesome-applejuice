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
      state[field] = value; /* eslint-disable-line */
    },
  },
  actions: {

  },
});
