'''
We are going to make a rock, paper ,cissor game!
'''
import random
computer = random.choice([0,-1,1])
youstr = input("Enter your choice: ")
youDict1={"Stone":1,"Paper":0,"Scissor":-1}
ReverseyouDict1={1:"Stone",0:"Paper",-1:"Scissor"}
you = youDict1[youstr]

print(f"Your Choice: {ReverseyouDict1[you]}")
print(f"Computer Choice: {ReverseyouDict1[computer]}")
if computer==you:
    print("It's Draw")
else:
    if computer==1 and you==0:
        print("You Won")
    elif computer==0 and you==-1:
        print("You Won")
    elif computer==-1 and you==1:
        print("You Won")
    else:
        print("You lose")