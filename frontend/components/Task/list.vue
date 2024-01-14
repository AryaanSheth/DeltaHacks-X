
<script setup lang='ts'>
const isAdmin = true;
const isOpen = ref(false)
</script>

<template>
    <div class="flex flex-col p-3 h-fit bg-[#5B6E5B] rounded-lg">
        <TaskCard taskName="Task Name1" taskDescription="taskDescription" :urgency="2" :compatibility="0.80"/>
        <TaskCard taskName="Task Name3" taskDescription="taskDescription" :urgency="1" :compatibility="0.75"/>
        <TaskCard taskName="Task Name2" taskDescription="taskDescription" :urgency="1" :compatibility="0.50"/>
        <TaskCard taskName="Task Name4" taskDescription="taskDescription" :urgency="1" :compatibility="0.5"/>

        <div class="self-center" v-if="isAdmin">
            <button class="add-task-button rounded-lg text-center py-3 px-20 mt-5 mb-2 bg-[#485B49] text-[#F1F1E9]" @click="isOpen = true">Add Task</button>
            <UModal v-model="isOpen">
                <!-- <TaskDetailedView /> -->
                <TaskAddModal/>
            </UModal>
        </div>
    </div>
</template>

<style scoped>
    .add-task-button:hover {
        background-color: #3f4f40;
    }
</style>