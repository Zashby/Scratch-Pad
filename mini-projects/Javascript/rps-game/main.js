// let rockBtn = document.querySelector('.rock');
// let paperBtn = document.querySelector('.paper');
// let scissorsBtn = document.querySelector('.scissors');

// let gameLog = document.querySelector('#gamelog');

 function randomChoice(){
     let choice = ['rock', 'paper', 'scissors']
     let seed = Math.floor(Math.random() * 3)
     let compChoice = choice[seed]
     return compChoice
 }

// function playGame(){
//     let playerChoice = this.classList[1]
//     console.log(playerChoice)
//     let compChoice = randomChoice();
//     if( compChoice === playerChoice){console.log('draw')}

// }

// rockBtn.onclick = playGame

// paperBtn.onclick = playGame

// scissorsBtn.onclick = playGame
let gameLog = document.querySelector('#gamelog');
let buttons = document.querySelectorAll('.btn')
console.log(buttons)

buttons.forEach(
    function(button) {
        button.addEventListener('click', 
        function(){
            rps(button.classList[1])
    })
})

function rps(player){
    const choices = ['rock', 'paper', 'scissors']
    const computer = randomChoice()
    const playerChoice = choices.indexOf(player)
    const compChoice = choices.indexOf(computer)
    console.log(player)
    console.log(computer)
    let outcomeContainer = document.createElement('p')
        outcomeContainer.classList.add('result')
    if(playerChoice === compChoice){
        
        outcomeContainer.classList.add('tie')
        outcomeContainer.innerText = `Player played ${player}. Computer played ${computer}. Weee Ties`
        
        
    } else if(choices[(playerChoice+1)%3] === choices[compChoice]) {
        
        outcomeContainer.classList.add('lose')
        outcomeContainer.innerText = `Player played ${player}. Computer played ${computer}. You Lose`
        
        
    } else{
    outcomeContainer.classList.add('win')
    outcomeContainer.innerText = `Player played ${player}. Computer played ${computer}. You win!`
    }

    gameLog.prepend(outcomeContainer)
}