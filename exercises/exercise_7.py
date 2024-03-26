num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
operator = input("What is your arithmetic operator")
if operator == "+":
    result = num1 + num2
if operator == "*":
    result = num1 * num2
if operator == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        print("Division by 0!")
if operator == "-":
    result = num1 - num2
if operator == "mod":
    result = num1 % num2
if operator == "pow":
    result = num1 ** num2
if operator == "div":
    result = num1 // num2
print(result)