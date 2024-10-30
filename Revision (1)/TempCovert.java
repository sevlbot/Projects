import java.text.DecimalFormat;

public class TempCovert
{
  public static void F2C(double fahrenheit)
  {
    DecimalFormat df = new DecimalFormat("#.00");
    double celsius = (fahrenheit - 32.0) * 5.0 / 9.0;
    System.out.println(fahrenheit + "F = " + df.format(celsius) + "C");
  }

  public static void F2C(int fahrenheit)
  {
    DecimalFormat df = new DecimalFormat("#.00");
    double celsius = (fahrenheit - 32.0) * 5.0 / 9.0;
    System.out.println(fahrenheit + "F = " + df.format(celsius) + "C");
  }

  public static void C2F(double celsius)
  {
    DecimalFormat df = new DecimalFormat("#.00");
    double fahrenheit = (celsius * 9.0) / 5 + 32;
    System.out.println(celsius + "C = " + df.format(fahrenheit) + "F");
  }

  public static void C2F(int celsius)
  {
    DecimalFormat df = new DecimalFormat("#.00");
    double fahrenheit = (celsius * 9.0) / 5 + 32;
    System.out.println(celsius + "C = " + df.format(fahrenheit) + "F");
  }
}
