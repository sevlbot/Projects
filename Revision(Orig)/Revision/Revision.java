import java.util.*;
import java.util.concurrent.TimeUnit;
import java.io.*;
import java.text.DecimalFormat;

class Revision {

  public static void main(String[] args)
  {
    int userChoice = -1;
    int numOptions = 6;
    boolean validInput = false;
    DecimalFormat df = new DecimalFormat("#.00");
    int[] array = null;
    Scanner sc = new Scanner(System.in);
    double cels, faren;

    FileInputStream fileStream = null;
    InputStreamReader rdr;
    BufferedReader bufRdr;
    String line;
    String filename = "numberFile.csv";

    // Clear Screen
    System.out.print("\033[H\033[2J");  
    System.out.flush();

    // Title Menu
    System.out.println("Welcome to Keven's Amazing Tutorial");
    try
    {
      TimeUnit.SECONDS.sleep(3);
    } catch (InterruptedException e) {
      System.out.println("No sleep");
    }

    // File I/O
    try
    {
      fileStream = new FileInputStream(filename);
      rdr        = new InputStreamReader(fileStream);
      bufRdr     = new BufferedReader(rdr);
      line       = bufRdr.readLine();

      while(line != null)
      {
        // Process Line
        String[] splitLine;
        splitLine = line.split(",");
        array = new int[splitLine.length];
        
        for(int ii = 0; ii < splitLine.length; ii++)
        {
          array[ii] = Integer.parseInt(splitLine[ii]);
        } 
        System.out.println("");
        //


        line = bufRdr.readLine();
      }
      fileStream.close();
    } catch (FileNotFoundException e){ System.out.println("Cannot Find File");
    } catch (IOException e){ System.out.println("Reading File Exception");
    }

    do
    {
      // Options Menu
      System.out.println("\n\n\n\n");
      System.out.println("Please make a selection between 1 and " + numOptions + ". 0 to exit");
      System.out.println("(1) -> Test Program");
      System.out.println("(2) -> Print Hello World");
      System.out.println("(3) -> Fahrenheit to Celsius");
      System.out.println("(4) -> Celsius to Fahrenheit");
      System.out.println("(5) -> Print Array");
      System.out.println("(6) -> Sort Array");
        // Add extra options here
      System.out.println("(0) -> Exit");

      // Getting valid user input
      do
      {
        try
        {
          userChoice = sc.nextInt();
          validInput = true;
          
        } catch (InputMismatchException e) {
          // Clear Screen
          System.out.print("\033[H\033[2J");  
          System.out.flush();

          System.out.println("Pleaser enter an Integer");
          sc.nextLine(); // Consume input contents
          validInput = false;
        }
      } while (!validInput);

      // Processing User input
      switch (userChoice)
      {
        case 1:
          System.out.print("\033[H\033[2J");  
          System.out.flush();

          System.out.println("Testing Program\n");

          // Staff Testing
          Staff s1 = new Staff();
          Staff s2 = new Staff(123456,"Keven", "Rashleigh");
          Staff s3 = new Staff(s2);

          System.out.println(s1);
          System.out.println(s2);
          System.out.println(s3);

          System.out.println("s1 equals s2: " + s1.equals(s2));
          System.out.println("s2 equals s3: " + s2.equals(s3));

          // Team Testing
          UniUnit u1 = new UniUnit();
          UniUnit u2 = new UniUnit("COMP1007", "PDI", s1);
          UniUnit u3 = new UniUnit(u2);

          u1.addTutor(s1);
          u1.addTutor(s2);

          System.out.println();
          System.out.println(u1);
          System.out.println(u2);
          System.out.println(u3);

          System.out.println("u1 equals u2: " + u1.equals(u2));
          System.out.println("u2 equals u3: " + u2.equals(u3));

          userChoice = -1;
          break;
        case 2:
          System.out.print("\033[H\033[2J");  
          System.out.flush();

          System.out.println("Hello World");
          userChoice = -1;
          break;
        case 3:
          System.out.print("\033[H\033[2J");  
          System.out.flush();

          System.out.println("F to C");

          System.out.print("Please enter Fahrenheit: ");
          faren = sc.nextInt();
          cels = (faren - 32.0) * 5.0 / 9.0;
          System.out.println(faren + "F = " + df.format(cels) + "C");
          break;
        case 4:
          System.out.print("\033[H\033[2J");  
          System.out.flush();

          System.out.println("C to F");

          // Cels to Faren
          System.out.print("Please enter Celsius: ");
          cels = sc.nextInt();
          faren = (cels * 9.0) / 5 + 32;
          System.out.println(cels + "C = " + df.format(faren) + "F");

          break;
        case 5:
          System.out.print("\033[H\033[2J");  
          System.out.flush();

          // Print Array
          boolean commaNeeded = false;

          System.out.print("[");
          for (int i : array)
          {
            if (!commaNeeded)
            {
              commaNeeded = true;
            } else {
              System.out.print(", ");
            }
            System.out.print(i); 
          }
          System.out.print("]");

          userChoice = -1;
          break;
        case 6:
          System.out.print("\033[H\033[2J");  
          System.out.flush();
          // Bubble Sort
          for(int pass=0;pass<(array.length-1);pass++)
          {
            for(int i=0;i<(array.length-1-pass);i++)
            {
              if(array[i]>array[i+1])
              {
                int temp=array[i];array[i]=array[i+1];array[i+1]=temp;
              }
            }
          }

          System.out.println("Array Sorted");

          break;
        
        case 0:
          System.out.println("Thank you for using my program");
          sc.close();
          break;
      }
    } while (userChoice != 0);
  }
}