import Vue from 'vue'
import App from './App.vue'
import router from './router'
import vuetify from './plugins/vuetify';
import VuetifyDialog from 'vuetify-dialog'
import * as VueGoogleMaps from 'vue2-google-maps'
import VueSidebarMenu from 'vue-sidebar-menu'
import 'vue-sidebar-menu/dist/vue-sidebar-menu.css'

import { domain, clientId, audience } from "../auth_config.json";
import { Auth0Plugin } from "./auth";

Vue.use(VueSidebarMenu)

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

Vue.use(Auth0Plugin, {
  domain,
  clientId,
  audience,
  onRedirectCallback: appState => {
    router.push(
      appState && appState.targetUrl
        ? appState.targetUrl
        : window.location.pathname
    );
  }
});

new Vue({
  vuetify,
  router,
  render: h => h(App)

}).$mount('#app')