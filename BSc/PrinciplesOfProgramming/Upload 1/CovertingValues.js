/**
* Author: Paul-David Jarvis | S5115232
* Date: 03/10/18
* Week: 12
* Description: A program that convert values.
*/

		var weightPounds = 200;
		var weightKilograms = weightPounds * 0.45359237;
		console.log(weightPounds + "lbs is equivalent to " + weightKilograms + "kg");
		
		var britishPounds = 100;
		var euroMoney = britishPounds * 1.13;
		console.log("£" + britishPounds + " is equivalent to €" + euroMoney);
		
		var fahrenheit = 75;
		var celsius = (fahrenheit - 32) * 5/9; // Formula found at http://manuelsweb.com/temp.htm
		console.log(fahrenheit + " °F is equivalent to " + celsius + " °C");
		
		var timeHours = 1;
		var convertedHours = timeHours * 60 * 60; // Formula found at http://www.math-only-math.com/conversion-of-hours-into-seconds.html
		
		var timeMinutes = 28;
		var convertedMinutes = timeMinutes * 60;
		
		var timeSeconds = 42;
		
		var convertedTime = convertedHours + convertedMinutes + timeSeconds;
		
		console.log(timeHours + " hour " + timeMinutes + " minutes " + timeSeconds + " seconds is equivalent to " + convertedTime + " seconds.");