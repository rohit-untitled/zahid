class Employee:
    def getEmployeeinfo(self):
        self.id=input("enter the id")
        self.name=input("enter the name")
        self.department=input("enter the department")
    def printresult(self):
        print(self.id, self.name, self.department)
EmpArray = []
while(True):
    emp=Employee()
    emp.getEmployeeinfo()
    EmpArray.append(emp)
    ch=input("Add More Employee y,/n")
    if (ch=='n'):
        break

print("Employee Detail are")
for emp in EmpArray:
    emp.printresult()