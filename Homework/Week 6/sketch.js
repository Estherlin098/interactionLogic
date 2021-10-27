//this is Esther Week 6 Homework
//this game is to play up or down game with computer using arrow keys
//to win this game, the play needs to try to guess what the computer might do (arrow up/down/left/right)
//and press the opposite arrow keys 

//defining variables
const emoji = {
  arrowUp: '⬆️',
  arrowDown: '⬇️',
  arrowLeft: '⬅️',
  arrowRight: '➡️',
  computer: '🤖',
  player: '👧🏻',
};

const moves = [
  '⬆️', '⬇️', '⬅️', '➡️'
]

var playerScore = 0;
var computerScore = 0;
var playerCurrentMove = ''; 
var computerMoves = '';
var timer = 3;
var gameRound = 0;
var input = "";

function setup() {
  createCanvas(windowWidth, windowHeight); 
  textAlign(CENTER, CENTER);
  noStroke();
}

function draw() {
  background(200);
  textSize(30)
  text("Press an arrow key that you think will be different from the computer.", width/2, height/2 - 50 );
  text("Game starts in: " + timer, width/2, height/2);
  //input = keyPressed()

  timer = 0;
  if (frameCount % 60 == 0 && timer > 0) { // if the frameCount is divisible by 60, then a second has passed. it will stop at 0
    timer --;
  }
  //when the timer reaches 0, start the game
  if (timer == 0) {
    background(200);
    gameStart();
    checkGameStatus();
  }
}

function checkGameStatus() {
  //check game status at the end of the game
  if (playerScore > computerScore) {
    console.log("score show")
    textSize(40);
    text("You win!", 50, height/2 + 40);
  } else if (playerScore == computerScore) {
    text("It's a tie!", width/2, height/2 + 40);
  } else {
    text("You lose...Please try again");
  } 
}

function keyPressed() {
  if (keyCode === UP_ARROW) {
    playerCurrentMove = emoji['arrowUp'];
  }
  else if (keyCode === DOWN_ARROW) {
    playerCurrentMove = emoji['arrowDown'];
  }
  else if (keyCode === LEFT_ARROW) {
    playerCurrentMove = emoji['arrowLeft'];
  }
  else if (keyCode === RIGHT_ARROW) {
    playerCurrentMove = '➡️';
  }

  //compare the result
  computerMoves = random(moves);
  if (playerCurrentMove != computerMoves) {
    playerScore += 1;
  } else {
    computerScore += 1;
  }
}

function gameStart() {
  //left side display
  textSize(100);
  text(playerCurrentMove, 300, windowHeight / 2); // Display last key pressed.
  fill(255);
  rect(width/2,0,windowWidth / 2,windowHeight); // right half
  fill(0);
  textSize(20);
  text(emoji['player'] + ": " + playerScore, 60, 50); //computer player text

  //right side display
  textSize(100);
  //computerMoves = (gameRound == 1) ? computerMoves : random(moves);
  text(computerMoves, windowWidth - 300, windowHeight / 2);
  textSize(20);
  text(emoji['computer'] + ": " + computerScore, windowWidth - 70, 50); //computer player text
  textSize(100);
}