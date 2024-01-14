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

</script>

<template>
    <div class="p-4 bg-[#5B6E5B] flex flex-col">
        <h1 class="text-3xl">{{taskName}}</h1>
        <div class="pt-3 pb-3">
            {{ taskDescription }}
        </div>
        <hr>
        <h2 class="pl-5">Urgency: {{ getComputedUrgency }}</h2>
        <h2 class="pl-5">Compatibility: {{ getComputedCompatibility }}%</h2>
        <button class="accept-button bg-[#485B49] rounded-lg text-center py-3 px-10 mt-6 self-end">Accept Task</button>
    </div>
</template>

<style scoped>
    .accept-button:hover {
        background-color: #3f4f40;
    }
</style>