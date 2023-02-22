import "./styles.css";

//  # Todo
let newTodo = document.querySelector("#new-todo");
let createTodoBtn = document.querySelector("#create-todo-btn");

let toDoList = [];

let toDoneList = [];

function enumerateToDoList() {
  document.querySelector(".todo-list").innerHTML = "";
  for (let i = 0; i < toDoList.length; i++) {
    let p = document.createElement("p");
    p.innerText = toDoList[i];
    let cBtn = document.createElement("button");
    cBtn.innerText = "Complete";
    let dBtn = document.createElement("button");
    dBtn.innerText = "Delete";
    p.append(cBtn, dBtn);
    document.querySelector(".todo-list").appendChild(p);
    cBtn.onclick = () => completeTodo(i, toDoList);
    dBtn.onclick = () => deleteTodo(i, toDoList);
  }
}

function enumerateToDoneList() {
  document.querySelector(".completed").innerHTML = "";
  for (let i = 0; i < toDoneList.length; i++) {
    let p = document.createElement("p");
    p.innerText = toDoneList[i];
    let cBtn = document.createElement("button");
    cBtn.innerText = "Mark incomplete";
    let dBtn = document.createElement("button");
    dBtn.innerText = "Delete";
    document.querySelector(".completed").appendChild(p);
    p.append(cBtn, dBtn);
    cBtn.onclick = () => completeTodo(i, toDoneList);
    dBtn.onclick = () => deleteTodo(i, toDoneList);
  }
}

function completeTodo(i, list) {
  let completedTodoArray = list.splice(i, 1);
  let completedTodo = completedTodoArray[0];
  if (list == toDoList) {
    toDoneList.push(completedTodo);
  } else if (list == toDoneList){
    toDoList.push(completedTodo);
  }
  enumerateToDoList();
  enumerateToDoneList();
}

function deleteTodo(i, list) {
  list.splice(i, 1);
  enumerateToDoList();
  enumerateToDoneList();
}

// Let's make a todo-list with the following features:
createTodoBtn.addEventListener("click", function createTodo() {
  let input = newTodo.value;
  toDoList.push(input);
  console.log(toDoList);
  enumerateToDoList();
  enumerateToDoneList();
  newTodo.value = "";
});