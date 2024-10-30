import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.InputStreamReader;

public class FileIO
{
  public static int[] readIntFile(String filename)
  {
    int[] array = null;
    try
    {
      FileInputStream fileStream = new FileInputStream(filename);
      InputStreamReader rdr        = new InputStreamReader(fileStream);
      BufferedReader bufRdr     = new BufferedReader(rdr);
      String line       = bufRdr.readLine();

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
    return array;
  }
}
