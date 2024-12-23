# bizda son musbatlikka tekshirish va juft bo'lsa uni darajaga ko'tarish kerak bo'ladi
from time import process_time

from queue import PriorityQueue

import math

# Biz bu kodda 2 masalani hammasini bir marta kiritish orqali hisoblasak bo'ladi
# son=int(input("Bu yerga son kiriting="))
#
# if son!=0: # bu yerda kirib keladigan sonni katta yoki kichiklikka tekshiradi
#     son1=son%2 # bu yerda esa son ni 2 bo'lib qoldig'ini olib yangi o'zgaruvchiga yuklab qo'yadi
#     if son1==0: # bu yerda esa son1 ni 0 ga teng ekanligini tekshiradi
#         if son<0: # bu yerda esa son ni 0 dan kichiklikka tekshiradi
#             son2=son*-1
#             print('Son moduli',son2)
#             exit()
#         else:
#             son=son**2
#             print("juft soning kvadrati",son)
#             exit()
#     else:
#         if son<0:
#             # aslida manfiy sondan ildiz chiqarib bo'lmaydi
#             # lekin esa biz sonni musbat ko'rnishga keltirib undan ildiz olishimiz mumkin
#             son2=son*-1
#             son2=math.sqrt(son2)
#             print("ildizdan chiqarish",son2)
#             exit()
#         else:
#             son=son**3
#             print('toq son kubi=',son)
#             exit()
# else:
#     print('son nolga teng')
# 2.1 kettdi

# if son>0:
#     son1=son%2
#     if son1==0:
#         son=son**2
#         print("natija=",son)
#     else:
#         print("son toq son hisoblanadi:")
# else:
#     print("son musbat bo'lsin")
# if son>0:
#     son1=son%2
#     if son1==1:
#         son=son**3
#         print("juft soning kubi",son)
#         exit()
#     else:
#         print('Son juft ekan')
#         exit()
# print('bu son manfiy hisoblanadi')
# # 2.2 ketdi

# if son<0:
#     son1=son%2
#     if son1==0:
#         son2=son*-1
#         print("Natija=",son2)
#         exit()
#     else:
#         print("Bu son manfiy toq hisoblanadi")
#         exit()
# else:
#     print("Siz manfiy son kiriting")
# 2.3 ketdi
# if son<0:
#     son1=son%2
#     if son1==1:
#         son=son*-1
#         son2=math.sqrt(son)
#         print("Natija=",son2)
#         exit()
#     else:
#         print("Bu son manfiy juft hisoblanadi")
#         exit()
# else:
#     print("Siz manfiy son kiriting")

# if son==0:
#     print("son nolga teng")

# x=int(input('son kiriting='))
# y=int(input('son kiriting='))
# a=int(input('son kiriting='))
# b=int(input('son kiriting='))
# c=int(input('son kiriting='))
#-------------------------------------------------------------
# x=float(input('son kiriting='))
# y=float(input('son kiriting='))
# if x>y:
#     z=x-y
#     print("natija=",z)
# else:
#     z=y-x+1
#     print("natija=",z)
#--------------------------------------------------------------
# x=float(input('son kiriting='))
# y=float(input('son kiriting='))
# if x>y:
#     print("natija=",x)
# else:
#     print("natija=",y)
#------------------------------------------------------------
# x= float(input('son kiriting='))
# y=float(input('son kiriting='))
# if x<=y:
#     x*=0
#     print('natija=',x)
# else:
#     print("natija=",x)
#-------------------------------------------------------------
# x=float(input('son kiriting='))
# y=float(input('son kiriting='))
# c=float(input(" son kiriting"))
#
# if 1<x<3 or 1<y<3 or 1<c<3:
#     print(" Bu sonlar (1,3) oralig'ida yotadi ")
# else:
#     print(" yo'q bular (1,3) oralig'ida yotmaydi ")
#-----------------------------------------------------------
# yil=int(input("yil kiriting="))
# if yil%4==0 or yil%100!=0 or yil%400==0:
#     print("bu yil kabisa yili",yil)
# else:
#     print(" kabisa yili emas",yil)

#-------------------------------------------------------------

# a=int(input("son kiriting"))
# b=int(input("son kiriting"))
# c=str(input("amal kiritning"))
# if c=="+":
#     natija=a+b
#     print(natija)
#     exit()
# elif c=="-":
#     natija=a-b
#     print(natija)
#     exit()
# elif c=="*":
#     natija=a*b
#     print(natija)
#     exit()
# elif c=="/":
#     if b!=0:
#         natija=a/b
#         print(natija)
#         exit()
#     else:
#         print("sonni no'lga  bo'lib bo'lmaydi")
#         exit()
# else:
#     print(" to'g'ri ammal kiriting")
#----------------------------------------------------------
# a=int(input("son kiriting"))
# c=int(input("son kiritning"))
# if a<0 and b<0 and c<0:
#     print(" musbat son kiriting")
# elif a+b>c or a+c>b or c+b>a:
#     if a==b or a==c or b==c:
#         print(" teng yonli uchburchak")
#     elif a==b==c:
#         print("teng tomonli uchburchak")
#     else:
#         print("turli tomonli uchburchak")
# else:
#     print("uchburchak yasab bo'lmaydi")
# b=int(input("son kiriting"))
#----------------------------------------------------------
a=int(input("son kiriting"))
b=int(input("son kiriting"))
c=int(input("son kiritning"))
d=int(input('son kiriting'))
e=int(input('son kiriting'))
if a>b and a>c and a>d and a>e:
    print('eng katta son',a)
elif b>a and b>c and b>d and b>e:
    print(" eng katta son",b)
elif c>a and c>b and c>d and c>e:
    print("eng katta son",c)
elif d>a and d>b and d>c and d>e:
    print("eng katta son",d)
elif e>a and e>b and e>c and e>d:
    print(" eng katta son",e)
else:
    print("bu sonlar teng")
#--------------------------------------------------------

# x=int(input("son kiriting"))
# y=int (input("son kiriting"))
# a=int(input("son kiriting"))
# b=int(input("son kiriting"))
# c=int(input("son kiriting"))
# if a<=x and b<=y or a<=y and b<=x:
#     print("sig'adi")
# elif b<=x and c<=y or b<=y and c<=x:
#     print("sig'adi")
# elif c<=x and a<=y or c<=y and a<=x:
#     print("sig'adi")
# else:
#     print("sig'maydi")

