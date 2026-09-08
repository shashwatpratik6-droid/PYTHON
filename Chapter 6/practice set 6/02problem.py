a = int(input("Enter maths marks: "))
b = int(input("Enter physics marks: "))
c = int(input("Enter chemistry marks: "))
total_percentage =((a+b+c)/300 *100 )
if(total_percentage >= 40 and a>33 and b>33 and c>33):
    print("pass:" , total_percentage)
else:
    print("fail:" , total_percentage)    