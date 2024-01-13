<script setup lang='ts'>
const isAdmin = true;
</script>

<template>
    <div class="flex flex-col h-screen w-full bg-[#3D3F36] text-white">
        <AppHeader />
        <div class="flex">
            <SideBar />
            <div class="flex flex-col w-full p-5">
                <div class="flex w-full justify-between pb-5">
                    <h1 class="text-3xl text-center">PROJECT NAME</h1>
                    <button class="border rounded-lg text-center py-3 px-10" v-if="isAdmin">Invite Members</button>
                </div>
                <TaskList />
            </div>
        </div>
    </div>
</template>

<style scoped></style>