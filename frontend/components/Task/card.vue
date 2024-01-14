<script setup lang='ts'>
const props = defineProps<{
    taskName: string
    taskDescription: string
    urgency: number // 1, 2, 3
    compatibility: number // number bw 0-1
}>()

const getComputedUrgency = computed(() => {
    if (props.urgency === 1) {
        return "High"
    } else if (props.urgency === 2) {
        return "Medium"
    } else {
        return "Low"
    }
})

const getComputedCompatibility = computed(() => {
    return (props.compatibility * 100)
})


const isOpen = ref(false)
</script>

<template>
    <div class="flex justify-between bg-[#778F77] my-2 px-3 py-1 rounded-md text-black">
        <div class="flex">
            <Icon name="ph:circle-fill" color="#fb4934" class="text-2x1 mt-2" />
            <!-- This changes colour based on the status of task-->
            <div class="flex-col ml-5">
                <h1 class="cursor-pointer font-bold text-2xl text-[#182017] task-name" @click="isOpen = true">{{ taskName }}
                </h1>
                <h2 class="pl-5 text-[#182017]">Urgency: {{ getComputedUrgency }}</h2>
                <h2 class="pl-5 text-[#182017]">Compatibility: {{ getComputedCompatibility }}%</h2>
            </div>
        </div>
        <Icon name="ph:dots-three-outline-fill" color="black" class="elipses text-2xl" />
    </div>

    <UModal v-model="isOpen">
        <TaskDetailedView :taskName="taskName" :taskDescription="taskDescription" :urgency="urgency" :compatibility="compatibility"/>
    </UModal>
</template>

<style scoped>
.elipses:hover {
    cursor: pointer;
}

.task-name:hover {
    text-decoration: underline;
}
</style>