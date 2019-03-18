import Vue from 'vue';
import Router from 'vue-router';
import Customers from '@/components/Customers';
import Businesses from '@/components/Businesses';
import Products from '@/components/Products';
import Orders from '@/components/Orders';

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
      path: '/products',
      name: 'Products',
      component: Products,
    },
    {
      path: '/orders',
      name: 'Orders',
      component: Orders,
    },
  ],
  mode: 'history',
});
