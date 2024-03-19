three_digit = int(input("Enter a three digit number:  "))
digit_1 = three_digit % 10
digit_2 = (three_digit//10) % 10
digit_3 = three_digit//100
sum_1_3 = digit_1 + digit_3
if sum_1_3 < digit_2:
    print("<")
elif sum_1_3 == digit_2:
    print("=")
else:
    print(">")