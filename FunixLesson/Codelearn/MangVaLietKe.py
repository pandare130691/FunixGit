#1
n = int(input())
lst = []
for i in range(n):
    lst.append(int(input()))
print(min(lst))

#2
n = int(input())
lst = []
for i in range(n):
    lst.append(int(input()))
print(sum(lst))

#3
lst = []
n = int(input())
for i in range(n):
    lst.append(int(input()))
lst.sort(reverse=False)
print(lst)

#4
lst = []
n = int(input())
for i in range(n):
    lst.append(int(input()))
lst2 = []
for i in lst:
    if(i%2!=0):
        lst2.append(i)
print(lst2)

#5
lst = []
n = int(input())
for i in range(n):
    lst.append(int(input()))
lst2 = list()
for i in lst:
    if i%5==0:
        lst2.append(i)
if len(lst2)==0:
    lst2 = [0]
print(lst2)

