x =float(input(" Enter Your Units \n"))
print(x)


a = x <= 200
b = x > 200 and x <= 300
c = x > 300 and x <= 400

d = a and b

if a:
    print("Rs.", x*1)

elif b:
    print("Rs.", x*1.5)

elif c:
    print("Rs.", x*2)


z = (a and b and c) * 5/100         #duty tax
print("Rs.", z)

#w = (x*1)+z or (x*1.5)+z or (x*2)+z
#print(w)


#u = z * 8/100         #GST
#print("Rs.", u)

#v= z + u              #Total Expenses
#print("Rs.", v)

