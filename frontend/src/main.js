import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap/dist/js/bootstrap.js';
import 'normalize.css';

import '@/config/variables.css';

import { createApp } from 'vue';
import App from './App.vue';
import router from '@/router/index.js';

import Highcharts from 'highcharts';
import HighchartsVue from 'highcharts-vue';
import { isDarkMode, toggleDarkMode } from '@/config/darkmode.js';

const app = createApp(App);

isDarkMode.value = localStorage.getItem('darkMode') === 'dark';

document.documentElement.classList.toggle('dark', isDarkMode.value);


app.use(router);
app.use(HighchartsVue, { Highcharts });

app.config.globalProperties.$isDarkMode = isDarkMode;
app.config.globalProperties.$toggleDarkMode = toggleDarkMode;
app.mount('#app');

