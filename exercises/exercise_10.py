x1 = int(input("What is the value of the x co-ordinate of point 1"))
y1 = int(input("What is the value of the y co-ordinate of point 1"))
x2 = int(input("What is the value of the x co-ordinate of point 2"))
y2 = int(input("What is the value of the y co-ordinate of point 2"))
x3 = int(input("What is the value of the x co-ordinate of point 3"))
y3 = int(input("What is the value of the y co-ordinate of point 3"))
length_1_2 = ((x2-x1)**2) + ((y2-y1)**2)
length_1_3 = ((x3-x1)**2) + ((y3-y1)**2)
length_2_3 = ((x3-x2)**2) + ((y3-y2)**2)
right_angle = ""
if length_1_2 + length_1_3 == length_2_3:
    right_angle = "yes"
elif length_1_2 + length_2_3 == length_1_3:
    right_angle = "yes"
elif length_1_3 + length_2_3 == length_1_2:
    right_angle = "yes"
else:
    right_angle = "no"
print(right_angle)