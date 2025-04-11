
x = int(input(" Enter Your Salary: \n "))
print(x)

if x <= 100000:
    print(" No Tax ")
    print("Rs.", 0)

elif x > 100000 and x <= 300000:
    print(" 2% Tax ")
    print("Rs.", x * 2/100)

elif x > 300000 and x <= 700000:
    print(" 4% Tax ")
    print("Rs.", x * 4/100)

elif x > 700000 and x <= 1000000:
    print(" 6% Tax ")
    print("Rs.", x * 6/100)

else:
    print(" 11% Tax ")
    print("Rs.", x * 11/100)

