<script setup lang="ts">
import type { FormError, FormSubmitEvent } from '#ui/types'

const state = reactive({
    name: undefined,
    email: undefined
})

const validate = (state: any): FormError[] => {
    const errors = []
    if (!state.name) errors.push({ path: 'name', message: 'Required' })
    if (!state.email) errors.push({ path: 'email', message: 'Required' })
    return errors
}

async function onSubmit(event: FormSubmitEvent<any>) {
    console.log(event.data)
}
</script>

<template>
    <div class="flex flex-col h-screen w-full bg-image">
        <AppHeader />

        <UForm :validate="validate" :state="state" class="space-y-4 w-1/2 self-center bg-[#5B6E5B] rounded-xl px-10 py-10 mt-5" @submit="onSubmit">
            <h1 class="text-center text-2xl text-[#F1F1E9]">You are invited to join "Project Name"</h1>

            <div class="mb-5">
                <label for="name" class="block mb-2 text-md font-medium text-gray-900 dark:text-white">Name</label>
                <input type="name" id="name"
                    class="bg-[#5B6E5B] border border-gray-300 text-white text-sm rounded-lg block w-full p-2.5"
                    placeholder="" required>
            </div>
            <div class="mb-5">
                <label for="email" class="block mb-2 text-md font-medium text-white dark:text-white">Email</label>
                <input type="email" id="email"
                    class="bg-[#5B6E5B] border border-gray-300 text-white text-sm rounded-lg block w-full p-2.5"
                    required>
            </div>

            <h1 class="text-md ">Resume</h1>

            <div class="flex items-center justify-center w-full">
                <label for="dropzone-file"
                    class="flex flex-col items-center justify-center w-full h-64 border-2 border-gray-300 border-dashed rounded-lg cursor-pointer">
                    <div class="flex flex-col items-center justify-center pt-5 pb-6">
                        <svg class="w-8 h-8 mb-4 text-slate-50" aria-hidden="true"
                            xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 20 16">
                            <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                d="M13 13h3a3 3 0 0 0 0-6h-.025A5.56 5.56 0 0 0 16 6.5 5.5 5.5 0 0 0 5.207 5.021C5.137 5.017 5.071 5 5 5a4 4 0 0 0 0 8h2.167M10 15V6m0 0L8 8m2-2 2 2" />
                        </svg>
                        <p class="mb-2 text-sm text-slate-50"><span class="font-semibold">Click to
                                upload</span> or drag and drop</p>
                        <p class="text-xs text-slate-60">PDF (MAX. 4MB)</p>
                    </div>
                    <input id="dropzone-file" type="file" class="hidden" />
                </label>
            </div>

            <button
                class="invite-button rounded-lg text-center py-3 px-10 bg-[#485B49] text-[#F1F1E9] hover:border-none self-center"
                type="submit">Submit</button>
        </UForm>
</div></template>

<style scoped>
    .invite-button:hover {
        background-color: #3f4f40;
    }

    .bg-image {
        background-image: url('~/assets/images/background.png');
        background-repeat: right;
        background-size: 50%;
    }
</style>
