p1 = "make a lot of money"
p2 = "subscribe now"
p3 = "buy now"
x = input("Enter your message: ")
if(p1 in x or p2 in x or p3 in x ):
    print("This message is spam")
else:
    print("This message is not spam")