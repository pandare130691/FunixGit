#1
a = int(input())
h = int(input())

area = a*h/2

print("The area of triangle is", area)

#2
a = int(input())
b = int(input())
print(a**b)

#3
x = int(input())
y = int(input())
print("x > y:", x > y)

#4
a = int(input())
Total = int(input())
Total += a # Using += Operator
print("The Value of the Total after using += Operator is:", Total)
Total -= a # Using -= Operator
print("The Value of the Total after using -= Operator is:", Total)
Total *= a # Using *= Operator
print("The Value of the Total after using *= Operator is:", Total)
Total //= a # Using //= Operator
print("The Value of the Total after using //= Operator is:", Total)
Total **= a # Using **= Operator
print("The Value of the Total after using **= Operator is:", Total)
Total /= a # Using /= Operator
print("The Value of the Total after using /= Operator is:", Total)
Total %= a # Using %= Operator
print("The Value of the Total after using %= Operator is:", Total)

#5
x = input()
print('H' in x)

#6
a = int(input())
b = int(input())

print(a is b)

#7
x = int(input())
y = int(input())
z = int(input())
t = int(input())

print("Result evaluation is", (x > y) and (z < t))
