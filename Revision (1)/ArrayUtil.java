public class ArrayUtil
{
  public static void printArray(int[] array)
  {
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
  }

  public static void printArray(double[] array)
  {
    boolean commaNeeded = false;

    System.out.print("[");
    for (double i : array)
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
  }

  public static void printArray(String[] array)
  {
    boolean commaNeeded = false;

    System.out.print("[");
    for (String i : array)
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
  }

  public static void printArray(Staff[] array)
  {
    boolean commaNeeded = false;

    System.out.print("[");
    for (Staff i : array)
    {
      if (!commaNeeded)
      {
        commaNeeded = true;
      } else {
        System.out.print(", ");
      }
      System.out.print(i.toString()); 
    }
    System.out.print("]");
  }
}
