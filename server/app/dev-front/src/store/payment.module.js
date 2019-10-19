import { PaymentsService } from "@/common/api.service";
import {
    FETCH_PAYMENTS
} from "./actions.type";
import {
    SET_PAYMENTS
} from "./mutations.type";

export const state = {
    payments: []
};

const getters = {
    payments(state){
        return state.payments;
    }
};

export const actions = {
    [FETCH_PAYMENTS](context, course_id){
        return PaymentsService.get()
            .then(({data}) => {
                context.commit(SET_PAYMENTS, data.results)
            })
    }
};

export const mutations = {
    [SET_PAYMENTS](state, payments){
        state.payments = payments;
    }
};

export default {
    state,
    actions,
    mutations,
    getters
};
