import Vue from 'vue'
import App from './App.vue'
import vuetify from './plugins/vuetify';
import VuetifyDialog from 'vuetify-dialog'
import * as VueGoogleMaps from 'vue2-google-maps'

Vue.use(VueGoogleMaps, {
  load: {
    key: 'AIzaSyD0VuxLCHgrHGPT1SitPMHecNCZHsbXe9A',
    libraries: 'places'
  }
})

Vue.config.productionTip = false

Vue.use(VuetifyDialog, {
  context: {
    vuetify
  }
})

new Vue({
  vuetify,
  render: h => h(App)

}).$mount('#app')