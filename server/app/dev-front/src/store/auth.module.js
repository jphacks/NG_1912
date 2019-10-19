import ApiService from "@/common/api.service";
import Vue from "vue";
import TokenService from "@/common/token.service";
import {
    LOGIN,
    LOGOUT,
    REGISTER,
    CHECK_AUTH,
    CONFIRM_USER,
    UPDATE_USER,
    UPDATE_USER_PASSWORD
} from "./actions.type"
import { SET_AUTH_TOKEN, SET_USER, PURGE_AUTH, SET_ERROR } from "./mutations.type";

const state = {
    errors: null,
    user: {},
    isAuthenticated: !!TokenService.getToken()
};

const getters = {
    currentUser(state) {
        return state.user;
    },
    isAuthenticated(state) {
        return state.isAuthenticated;
    }
};

const actions = {
    [LOGIN](context, credentials) {
        return new Promise(resolve => {
            ApiService.post("auth/login", credentials)
                .then(({ data }) => {
                    context.commit(SET_AUTH_TOKEN, data.key);
                    resolve(data);
                })
                .catch(({ response }) => {
                    context.commit(SET_ERROR, response.data.errors);
                });
        });
    },
    [LOGOUT](context){
        return new Promise(resolve => {
            ApiService.post("auth/logout",null)
                .then(({data}) => {
                    context.commit(PURGE_AUTH);
                    resolve(data);
                })
                .catch(({ response }) => {
                    console.log(response);
                })
        });
    },
    [REGISTER](context, credentials){
        return new Promise((resolve, reject) => {
            ApiService.post("auth/registration", credentials)
                .then(({ data }) => {
                    alert(data.detail);
                    resolve(data);
                })
                .catch(({ response }) => {
                    context.commit(SET_ERROR, response.data.errors);
                    reject(response);
                });
        });
    },
    [CONFIRM_USER](context,key){
        ApiService.post("auth/registration/verify-email", key)
            .then(({data}) => {
                alert(data.detail);
            })
    },
    [CHECK_AUTH](context){
        if (TokenService.getToken()) {
            ApiService.setHeader();
            ApiService.get("auth/user")
                .then(({ data }) => {
                    context.commit(SET_USER, data);
                })
                .catch(({ response }) => {
                    context.commit(SET_ERROR, response.data.errors);
                });
        } else {
            context.commit(PURGE_AUTH);
        }
    },
    [UPDATE_USER](context, user) {
        return ApiService.patch("auth/user", user);
    },
    [UPDATE_USER_PASSWORD](context, password) {
        return ApiService.post("auth/password/change", password)
            .then(({data}) => {
                alert(data.detail);
            })
    }
};

const mutations = {
    [SET_ERROR](state, error) {
        state.errors = error;
    },
    [SET_AUTH_TOKEN](state, token) {
        TokenService.saveToken(token);
        state.isAuthenticated = true;
    },
    [SET_USER](state, user){
        state.user = user;
        state.errors = {};
    },
    [PURGE_AUTH](state) {
        state.isAuthenticated = false;
        state.user = {};
        state.errors = {};
        TokenService.destroyToken();
        delete Vue.axios.defaults.headers.common["Authorization"]
    }
};

export default {
    state,
    actions,
    mutations,
    getters
};
