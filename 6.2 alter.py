
x = float(input("Enter Your Units \n"))

a = (x - 200)
b = (x - 300)


if x <= 200:
    print("Rs.", x * 1 )

elif x <= 300:
    print("Rs.", (200 * 1) + (a * 1.5) )

elif x <= 400:
    print("Rs.", (200 * 1) + (100 * 1.5) + (b * 2) )



