function boxOver(box) {
  box.innerHTML = "You really just do what anyone tells you to do?";
  box.style.color = "cyan";
}

function boxOff(box) {
  box.innerHTML = "Hey, mouse over me again though";
  box.style.color = "black";
  console.log("Again!");
}
