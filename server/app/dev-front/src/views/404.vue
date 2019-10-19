<template>
    <div id="notFound" class="container d-flex justify-content-center align-items-center">
        <h1 class="mr-3 pr-3 align-top border-right inline-block align-content-center">404</h1>
        <div class="inline-block align-middle">
            <h2 class="font-weight-normal lead">お探しのページは見つかりませんでした.</h2>
        </div>
    </div>
</template>

<script>
    export default {
        name: "404.vue"
    }
</script>

<style scoped lang="scss">
  #notFound{
    height: calc(100vh - 56px);
  }
</style>
