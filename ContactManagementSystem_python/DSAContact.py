class DSAContact():
    def __init__(self, number, name,  email, group):
        self.name = name
        self.number = number
        self.email = email
        self.group = group

    def getNumber(self):
        return self.number

    def getName(self):
        return self.name

    def getEmail(self):
        return self.email

    def getGroup(self):
        return self.group

    def __str__(self):
        return "Number: " + str(self.number) + "\nName: " + self.name + "\nEmail: " + self.email + "\nGroup: " + self.group + "\n" 


