/**
* @Paul-David Jarvis, S5115232
* Task 8
* Week 16
* Upload 3 Task 2
* 25/10/18
* a program that simulates the higher or lower card guessing game.
*/

var cardNumber = Math.round(Math.random() * 13) + 1;
console.log(cardNumber);
game = true;

while(game){
	var userGuess = prompt("(H)igher or(L)ower : ");
	var userGuess = userGuess.toUpperCase();
	var newCard = Math.round(Math.random() * 13) + 1;
	
	if(cardNumber > newCard && userGuess == "L") {
		console.log("Correct");
		console.log(newCard);
		
	}else if(cardNumber < newCard && userGuess == "H") {
		console.log("Correct"); 
		console.log(newCard);
	
	}else {
		console.log("Incorrect");
		console.log(newCard);
		var playAgain = prompt("play again? Y/N :");
		var playAgain = playAgain.toUpperCase();
		if(playAgain == "N") {
			game = false;
		}
	}
		cardNumber = newCard;
}