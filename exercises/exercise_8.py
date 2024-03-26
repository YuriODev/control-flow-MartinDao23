num = input("Enter a three digit number: ")
integer = input("What are you looking for? ")
inside = False
for i in range (len(num)):
    if num[i] == integer:
        inside = True 
print(inside)