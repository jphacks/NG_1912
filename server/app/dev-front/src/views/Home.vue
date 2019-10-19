<template>
    <b-container class="mt-5">
        <h2 class="font-weight-normal mb-3">注文履歴</h2>

        <h5 v-show="payments.length === 0">表示する注文履歴が存在しません</h5>
        <div v-show="payments.length !== 0" v-for="payment in payments" class="custom-border mt-3">
            <b-card-header>
                <b-row>
                    <b-col cols="6">
                        合計&nbsp;:&nbsp;
                        <span v-if="payment.is_completed" class="font-weight-bold"><span class="text-info h2">&nbsp;{{ Math.floor( payment.price * (1 + payment.tax_rate / 100)) }}&nbsp;</span><small>円&nbsp;(税込)</small></span>
                        <span v-else class="font-weight-bold"><span class="text-warning h2">&nbsp;{{ Math.floor( payment.price * (1 + 10 / 100)) }}&nbsp;</span><small>円&nbsp;(税込)</small></span>
                    </b-col>
                    <b-col cols="6">
                        税率&nbsp;:&nbsp;
                        <span v-if="payment.is_completed" class="font-weight-bold"><span class="text-info h2">&nbsp;{{ payment.tax_rate }}&nbsp;</span><small>&#37;</small></span>
                        <span v-else class="font-weight-bold"><span class="text-warning h2">&nbsp;10&nbsp;</span><small>&#37;</small></span>
                    </b-col>
                </b-row>
            </b-card-header>
            <b-list-group flush>
                <b-list-group-item v-for="choice in payment.choices">{{ choice.food.name }}&nbsp;:&nbsp;{{ choice.food.price }}&nbsp;円&nbsp;&times;&nbsp;{{ choice.food_count }}&nbsp;=&nbsp;{{ choice.price }}&nbsp;円</b-list-group-item>
            </b-list-group>
        </div>

    </b-container>
</template>

<script>
    import { mapGetters } from "vuex"
    import {
        FETCH_PAYMENTS,
    } from "@/store/actions.type";

    export default {
        name: "Home",
        mounted() {
            this.$store.dispatch(FETCH_PAYMENTS);
        },
        computed: {
            ...mapGetters(["payments"])
        }
    }
</script>

<style scoped lang="scss">
    .custom-border{
        border: 1px solid rgba(0, 0, 0, 0.125);
        border-radius: 0.25rem;
    }
</style>
