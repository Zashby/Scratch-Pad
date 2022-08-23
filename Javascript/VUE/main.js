
Vue.createApp({
    data() {
        return {
            message: 'class hedgehog',
            todoText: '',
            todoList: [],
            nextId: 0,
        
    }},
    // creating function based on user input such as button. Use data. or this. to access data in function
    methods: {
        surprise: function(){
            alert(this.message)
        },
        addTodo: function(){
            this.todoList.push({
            text: this.todoText, 
            id: this.nextId,
            completed: false,
            });
            this.nextId +=1;
            this.todoText = '';
            this.saveToLocal();
        },
        removeTodo: function(id){
            // const index = todo.id
            // this.todoList.splice(index, 1);
            this.todoList = this.todoList.filter(todo => todo.id != id)
            this.saveToLocal();
        },
        completeTodo:function(id){
            this.todoList.forEach(todo =>{
                if(todo.id === id){
                    todo.completed = !todo.completed;
                }
            })
            this.saveToLocal();
        },
        saveToLocal:function(){
            const todoListString = JSON.stringify(this.todoList);
            console.log(todoListString);
            localStorage.setItem('todoItems', todoListString);
            localStorage.setItem('nextID', this.nextId)
        }

    },
    computed: {completedTodoList:function(){
        return this.todoList.filter(todo=> todo.completed ===true)
    },
    incompleteTodoList:function(){
        return this.todoList.filter(todo=> todo.completed ===false)
    }, percentComplete: function(){
        return this.completedTodoList.length / this.todoList.length *100
    }

    },
    created: function(){
        if(localStorage.getItem('todoItems')){
            this.todoList = JSON.parse(localStorage.getItem('todoItems'));
        } else{
            this.todoList = [];
        }
        if(localStorage.getItem('nextId')){
            this.nextId = Number(localStorage.getItem('nextId'));
        } else {
            this.nextId = 0;
        }
        console.log(this.todoList)
    },   

}).mount('#app')