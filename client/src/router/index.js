import Vue from 'vue';
import Router from 'vue-router';
import Customers from '@/components/Customers';
import Businesses from '@/components/Businesses';

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: '/customers',
      name: 'Customers',
      component: Customers,
    },
    {
      path: '/businesses',
      name: 'Businesses',
      component: Businesses,
    },
    {
      path: '/orders',
      name: 'Orders',
      component: Orders,
    },
    {
      path: '/products',
      name: 'Products',
      component: Products,
    }
  ],
  mode: 'history',
});
