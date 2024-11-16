# Welcome to calculator!!!!
print("\n========== Welcome to Calculator! ==========\n")

while True:

    # What would you like to do? (add, sub, mult, div)
    choice = int(input("1 - Add, 2 - Subtract, 3 - Multiply, 4 - Divide, 5 - Quit: "))

    # add
    if choice == 1:
        a = int(input("Enter number: "))
        b = int(input("Enter another number: "))
        print(print(f"{a} + {b} = ", a + b))

    # Subtraction
    elif choice == 2:
        a = int(input("Enter number: "))
        b = int(input("Enter another number: "))
        print(print(f"{a} - {b} = ", a - b))

    # Multiplication
    elif choice == 3:
        a = int(input("Enter number: "))
        b = int(input("Enter another number: "))
        print(print(f"{a} * {b} = ", a * b))

    # Division
    elif choice == 4:
        a = int(input("Enter number: "))
        b = int(input("Enter another number: "))
        print(print(f"{a} / {b} = ", a / b))

    else:
        print("Bye!")
        break