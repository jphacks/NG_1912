<template>
    <div class="mt-3">
        <div v-if="testShow" id="test">
            <p v-show="!testContentShow">送信しました</p>
            <div v-show="testContentShow" v-for="test in lesson_tests" class="card mb-4 shadow-sm">
                <div class="card-body">
                    <h5 class="card-title">{{ test.content }}</h5>
                    <b-form-radio v-for="choice in test.choices" v-model="test.choiced_id" v-bind:value="choice.id">{{ choice.text }}</b-form-radio>
                </div>
            </div>
        </div>

        <div v-else id="confirmMyAnswer">
            <div v-for="result in lesson_tests_result" class="card mb-4 shadow-sm">
                <div class="card-body">
                    <h3 class="card-title">{{ result["test"].content }}</h3>
                    <h6>あなたの選択</h6>
                    <ul>
                        <li v-for="choice in result['test'].choices">
                            <p v-if="choice.id === result.choice_id" class="font-weight-bold">{{ choice.text }}</p>
                            <p v-else >{{ choice.text }}</p>
                        </li>
                    </ul>

                    <h5 v-if="result.isCorrect" class="card-text text-primary">正解</h5>
                    <h5 v-else class="card-text text-danger">不正解</h5>
                </div>
            </div>

        </div>

        <b-button v-if="testShow" class="mt-4" @click="submitAnswer" variant="primary">送信</b-button>
        <b-button v-else class="ml-3 mt-4" @click="doTest" variant="primary">テストを行う</b-button>
        <b-button v-if="testShow && lesson_tests_result.length !== 0" class="ml-3 mt-4" @click="confirmMyAnswer" variant="primary">以前の回答を確認</b-button>
    </div>
</template>

<style lang="scss" scoped>
    #test{
        height: 350px;
        overflow: auto;
    }
    #confirmMyAnswer{
        height: 350px;
        overflow: auto;
    }
</style>

<script>
    import { mapGetters } from "vuex";
    import {
        FETCH_LESSON_TESTS,
        FETCH_LESSON_TESTS_RESULT,
        CREATE_LESSON_TESTS_RESULT
    } from "@/store/actions.type";

    export default {
        name: "Test",
        props: {
            lesson_id: {
                type: Number,
                required: true
            }
        },
        data() {
            return{
                testContentShow: true,
                testShow: true
            }
        },
        mounted() {
            this.$store.dispatch(FETCH_LESSON_TESTS, this.lesson_id);
            this.$store.dispatch(FETCH_LESSON_TESTS_RESULT, this.lesson_id);
        },
        computed: {
            ...mapGetters(["lesson_tests", "lesson_tests_result"])
        },
        methods: {
            confirmMyAnswer(){
                this.testShow = !this.testShow;
            },
            doTest(){
                this.testShow = !this.testShow;
                this.testContentShow = true;
            },
            submitAnswer(){
                let answers = {
                    lesson_id: this.lesson_id,
                    answers: []
                };
                for(let test of this.lesson_tests){
                    let choice = {
                        test_id: test.id,
                        choice_id: test.choiced_id
                    };
                    answers.answers.push(choice);
                }

                this.$store
                    .dispatch(CREATE_LESSON_TESTS_RESULT, answers)
                    .then( (data) => {
                        this.testContentShow = !this.testContentShow;
                        this.$store.dispatch(FETCH_LESSON_TESTS_RESULT, this.lesson_id);
                    });
            }
        }
    }
</script>
