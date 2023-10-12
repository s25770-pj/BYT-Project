import { createRouter, createWebHashHistory } from 'vue-router';

import Home from '@/view/MainPage.vue';
import Panel from '@/view/UserPanel.vue';
import LogIn from '@/view/LoginPage.vue';
import NotFound from '@/view/NotFoundPage.vue';
import AboutUs from '@/view/AboutUs.vue';
import Profil from '@/components/Panel/ProfilPage.vue';
import Statistics from '@/components/Panel/UserStatistics.vue';
import Learning from '@/components/Panel/LearningPage.vue';
const routes = [
  {
    path: '/',
    component: Home
  },
  {
    path: '/panel',
    component: Panel,
    children: [
      {
        path: '',
        components: {
          default:Statistics
        }
      },
      {
        path: 'profil',
        components: {
          default: Profil,
        }
      },
      {
        path: 'learning',
        components: {
          default: Learning,
        }
      }
    ]
  },
  {
    path: '/LogIn',
    component: LogIn
  },
  {
    path: '/aboutUs',
    component: AboutUs
  },
  {
    path: '/profil',
    components: Profil
  },
  {
    path: '/:catchAll(.*)',
    component: NotFound
  }
];

const router = createRouter({
  history: createWebHashHistory(),
  routes,
});

export default router;