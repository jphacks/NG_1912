<template>
    <div>
        <b-row>
            <b-col cols="3">
                <p class="font-weight-bold">セクションを選択</p>
                <div id="section-selection">
                    <b-form-group>
                        <b-form-radio v-for="section in lesson_sections" v-model="lesson_section" v-bind:value="section.id">{{ section.name }}</b-form-radio>
                    </b-form-group>
                </div>
                <b-button block class="mt-3" variant="primary" v-b-modal.submit-question v-bind:disabled="!lesson_section">上記の選択したセクションで新規質問投稿</b-button>
            </b-col>
            <b-col cols="9">
                <b-input-group>
                    <b-form-input type="search" v-model="query" class="mr-2"></b-form-input>
                    <b-button variant="outline-success" @click="search">Search</b-button>
                </b-input-group>

                <div id="question-selection" class="mt-3">
                    <div v-for="question in lesson_questions" class="card mb-4 shadow-sm">
                        <div class="card-body">
                            <h5 class="card-title"><a href="#" v-b-modal.view-reply @click.prevent="CurrentQuestion = question">{{ question.title }}</a></h5>
                            <p class="card-text">{{ question.description }}</p>
                            <p class="card-text">回答数 : {{ question.answer_count }}</p>
                            <b-button block v-if="question.user_id === currentUser.pk" variant="success" @click="CurrentQuestion = question" v-b-modal.update-question>編集</b-button>
                            <b-button block variant="primary" @click="CurrentQuestion = question" v-b-modal.submit-reply>回答</b-button>
                        </div>
                    </div>
                </div>
            </b-col>
        </b-row>

        <b-modal id="submit-question" ref="submitQuestionModal" title="質問を投稿"
                 @show="resetSubmitQuestionModal" @hidden="resetSubmitQuestionModal" @ok="handleSubmitQuestionOk" @hide="reloadQuestion">
            <form ref="submitQuestionForm" @submit.stop.prevent="handleSubmitQuestion">
                <b-form-group label="タイトル" label-for="title" invalid-feedback="タイトルは必須です">
                    <b-form-input id="title" v-model="title" required></b-form-input>
                </b-form-group>

                <b-form-group label="タグ" label-for="tags">
                    <b-form-input id="tags" v-model="tags"></b-form-input>
                </b-form-group>

                <b-form-group label="質問内容" label-for="description" invalid-feedback="質問内容は必須です">
                    <b-form-textarea id="description" v-model="description" required></b-form-textarea>
                </b-form-group>
            </form>
        </b-modal>

        <b-modal id="update-question" ref="updateQuestionModal" title="質問を編集"
                 @show="resetUpdateQuestionModal" @hidden="resetUpdateQuestionModal" @ok="handleUpdateQuestionOk" @hide="reloadQuestion">
            <form ref="updateQuestionForm" @submit.stop.prevent="handleUpdateQuestion">
                <b-form-group label="タイトル" label-for="title" invalid-feedback="タイトルは必須です">
                    <b-form-input id="title" v-model="title" v-bind:disabled="CurrentQuestion['answer_count'] !== 0" required></b-form-input>
                </b-form-group>

                <b-form-group label="タグ" label-for="tags">
                    <b-form-input id="tags" v-model="tags" v-bind:disabled="CurrentQuestion['answer_count'] !== 0"></b-form-input>
                </b-form-group>

                <b-form-group label="質問内容" label-for="description" invalid-feedback="質問内容は必須です">
                    <b-form-textarea v-bind:disabled="CurrentQuestion['answer_count'] !== 0" id="description" v-model="description" required></b-form-textarea>
                </b-form-group>

                <b-form-group v-if="CurrentQuestion['answer_count'] !== 0" label="追記内容" label-for="description" invalid-feedback="質問内容は必須です">
                    <b-form-textarea id="description" v-model="additional_description" required></b-form-textarea>
                </b-form-group>
            </form>
        </b-modal>


        <b-modal id="view-reply" ref="viewReplyModal" title="返信を閲覧"
                 @show="resetViewReplyModal" @hidden="resetViewReplyModal">
            <h3>質問内容 : {{ CurrentQuestion.title }}</h3>
            <h3 v-if="CurrentQuestion.answer_count !== 0">追記内容 : {{ CurrentQuestion.additional_description}}</h3>
            <template v-if="CurrentQuestion.answer_count === 0">
                <hr>
                返信はありません
            </template>
            <template v-else>
                <hr>
                <ul>
                    <li v-for="answer in question_answers">
                        <h5 class="text-warning" v-if="currentUser.pk===answer.user_id">{{ answer.content }}</h5>
                        <h5 v-else>{{ answer.content }}</h5>
                    </li>
                </ul>
            </template>
        </b-modal>

        <b-modal id="submit-reply" ref="submitReplyModal" title="返信を行う"
                 @show="resetSubmitReplyModal" @hidden="resetSubmitReplyModal" @ok="handleSubmitReplyOk" @hide="reloadQuestion">
            <form ref="submitReplyForm" @submit.stop.prevent="handleSubmitReply">
                <b-form-group label="質問内容" label-for="content" invalid-feedback="質問内容は必須です">
                    <b-form-textarea id="content" v-model="content" required></b-form-textarea>
                </b-form-group>
            </form>
        </b-modal>


    </div>

</template>

<script>
    import { mapGetters } from "vuex";
    import {
        FETCH_LESSON_SECTIONS,
        FETCH_LESSON_QUESTIONS,
        CREATE_LESSON_QUESTIONS,
        UPDATE_LESSON_QUESTION,
        FETCH_QUESTION_ANSWERS,
        CREATE_QUESTION_ANSWER,
        FETCH_LESSON_SEARCH_QUESTIONS
    } from "@/store/actions.type";

    export default {
        name: "QandA",
        props: {
            lesson_id: {
                type: Number,
                required: true
            }
        },
        data () {
            return {
                lesson_section: null,
                title: "",
                tags: "",
                description: "",
                additional_description: "",
                CurrentQuestion: {
                    answer_count: 0
                },
                content: "",
                query: ""
            }
        },
        mounted() {
            this.$store.dispatch(FETCH_LESSON_SECTIONS, this.lesson_id);
            this.$store.dispatch(FETCH_LESSON_QUESTIONS, this.lesson_id);
        },
        methods: {
            search() {
                this.$store.dispatch(FETCH_LESSON_SEARCH_QUESTIONS, this.query);
            },
            // SubmitQuestion
            checkSubmitFormValidity() {
                return  this.$refs.submitQuestionForm.checkValidity();
            },
            resetSubmitQuestionModal() {
                this.title = "";
                this.tags = "";
                this.description = "";
            },
            handleSubmitQuestionOk(bvModalEvt) {
                bvModalEvt.preventDefault();
                this.handleSubmitQuestion();
            },
            handleSubmitQuestion() {
                if (!this.checkSubmitFormValidity()) {
                    return
                }

                let question = {
                    "title": this.title,
                    "description": this.description,
                    "section_id": this.lesson_section,
                    "tags" : []
                };

                let tag_list = this.tags.split(',');
                if(tag_list.length === 1 && tag_list[0] === "") {
                    delete question["tags"];
                }else {
                    for(let tag of tag_list){
                        question["tags"].push({
                            "name" : tag
                        })
                    }
                }

                this.$store.dispatch(CREATE_LESSON_QUESTIONS, question);

                this.$nextTick(() => {
                    this.$refs.submitQuestionModal.hide()
                })
            },
            reloadQuestion() {
                this.$store.dispatch(FETCH_LESSON_QUESTIONS, this.lesson_id);
            },

            // UpdateQuestion
            checkUpdateFormValidity() {
                return  this.$refs.updateQuestionForm.checkValidity();
            },
            resetUpdateQuestionModal() {
                let tag_str = "";
                for( let tag of this.CurrentQuestion.tags){
                    tag_str =  tag.name + "," + tag_str
                }

                this.title = this.CurrentQuestion.title;
                this.tags = tag_str.slice( 0, -1 ) ;
                this.description = this.CurrentQuestion.description;
                this.additional_description = this.CurrentQuestion.additional_description;
            },
            handleUpdateQuestionOk(bvModalEvt) {
                bvModalEvt.preventDefault();
                this.handleUpdateQuestion();
            },
            handleUpdateQuestion() {
                if (!this.checkUpdateFormValidity()) {
                    return
                }

                let question = {
                    "title": this.title,
                    "description": this.description,
                    "additional_description": this.additional_description,
                    "tags" : []
                };

                let tag_list = this.tags.split(',');
                if(tag_list.length === 1 && tag_list[0] === "") {
                    delete question["tags"];
                }else {
                    for(let tag of tag_list){
                        question["tags"].push({
                            "name" : tag
                        })
                    }
                }

                this.$store.dispatch(UPDATE_LESSON_QUESTION, {
                    "id": this.CurrentQuestion.id,
                    "question": question
                });

                this.$nextTick(() => {
                    this.$refs.updateQuestionModal.hide()
                })
            },

            // ViewReply
            resetViewReplyModal() {
                this.$store.dispatch(FETCH_QUESTION_ANSWERS, this.CurrentQuestion.id);
            },

            // SubmitReply
            checkSubmitReplyFormValidity() {
                return  this.$refs.submitReplyForm.checkValidity();
            },
            resetSubmitReplyModal() {
                this.content = "";
            },
            handleSubmitReplyOk(bvModalEvt) {
                bvModalEvt.preventDefault();
                this.handleSubmitReply();
            },
            handleSubmitReply() {
                if (!this.checkSubmitReplyFormValidity()) {
                    return
                }

                let answer = {
                    "content": this.content,
                    "question_id": this.CurrentQuestion.id
                };

                this.$store.dispatch(CREATE_QUESTION_ANSWER, answer);

                this.$nextTick(() => {
                    this.$refs.submitReplyModal.hide()
                })
            }
        },
        computed: {
            ...mapGetters(["lesson_sections", "lesson_questions", "currentUser", "question_answers"])
        }
    }
</script>

<style scoped lang="scss">
    #section-selection{
        height: 200px;
        overflow: auto;
    }

    #question-selection{
        height: 380px;
        overflow: auto;
    }
</style>