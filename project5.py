# Employee Management System

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("\nPerson Details")
        print("Name :", self.name)
        print("Age :", self.age)

class Employee(Person):

    def __init__(self, name, age, emp_id, salary):
        super().__init__(name, age)
        self.__emp_id = emp_id
        self.__salary = salary

    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        self.__salary = salary

    def display(self):

        print("\nEmployee Details")
        print("Name :", self.name)
        print("Age :", self.age)
        print("Employee ID :", self.__emp_id)
        print("Salary :", self.__salary)
    
class Manager(Employee):
    def __init__(self, name, age, emp_id, salary, department):
        super().__init__(name, age, emp_id, salary)
        self.department = department

    def display(self):
        print("\nManager Details:")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Employee ID:", self.get_emp_id())
        print("Salary: $", self.get_salary())
        print("Department:", self.department)

class Developer(Employee):

    def __init__(self, name, age, emp_id, salary, language):
        super().__init__(name, age, emp_id, salary)
        self.language = language

    def display(self):
        print("Developer Details")
        super().display()
        print("Programming Language :", self.language)

while True:

    print("\nWelcome to the Employee Management System")
    print("choose an option:")
    print("1. Create Person")
    print("2. Create Employee")
    print("3. Create Manager")
    print("4. Show Details")
    print("5. Exit")

    choice = int(input("\nEnter Your Choice : "))

    if choice == 1:
        name = input("Enter Name : ")
        age = int(input("Enter Age : "))
        p = Person(name, age)
        print(f"\nPerson created with name: {name} and age: {age}.")
    
    elif choice == 2:

        name = input("Enter Name : ")
        age = int(input("Enter Age : "))
        emp_id = input("Enter Employee ID : ")
        salary = float(input("Enter Salary : "))
        e = Employee(name, age, emp_id, salary)
        print(f"\nEmployee created with name: {name}, age: {age}, employee ID: {emp_id}, and salary: ${salary}.")

    elif choice == 3:

        name = input("Enter Name : ")
        age = int(input("Enter Age : "))
        emp_id = input("Enter Employee ID : ")
        salary = float(input("Enter Salary : "))
        department = input("Enter Department : ")
        m = Manager(name, age, emp_id, salary, department)
        print(f"\nManager created with name: {name}, age: {age}, employee ID: {emp_id}, salary: ${salary}, and department: {department}.")
    
    elif choice == 4:

        print("\nChoose details to show:")
        print("1. Person")
        print("2. Employee")
        print("3. Manager")

        show = int(input("Enter your choice: "))

        if show == 1 and p:
            p.display()

        elif show == 2 and e:
            e.display()

        elif show == 3 and m:
            m.display()

        else:
            print("No data found.")

        
    elif choice == 5:
        print("Exiting the Employee Management System. Goodbye!")
        break

    else:
        print("Invalid Choice")
    print("\n ---Choose another operation---")

        
        