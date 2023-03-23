<script lang='ts'>
    import { onMount, onDestroy } from 'svelte';
    import { currentUser, pb } from './pocketbase'

    let messages = [];
    let newMessage: string;
    let unsubscribe: () => void;

    onMount(async() => {
        const resultList = await pb.collection('messages').getList(1,50, {
            sort :'created',
            expand:'user',
            });
        
        messages=resultList.items; 

        unsubscribe = await 
        pb.collection('messages').subscribe('*', async ({action, record }) => {
            if (action == 'create'){
                    const user = await pb.collection('users').getOne(record.user)
                    record.expand = { user };
                    messages = [...messages, record];

            }
            if (action == 'delete'){
                messages = messages.filter((m) => m.id !== record.id);
            }
        });    
    
    
        });

    onDestroy(() => {
     unsubscribe?.();   
    })

    async function sendMessage(){
      const data ={
        user: $currentUser.id,
        message :newMessage
      };  
      const createdMessage = await pb.collection('messages').create(data);
      newMessage = "";
    };


</script>

<div class="messages">
    {#each messages as message(message.id) }
       <div class="msg">
            <img class='avatar' src="" alt="" width=40px>
        <div>
            <small>sent by @{message.expand?.user?.username}</small>
            <p class="msg-text">{message.message}</p>
        </div>
       </div> 
    {/each}
</div>

<form on:submit|preventDefault={sendMessage}>
    <input placeholder='Message' bind:value={newMessage} type="text">
    <button type='submit'>send</button>
</form>