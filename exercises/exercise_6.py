x1 = int(input("What is the x co-ordinate of point 1"))
y1 = int(input("What is the y co-ordinate of point 1"))
x2 = int(input("What is the x co-ordinate of point 2"))
y2 = int(input("What is the y co-ordinate of point 2"))
distance1 = ((x1**2)+(y1**2))**(1/2)
distance2 = ((x2**2)+(y2**2))**(1/2)
if distance1>distance2: 
    output = "A is further from the origin"
elif distance1==distance2 :
    output = "A and B are at the same distance from the origin"
else:
    output = "B is further from the origin"
print(output)