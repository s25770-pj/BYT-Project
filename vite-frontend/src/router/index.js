import { createRouter, createWebHashHistory } from 'vue-router';

import PanelRouter from '@/modules/panel/router/index.js';

const routes = [
  {path: '/',name:"Home",component:()=>import('@/view/MainPage.vue')},
  {path: '/LogIn',name:"logIn",component:()=>import('@/view/LoginPage.vue')},
  {path: '/Register',name:"register",component:()=>import('@/view/RegisterUser.vue')},
  {path: '/aboutUs', name:"aboutUs",component:()=>import('@/view/AboutUs.vue')},
  {path: '/:catchAll(.*)', name:"notFound",component:()=>import('@/view/NotFoundPage.vue')},
  PanelRouter
];

const router = createRouter({
  history: createWebHashHistory(),
  routes,
});

export default router;