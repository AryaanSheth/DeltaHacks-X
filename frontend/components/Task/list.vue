
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
            <button class="add-task-button rounded-lg text-center py-3 px-20 mt-5 mb-2 bg-[#485B49] text-[#F1F1E9]" @click="isOpen = true"> Add Task </button>
            <UModal v-model="isOpen">
                <div class="p-4 bg-[#5B6E5B]">
                    <h1 class="text-3xl text-[#F1F1E9]">Task Name</h1>
                    <div class="pt-3 pb-3 text-[#F1F1E9]">
                        DETAILED DESCRIPTION Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
                        sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad 
                        minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo 
                        consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu 
                        fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui 
                        officia deserunt mollit anim id est laborum.
                    </div>
                    <hr>
                    <div>
                        
                    </div>
                </div>
            </UModal>
        </div>
    </div>
</template>

<style scoped>
    .add-task-button:hover {
        background-color: #3f4f40;
    }
</style>