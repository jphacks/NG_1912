(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-488a6c3a"],{"0165":function(t,e,a){},"73cf":function(t,e,a){"use strict";a.r(e);var s=function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("div",{staticClass:"main d-flex align-items-center user-form"},[a("div",{staticClass:"container"},[a("div",{staticClass:"card"},[a("div",{staticClass:"card-body  d-flex align-items-center "},[a("form",{staticClass:"form",on:{submit:function(e){return e.preventDefault(),t.onSubmit(e)}}},[a("h3",{staticClass:"text-center text-info"},[t._v("ユーザー登録")]),a("div",{staticClass:"form-group"},[a("label",{staticClass:"text-info",attrs:{for:"username"}},[t._v("ユーザー名")]),a("input",{directives:[{name:"model",rawName:"v-model",value:t.username,expression:"username"}],staticClass:"form-control",attrs:{type:"text",id:"username",placeholder:"ユーザー名",required:""},domProps:{value:t.username},on:{input:function(e){e.target.composing||(t.username=e.target.value)}}})]),a("div",{staticClass:"form-group"},[a("label",{staticClass:"text-info",attrs:{for:"email"}},[t._v("Email")]),a("input",{directives:[{name:"model",rawName:"v-model",value:t.email,expression:"email"}],staticClass:"form-control",attrs:{type:"email",id:"email",placeholder:"Email",required:""},domProps:{value:t.email},on:{input:function(e){e.target.composing||(t.email=e.target.value)}}})]),a("div",{staticClass:"form-group"},[a("label",{staticClass:"text-info",attrs:{for:"first_name"}},[t._v("姓")]),a("input",{directives:[{name:"model",rawName:"v-model",value:t.first_name,expression:"first_name"}],staticClass:"form-control",attrs:{type:"text",id:"first_name",placeholder:"姓",required:""},domProps:{value:t.first_name},on:{input:function(e){e.target.composing||(t.first_name=e.target.value)}}})]),a("div",{staticClass:"form-group"},[a("label",{staticClass:"text-info",attrs:{for:"last_name"}},[t._v("名")]),a("input",{directives:[{name:"model",rawName:"v-model",value:t.last_name,expression:"last_name"}],staticClass:"form-control",attrs:{type:"text",id:"last_name",placeholder:"名",required:""},domProps:{value:t.last_name},on:{input:function(e){e.target.composing||(t.last_name=e.target.value)}}})]),a("div",{staticClass:"form-group"},[a("label",{staticClass:"text-info",attrs:{for:"password1"}},[t._v("パスワード")]),a("input",{directives:[{name:"model",rawName:"v-model",value:t.password1,expression:"password1"}],staticClass:"form-control",attrs:{type:"password",id:"password1",placeholder:"パスワード",required:""},domProps:{value:t.password1},on:{input:function(e){e.target.composing||(t.password1=e.target.value)}}})]),a("div",{staticClass:"form-group"},[a("label",{staticClass:"text-info",attrs:{for:"password2"}},[t._v("パスワード確認")]),a("input",{directives:[{name:"model",rawName:"v-model",value:t.password2,expression:"password2"}],staticClass:"form-control",attrs:{type:"password",id:"password2",placeholder:"パスワード確認",required:""},domProps:{value:t.password2},on:{input:function(e){e.target.composing||(t.password2=e.target.value)}}})]),a("div",{staticClass:"form-group"},[a("label",{staticClass:"text-info"},[t._v("顔画像登録")]),10!==t.images.length?a("b-button",{directives:[{name:"b-modal",rawName:"v-b-modal.captureFacesModal",modifiers:{captureFacesModal:!0}}],staticClass:"ml-3",attrs:{variant:"info"},on:{click:t.captureFace}},[t._v("登録する")]):a("b-button",{directives:[{name:"b-modal",rawName:"v-b-modal.captureFacesModal",modifiers:{captureFacesModal:!0}}],staticClass:"ml-3",attrs:{variant:"info"},on:{click:t.captureFace}},[t._v("再登録する")])],1),a("button",{staticClass:"btn btn-info"},[t._v("登録する")]),a("hr"),a("router-link",{attrs:{to:{name:"login"}}},[t._v("ログインする")])],1)])])]),a("b-modal",{ref:"captureFacesModal",attrs:{id:"captureFacesModal","ok-title":"撮影",title:"撮影する"},on:{shown:t.captureVideos,ok:t.captureFace,hide:t.stopVideos}},[a("video",{staticClass:"w-100",attrs:{id:"captureVideo"}}),a("canvas",{staticClass:"w-100",staticStyle:{display:"none"},attrs:{id:"captureImg"}})])],1)},r=[],i=(a("8e6e"),a("456d"),a("ac6a"),a("bd86")),o=a("2f62"),n=a("6c33");function c(t,e){var a=Object.keys(t);if(Object.getOwnPropertySymbols){var s=Object.getOwnPropertySymbols(t);e&&(s=s.filter((function(e){return Object.getOwnPropertyDescriptor(t,e).enumerable}))),a.push.apply(a,s)}return a}function l(t){for(var e=1;e<arguments.length;e++){var a=null!=arguments[e]?arguments[e]:{};e%2?c(a,!0).forEach((function(e){Object(i["a"])(t,e,a[e])})):Object.getOwnPropertyDescriptors?Object.defineProperties(t,Object.getOwnPropertyDescriptors(a)):c(a).forEach((function(e){Object.defineProperty(t,e,Object.getOwnPropertyDescriptor(a,e))}))}return t}var d={name:"Register",data:function(){return{username:"",email:"",password1:"",password2:"",first_name:"",last_name:"",images:[]}},computed:l({},Object(o["c"])({errors:function(t){return t.auth.errors}})),methods:{onSubmit:function(){var t=this;this.$store.dispatch(n["f"],{username:this.username,email:this.email,password1:this.password1,password2:this.password2,first_name:this.first_name,last_name:this.last_name,images:this.images}).then((function(){return t.$router.push({name:"root"})}))},captureVideos:function(){var t=document.getElementById("captureVideo"),e={video:!0};navigator.mediaDevices.getUserMedia(e).then((function(e){t.srcObject=e,t.play()})).catch((function(t){console.log("[JPHacks KMF] "+t)}))},stopVideos:function(t){if("ok"!==t.trigger){var e=document.getElementById("captureVideo"),a=e.srcObject;a.getTracks().forEach((function(t){t.stop()}))}},captureFace:function(t){var e=this;t.preventDefault(),10===this.images.length&&(this.images=[]);var a=document.getElementById("captureVideo"),s=document.getElementById("captureImg");s.setAttribute("width",a.videoWidth),s.setAttribute("height",a.videoHeight),s.getContext("2d").drawImage(a,0,0,a.videoWidth,a.videoHeight);var r=s.toDataURL("image/jpeg");this.images.push(r),this.$nextTick((function(){10===e.images.length&&e.$refs["captureFacesModal"].hide()}))}}},m=d,u=(a("aa5e"),a("2877")),p=Object(u["a"])(m,s,r,!1,null,"931e897a",null);e["default"]=p.exports},aa5e:function(t,e,a){"use strict";var s=a("0165"),r=a.n(s);r.a}}]);
//# sourceMappingURL=chunk-488a6c3a.9a1bd2de.js.map