age = int(input("What age?  "))
person = ""
if age <= 1:
    person = "infant"
elif age <= 13:
    person = "child"
elif age <= 20:
    person = "teenager"
else:
    person = "adult"
print(f"{person}")