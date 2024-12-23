# 1topshiriq
# for x in range(1,100):
#     if x%2==0:
#         print("juft sonlar",x)
#     else:
#         print("toq sonlar",x)
#------------------------------------
# n=int(input("son kiriting="))
# for x in range(1,n):
#     x=(n*(n+1))/2
#     print(x)
#     break
#------------------------------------
# n=int(input("son kiriting="))
# suma=0
# yig=0
# for x in range(1,n,2):
#     suma+=x
# print(suma)
# for a in range(2,n,2):
#     yig+=a
# print(yig)
#-----------------------------------
# a=[1,4,5,7,9,10]
# b=[5,6,7,9,12,45]
# c=[]
# for x in a:
#     for y in b:
#         c.append(x*y)
#
# print(c)
# #--------------------------------
from queue import PriorityQueue

# a=int(input("son kiriting="))
# b=[]
# for x in str(a):
#     b.append(int(x))
#     y=sum(b)
# print(y)
#--------------------------------
# import math
#
# a=[1,2,3]
# b=[]
# for x in a:
#     b.append(math.factorial(x))
# print(b)

#--------------------------------
a=[]
for x in range(1,101):
    if x%4==0 and x%3==0:
        a.append(x)
print(a)