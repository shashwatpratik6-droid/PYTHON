
# n = int(input())

# rev = 0

# while n > 0:
#     digit = n % 10
#     rev = rev * 10 + digit
#     n = n // 10

# print(rev)

# i = 1
# while i<=5:
#     print(i**3, end=" ")
#     i +=1

# i = 1
# while i<=10:
#     print(i)
#     i+=2

# product=1
# number=1
# while number<=5:
#     product=number*product
#     number+=1
# print(product)

# x = "Hello World"
# y = x[::-1]
# # print(y)

# loan =  int(input())
# installment = int(input())
# left=loan
# c=0
# while left>0:
#     c+=1
#     if left<installment:
#         left=0
#         print(f"Month {c}: Balance left = 0")
#     else:
#         left=left-installment
#         print(f"Month {c}: Balance left = {left}")
    
# print("Loan cleared after",c,"month(s)")

battery = int(input())
drain = int(input())
i = 0
while battery>0:
        i+=1
        battery = battery -drain
        if battery>0:
                if battery<=20 and battery>10:
                        print(f"Hour  {i}: Battery = {battery}% (Low battery)")  
                else:
                        print(f"Hour  {i}: Battery = {battery}%")
        elif battery<=0:
                print(f"Hour  {i}: Battery = 0%")
        else:
                print("")
print(f"Phone died after {i} hour(s).")


