x =float(input(" Enter Your Units \n"))
print(x)

a = (x * 1)
b = (x * 1.5)
c = (x * 2)


if x <= 200:
    print("Rs.", a)

elif x > 200 and x <= 300:
    print("Rs.", b)

elif x > 300 and x <= 400:
    print("Rs.", c)



y = x * 5/100             #duty tax
print("Rs.", y)

z = ( (a) or (b) or (c) ) + y  #duty tax + units expenses
print("Rs.", z)

u = z * 8/100             #GST
print("Rs.", u)

v = z + u                 #Total Expenses
print("Rs.", v)


