# -----------------------------problem


# 1) Write a program to calculate and display the payroll for employees based on hours worked and hourly wage. [ODD]
# Requirements:

# i. Use a struct to store each Employee's details: name, employeeID, hoursWorked, and hourlyWage.

# ii. Calculate the total pay for each employee (total pay = hoursWorked * hourlyWage).

# iii. Use a function calculatePay() to calculate and return the pay.

# iv. Display a summary report listing each employee’s name, hours worked, and total pay.

# v. Use loops and conditionals for processing multiple employees.

# ---------------------------------solution

class employee:
    def employeeDetails(self, EmpName, EmpId, EmpHourWorking, EmpHourleyWages):
        self.EmpName=EmpName
        self.EmpId=EmpId
        self.EmpHourWorking=EmpHourWorking
        self.EmpHourleyWages=EmpHourleyWages

    def calculatePay(self):
        totalPay=self.EmpHourWorking*self.EmpHourleyWages
        return totalPay
    
    def DisplayReport(self):
        print("\n")
        print("--------------------------------------Detail Report-------------------------------------")
        print(f"the name of the employee is {self.EmpName}")
        print(f"the Id of employee {self.EmpName} is {self.EmpId}")
        print(f"the working Hours of employee {self.EmpName} is {self.EmpHourWorking}")
        print(f"the hourley wages he\she receives {self.EmpHourleyWages}")

        print(f"the total amount he\she recieves in one day is {self.calculatePay()}")

        monthlyIncome=30*self.calculatePay()
        print(f"the monthly income he\she receives is {monthlyIncome}")


while True:
    print("\n")
    emp=employee()

    name=input("Enter the name of the Employee : ")
    emId=input("Enter ID of the same employee : ")
    hourWorking=int(input("Enter how much hours employee is working : "))
    hourleyWages=int(input("Enter how much amount is paid to employee for 1 hour working : "))
    
    emp.employeeDetails(name,emId,hourWorking,hourleyWages)
    emp.DisplayReport()

    continue_choice=input("Do you want to enter another employee? (yes/no): ").strip().lower()
    if continue_choice !="yes":
        print("---------------------Exiting------------------")
        print("Exiting the employee entry program.")
        break