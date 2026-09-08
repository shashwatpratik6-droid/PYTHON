x=int(input("Enter your marks: "))
if(x<=100 and x>=90):
    grade="A"
elif(x<90 and x>=80):
    grade="B"   
elif(x<80 and x>=70):
    grade="C"   
elif(x<70 and x>=60):
    grade="D"   
elif(x<60 and x>=50):
    grade="E"   
elif(x<50 ):
    grade="F"   
print("Your grade is: ", grade)
    