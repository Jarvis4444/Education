/**
* Author: Paul-David Jarvis | S5115232
* Date: 05/10/18
* Week: 13
* Description: A program that you input your first and last name and it outputs a username.
*/

var firstName = prompt("What is your first name: ");
var secondName = prompt("What is your second name: ");
var userName = firstName.substring(0, 1) + secondName.substring(0, 5);

alert("Your username is: " + userName);
