/**
* @Paul-David Jarvis, S5115232
* Task 4
* Week 16
* Upload 3 Task 1
* 25/10/18
* A program that reads a membership and age and tells the user the discount they will receive.
*/

var membership = prompt("Enter membership: ")
var membership = membership.toLowerCase();
var age = parseInt(prompt("Enter age: "));


if(membership == "gold") {
    if(age > 16 && age < 60) {
        console.log("You get 25% discount.");
        
    }else if (age <= 16 || age >= 60) {
         console.log("You get 35% discount.");
    }
}

else if (membership == "silver") {
 if(age > 16 && age < 60) {
        console.log("You get 15% discount.");
        
    }else if (age <= 16 || age >= 60) {
         console.log("You get 25% discount.");
    }
}

else if (membership == "bronze") { 
 if(age > 16 && age < 60) {
        console.log("You get 10% discount.");
        
    }else if (age <= 16 || age >= 60) {
          console.log("You get 20% discount.");
    }
}

else {
    console.log("Invalid Choice...");
}

