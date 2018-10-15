import Vue from 'vue';
import Router from 'vue-router';
import Home from './views/Home';
import RuralLife from './views/RuralLife';
import AppleStory from './views/AppleStory';
import QnA from './views/QnA';
import Buy from './views/Buy';


Vue.use(Router);

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home,
    },
    {
      path: '/rural-life',
      name: 'rural-life',
      component: RuralLife,
    },
    {
      path: '/apple-story',
      name: 'apple-story',
      component: AppleStory,
    },
    {
      path: '/qna',
      name: 'qna',
      component: QnA,
    },
    {
      path: '/buy',
      name: 'buy',
      component: Buy,
    },
    // {
    //   path: '/about',
    //   name: 'about',
    //   // route level code-splitting
    //   // this generates a separate chunk (about.[hash].js) for this route
    //   // which is lazy-loaded when the route is visited.
    //   component: () => import(/* webpackChunkName: "about" */ './views/About.vue'),
    // },
  ],
});
