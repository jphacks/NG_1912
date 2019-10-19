<template>
    <nav id="header" class="navbar navbar-dark bg-dark navbar-expand-md">

        <router-link v-if="!isAuthenticated" class="navbar-brand" :to="{name: 'root'}">e-learning</router-link>
        <router-link v-else class="navbar-brand" :to="{name: 'home'}">e-learning</router-link>

        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNavDropdown" aria-controls="navbarNavDropdown" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNavDropdown">
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
        </div>
    </nav>
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