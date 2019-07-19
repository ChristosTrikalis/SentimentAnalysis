import controller.Preprocessing;
import java.util.Scanner;
public class Launcher 
{
	public static void main(String[] args) 
	{
		System.out.println("Welcome to Sentiment Analysis system! \n");
		//TODO generate code for scraper
		Preprocessing pTexts = new Preprocessing();
		System.out.println("Would you like to see the form of preprocessed texts? (type Y/N)");
		
		Scanner input = new Scanner(System.in);
		String answer = input.nextLine();
		while(!answer.toUpperCase().contentEquals("Y") && !answer.toUpperCase().contentEquals("N"))
		{
			System.out.println("To see the form of preprocessed texts, type Y or N");
			answer = input.nextLine();
		}
		if(answer.equals("Y"))
			pTexts.printPreprocessedDocs();
		input.close();
		System.out.println("Goodbye motherfucker");
	}

}
