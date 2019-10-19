import Vue from "vue";
import axios from "axios";
import VueAxios from "vue-axios";
import TokenService from "@/common/token.service";
import { API_URL } from "@/common/config";
import { PURGE_AUTH } from "@/store/mutations.type";
import store from "@/store";
import router from "@/router";


const ApiService = {
    init() {
        Vue.use(VueAxios, axios);
        Vue.axios.defaults.baseURL = API_URL;
        Vue.axios.interceptors.response.use(
            response => response,
            error => {
                if (error.response.status === 401) {
                    console.log(error);
                    store.commit(PURGE_AUTH).then(() => {
                            router.push({name: "root"})
                        }
                    );
                }
                return Promise.reject(error);
            }
        )
    },

    setHeader() {
        Vue.axios.defaults.headers.common[
            "Authorization"
            ] = `Token ${TokenService.getToken()}`;
    },

    query(resource, params) {
        return Vue.axios.get(resource, params).catch(error => {
            throw new Error(`[JPHacks] ApiService ${error}`);
        });
    },

    get(resource, slug = ""){
        return Vue.axios.get(`${resource}/${slug}`).catch( error => {
            throw new Error(`[JPHacks] ApiService ${error}`);
        })
    },

    post(resource, params) {
        return Vue.axios.post(`${resource}/`, params);
    },

    patch(resource, params) {
        return Vue.axios.patch(`${resource}/`, params);
    },

    update(resource, slug, params) {
        return Vue.axios.patch(`${resource}/${slug}/`, params);
    },

    delete(resource) {
        return Vue.axios.delete(`${resource}/`).catch(error => {
            throw new Error(`[JPHacks] ApiService ${error}`);
        });
    }
};

export default ApiService;

export const FoodsService = {
    get(slug) {
        return ApiService.get("foods", slug);
    }
};

export const PaymentsService = {
    get(slug){
        return ApiService.get("payments", slug);
    }
};
