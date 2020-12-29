#1
#s = input()
#print(s.upper())

#2
#s = input()
#if len(s)<2:
#    print("")
#else:
#    print(s[:2]+s[-2:])

#3
#s1 = input()
#s2 = input()
#s11 = s2[:2]+s1[2:]
#s2 = s1[:2]+s2[2:]
#s1 = s11
#print(s1 + " " + s2)

#4
s = str(input())
print(' '.join(reversed(s.split(" "))))
