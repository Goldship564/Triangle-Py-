input("Welcome, press Enter to continue")

a = int(input("Please input a"))
b = int(input("Please input b"))
c = int(input("Please input c"))

def sum(a,b):
    return (a+b)

print(sum(a,b))

if sum(a,b)>=c:

    print("It is a triangle")

else:

    print("It is not a triangle")