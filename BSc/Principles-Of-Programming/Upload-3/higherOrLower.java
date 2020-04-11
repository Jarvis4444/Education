/**
* @Paul-David Jarvis, S5115232
* Task 8
* Week 16
* Upload 3 Task 2
* 25/10/18
* a program that simulates the higher or lower card guessing game.
*/

import java.util.Scanner;
import java.util.concurrent.ThreadLocalRandom; // https://stackoverflow.com/questions/363681/how-to-generate-random-integers-within-a-specific-range-in-java

public class higherOrLower {
	public static void main(String[] args) {

		boolean game = true;
		int cardNumber = ThreadLocalRandom.current().nextInt(1, 14);
		int cardNumber2 = ThreadLocalRandom.current().nextInt(1, 14);
		Scanner scan = new Scanner(System.in);

		do {
			System.out.println(cardNumber);
			System.out.println("(H)igher or(L)ower : ");
			String cardChoice = scan.nextLine();

			if (cardNumber > cardNumber2 && cardChoice.equalsIgnoreCase("L")
					|| (cardNumber < cardNumber2 && cardChoice.equalsIgnoreCase("H"))) {
				System.out.println("Correct");

			} else {
				System.out.println("Incorrect");
				System.out.println(cardNumber2);
				System.out.println("play again? Y/N :");
				String playAgain = scan.nextLine();

				if (playAgain.equalsIgnoreCase("N")) {
					game = false;
				}
			}

			cardNumber = ThreadLocalRandom.current().nextInt(1, 14);
			cardNumber2 = ThreadLocalRandom.current().nextInt(1, 14);

		} while (game);
		scan.close();
	}
}

