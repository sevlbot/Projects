public class UniUnit
{
  private String code;
  private String name;
  private Staff coordinator;
  private Staff[] tutors;

  // ************
  // CONSTRUCTORS
  // ************

  // Parameter Constructor
  public UniUnit (String code, String name, Staff coordinator)
  {
    this.code = code;
    this.name = name;
    this.coordinator = coordinator;
    this.tutors = new Staff[10];
  }

  // Default Constructor
  public UniUnit()
  {
    this.code = "COMP0000";
    this.name = "Default Unit";
    this.coordinator = new Staff();
    this.tutors = new Staff[10];
  }

  // Copy Constructor
  public UniUnit(UniUnit originalUniUnit)
  {
    this.code = new String(originalUniUnit.getCode());
    this.name = new String(originalUniUnit.getName());
    this.coordinator = originalUniUnit.getCoordinator();
    this.tutors = new Staff[10];
    
    for (Staff staff : originalUniUnit.tutors)
    {
      this.addTutor(staff);
    }
  }

  // ***********************
  // ACCESSORS (aka getters)
  // ***********************
  public String getCode() {return new String(this.code);}
  public String getName() {return new String(this.name);}
  public Staff getCoordinator() {return this.coordinator;}
  public Staff[] getTutors() {return this.tutors;}

  // **********************
  // MUTATORS (aka setters)
  // **********************
  public void setCode(String code) {this.code = new String(code);}
  public void setName(String name) {this.name = new String(name);}
  public void setCoordinator(Staff coordinator) {this.coordinator = coordinator;}

  // *********
  // OVERRIDES
  // *********
  @Override
  public String toString()
  {
    String objectString =
    "Code: " + this.code +
    "\nName: " + this.name +
    "\nCoordinator: " + this.coordinator.getFullName() +
    "\nTutors: ";

    boolean commaNeeded = false;
    
    for (Staff staff : tutors)
    {
      if (staff != null)
      {
        if (!commaNeeded)
        {
          commaNeeded = true;
        } else {
          objectString += ", ";
        }

        objectString += staff.getFullName();
      }  
    }
    objectString += "\n";

    return objectString;
  }

  @Override
  public boolean equals(Object o)
  {
    UniUnit inUnit = null;

    if (!(o instanceof UniUnit)) {return false;} else { inUnit = (UniUnit)o;}
    if (!(this.code.equals(inUnit.getCode()))) {return false;}
    if (!(this.name.equals(inUnit.getName()))) {return false;}
    if (!(this.coordinator.equals(inUnit.getCoordinator()))) {return false;}

    // We are assuming if these match its the same unit regardless of tutors

    return true;
  }

  public void addTutor(Staff tutor)
  {
    for (int ii = 0; ii < this.tutors.length; ii++)
    {
      if (tutors[ii] == null)
      {
        tutors[ii] = tutor;
        return;
      }
    }
    System.out.println("No Room for tutor");
  }
}
