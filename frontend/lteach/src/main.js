// // The Vue build version to load with the `import` command
// // (runtime-only or standalone) has been set in webpack.base.conf with an alias.
// import Vue from 'vue'
// import App from './App'
// import router from './router'

// Vue.config.productionTip = false

// /* eslint-disable no-new */
// new Vue({
//   el: '#app',
//   router,
//   components: { App },
//   template: '<App/>'
// })

import Vue from 'vue';
import TDesign from 'tdesign-vue';
import router from './router';
import App from './App.vue';
import store from './store';
import 'tdesign-vue/es/style/index.css';


Vue.config.productionTip = false

Vue.use(TDesign);

new Vue({
  el: '#app',
  render: h => h(App),
  router,
  components: { App },
  store: store,
  template: '<App/>'
});