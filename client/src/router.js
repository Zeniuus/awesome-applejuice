import Vue from 'vue';
import Router from 'vue-router';
import Home from './views/Home';
import RuralLife from './views/RuralLife';
import AppleStory from './views/AppleStory';
import QnA from './views/QnA';
import Order from './views/Order';
import OrderForm from './components/Order/OrderForm';
import OrderComplete from './components/Order/OrderComplete';
import MyOrder from './components/Order/MyOrder';
import Manage from './views/Manage';
import Signin from './views/Signin';
import NotFound from './views/NotFound';

import store from './store';


Vue.use(Router);

function adminGuard(to, from, next) {
  if (!store.state.authInitialized) {
    store.commit('initializeAuth');
  }

  if (store.state.jwt) {
    next();
  } else {
    /*
     * Navigate to NotFound component, without updating URL.
     * refs: https://github.com/vuejs/vue-router/issues/977#issuecomment-304498068
     */
    next({ name: 'not-found', params: [to.path] });
  }
}

const router = new Router({
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
      path: '/order',
      name: 'order',
      component: Order,
      children: [
        {
          path: 'purchase',
          name: 'order_purchase',
          component: OrderForm,
        },
        {
          path: 'my-order',
          name: 'order_my-order',
          component: MyOrder,
        },
        {
          path: 'complete',
          name: 'order_complete',
          component: OrderComplete,
          props: true,
        },
      ],
    },
    {
      path: '/manage',
      name: 'manage',
      component: Manage,
      beforeEnter: adminGuard,
    },
    {
      path: '/signin',
      name: 'signin',
      component: Signin,
    },
    {
      path: '*',
      name: 'not-found',
      component: NotFound,
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

export default router;
