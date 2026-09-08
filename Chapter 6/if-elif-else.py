x = int(input("Enter a natural number: "))

if(x<0):
    print("Invalid number")
elif(x==0):
    print("not valid")
elif(x%2==0):
    print("The number is divisible by 2")
else:
    print("The number is not divisible by 2")