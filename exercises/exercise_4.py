grade = int(input("Enter the grade:   "))
output = ""
if 1 > grade > 9:
    output = "level is absent"
elif grade <= 3:
    output = "initial level"
elif grade <= 6:
    output = "average level"
elif grade <= 9:
    output = "sufficient level"
else:
    output = "high level"
print(output)