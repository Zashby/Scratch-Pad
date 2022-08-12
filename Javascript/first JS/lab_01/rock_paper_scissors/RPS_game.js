const playerChoice = prompt("enter Rock, Paper, or Scissors: ").toLowerCase();


const computerArr = ['rock', 'paper', 'scissors']

const computerSeed = Math.floor(Math.random() * computerArr.length)

const computerChoice = computerArr[computerSeed]

alert(`Player played ${playerChoice} and computer played ${computerChoice}.`)

if( playerChoice == computerChoice){
    alert('Draw!')
} else if( playerChoice == 'rock') 
    if  (computerChoice == 'paper'){ alert('Computer Wins!')
        } else if(computerChoice == 'scissors'){ alert('Player wins!!')}

        if( playerChoice == 'paper') 
            if (computerChoice == 'scissors'){ alert('Computer wins!')} 
            else if (computerChoice == 'rock'){ alert('Player wins!')}

    if (playerChoice == 'scissors') 
        if (computerChoice == 'paper'){ alert('Player wins')} 
        else if (computerChoice == 'rock'){ alert('Computer wins!')} 

    if (computerArr.includes(playerChoice) == false){
        alert('Invalid player input. Please reload and try again!')
        }