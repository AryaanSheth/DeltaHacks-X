
<script setup lang='ts'>
const isAdmin = true;
const isOpen = ref(false)
</script>

<template>
    <div class="flex flex-col p-3 h-fit bg-[#5B6E5B] rounded-lg">
        <TaskCard/>
        <TaskCard/>
        <TaskCard/>
        <TaskCard/>
        <div class="self-center" v-if="isAdmin">
            <button class="add-task-button rounded-lg text-center py-3 px-20 mt-5 mb-2 bg-[#485B49] text-[#F1F1E9]" @click="isOpen = true">Add Task</button>
            <UModal v-model="isOpen">
                <TaskDetailedView />
            </UModal>
        </div>
    </div>
</template>

<style scoped>
    .add-task-button:hover {
        background-color: #3f4f40;
    }
</style>