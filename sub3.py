
x = str(input(" Enter Your Marks According To Following Subjects: "))
print(x)

y = int(input(" Science \n "))

if y < 33:
    print(y)

z = int(input(" SS \n "))

if z < 33:
    print(z)

a = int(input(" English \n "))

if a < 33:
    print(a)

b = int(input(" Maths \n "))

if b < 33:
    print(b)

c = int(input(" Gujrati \n "))

if c < 33:
    print(c)

##
s = ( y or z or a or b or c )

if s < 33:
    print(" Failed ")
else:
    print(" Passed ")
##

q = input(" Total Marks ")
q = y + z + a + b + c
print(q,"/500")


r = input(" Your Percentage: ")
r = q*100/500
print(r,"%")


w = str(input(" Your Grade: "))
print(w)


if r > 90:
    print(" Grade A ")

elif r > 80:
    print(" Grade B ")

elif r > 65:
    print(" Grade C ")

elif r > 50:
    print(" Grade D ")

elif r > 40:
    print(" Grade E ")

elif r < 40:
    print(" Grade F ")








