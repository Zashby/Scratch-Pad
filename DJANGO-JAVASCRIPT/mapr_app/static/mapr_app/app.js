const app = Vue.createApp({
// get around conflict with Jinja/Django/JavaScript delimiters conflicting
    delimiters: ['--','--'],
    data() {
        return {
            message : "Hello from vue",
            groups : [],
            selectedGroup : null,
            locations : [],
            map : null,
            layerGroup : null,
            markers : null,
        }
    },
    methods: {
        fetchLocations:function(){
            fetch(`/api/groups/${this.selectedGroup}`)
            .then(res => res.json())
            .then(data => this.locations = data.data)

        },
        configMap: function(){ 
            L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
            attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
            }).addTo(this.map);
            this.layerGroup = L.layerGroup();
            this.layerGroup.addTo(this.map)},
    },
    watch: {
        locations: function(locations){
            this.layerGroup.clearLayers();
            for(let user of locations){
                this.layerGroup.addLayer(
                    L.marker([user.location__latitude, user.location__longitude]).bindPopup(user.username).openPopup()
                )
            }

        }
    },
    created: function(){
        fetch('/api/groups')
        .then(response => response.json())
        .then(data => {
            this.groups = data.data;
        })
    },
    mounted: function(){
        navigator.geolocation.getCurrentPosition(position => {
            this.map = L.map('map')
            .setView([position.coords.latitude, position.coords.longitude], 4);
            this.configMap()
        }, err => {
            this.map = L.map('map').setView([0,0], 4);
            this.configMap()
    }
        )
        
        
    }

}).mount('#app')


