<template>
    <div class="container mt-4">
        <button type="button" class="btn btn-primary">Categories</button>

        <div id="info" class="row mt-3 mb-5">
            <div class="col-8 border pt-3 pb-3">
                <p class="font-weight-bold">おすすめのコース</p>
                <div id="recommend-card" class="card shadow-sm">
                    <div class="card-body">
                        <h5 class="card-title">test</h5>
                        <p class="card-text">test</p>
                    </div>
                </div>
            </div>

            <div class="col-4 border pt-3 pb-3">
                <p class="font-weight-bold">投稿Q&A一覧</p>

                <div id="q_and_a-cards">
                    <div class="card mb-4 shadow-sm">
                        <div class="card-body">
                            <h5 class="card-title">test</h5>
                            <p class="card-text">test</p>
                            <small>2019/06/30</small>
                        </div>
                    </div>
                    <div class="card mb-4 shadow-sm">
                        <div class="card-body">
                            <h5 class="card-title">test</h5>
                            <p class="card-text">test</p>
                            <small>2019/06/30</small>
                        </div>
                    </div>
                </div>
            </div>
        </div>


    </div>
</template>

<script>
    import { mapGetters } from "vuex"
    import {
        FETCH_SUBSCRIBE_COURSES,
    } from "@/store/actions.type";

    export default {
        name: "Home",
        mounted() {
            this.$store.dispatch(FETCH_SUBSCRIBE_COURSES);
        },
        computed: {
            ...mapGetters([])
        }
    }
</script>

<style scoped lang="scss">
    #recommend-card{
        height: 250px;
    }

    #q_and_a-cards{
        height: 250px;
        overflow: auto;
    }
</style>
