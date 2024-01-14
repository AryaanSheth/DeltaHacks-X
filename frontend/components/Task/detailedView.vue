<script setup lang='ts'>
</script>

<template>
    <div class="p-4 bg-[#5B6E5B] flex flex-col">
        <h1 class="text-3xl">Task Name</h1>
        <div class="pt-3 pb-3">
            DETAILED DESCRIPTION Lorem ipsum dolor sit amet, consectetur adipiscing elit,
            sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad
            minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
            consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu
            fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui
            officia deserunt mollit anim id est laborum.
        </div>
        <hr>
        <button class="accept-button bg-[#485B49] rounded-lg text-center py-3 px-10 mt-6 self-end">Accept Task</button>
    </div>
</template>

<style scoped>
    .accept-button:hover {
        background-color: #3f4f40;
    }
</style>