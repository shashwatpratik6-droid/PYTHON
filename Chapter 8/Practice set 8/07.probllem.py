def table(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n*i}")


n = int(input("Enter a number: "))
x = table(n)
print("The multiplication table ", n , "is:", x)