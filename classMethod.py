# ----------------------------class method in python

class employees:
    company="apple"
    def show(self):
        print(f"the name of the employee is {self.name} and the company is {self.company}")

    def changeCompany(cls, newCompany):
        cls.company=newCompany

emp1=employees()
emp1.name="piyush"
emp1.show()

# here class variable is not changed here you created an instance of the class variable
emp1.changeCompany("tesla")
emp1.show()
print(employees.company)
print("\n")


# --------------------------------------------how to change the class variable

class students:
    school="DAV"
    def show(self):
        print(f"the student name is {self.name} and the school name is {self.school}")

    @classmethod
    def changeSchool(cls,newSchool):
        cls.school=newSchool

sch1=students()
sch1.name="piyush"
sch1.show()

# changing class variable
sch1.changeSchool("st clear's school")
sch1.show()
print(students.school)