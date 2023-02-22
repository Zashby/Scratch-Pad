const newTodo = document.querySelector('#new-todo');
const createButton = document.querySelector('#create-new-todo');
const todoContainer = document.querySelector('#todo-container');
const completedContainer = document.querySelector('#completed-container');

function enumerateTodos(){
    for( let todo of todoContainer.children ){
        let span = document.createElement('span');
        deleteTodoButton(span);
        completeTodoButton(span);
        todo.appendChild(span);
    }
    for( let todo of completedContainer.children ){
        let span = document.createElement('span');
        deleteTodoButton(span);
        completeTodoButton(span);
        todo.appendChild(span);
    }
    
}

function deleteTodoButton(element){
    let deleteButton = document.createElement('button');
    deleteButton.innerHTML = 'Delete';
    element.appendChild(deleteButton); 
    deleteButton.onclick = function(){
        this.parentElement.parentElement.remove()
    }
    console.log(element)
}

function completeTodoButton(element){
    let completeButton = document.createElement('button');
    completeButton.innerHTML = 'Complete';
    completeButton.onclick = function(){
        let el = this.parentElement.parentElement
        el.classList.toggle('completed')
        if(el.parentElement == todoContainer){
            completedContainer.appendChild(el)
            completeButton.innerHTML = 'Incomplete'
        } else {todoContainer.appendChild(el)
        completeButton.innerHTML = 'complete'}
    }
    element.appendChild(completeButton); 

}

createButton.onclick= function(){
    if(!newTodo.value){
        alert('Please input a new todo');
    } else{
    let p = document.createElement('p');
    p.innerText = newTodo.value;
    todoContainer.appendChild(p);
    let span = document.createElement('span');
        deleteTodoButton(span);
        completeTodoButton(span);
        p.appendChild(span);
    newTodo.value = '';}
 }


enumerateTodos()