
import math

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

funct = int(input("Enter a number to continue: "))

if funct == 1:
    num1 = int(input("First Number: "))
    num2 = int(input("Second Number: "))
    num3 = num1 + num2
    print(f"The sum is = {num3}")

if funct == 2:
    num1 = int(input("First Number: "))
    num2 = int(input("Second Number: "))
    num3 = num1 - num2
    print(f"The difference is = {num3}")

if funct == 3:
    num1 = int(input("First Number: "))
    num2 = int(input("Second Number: "))
    num3 = num1 * num2
    print(f"The product is = {num3}")

if funct == 4:
    num1 = int(input("First Number: "))
    num2 = int(input("Second Number: "))
    num3 = num1 / num2
    print(f"The quotient is = {num3}")

if funct == 5:
    num = int(input("Enter the Number: "))
    square = num * num
    print(f"The square is = {square}")

if funct == 6:
    num = int(input("Enter the Number: "))
    cube = num * num * num
    print(f"The cube is = {cube}")

if funct == 7:
    num = int(input("Enter the Number: "))
    sqroot = math.sqrt((num))
    print(f"The Square Root of the Number is: {sqroot}")

if funct == 8:
    num = int(input("Enter the Number: "))
    cbroot = math.cbrt(num)
    print(f"The Cube Root of the Number is: {cbroot}")

print("Thank you for using our Calculator!")

