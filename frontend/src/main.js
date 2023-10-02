import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap/dist/js/bootstrap.js';
import 'normalize.css';

import { createApp } from 'vue';
import App from './App.vue';
import router from '@/router/index.js';

createApp(App).use(router).mount('#app');
