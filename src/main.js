//import './assets/main.css'

import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'
import router from './router'

import VueDatePicker from '@vuepic/vue-datepicker';
import '@vuepic/vue-datepicker/dist/main.css'
import 'bootstrap/dist/css/bootstrap.min.css'
import 'bootstrap'
import 'bootstrap-icons/font/bootstrap-icons.css'
import 'sidebarjs/lib/sidebarjs.min.css'
import './css/style.css'
import './css/table.css'
import './css/dropdown.css'
import 'datatables.net'
import 'datatables.net-dt/css/dataTables.dataTables.min.css'

const app = createApp(App)

app.use(createPinia())
app.use(router)

app.mount('#app')
