#1
age = int(input())
if age <5:
 print("Your cat is young")
else:
 print("Your cat is old")

 #2
 temperature = int(input())

if temperature>=100:
 print("Stay at home and enjoy a good movie")
elif temperature>=92:
 print("Stay at home")
elif temperature==75:
 print("Go outside and enjoy the weather")
elif temperature<0:
 print("It's cool outside")
else:
 print("Let's go to school")

 #3
 x = int(input())
y = int(input())
z = int(input())

if x%2==0:
 if y>=20:
  print("y is greater than or equal to 20")
 else:
  print("y is less than 20")
else:
 if z>=30:
  print("z is greater than or equal to 30")
 else:
  print("z is less than 30")

  #4
  a = int(input())
b = int(input())
c = int(input())
avg = (a+b+c)/3

if(avg>a and avg >b):
 print("The average value is greater than both a and b")
if(avg>a and avg>c):
 print("The average value is greater than both a and c")
if(avg>b and avg>c):
 print("The average value is greater than both b and c")
if(avg>a and avg<=b and avg<=c):
 print("The average value is greater than a")
if(avg>b and avg<=a and avg<=c):
 print("The average value is greater than b")
if(avg>c and avg<=a and avg<=b):
 print("The average value is greater than c")

 #5
 age = int(input())

if age<=0:
 print("This can hardly be true")
if age==1:
 print("About 1 human year")
if age==2:
 print("About 2 human years")
if age>2:
 print("Over 5 human years")
