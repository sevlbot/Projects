public class Tests
{
  public static void testStaff()
  {
    Staff[] staff = makeStaff();

    System.out.println(staff[0]);
    System.out.println(staff[1]);
    System.out.println(staff[2]);

    System.out.println("s1 equals s2: " + staff[0].equals(staff[2]));
    System.out.println("s2 equals s3: " + staff[2].equals(staff[3]));
  }

  public static void testUnits()
  {
    Staff[] staff = makeStaff();

    UniUnit u1 = new UniUnit();
    UniUnit u2 = new UniUnit("COMP1007", "PDI", staff[0]);
    UniUnit u3 = new UniUnit(u2);


    u1.addTutor(staff[0]);
    u1.addTutor(staff[1]);

    System.out.println();
    System.out.println(u1);
    System.out.println(u2);
    System.out.println(u3);

    System.out.println("u1 equals u2: " + u1.equals(u2));
    System.out.println("u2 equals u3: " + u2.equals(u3));
  }

  private static Staff[] makeStaff()
  {
    Staff[] staff = new Staff[3];
  
    staff[0] = new Staff();
    staff[1] = new Staff(123456,"Keven", "Rashleigh");
    staff[2] = new Staff(staff[1]);
  
    return staff;
  }
}
