<script lang="ts">
    import { enhance } from '$app/forms';
    import type { PageData } from './$types';
    
    export let data: PageData;
</script>

<h1>{data.boatName}</h1>

<form method="POST" use:enhance action="?/rename">

    <input type="text" name='boatName'>
    <button type="submit">submit</button>

    <button formaction="?/capitalize">capitalize</button>
</form>