number = int(input("Enter a number between 0 and 36:   "))
colour = ""
if number == 0:
    colour = "green"
elif number <= 10:
    colour = "red" if number%2 == 1 else "black"
elif number <= 18:
    colour = "black" if number%2 == 1 else "red"
elif number <= 28:
    colour = "red" if number%2 == 1 else "black"
else:
    colour = "black" if number%2 == 1 else "red"
print(colour)