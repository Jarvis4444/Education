/**
* Author: Paul-David Jarvis | S5115232
* Date: 05/10/18
* Week: 13
* Description: A program that stores your results for 6 units and prints them.
*/

var unit = [CF, DAD, POP, APP, NCS, SAD];
var CF = prompt("Please enter the grade you received for CF: ");
var DAD = prompt("Please enter the grade you received for DAD: ");
var POP = prompt("Please enter the grade you received for POP: ");
var APP = prompt("Please enter the grade you received for APP: ");
var NCS = prompt("Please enter the grade you received for NCS: ");
var SAD = prompt("Please enter the grade you received for SAD: ");
var AVG = (CF + DAD + POP + APP + NCS + SAD) / 6;

alert("Your marks are: \n" 
	+ "Computer Fundamentals: " + CF 
		+ "\n Data And Databases: " + DAD 
			+ "\n Principles of Programming: " + POP 
				+ "\n Application Principles of Programming: " + APP 
					+ "\n Networks & CyberSecurity: " + NCS 
						+ "\n Systems Anaylsis Developmen: " + SAD); 
