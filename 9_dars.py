# def tuloq_ism(ism,familiya):
#     print(f'foydalanuvchi ismi={ism.title()}','\n' f'foydalanuvchi familiyasi={familiya.title()}')
# tuloq_ism(ism="alijon",familiya='toshbulov')
#1masala-----------------
# def hisoblash(ism,yosh,joriy=2024):
#     print(f"ismingiz={ism} va tug'ulgan yiliz {yosh-joriy} yil")
# aism=input("ismnigizni kiriting=")
# byosh=int(input("yoshingizni kiriting="))
# hisoblash(aism,byosh)
#2masala-------------------
# def funksiya():
#     son=ason**2
#     son1=ason**3
#     print("soning kvadrati=",son,"\nsoning kubi=",son1)
# ason=int(input("Son kiriting="))
# funksiya()
# 3masala-----------------------
# def tekshirish():
#     if son%2==0:
#         print("son juft son")
#     else:
#         print("son toq")
# son=int(input("son kiriting="))
# tekshirish()
#4masala------------------------
# def katta():
#     while True:
#         son1=int(input("1 chi son kiriting="))
#         son2=int(input("2 chi sonni kiriting="))
#         if son1>son2:
#             print("katta son=",son1)
#         elif son2>son1:
#             print("katta son=",son2)
#         else:
#             print("Bu ikki son teng")
# katta()
#5masala-----------------------
# def kotaruvch():
#     while True:
#         x=int(input("son kiriting="))
#         y=int(input("son kiriting="))
#         print(f"sonni darajaga ko'tarish={x ** y}")
# kotaruvch()
#6masala------------------------
# def kotaruvch(y,y1):
#     while True:
#         x=int(input("son kiriting="))
#         # y=int(input("son kiriting="))
#         print(f"sonni darajaga ko'tarish={x ** y} va {x**y1}")
# kotaruvch(y=3,y1=2)
#7masala---------------------
# def bolish():
#     son=int(input("son kiriting="))
#     for i in range(2,11):
#         if son%i==0:
#             print("qoldiqsiz bo'linadigan=",i)
#         else:
#             print("qoldiqli bo'ladi=",i)
# bolish()
#8masala---------------------
def foydalanuvchi(ims,familiyasi,yoshi,tugulgan_yili,tugulgan_joyi,emil,tel_raqam):
    user2={
        'Ismi':ims,
        'Familiyasi':familiyasi,
        "Yoshi":yoshi,
        "Tug'ulganyili":tugulgan_yili,
        "tug'lgan joyi":tugulgan_joyi,
        "Email":emil,
        "Telefon raqami":tel_raqam
    }
    return user2
print("ro'yxatni shakillantiramiz")
user1=[]
while True:
    print("bazi ma'lumotlarni kiriting")
    ims=input("Ismingizni kiriting=")
    familiyasi=input("Familiyangizni kiriting=")
    yoshi=int(input("Yoshingizni kiriting="))
    tugulgan_yili=int(input("Tug'ulgan yilingizni kiriting="))
    tugulgan_joyi=input("Tug'ulgan joyingiz=")
    emil=input('Email-ingizni kiriting=')
    tel_raqam=int(input("Telefon raqamizni kiriting="))
    user1.append(foydalanuvchi(ims,familiyasi,yoshi,tugulgan_yili,tugulgan_joyi,emil,tel_raqam))
    keyingi=input("yana ma'lumot qo'shasizmi(yes/no)=")
    if keyingi=='no':
        break
print(user1)
# 9-masala---------------------
# def sonlar():
#     while True:
#         son1 = int(input("son kiriting="))
#         son2 = int(input("son kiriting="))
#         son3 = int(input("son kiriting="))
#         if son1>son2>son3:
#             print( "Eng katta=",son1)
#         elif son1<son2>son3:
#             print("eng katta son=",son2)
#         else:
#             print('eng katta son=',son3)
#         a=input("exit yoki qolmoq deb yozing=")
#         if a=='exit':
#             break
# sonlar()
#10 masala----------------------
# def talaba(ism_familiya,yosh, kursi,):
#     talaba_dict={
#         'Ism familiya':ism_familiya,
#         "Yosh":yosh,
#         "Kurs":kursi,
#     }



