f = open("file.txt")
print(f.read())
f.close
# all the close and open can be down by with statement.


with open("file.txt") as f:
    print(f.read())