import Vue from "vue";
import Router from "vue-router";
import Root from "./views/Root";

Vue.use(Router);

export default new Router({
  mode: "history",
  base: process.env.BASE_URL,
  routes: [
    {
      path: "/",
      name: "root",
      component: Root,
      meta: { isPublic: true }
    },
    {
      path: "/home",
      name: "home",
      component: () => import("@/views/Home"),
    },
    {
      path: "/login",
      name: "login",
      component: () => import("@/views/Login"),
      meta: { isPublic: true }
    },
    {
      path: "/register",
      name: "register",
      component: () => import("@/views/Register"),
      meta: { isPublic: true }
    },
    {
      path: "/404",
      component: () => import("@/views/404"),
      meta: { isPublic: true }
    },
    {
      path: '*',
      redirect: '/404',
      meta: { isPublic: true }
    }
  ]
});
