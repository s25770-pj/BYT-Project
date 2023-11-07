import { createRouter, createWebHashHistory } from 'vue-router';

import Home from '@/view/MainPage.vue';

import LogIn from '@/view/LoginPage.vue';
import NotFound from '@/view/NotFoundPage.vue';
import AboutUs from '@/view/AboutUs.vue';
import Register from '@/view/RegisterUser.vue';

import PanelRouter from '@/modules/panel/router/index.js';

const routes = [
  {
    path: '/',
    component: Home
  },
  {
    path: '/LogIn',
    component: LogIn
  },
  {
    path: '/Register',
    component: Register
  },
  {
    path: '/aboutUs',
    component: AboutUs
  },
  {
    path: '/:catchAll(.*)',
    component: NotFound
  },
  PanelRouter
];

const router = createRouter({
  history: createWebHashHistory(),
  routes,
});

export default router;