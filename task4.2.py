
x = input("Enter a number: \n")
y = int(x)

if y > 1:
    for i in range(2,y):
        if(y%i)==0:
            print(y,"is a Composite number")
            break
    else:
        print(y,"is a Prime number")

else:
    print(y,"is Neutral")

