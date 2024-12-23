# kun=int(input("san kiriting"))
# if 1<=kun and kun<=10:
#     print("1 deka")
# elif 11<=kun and kun<=20:
#     print("2 deka")
# elif 21<=kun and kun<=30:
#     print("3 deka")
# else:
#     print("kun 30da katta bo'lmasin va mafiy son kiritmang")
#-------------------------------------------------------------
# yosh=int(input("Yoshingizni kiriting="))
# balans=float(input("Balansingizni kirting="))
# if yosh<18:
#     print("Kechirasiz siz kredit beriladigan yoshda emasiz:")
# elif 18<=yosh<=26:
#     if 10000<=balans:
#         kredit=balans*(30/100)
#         print("siz shuncha qiymatda pul olishigiz mumkin=",kredit)
#     else:
#         print("kechirasiz sizga limit berilmaydi15:")
# elif yosh>=26:
#     if 5000<=balans<=20000:
#
#         kredit=balans*(50/100)
#         print("siz shuncha qiyatda pul olishingiz mumkin---",kredit)
#     elif 20000<balans:
#         print("kechirasiz siz bank offisiga borib kredit olishingiz mumkin:")
#     else:
#         print("kechirasiz sizga limit berilmaydi--:")
# else:
#     print("to'g'ri son kiriting")
#----------------------------------------------------------------
# avto=int(input("avtomabil yili="))
# if avto>0 and avto<2024:
#     avto_yosh = 2024 - avto
#     print(avto_yosh)
# else:
#     print(" avtomabil yoshini to'g'ri kiriting")
#     exit()
#
# avto_narx=float(input("avtomabil narxini kiriting="))
# avto_tajriba=int(input("avtomabil boshqarish bo'yicha tajribangizni kirting="))
# if avto_yosh<=5:
#     if avto_tajriba<1:
#         sumg= avto_narx * (10 / 100)
#         if sumg>10000000:
#             suma=sumg-(sumg*0.05)
#             print("sizga chegirma=",suma)
#         else:
#             print("sizning sug'urta narxingiz=", sumg)
#     elif 1<=avto_tajriba<=3:
#         sumg=avto_narx*(7/100)
#         if sumg>10000000:
#             suma=sumg-(sumg*0.05)
#             print("sizga chegirma=",suma)
#         else:
#             print("sizning avto sug'urta narxingiz=",sumg)
#     elif avto_tajriba>3:
#         sumg=avto_narx*(5/100)
#         if sumg>1000000:
#             suma=sumg-(sumg*0.05)
#             print("sizga chegirma=",suma)
#         else:
#             print("sizga sug'urta narxi=",sumg)
#     else:
#         exit()
# elif avto_yosh>5:
#     if avto_tajriba<=3:
#         sumg=avto_narx*(8/100)
#         if sumg>10000000:
#             suma=sumg-(sumg*(5/100))
#             print("sizga chegirma=",suma)
#         print("sug'urta narxi=",sumg)
#     elif avto_tajriba>3:
#         sumg=avto_narx*(6/100)
#         if sumg>10000000:
#             suma=sumg-(sumg*(5/100))
#             print("sizga chegirma=",suma)
#         else:
#             print("sug'urta narxi1=",sumg)
#     else:
#         exit()
# else:
#     exit()