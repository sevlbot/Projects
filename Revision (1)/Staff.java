public class Staff
{
  private int id;
  private String firstName;
  private String lastName;

  // ************
  // CONSTRUCTORS
  // ************

  // Parameter Constructor
  public Staff(int id, String firstName, String lastName)
  {
    this.id = id;
    this.firstName = firstName;
    this.lastName = lastName;
  }

  // Default Constructor
  public Staff()
  {
    this.id = 0;
    this.firstName = "Joe";
    this.lastName = "Blogs";
  }

  // Copy Constructor
  public Staff(Staff originalStaff)
  {
    this.id = originalStaff.getId();
    this.firstName = new String(originalStaff.getFirstName());
    this.lastName = new String(originalStaff.getLastName());
  }

  // ***********************
  // ACCESSORS (aka getters)
  // ***********************
  public int getId() {return this.id;}
  public String getFirstName() {return this.firstName;}
  public String getLastName() {return this.lastName;}
  public String getEmail() {return this.firstName + this.lastName + "curtin.edu.au";}
  public String getFullName() {return this.firstName + " " + this.lastName;}

  // **********************
  // MUTATORS (aka setters)
  // **********************
  public void setId(int id) {this.id = id;}
  public void setFirstName(String firstName) {this.firstName = new String(firstName);}
  public void setLastName(String lastName) {this.lastName = new String(lastName);}

  // *********
  // OVERRIDES
  // *********

  @Override
  public String toString()
  {
    String objectString =
    "Id: " + this.id +
    "\nFirst Name: " + this.firstName +
    "\nLast Name: " + this.lastName +
    "\n";

    return objectString;
  }

  @Override
  public boolean equals(Object o)
  {
    Staff inStaff = null;

    if (!(o instanceof Staff)) {return false;} else { inStaff = (Staff)o;}
    if (!(this.id == inStaff.getId())) {return false;}
    if (!(this.firstName.equals(inStaff.getFirstName()))) {return false;}
    if (!(this.lastName.equals(inStaff.getLastName()))) {return false;}

    return true;
  }
}
