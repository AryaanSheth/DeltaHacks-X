
<script setup lang='ts'>
const isAdmin = true;
const isOpen = ref(false)
</script>

<template>
    <div class="flex flex-col p-3 h-fit bg-[#5B6E5B] rounded-lg">
        <TaskCard taskName="name1" taskDescription="taskDescription1" :urgency="2" :compatibility="0.80"/>
        <TaskCard taskName="name3" taskDescription="taskDescription3" :urgency="1" :compatibility="0.75"/>
        <TaskCard taskName="name2" taskDescription="taskDescription2" :urgency="1" :compatibility="0.5"/>
        <TaskCard taskName="name4" taskDescription="taskDescription4" :urgency="1" :compatibility="0.1"/>

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