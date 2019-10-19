<template>
    <div class="d-flex align-items-center user-form">
        <div class="container">
            <div class="card">
                <div class="card-body  d-flex align-items-center ">
                    <form class="form" v-on:submit.prevent="onSubmit(email, password)">

                        <h3 class="text-center text-info">ログイン</h3>

                        <div class="form-group">
                            <label class="text-info" for="email">Email</label>
                            <input v-model="email" type="email" id="email" placeholder="Email" class="form-control" required>
                        </div>

                        <div class="form-group">
                            <label class="text-info" for="password">パスワード</label>
                            <input v-model="password" type="password" id="password" placeholder="パスワード" class="form-control" required>
                        </div>

                        <button class="btn btn-info">ログイン</button>
                    </form>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    import { mapState } from "vuex";
    import { LOGIN } from "@/store/actions.type";

    export default {
        name: "Login",
        data(){
            return {
                email: null,
                password: null
            }
        },
        methods: {
            onSubmit(email, password){
                this.$store
                    .dispatch(LOGIN, { email, password })
                    .then(() => this.$router.push({ name: "home" }));
            }
        },
        computed: {
            ...mapState({
                errors: state => state.auth.errors
            })
        }
    }
</script>

<style scoped lang="scss">
    .user-form{
        height: calc(100vh - 56px);
        form{
            width: 100%;
        }
    }
</style>
