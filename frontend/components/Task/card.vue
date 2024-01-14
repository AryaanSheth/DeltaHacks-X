<script setup lang='ts'>
</script>

<template>
    <div class="flex justify-between bg-[#778F77] my-2 px-3 py-1 rounded-md text-black">
        <Icon name="ph:circle-fill" color="#fb4934" class="text-2x1"/>  <!-- This changes colour based on the status of task-->
        <div class="flex-col ml-5">
            <h1 class="task-name font-bold text-2xl text-[#182017]">Task Name</h1>
            <h2 class="pl-5 text-[#182017]">Urgency: High</h2>
            <h2 class="pl-5 text-[#182017]">Compatibility: 50%</h2>
        </div>
        <Icon name="ph:dots-three-outline-fill" color="black" class="elipses text-2xl"/>
    </div>
</template>

<style scoped>
    .task-name {
        position: relative;
        display: inline-block;
        cursor: pointer;
    }

    .task-name::after {
        content: '';
        position: absolute;
        width: 0;
        height: 2px;
        bottom: 0;
        left: 50%;
        background: #000;
        transition: all 0.5s;
        transform: translateX(-50%);
    }

    .task-name:hover::after {
        width: 100%;
    }

    .elipses:hover {
        cursor: pointer;
    }
</style>