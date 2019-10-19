<template>
    <div class="main d-flex align-items-center user-form">
        <div class="container">
            <div class="card">
                <div class="card-body  d-flex align-items-center ">
                    <form class="form" v-on:submit.prevent="onSubmit">

                        <h3 class="text-center text-info">ユーザー登録</h3>

                        <div class="form-group">
                            <label class="text-info" for="username">ユーザー名</label>
                            <input v-model="username" type="text" id="username" placeholder="ユーザー名" class="form-control" required>
                        </div>

                        <div class="form-group">
                            <label class="text-info" for="email">Email</label>
                            <input v-model="email" type="email" id="email" placeholder="Email" class="form-control" required>
                        </div>

                        <div class="form-group">
                            <label class="text-info" for="first_name">姓</label>
                            <input v-model="first_name" type="text" id="first_name" placeholder="姓" class="form-control" required>
                        </div>

                        <div class="form-group">
                            <label class="text-info" for="last_name">名</label>
                            <input v-model="last_name" type="text" id="last_name" placeholder="名" class="form-control" required>
                        </div>

                        <div class="form-group">
                            <label class="text-info" for="password1">パスワード</label>
                            <input v-model="password1" type="password" id="password1" placeholder="パスワード" class="form-control" required>
                        </div>

                        <div class="form-group">
                            <label class="text-info" for="password2">パスワード確認</label>
                            <input v-model="password2" type="password" id="password2" placeholder="パスワード確認" class="form-control" required>
                        </div>

                        <button class="btn btn-info">登録する</button>

                        <hr>
                        <router-link :to="{ name: 'login'}">ログインする</router-link>
                    </form>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    import { mapState } from "vuex";
    import { REGISTER } from "@/store/actions.type";

    export default {
        name: "Register",
        data() {
            return {
                username: "",
                email: "",
                password1: "",
                password2: "",
                first_name: "",
                last_name: ""
            }
        },
        computed: {
            ...mapState({
                errors: state => state.auth.errors
            })
        },
        methods: {
            onSubmit() {
                this.$store
                    .dispatch(REGISTER, {
                        username: this.username,
                        email: this.email,
                        password1: this.password1,
                        password2: this.password2,
                        first_name: this.first_name,
                        last_name: this.last_name,
                        gender: this.gender,
                        age: this.age,
                        pref: this.pref
                    })
                    .then(() => this.$router.push({name: "root"}))
            }
        }
    }
</script>

<style scoped lang="scss">
    .user-form{
        height: calc(100vh - 56px);
        margin-top: 60px;
        margin-bottom: 60px;
        form{
            width: 100%;
        }
    }
</style>
