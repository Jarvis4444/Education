/**
* @Paul-David Jarvis, S5115232
* Task 1
* Week 15
* 18/10/18
* A program that prompts the user to input salaries, adds them up and outputs the total and average.
* The program will stop running when the user inputs "-1"
*/

var count = 0;
var totalSalary = 0.0;
var salaryCheck = true;

while(salaryCheck){
	var inputtedSalary = parseFloat(prompt("Enter Salary: "));
	if (inputtedSalary == -1) {
		salaryCheck = false;
		}else {
		totalSalary += inputtedSalary; 
		count++;
		console.log("£"inputtedSalary);
	}
}
console.log("Total salary is: £" + totalSalary);
console.log("Average salary is: £" + (totalSalary / count));