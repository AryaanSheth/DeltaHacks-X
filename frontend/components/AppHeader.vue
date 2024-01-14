<script setup lang='ts'>
const isOpen = ref(false)
</script>

<template>
    <div class="w-full h-15 text-left border border-[#61554e] bg-[#665b53] flex justify-between items-center" style="opacity: 80%;">
        <div class="flex">
            <NuxtLink to="/">
                <img src="~/assets/images/tiger.png" width="40">
            </NuxtLink>
            <NuxtLink to="/">
                <img src="~/assets/images/taiket.png" width="80">
            </NuxtLink>
        </div>
        <div>
        <button class="elipses text-2xl" @click="isOpen = true">
            <Icon name="ph:question" color="#F1F1E9" />
        </button>
        <UModal v-model="isOpen">
                <TaskHelp/>
            </UModal>
        </div>
    </div>
</template>

<style scoped>
</style>