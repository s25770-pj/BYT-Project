import { createRouter, createWebHistory } from 'vue-router';

import Home from '@/view/MainPage.vue';
import Panel from '@/view/UserPanel.vue';

const routes = [
  {
    path: '/',
    component: Home,
  },
  {
    path: '/panel',
    component: Panel,
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;