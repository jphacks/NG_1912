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

                        <div class="form-group">
                            <label class="text-info">顔画像登録</label>
                            <b-button v-b-modal.captureFacesModal class="ml-3" @click="captureFace" v-if="images.length !== 10" variant="info">登録する</b-button>
                            <b-button v-b-modal.captureFacesModal class="ml-3" @click="captureFace" v-else variant="info">再登録する</b-button>
                        </div>

                        <button class="btn btn-info">登録する</button>

                        <hr>
                        <router-link :to="{ name: 'login'}">ログインする</router-link>
                    </form>
                </div>
            </div>
        </div>

        <b-modal id="captureFacesModal"
                 ref="captureFacesModal"
                 @shown="captureVideos"
                 @ok="captureFace"
                 ok-title="撮影"
                 @hide="stopVideos"
                 title="撮影する">
            <video id="captureVideo" class="w-100"></video>
            <canvas id="captureImg" class="w-100" style="display: none"></canvas>
        </b-modal>

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
                last_name: "",
                images: []
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
                        images: this.images,
                    })
                    .then(() => this.$router.push({name: "root"}))
            },
            captureVideos() {
                let video = document.getElementById('captureVideo');
                let constrains = { video: true };
                navigator.mediaDevices.getUserMedia(constrains)
                    .then(function(stream) {
                        video.srcObject = stream; // streamはユーザーのカメラとマイクの情報で、これをvideoの入力ソースにする
                        video.play();
                    })
                    .catch(function(err) {
                        console.log("[JPHacks KMF] " + err)
                    });
            },
            stopVideos(trigger) {
                if(trigger.trigger !== 'ok'){
                    let video = document.getElementById('captureVideo');
                    let stream = video.srcObject;

                    stream.getTracks().forEach(function(track) {
                        track.stop();
                    });
                }
            },
            captureFace(bvModalEvt) {
                bvModalEvt.preventDefault();

                if (this.images.length === 10){
                    this.images = []
                }

                let video = document.getElementById('captureVideo');
                let canvas = document.getElementById("captureImg");
                canvas.setAttribute('width', video.videoWidth);
                canvas.setAttribute('height', video.videoHeight);

                canvas.getContext("2d").drawImage(video, 0, 0, video.videoWidth, video.videoHeight);
                let dataURI = canvas.toDataURL("image/jpeg");
                this.images.push(dataURI);

                this.$nextTick(() => {
                    if (this.images.length === 10){
                        this.$refs['captureFacesModal'].hide();
                    }
                });
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
