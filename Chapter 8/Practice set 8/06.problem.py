def inch_to_cm(inch):
    cm = inch * 2.54
    return cm   


n = int(input("Enter length in inch: "))
c = inch_to_cm(n)
print("Length in cm is:", c)