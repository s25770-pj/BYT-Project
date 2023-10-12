import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap/dist/js/bootstrap.js';
import 'normalize.css';

import { createApp } from 'vue';
import App from './App.vue';
import router from '@/router/index.js';

import Highcharts from 'highcharts';
import HighchartsVue from 'highcharts-vue';

const app = createApp(App);

app.use(router);
app.use(HighchartsVue, { Highcharts });

app.mount('#app');

