<script setup lang='ts'>
</script>

<template>
    <div class="p-4 bg-[#5B6E5B] flex flex-col">
        <h1 class="text-3xl">Quick Guide</h1>
        <div class="pt-3 pb-3">
            Clicking on the task name will open a detailed view of the task. <br>
            You can accept the task from there by clicking "Accept Task".
            <hr>
            The coloured icons beside the task name indicate the status of the task. <br>
            <span class="red-text">Red</span> means the task has not been accepted by anyone. <br>
            <span class="yellow-text">Yellow</span> means the task is in progress. <br>
            <span class="pink-text">Pink</span> means the task has been completed!
        </div>
        <hr>
    </div>
</template>

<style scoped>
    .red-text {
        color: #fb4934;
    }

    .pink-text {
        color: #bfa4ab;
    }

    .yellow-text {
        color: #fabd2f;
    }
</style>