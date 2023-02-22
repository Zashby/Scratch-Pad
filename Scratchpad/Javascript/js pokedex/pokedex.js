const app = Vue.createApp({
    // get around conflict with Jinja/Django/JavaScript delimiters conflicting
        delimiters: ['--','--'],
    data(){
        return{
            test : 'test success',
            pokemon : [],
            pokeSearch: null,

            pokemonDisplay: []
            
            
        }
    },
    methods: {
        searchPokemon: function(){
            fetch(`/api/pokesearch/${this.pokeSearch}`).then(res => res.json()).then(data=> {
                this.pokemonDisplay = data;
            })

        },
        pokePage : function(x){
            let check = Number(x.target.value);

            if(check === 1){
                this.pokemonDisplay= this.pokemon.slice(0,25);
            } else{
                this.pokemonDisplay = this.pokemon.slice(25*check,25*(check+1))
            }

            
            }
            
        
    },
    

    created: function(){
        fetch('https://pokeapi.co/api/v2/pokemon?limit=151&offset=0')
        .then(res => res.json())
        .then(data => {this.pokemonDisplay = data.results})
        
        
    }, 
    mounted: function(){
        
        },
    watch: function(pokemon){
            this.$forceUpdate();
        }
}).mount('#app')