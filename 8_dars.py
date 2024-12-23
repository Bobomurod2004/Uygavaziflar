# while True:
#     a = input("siz yaxshi ko'rgan kitobingizni kiriting=")
#     if a.lower()=='stop':
#         print("to'xtatildi")
#         break
#     else:
#         print(a)
#---------------------------------------------------
# while True:
#     yosh=int(input("yoshingizni kiriting="))
#     if yosh<7:
#         print("chipta narxi 2000 so'm")
#         break
#     elif 7<=yosh<=18:
#         print("chipta narxi 3000 so'm")
#         break
#     elif 18<yosh<=65:
#         print('chipta narxi 10000 so\'m')
#         break
#     else:
#         print("sizga tekin")
#         break

# mylist=[]
# while True:
#     mhsulot_nomi=input("mahsulot nomini kriiting: ")
#     if mhsulot_nomi=='exit':
#         break
#     mylist.append(mhsulot_nomi)
# print(mylist)

#----------------------------------------------
# a=[]
# while True:
#     maxsulot= input("maxsulot kiriting=")
#     if maxsulot.lower()=='stop':
#         print("to'xtatildi")
#         break
#     else:
#         a.append(maxsulot)
#         print(a)
#---------------------------------------------
# my_dict={}
# while True:
#     maxsulot_nomi=input("maxsulot nomini kiriting=")
#     if maxsulot_nomi.lower()=="stop":
#         print("dastur to'xtadi")
#         break
#
#     narxi=input("maxsulot narxini kiriting=")
#     if narxi.isdigit():
#         my_dict[maxsulot_nomi]=narxi
#     else:
#         print("son kiriting")
# print("maxsulot narxlari=")
# for maxsulot_nomi,narxi in my_dict.items():
#     print('narx',maxsulot_nomi,narxi)

