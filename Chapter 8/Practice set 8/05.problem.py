def pattern(n):
    if n == 0:
        return
    print("*" * n)
    pattern(n - 1)

n = int(input("Enter a number: "))
print("The pattern is:" , pattern(n))