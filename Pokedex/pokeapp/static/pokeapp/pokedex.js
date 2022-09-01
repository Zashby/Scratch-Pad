const app = Vue.createApp({
    // get around conflict with Jinja/Django/JavaScript delimiters conflicting
        delimiters: ['--','--'],
    data(){
        return{
            test : 'test success',
            pokemon : [],
            pokeSearch: null,
            csrfToken : document.getElementsByName('csrfmiddlewaretoken')
            
            
        }
    },
    methods: {
        searchPokemon: function(){
            fetch(`/api/pokesearch/${this.pokeSearch}`).then(res => res.json()).then(data=> {
                this.pokemon = data;
            })

                }
    },
    watch: function(pokemon){
        this.$forceUpdate();
    },

    created: function(){
        fetch('/api/pokemonlist')
        .then(res => res.json())
        .then(data => {this.pokemon = data})
        
    }, 
    mounted: function(){
            if( this.csrfToken){
                console.log(this.csrfToken)
            } else{
                console.log('no token')
            }
        }
}).mount('#app')