import time
start=time.perf_counter()
class Employee:
    def __init__(self, name, id, department):
        self.__name = name
        self.__id = id
        self.__department = department
    def set_name(self, name):
        self.__name = name
    def set_id(self, id):
        self.__id = id
    def set_department(self, department):
        self.__department = department
    def get_name(self):
        return self.__name
    def get_id(self):
        return self.__id
    def get_department(self):
        return self.__department
    def __str__(self):
        return 'Name: ' + self.__name + \
               '\nID number: ' + self.__id + \
               '\nDepartment: ' + self.__department
def main():
    emp1 = emp.Employee('name', 'id', 'department')
    emp1.set_name('Suma')
    emp1.set_id('47899')
    emp1.set_department('Accounting')
    print(emp1)
end=time.perf_counter()
print()
print("time=",end-start)
