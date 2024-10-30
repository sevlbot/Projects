import java.util.concurrent.TimeUnit;

public class Menu
{
  public static void title()
  {
    System.out.println("Welcome to Keven's Amazing Tutorial");
  }

  public static void clearScreen()
  {
    System.out.print("\033[H\033[2J");  
    System.out.flush();
  }

  public static void timeDelay()
  {
    try
    {
      TimeUnit.SECONDS.sleep(3);
    } catch (InterruptedException e) {
      System.out.println("No sleep");
    }
  }

  public static void optionsMenu(int numOptions)
  {
    System.out.println("\n\n\n\n");
      System.out.println("Please make a selection between 1 and " + numOptions + ". 0 to exit");
      System.out.println("(1) -> Test Program");
      System.out.println("(2) -> Print Hello World");
      System.out.println("(3) -> Fahrenheit to celsiusius");
      System.out.println("(4) -> celsiusius to Fahrenheit");
      System.out.println("(5) -> Print Array");
      System.out.println("(6) -> Sort Array");
        // Add extra options here
      System.out.println("(0) -> Exit");
  }
}
