<template>
    <b-navbar id="header" toggleable="lg" type="dark" variant="info">
        <b-navbar-brand v-if="!isAuthenticated" :to="{name: 'root'}">zesei</b-navbar-brand>
        <b-navbar-brand v-else :to="{name: 'home'}">zesei</b-navbar-brand>

        <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

        <b-collapse id="nav-collapse" is-nav>
            <ul class="navbar-nav mr-auto"></ul>

            <ul v-if="!isAuthenticated" class="navbar-nav">
                <li class="nav-item"><router-link :to="{name: 'register'}" class="nav-link">ユーザー登録</router-link></li>
                <li class="nav-item"><router-link :to="{name: 'login'}" class="nav-link">ログイン</router-link></li>
            </ul>
            <ul v-else class="navbar-nav">
                <li class="nav-item"><span class="navbar-text font-weight-bold">{{ currentUser.username }} さん</span></li>
                <li class="nav-item"><router-link :to="{name: 'user'}" class="nav-link">プロフィール更新</router-link></li>
                <li class="nav-item"><a class="nav-link" @click="logout">ログアウト</a></li>
            </ul>
        </b-collapse>
    </b-navbar>

</template>

<script>
    import { LOGOUT } from "@/store/actions.type";
    import { mapGetters } from "vuex";
    export default {
        name: "Header",
        computed: {
            ...mapGetters(["currentUser", "isAuthenticated"])
        },
        methods: {
            logout() {
                this.$store.dispatch(LOGOUT).then(() => {
                    this.$router.push({name: "root"})
                });
            }
        }
    }
</script>
