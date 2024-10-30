public class Sort
{
  public static int[] bubbleSort(int[] array)
  {
    for(int pass=0;pass<(array.length-1);pass++)
    {
      for(int i=0;i<(array.length-1-pass);i++)
      {
        if(array[i]>array[i+1])
        {
          int temp=array[i];
          array[i]=array[i+1];
          array[i+1]=temp;
        }
      }
    }
    System.out.println("Array Sorted");

    return array;
  }

  public static double[] bubbleSort(double[] array)
  {
    for(int pass=0;pass<(array.length-1);pass++)
    {
      for(int i=0;i<(array.length-1-pass);i++)
      {
        if(array[i]>array[i+1])
        {
          double temp=array[i];
          array[i]=array[i+1];
          array[i+1]=temp;
        }
      }
    }
    System.out.println("Array Sorted");

    return array;
  }
}
