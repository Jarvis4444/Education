/**
* @Paul-David Jarvis, S5115232
* Task 7
* Week 14
* 11/10/18
* A program that asks the user whether a coin flip would be heads or tails and outputs if they're right.
*/

var coinflip = Math.floor((Math.random() * 2));
var userchoice = prompt("Heads or Tails");
var userchoice = userchoice.toLowerCase();

if (userchoice == "heads" && coinflip == 0) {
	console.log("Congratulations! Your choice was correct.");
	console.log(coinflip);
	
} else if (userchoice == "tails" && coinflip == 1) {
	console.log("Congratulations! Your choice was correct."); 
	console.log(coinflip);
	
 }else {
	console.log("Unlucky!! Your choice was incorrect.");
	console.log(coinflip);
 }
