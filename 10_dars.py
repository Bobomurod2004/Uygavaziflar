# from datetime import datetime
# now = datetime.now()
# tugilgan = datetime(2004, 4, 16)
# farq = now - tugilgan
# print(f"Farq: {farq.days} kun")
# #-------------------------------
# from datetime import datetime
# for i in range(1):
#     now=datetime.now()
# 4-masla-----------------------
# def maxsulot(Maxsulot_nomi,Maxsulot_turi,Maxsulot_narxi):
#     my_dict={
#         'Maxsulot_nomi':Maxsulot_nomi,
#         'Maxsulot_narxi':Maxsulot_narxi,
#         'maxsulot_turi':Maxsulot_turi
#     }
#     return my_dict
# print()
# my_dict2=[]
# while True:
#     Maxsulot_nomi=input("Maxsulot nomini kiriting=")
#     Maxsulot_narxi=int(input("Maxsulot narxini kiriting="))
#     Maxsulot_turi=input("Maxsulot turini kiriting=")
#     yana=input("dasturni davom etirasizmi yes/no=")
#     my_dict2.append(maxsulot(Maxsulot_nomi,Maxsulot_narxi,Maxsulot_turi))
#     if yana.lower()=='no':
#         break
#     else:
#         print("qayta kiriting")
# print(my_dict2)
#5masala----------------------------
# def maxsulot(Maxsulot_nomi,Maxsulot_narxi,Maxsulot_turi):
#     my_dict={
#         'Maxsulot_nomi':Maxsulot_nomi,
#         'Maxsulot_narxi':Maxsulot_narxi,
#         'maxsulot_turi':Maxsulot_turi
#     }
#     return my_dict
# my_dict2=[]
# while True:
#     Maxsulot_nomi=input("Maxsulot nomini kiriting=")
#     Maxsulot_narxi=int(input("Maxsulot narxini kiriting="))
#     Maxsulot_turi=input("Maxsulot turini kiriting=")
#     yana=input("dasturni davom etirasizmi yes/no=").lower()
#     my_dict2.append(maxsulot(Maxsulot_nomi,Maxsulot_narxi,Maxsulot_turi))
#     if yana=='no':
#         break
#
# print(my_dict2)
# while True:
#     maxsulotlar=input("maxsulot nomini kiriting=").lower()
#     for maxsulot in my_dict2:
#         if maxsulot['Maxsulot_nomi'] == maxsulotlar:
#             print("maxsulot narxi=",maxsulot['Maxsulot_narxi'])
#         else:
#             print("bizda bunday maxsulot yo'q")
#         qidirish=input("yana maxsulot qidarasizmi (ha/yo'q)=").lower()
#         if qidirish=='yo\'q':
#             break
#masal-----------------------------
# import time
# for i in range(60,0,-1):
#     print(f'qolgan vaqt:{i}soniya',end="\r")
#     time.sleep(1)
# print('\n vaqt tugadi')
# ----------------------------------
# n=int(input("son kiriting"))
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(j,end=' ')
#     print()

