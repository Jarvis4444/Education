/**
* @Paul-David Jarvis, S5115232
* Task 4
* Week 16
* Upload 3 Task 1
* 25/10/18
* A program that reads a membership and age and tells the user the discount they will receive.
*/

import java.util.Scanner;

public class leisureCentre {
	public static void main(String[] args) {

		Scanner membershipScanner = new Scanner(System.in);
		System.out.println("Enter Membership: ");
		String membership = membershipScanner.nextLine();

		Scanner ageScanner = new Scanner(System.in);
		System.out.println("Enter Age: ");
		int age = ageScanner.nextInt();
		ageScanner.close();
		membershipScanner.close();

		if (membership.equalsIgnoreCase("gold")) {
			if (age > 16 && age < 60) {
				System.out.println("You get 25% discount.");

			} else if (age <= 16 || age >= 60) {
				System.out.println("You get 35% discount.");
			}
		}

		else if (membership.equalsIgnoreCase("silver")) {
			if (age > 16 && age < 60) {
				System.out.println("You get 15% discount.");

			} else if (age <= 16 || age >= 60) {
				System.out.println("You get 25% discount.");
			}
		}

		else if (membership.equalsIgnoreCase("bronze")) {
			if (age > 16 && age < 60) {
				System.out.println("You get 10% discount.");

			} else if (age <= 16 || age >= 60) {
				System.out.println("You get 20% discount.");
			}
		}

		else {
			System.out.println("Invalid Choice...");
		}

	}
}
