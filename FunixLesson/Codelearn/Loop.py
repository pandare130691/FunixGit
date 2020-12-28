#1
n1 = int(input())
sum =0
for i in range(1,n1+1):
	sum += i
print(sum)

#2
a = int(input())
b = int(input())
answer = 0
for i in range(a, b + 1):
    if i % 2 != 0:
        answer += i
print(answer)

#3
s = input()
for c in s:
    if(c!='y'):
     print("Current character:", c)

#4
n = int(input())
b = 1
while b <= 5:
    print(n, "*", b, "=", n * b)
    b += 1

#5
a = int(input())
b = int(input())
count_odd = 0
count_even = 0
while a<=b:
	if a%2==0:
		count_even += 1
	else:
		count_odd += 1
	a += 1
print("Number of even numbers:",count_even)
print("Number of odd numbers:",count_odd)

#6
n = int(input())
sum = 0
for i in range(1, n+1):
	sum += i/(i+1)
sum = round(sum, 2)
print(sum)
