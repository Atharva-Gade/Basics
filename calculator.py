
print("Welcome to the Calculator! \n Select a function to continue: \n " 
"1. Addition \n" \
" 2. Subtraction \n" \
" 3. Multiplication \n" \
" 4. Division \n" \
" 5. Square \n" \
" 6. Cube \n")

funct = int(input("Enter a number to continue: "))

if funct == 1:
    num1 = int(input("First Number: "))
    num2 = int(input("Second Number: "))
    num3 = num1 + num2
    print("The sum is =", num3)

if funct == 2:
    num1 = int(input("First Number: "))
    num2 = int(input("Second Number: "))
    num3 = num1 - num2
    print("The difference is =", num3)

if funct == 3:
    num1 = int(input("First Number: "))
    num2 = int(input("Second Number: "))
    num3 = num1 * num2
    print("The product is =", num3)

if funct == 4:
    num1 = int(input("First Number: "))
    num2 = int(input("Second Number: "))
    num3 = num1 / num2
    print("The quotient is =", num3)

if funct == 5:
    num = int(input("Enter the Number: "))
    square = num * num
    print("The square is =", square)

if funct == 6:
    num = int(input("Enter the Number: "))
    cube = num * num * num
    print("The cube is =", cube)

print("Thank you for using our Calculator!")

