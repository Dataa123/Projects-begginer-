// Creating variable of dice roll
const myBtn = document.getElementById('mybtn');
const resetBtn = document.getElementById('reset');

// Creating variables of scores
const myScore = document.getElementById('your-score');
const compScore = document.getElementById('computer-score');

// Creating variable of dices
const myDiceP = document.getElementById('p-dice-you');
const compDiceP = document.getElementById('p-dice-computer');

let changeP = document.getElementById('changep');

let score1 = 0;
let score2 = 0;

// Creating function that displays random numbers from 1 to 6 after clicking myBtn, also increasing score, depended you won or not or it was tie
myBtn.addEventListener('click', function(){
    let random1 = (Math.floor(Math.random() * 6) + 1)
    let random2 = (Math.floor(Math.random() * 6) + 1)
    myDiceP.textContent = "YOU: " + random1
    compDiceP.textContent = "COMPUTER: " + random2
    
    // Working on increasing scores
    if (random1 > random2){
        score1++
        myScore.textContent = score1
        changeP.textContent = "You Win ! ! !"
    } else if (random2 > random1){
          score2++
          compScore.textContent = score2
          changeP.textContent = "You Lose ! ! !"
    } else if (random1 == random2){
          score1 = score1
          score2 = score2
          changeP.textContent = "Tie ! ! !"
     }
})

resetBtn.addEventListener('click', function(){
    score1 = 0
    myScore.textContent = score1
    score2 = 0
    compScore.textContent = score2
    random1 = 0
    myDiceP.textContent = "YOU: " + random1
    random2 = 0
    compDiceP.textContent = "COMPUTER: " + random2
    changeP.textContent = ""
})