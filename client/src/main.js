import Vue from 'vue';
import axios from 'axios';

import App from './App.vue';
import router from './router';
import store from './store';
import bulma from './main.scss'; /* eslint-disable-line */


Vue.config.productionTip = false;

axios.interceptors.request.use((config) => {
  if (store.state.jwt) {
    /* eslint-disable-next-line no-param-reassign, dot-notation */
    config.headers['Authorization'] = `Bearer ${store.state.jwt}`;
  }
  return config;
});
Vue.prototype.$http = axios;

new Vue({
  router,
  store,
  render: h => h(App),
}).$mount('#app');
