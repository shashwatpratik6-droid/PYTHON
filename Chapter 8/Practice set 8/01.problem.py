def greatest():
    a = int(input("enter a number: "))
    b = int(input("enter a number: "))
    c = int(input("enter a number: "))
    if a > b and a > c:
        print("The greatest number is:", a)
    elif b > a and b > c:
        print("The greatest number is:", b)
    else:
        print("The greatest number is:", c)

greatest()