'''
Cho hai số nguyên a và b được nhập từ bàn phím, 
bạn hãy viết chương trình đếm số các số chẵn và số các số lẻ trong khoảng từ a tới b. 
Sau đó hiển thị ra màn hình thông tin sau:
Number of even numbers: {P1}
Number of odd numbers: {P2}
'''
a = int(input())
b = int(input())
count_odd = 0
count_even = 0

while a<=b:
	if a%2==0:
		count_odd += 1
	else:
		count_even += 1
	a += 1

print("Number of even numbers:",count_even)
print("Number of odd numbers:",count_odd)