/**
 * @Paul-David Jarvis, S5115232
 * Task 4
 * Week 19
 * Upload 4 Task 1
 * 25/10/18
 * A program that outputs 3 random numbers in a certain range and an array of numbers
 */

import java.util.concurrent.ThreadLocalRandom;

public class randomNumberGenerator {
	public static void main(String[] args) {
		System.out.println(randomnumber());
		System.out.println(randomnumber2());
		System.out.println(randomnumber3(10, 20));
		int[] returnedArray = randomArrayc();
		for(int i = 0; i < returnedArray.length; i++){
			System.out.print(returnedArray[i] + ", ");
		}

	}

	public static int randomnumber() {
		int randomNumber = ThreadLocalRandom.current().nextInt(1, 100);
		return randomNumber;
		// https://explainjava.com/random-number-generator-java/
	}

	public static int randomnumber2() {
		int randomNumber2 = ThreadLocalRandom.current().nextInt(1, 50);
		return randomNumber2;
	}

	public static int randomnumber3(int min, int max) {
		int randomNumber3 = ThreadLocalRandom.current().nextInt(min, max);
		return randomNumber3;
	}	

	public static int[] randomArrayc() {
		int[] randomArray = {0 , 0, 0, 0, 0, 0, 0, 0, 0, 0, 0}; 
		int i = 0;

		while(i < randomArray.length) {
			int randomNumber4 = ThreadLocalRandom.current().nextInt(1, 100);
			boolean check = false;
			// https://www.tutorialspoint.com/java/java_loop_control.htm
			for(int j = 0; j < randomArray.length; j++) {
				if(randomArray[j] == randomNumber4) {
					check = true;
				}
			}
			
			if(check == false) {
				randomArray[i] = randomNumber4;
				i++;
			}
		}

		return randomArray;
	}

}

