
Vue.createApp({
    data() {
        return {
            message: 'class hedgehog',
            todoText: '',
            todoList: [],
    }},
    // creating function based on user input such as button. Use data. or this. to access data in function
    methods: {
        surprise: function(){
            alert(this.message)
        },
        addTodo: function(){
            this.todoList.push(this.todoText);
            this.todoText = '';
        },
        removeTodo: function(todo){
            const index = this.todoList.indexOf(todo)
            this.todoList.splice(index, 1);
        }

    }

}).mount('#app')