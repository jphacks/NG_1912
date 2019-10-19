<template>
    <b-row>
        <b-col cols="6">
            <editor v-model="editorContent" @init="editorInit" lang="python" theme="twilight" width="100%" height="450"></editor>
        <b-button block variant="primary" @click="submitCode">送信</b-button>
        </b-col>
        <b-col cols="6">
            <editor v-model="ResultContent" @init="editorInit" lang="python" theme="twilight" width="100%" height="450"></editor>
        </b-col>
    </b-row>
</template>


<style scoped lang="scss">

</style>

<script>
    export default {
        name: "Code",
        components: {
            editor: require('vue2-ace-editor'),
        },
        props: {
            lesson_id: {
                type: Number,
                required: true
            }
        },
        data() {
            return {
                editorContent: "",
                ResultContent: ""
            }
        },
        methods: {
            editorInit() {
                require('brace/ext/language_tools'); //language extension prerequsite...
                require('brace/mode/python');    //language
                require('brace/theme/twilight');
                require('brace/snippets/javascript');
            },
            submitCode() {
                console.log(this.editorContent);
            }
        }
    }
</script>
