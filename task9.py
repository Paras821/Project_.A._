
def marks():
    x = str(" Your Marks According To Following Subjects: \n")
    print(x)

marks()

def a():
    p = int(85)
    print("Science \n " , p)

a()

def b():
    q = int(80)
    print("SS \n" , q)

b()

def c():
    r = int(95)
    print("English \n" , r)

c()

def d():
    s = int(90)
    print("Maths \n" , s)

d()

def e():
    t = int(80)
    print("Gujrati \n" , t)

e()

def y():
    o = int(85 + 80 + 95 + 90 + 80)
    print("Total Marks: \n" , o)

y()


def perc():
    z =float(430/5)
    print("Your Percentage: \n" , z)

    if z > 90 :
        result = "Grade A"
        print(result)

    elif z > 80 :
        result = "Grade B"
        print(result)

    elif z > 70 :
        result = "Grade C"
        print(result)

    elif z > 55 :
        result = "Grade D"
        print(result)

    elif z > 45 :
        result = "Grade E"
        print(result)

    else:
        result = "Failed"
        print(result)

perc()

