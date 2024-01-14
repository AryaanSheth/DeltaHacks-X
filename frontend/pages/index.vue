<script setup lang='ts'>
const isAdmin = true;
</script>

<template>
    <div class="flex flex-col h-screen w-full">
        <AppHeader />
        <div class="flex">
            <SideBar />
            <div class="flex flex-col w-full p-5">
                <div class="flex w-full justify-between pb-5">
                    <h1 class="text-3xl text-center text-[#F1F1E9]">PROJECT NAME</h1>
                    <button class="invite-button rounded-lg text-center py-3 px-10 bg-[#485B49]" v-if="isAdmin">Invite Members</button>
                </div>
                <TaskList />
            </div>
        </div>
    </div>
</template>

<style scoped>
    .invite-button:hover {
        background-color: #3f4f40;
    }
</style>