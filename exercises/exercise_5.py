a = int(input("Enter A  "))
b = int(input("Enter B  "))
c = int(input("Enter C  "))
if (b**2-4*a*c) < 0:
    print("ro real roots")
elif (b**2-4*a*c) == 0:
    root1 = (-b+(b**2-4*a*c)**0.5)/(2*a)
    print(root1)
else:
    root1 = (-b+(b**2-4*a*c)**0.5)/(2*a)
    root2 = (-b-(b**2-4*a*c)**0.5)/(2*a)
    print(f"{root1} and {root2}")