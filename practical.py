import cmath
print("enter a b c if quadratic equation is ax + by +c = 0")
a = int(input("enter a "))
b = int(input("enter b "))
c = int(input("enter c "))
dis= (b**2) - (4*a*c)

x= (-b-cmath.sqrt(dis))/(2*a)
y= (-b+cmath.sqrt(dis))/(2*a)

print("the roots of the equation are :")
print(x)
print(y)