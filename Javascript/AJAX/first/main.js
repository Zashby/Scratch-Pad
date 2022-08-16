let todosContainer = document.querySelector('#todos')
// Old school - loss of .catch() function
// fetch('https://jsonplaceholder.typicode.com/todos/')
// .then(
//     function(response){
//         return response.json();
//     }
// ).then( (data)=>showTodos(data)
// ).catch()
async function getData(){
    
    const response = await fetch('https://jsonplaceholder.typicode.com/todos');
    const data = await response.json();

    showTodos(data);
}
// Be sure to call the async function
getData()

function showTodos(data){ for(todo of data){
    const p = document.createElement('p');
    p.textContent = todo.title;
    todosContainer.appendChild(p);}}

//new school 


console.log("hello There")