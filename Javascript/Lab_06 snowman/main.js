const newGame = document.querySelector('#new-game');
const fullGuess = document.querySelector('#full-guess');
const fullGuessContainer = document.querySelector('#full-guess-container');
const wordContainer = document.querySelector('#word-container');
const snowmanInputContainer = document.querySelector('#snowman-input-container');
const alphabet = Array.from('abcdefghijklmnopqrstuvwxyz');
const gameContainer =  document.querySelector('#game-container')
const guessbutton = document.querySelector('#guess-button');
const score = document.querySelector('#score');

let incorrectGuesses = 0;
let correctGuesses = 0;
let letButton;


let guessLetters = []
let snowWord



async function pullWord() {
    const seed = (Math.floor(Math.random() * 7)+5);
    const request = await fetch(`https://random-word-api.herokuapp.com/word?length=${seed}`);
    const data = await request.json()
    displayData(data[0], guessLetters);
    snowWord =  data[0]
}

function displayData(word, guess){
    wordContainer.innerHTML = ''
    let snowWord = word.split("");
    correctGuesses = 0;
    for(letter of snowWord) {
        if(guess.includes(letter)) {
            correctGuesses += 1;
        let element=document.createElement('h3');
        element.innerText = `${letter}`
        element.style.textDecoration = 'underline';
        wordContainer.appendChild(element);} else{
                let element=document.createElement('h3');
                element.innerText = '_'
                element.style.textDecoration = 'underline';
                wordContainer.appendChild(element);

        }
    if(correctGuesses === word.length){
        
    } 

}
if(correctGuesses === word.length){
    win()
} else if(incorrectGuesses === 10){
    loss()
}


}


function displayInput(){
    snowmanInputContainer.innerHTML = ''
    for(letter of alphabet){
        let letButton=document.createElement('button');
        letButton.innerText = letter;
        letButton.className = 'letter-button'
        letButton.value = letter
        letButton.onclick = function(){
            guessLetters.push(letButton.value);
            letButton.disabled = true;

            if(!snowWord.split('').includes(letButton.value)){
                incorrectGuesses += 1;
                updateScore()
            }
            displayData(snowWord, guessLetters)
        }
        snowmanInputContainer.appendChild(letButton);
        
        

    }
}

async function pullWord() {
    newGame.style.visiblity = 'hidden';
    const seed = (Math.floor(Math.random() * 7)+5);
    const request = await fetch(`https://random-word-api.herokuapp.com/word?length=${seed}`);
    const data = await request.json()
    displayData(data[0], guessLetters);
    snowWord =  data[0]


}

newGame.onclick = function(){
    pullWord();
    displayInput();
    newGame.style.visibility = 'hidden';
    correctGuesses=0
    incorrectGuesses=0
    guessLetters = [];
    updateScore()
}

guessbutton.onclick = function(){
    if(fullGuess.value === snowWord){
        win()

    }   else {
        incorrectGuesses++;
        updateScore()
    }
    
    if(incorrectGuesses === 10){
        loss()
    }

}

function updateScore(){
    score.innerHTML = `Guesses remaining: ${10-incorrectGuesses}`
}

function win(){
    wordContainer.innerHTML = `<h2>YOU ARE A WINNER! The word was ${snowWord}</h2>`;  
   snowmanInputContainer.innerHTML = ''
   newGame.style.visibility = 'visible';
}

function loss(){
    wordContainer.innerHTML = `<h3>The correct word was ${snowWord}</h3>`;
    snowmanInputContainer.innerHTML = ''
    newGame.style.visibility = 'visible';
}

displayInput()
pullWord()

