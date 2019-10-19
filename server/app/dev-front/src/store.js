import Vue from "vue";
import Vuex from "vuex";
import auth from "./store/auth.module";
import payment from "./store/payment.module"

Vue.use(Vuex);

export default new Vuex.Store({
  modules:{
    auth,
    payment
  },
});
