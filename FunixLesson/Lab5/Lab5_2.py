# nhap a, b. Tinh tong nhung so tu a den b (co chua b)

def CallSumOdd(a,b):
	n2 = 0
	while(a <= b):
		if a % 2 != 0:
			n2+= a
		a += 1
	return n2

a = int(input("a = : "))
b = int(input("b = : "))
if(a>b):
	print("Vui long nhap b>=a")
	a = int(input("a = : "))
	b = int(input("b = : "))
else:
	result = CallSumOdd(a,b)
	print(result)

a = int(input())
b = int(input())
answer = 0
for i in range(a, b + 1):
    if i % 2 != 0:
        answer += i
print(answer)

