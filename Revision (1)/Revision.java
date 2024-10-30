import java.util.*;

class Revision
{

  public static void main(String[] args)
  {
    int userChoice = -1;
    int numOptions = 6;
    int[] array = null;
    Scanner sc = new Scanner(System.in);
    double celsius, fahrenheit;
    String filename = "numberFile.csv";

    // Program Setup
    Menu.clearScreen();
    Menu.title();
    Menu.timeDelay();
    array = FileIO.readIntFile(filename);

    do
    {
      Menu.optionsMenu(numOptions);
      userChoice = UserInput.getUserInt(sc, 0, numOptions);

      switch (userChoice)
      {
        case 1: // Tests
          Menu.clearScreen();
          System.out.println("Testing Program\n");
          Tests.testStaff();
          Tests.testUnits();
          userChoice = -1;
          break;
        case 2: // Hello World
          Menu.clearScreen();
          System.out.println("Hello World");
          userChoice = -1;
          break;
        case 3: // F2C Convert
          Menu.clearScreen();
          System.out.print("Please enter Fahrenheit: ");
          fahrenheit = UserInput.getUserInt(sc, -200, 200);
          TempCovert.F2C(fahrenheit);
          break;
        case 4: // C2F Convert
          Menu.clearScreen();
          System.out.print("Please enter celsiusius: ");
          celsius = UserInput.getUserInt(sc, -200, 200);
          TempCovert.C2F(celsius);
          break;
        case 5: // Print Array
          Menu.clearScreen();
          ArrayUtil.printArray(array);
          userChoice = -1;
          break;
        case 6: // Sort Array
          Menu.clearScreen();
          array = Sort.bubbleSort(array);
          break;
        
        case 0: // Exit
          System.out.println("Thank you for using my program");
          sc.close();
          break;
      }
    } while (userChoice != 0);
  }
}