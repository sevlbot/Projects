import java.util.InputMismatchException;
import java.util.Scanner;

public class UserInput
{
  public static int getUserInt(Scanner sc, int min, int max)
  {
    int userChoice = -1;
    boolean validInput;
    do
      {
        validInput = false;
        try
        {
          userChoice = sc.nextInt();

          if (userChoice < min)
          {
            System.out.println("Please enter a integer greater than " + min);
            validInput = false;
          }

          if (userChoice >= max)
          {
            System.out.println("Please enter an integer less than " + max);
            validInput = false;
          }

          if (userChoice >= min && userChoice <= max)
          {
            validInput = true;
          }
          
        } catch (InputMismatchException e){
          // Clear Screen
          System.out.print("\033[H\033[2J");  
          System.out.flush();

          System.out.println("Pleaser enter an Integer");
          sc.nextLine(); // Consume input contents
          validInput = false;
        }
      } while (!validInput);

      return userChoice;
  }
  
}
