<script setup lang='ts'>
</script>

<template>
     <div class="flex flex-col h-screen w-full bg-image justify-center align-middle">
        <h1 class="text-2xl">Sending data</h1>
        <svg class="spinner" width="65px" height="65px" viewBox="0 0 66 66" xmlns="http://www.w3.org/2000/svg">
   <circle class="path" fill="none" stroke-width="6" stroke-linecap="round" cx="33" cy="33" r="30"></circle>
</svg>

     </div>
</template>

<style scoped>
    .bg-image {
        background-image: url('~/assets/images/background.png');
        background-repeat: right;
        background-size: 50%;
    }
</style>
