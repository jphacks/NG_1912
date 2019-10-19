import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";

import BootstrapVue from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import { CHECK_AUTH } from "./store/actions.type"
import ApiService from "./common/api.service";

Vue.config.productionTip = false;
Vue.use(BootstrapVue);

ApiService.init();

// Ensure we checked auth before each page load.
router.beforeEach((to, from, next) => {
        Promise.all([store.dispatch(CHECK_AUTH)])
            .then(() => {
                    if (to.matched.some(record => !record.meta.isPublic) && !store.getters.isAuthenticated) {
                        next({
                            path: '/login',
                            query: { redirect: to.fullPath }
                        })
                    }else {
                        next();
                    }
                }
            );
    }
);

new Vue({
    router,
    store,
    render: h => h(App)
}).$mount("#app");


