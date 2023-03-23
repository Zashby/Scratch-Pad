<script lang="ts">
  import svelteLogo from './assets/svelte.svg';
  import Counter from './lib/Counter.svelte';
  import Login from './lib/Login.svelte';
  import Message from './lib/Message.svelte';
  import { currentUser } from './lib/pocketbase';
</script>

<h1>ChatApp</h1>

<Login />
{#if currentUser}

<Message/>

{/if}