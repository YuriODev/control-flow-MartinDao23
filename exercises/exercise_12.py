number = input("Enter a four digit number")
first = int(number[0])
second = int(number[1])
third = int(number[2])
fourth = int(number[3])
if first%2 == 0:
    first = "*"
if second%2 == 0:
    second = "*"
if third%2 == 0:
    third = "*"
if fourth%2 == 0:
    fourth = "*"
print(str(first)+str(second)+str(third)+str(fourth))