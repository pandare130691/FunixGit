#1
def sum_of_list(lst):
    ans = 0
    for i in lst:
        ans += i
    return ans

lst = []
n = int(input())
for i in range(n):
    lst.append(int(input()))
print(sum_of_list(lst))

#2
def max3(a, b, c):
    ans = a
    for i in [a,b,c]:
     if(i>ans):
      ans = i
    return ans

a = int(input())
b = int(input())
c = int(input())
print(max3(a, b, c))

#3
def show(input):
    nLower = 0;
    nUpper = 0
    for i in s:
     if i.isupper():
        nUpper += 1
     if i.islower():
        nLower += 1
    print("Given string:", input)
    print("Number of uppercase letters:", nUpper)
    print("Number of lowercase letters:", nLower)


s = str(input())
show(s)

#4
def get_unique_values(lst):
    ans = []
    for i in lst:
        if i not in ans:
            ans.append(i)
    return ans
n = int(input())
lst = []
for i in range(n):
    lst.append(int(input()))
print(get_unique_values(lst))

#5
def is_prime(n):
    rt = True
    if n==0:
        rt = False
    elif n==1:
        rt = True
    else:
        for i in range(1, n+1):
            if i!=1 and i!=n and n%i==0:
                rt = False
                break
    return rt

n = int(input())
print(is_prime(n))

