/**
* @Paul-David Jarvis, S5115232
* Task 4
* Week 14
* 11/10/18
* A program that reads in the speed limit and the speed a car was doing and offers
* a fine if they're over the speeding limit.
*/

var speedLimit = parseInt (prompt("Enter Speed Limit: ")); 
var carSpeed = parseInt (prompt("Enter Car Speed: "));

		if (carSpeed <= speedLimit) {
            console.log("Under the speed limit - no fine.");

        } else if (carSpeed <= speedLimit + 4) {
            console.log("Over the speed limit - just - please be careful of your speed in the future.");

        } else if (carSpeed <= speedLimit + 9) {
            console.log("5 miles or more over limit - fined £50");

        } else if (carSpeed <= speedLimit + 14) {
            console.log("10 miles or more over limit - fined £100");

        } else if (carSpeed <= speedLimit + 19) {
           console.log("15 miles or more over limit - fined £150 and 3 points");

        } else {
           console.log("20 miles or more over limit - fined £1000 and disqualified");
    	}