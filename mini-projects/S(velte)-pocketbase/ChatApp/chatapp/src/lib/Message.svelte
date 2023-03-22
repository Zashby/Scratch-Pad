<script lang='ts'>
    import { onMount, onDestroy } from 'svelte';
    import { currentUser, pb } from './pocketbase'

    let messages = [];


    onMount(async() => {
        const resultList = await pb.collection('messages').getList(1,50, {
            sort :'created',
            ttexpand:'user',
            })
    })


</script>