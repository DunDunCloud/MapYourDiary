import Vue from 'vue';
import Vuetify, {
  VSnackbar,
  VIcon,
  VDialog,
  VSpacer,
  VBtn,
  VToolbar,
  VToolbarTitle,
  VAlert
} from 'vuetify/lib';


Vue.use(Vuetify, {
  iconfont: 'md',
  components: {
    VSnackbar,
    VIcon,
    VDialog,
    VSpacer,
    VBtn,
    VToolbar,
    VToolbarTitle,
    VAlert
  }
})

export default new Vuetify({
});

