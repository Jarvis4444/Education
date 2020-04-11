/**
* @Paul-David Jarvis, S5115232
* Task 8
* Week 16
* 25/10/18
* A program that reads words from the user, moves the first letter to the back and reverses
* and checks whether it's the same word as the word that was inputted.
*/

var wordLoop = true;

while (wordLoop) {
	var inputtedWord = prompt("Enter word to be tested.... ");
	var inputtedWord = inputtedWord.toLowerCase();
	var firstLetter = inputtedWord.slice(0, 1);
	var changedWord = inputtedWord.slice(1) + firstLetter;
	var reversedWord = changedWord.split('').reverse().join(''); // Found the second part of line 8 by searching "js reverse string"
	
if (inputtedWord == "quit") {
	wordLoop = false;
}else if (reversedWord != inputtedWord) {
	console.log(reversedWord + " is not the same as " + inputtedWord);
}else {
	console.log(reversedWord + " is the same as " + inputtedWord);
 }
}

