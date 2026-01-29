
import math

def run_calc ():

    print("Welcome to the Calculator 🧮 ! \nSelect a function to continue: \n" 
    " ---------------------------------- \n" \
    " 1. Addition \n" \
    " 2. Subtraction \n" \
    " 3. Multiplication \n" \
    " 4. Division \n" \
    " 5. Square \n" \
    " 6. Cube \n" 
    " 7. Square Root \n" \
    " 8. Cube Root \n"
    "----------------------------------")

    funct = int(input("Enter a number to continue:\n"))

    if funct == 1:
        num1 = int(input("First Number:\n"))
        num2 = int(input("Second Number:\n"))
        num3 = num1 + num2
        print(f"The Sum is = {num3}")

    elif funct == 2:
        num1 = int(input("First Number:\n"))
        num2 = int(input("Second Number:\n"))
        num3 = num1 - num2
        print(f"The Difference is = {num3}")

    elif funct == 3:
        num1 = int(input("First Number:\n"))
        num2 = int(input("Second Number:\n"))
        num3 = num1 * num2
        print(f"The Product is = {num3}")

    elif funct == 4:
        num1 = int(input("First Number:\n"))
        num2 = int(input("Second Number:\n"))
        num3 = num1 / num2
        print(f"The Quotient is = {num3}")

    elif funct == 5:
        num = int(input("Enter the Number:\n"))
        square = num * num
        print(f"The Square of the number is = {square}")

    elif funct == 6:
        num = int(input("Enter the Number:\n"))
        cube = num * num * num
        print(f"The Cube of the number is = {cube}")

    elif funct == 7:
        num = int(input("Enter the Number:\n"))
        sqroot = math.sqrt((num))
        print(f"The Square Root of the number is: {sqroot}")

    elif funct == 8:
        num = int(input("Enter the Number:\n"))
        cbroot = math.cbrt(num)
        print(f"The Cube Root of the number is: {cbroot}")

    else:
        print("Invalid Input entered. Please try again!")
        run_calc()

while True:
    run_calc()
    restart = input("Restart the Calculator? (y/n)\n")
    
    if restart == "n":
        print("Thank you for using out Calculator.")
        break

    if restart == "y":
        run_calc()



