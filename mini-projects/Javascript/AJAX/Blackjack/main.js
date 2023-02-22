const cardContainer = document.querySelector('#card-container');
const drawButton = document.querySelector('#draw-button');
const score = document.querySelector('#score');
const advice = document.querySelector('#advice');
const newGame = document.querySelector('#new-game');
let deckId = ''
let playerCards = []

async function getDeck(){
    const response = await fetch('https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1')
    const data = await response.json()
    dealCards(data.deck_id)
    deckId = data.deck_id
    playerCards = []
}

async function dealCards(deckId, amount=2){
    const response = await fetch(`https://deckofcardsapi.com/api/deck/${deckId}/draw/?count=${amount}`)
    const data = await response.json()
    for(let card of data.cards){
        playerCards.push(card)}
    displayCards(playerCards)
    
    
}
getDeck()

async function restart(deckId){
    const response = await fetch(`https://deckofcardsapi.com/api/deck/${deckId}/shuffle/`)
    const data = await response.json()
    playerCards = []
    dealCards(data.deck_id)
    drawButton.disabled = false
}

function displayCards(cards){
    let total = 0;
    cardContainer.innerHTML = ''
    for(let card of cards){

        let image = document.createElement('img')
        image.setAttribute('src', card.image)
        image.style.width = Math.max(100/playerCards.length)
        console.log(image)
        cardContainer.appendChild(image)
        if((Number(card.value))){
            total += Number(card.value)
        } else if (card.value === 'ACE'){total += 1
        } else{total+=10}
    }
    console.log(total)
    console.log(playerCards)
    score.innerText = `Total: ${total}`
    getAdvice(total)
}



function getAdvice(score){
    if(score>21){
        advice.innerText = "Dang dude, you are the absolute WORST"
        drawButton.disabled = true
    } else if(score == 21){ 
        advice.innerText = "Good job my dude, you won some grocery money"
    } else if(score >17){
        advice.innerText = 'Dang dude, you are so close? Will you be a hero, or a little baby?'
    } else{
        advice.innerText = 'Better start hitting Loser'
    }
}

drawButton.onclick = function(){dealCards(deckId, 1)}

newGame.onclick = function(){restart(deckId)}