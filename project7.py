import datetime
import time
import math
import random
import uuid

def create_file():
    name = input("Enter file name: ")
    open(name, "w").close()
    print("File created successfully!")

def write_file():
    name = input("Enter file name: ")
    data = input("Enter data to write: ")

    f = open(name, "w")
    f.write(data)
    f.close()

    print("Data written successfully!")

def read_file():
    name = input("Enter file name: ")

    f = open(name, "r")
    print("File Content:")
    print(f.read())
    f.close()

def append_file():
    name = input("Enter file name: ")
    data = input("Enter data to append: ")

    f = open(name, "a")
    f.write("\n" + data)
    f.close()

    print("Data appended successfully!")

def datetime_menu():

    while True:

        print("\nDatetime and Time Operations")
        print("1. Display current date and time")
        print("2. Difference between two dates")
        print("3. Format current date")
        print("4. Stopwatch")
        print("5. Countdown Timer")
        print("6. Back")

        ch = int(input("Enter your choice: "))

        if ch == 1:
            now = datetime.datetime.now()
            print("Current Date and Time:", now)

        elif ch == 2:
            d1 = input("Enter first date (YYYY-MM-DD): ")
            d2 = input("Enter second date (YYYY-MM-DD): ")

            date1 = datetime.datetime.strptime(d1, "%Y-%m-%d")
            date2 = datetime.datetime.strptime(d2, "%Y-%m-%d")

            print("Difference:", abs((date2-date1).days), "days")

        elif ch == 3:
            now = datetime.datetime.now()
            print(now.strftime("%d-%m-%Y %H:%M:%S"))

        elif ch == 4:
            start = time.time()
            input("Press Enter to stop stopwatch...")
            end = time.time()
            print("Time:", round(end-start,2), "seconds")

        elif ch == 5:
            sec = int(input("Enter seconds: "))

            while sec:
                print(sec)
                time.sleep(1)
                sec -= 1

            print("Time Up!")

        elif ch == 6:
            break

def math_menu():

    while True:

        print("\nMathematical Operations")
        print("1. Factorial")
        print("2. Compound Interest")
        print("3. Trigonometry")
        print("4. Area of Circle")
        print("5. Back")

        ch = int(input("Enter your choice: "))

        if ch == 1:
            n = int(input("Enter number: "))
            print("Factorial:", math.factorial(n))

        elif ch == 2:
            p = float(input("Principal Amount: "))
            r = float(input("Rate: "))
            t = float(input("Time: "))

            ci = p * ((1 + r/100) ** t)

            print("Compound Interest:", round(ci,2))

        elif ch == 3:
            angle = float(input("Enter angle: "))
            print("Sin =", math.sin(math.radians(angle)))
            print("Cos =", math.cos(math.radians(angle)))
            print("Tan =", math.tan(math.radians(angle)))

        elif ch == 4:
            r = float(input("Enter radius: "))
            print("Area =", math.pi * r * r)

        elif ch == 5:
            break

def random_menu():

    while True:

        print("\nRandom Data Generation")
        print("1. Random Number")
        print("2. Random List")
        print("3. Random Password")
        print("4. Random OTP")
        print("5. Back")

        ch = int(input("Enter your choice: "))

        if ch == 1:
            print(random.randint(1,100))
        elif ch == 2:
            data = random.sample(range(1,100),5)
            print(data)
        elif ch == 3:
            chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789"
            length = int(input("Password Length: "))

            password = ""

            for i in range(length):
                password += random.choice(chars)

            print("Password:", password)
        elif ch == 4:
            otp = random.randint(1000,9999)
            print("OTP:", otp)
        elif ch == 5:
            break
        
def generate_uuid():
    print("Generated UUID:", uuid.uuid4())

def explore_module():
    module_name = input("Enter module name: ")

    if module_name == "math":
        print(dir(math))
    elif module_name == "random":
        print(dir(random))
    elif module_name == "datetime":
        print(dir(datetime))

    else:
        print("Module not available")
        
def file_menu():

    while True:

        print("\nFile Operations")
        print("1. Create File")
        print("2. Write File")
        print("3. Read File")
        print("4. Append File")
        print("5. Back")

        ch = int(input("Enter your choice: "))

        if ch == 1:
            create_file()
        elif ch == 2:
            write_file()
        elif ch == 3:
            read_file()
        elif ch == 4:
            append_file()
        elif ch == 5:
            break

def main():

    while True:

        print("\n==============================")
        print("Welcome to Multi Utility Toolkit")
        print("==============================")

        print("1. Datetime and Time Operations")
        print("2. Mathematical Operations")
        print("3. Random Data Generation")
        print("4. Generate UUID")
        print("5. File Operations")
        print("6. Explore Module Attributes")
        print("7. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            datetime_menu()
        elif choice == 2:
            math_menu()
        elif choice == 3:
            random_menu()
        elif choice == 4:
            generate_uuid()
        elif choice == 5:
            file_menu()
        elif choice == 6:
            explore_module()
        elif choice == 7:
            print("thank you for using Multi Utility Toolkit. Goodbye!")
            break

        else:
            print("Invalid Choice")


if __name__ == "__main__":
    main()