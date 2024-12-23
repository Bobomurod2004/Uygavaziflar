# set={1,4,7,8,5}
# if 10 in set:
#     set.remove(10)
#     print(set)
#
# else:
#     set.add(10)
#     print(set)
# #----------------------------
# set1={2,4,6,8,10}
# set2={7,9,11,13,15}
# z=set1.union(set2)
# y=set1.difference(set2)
# print(z,'\n',y)
# print(set1.union(set2))
#-----------------------------
# set={'men','bugun',"zo'r",'kitob',"ko'rdim",'va','men','uni','oldim'}


# set={1,2,3,4,5,6,7,8,9,10}
# set2={5,6,7,8,9,10,11,12,13,14,15}
# x=set.difference(set2)
# print(x)
#------------------------------

# set={'alijon','umid',"muhammadjafar",'ruslan','bahodir'}
# set2={'bahodir','umid'}
# set3=set-set2
# print(set3)
#------------------------------
# talaba={
#     "name":"",
#     "age":'',
#     "fakultet":''
# }
# talaba["name"]=input("Ismni kirting=")
# talaba["age"]=input("Yoshni kiriting=")
# talaba["fakultet"]=input("Fakultetni kiriting=")
# print(talaba)
#-------------------------------
a=input("maxsulot nomi kiriting=")
maxsulot={"olma":2500,"nok":36000,'kitob':45000,'kiyim':450000}
if a in maxsulot:
    print(maxsulot.get(a))
else:
    print("maxsulot topilmadi")
print("max= ",max(maxsulot.values()))
#----------------------------------
#
#----------------------------------

# user={
#     "umid":942651079,
#     "azam ":995222232,
#     "aziz":989558855
# }
# user[""]=input("tel raqam kiriting")
#-----------------------------------
import  random
# b=random.randint(1,100)
# print(b)
# a=int(input("biron bir son kiriting="))
# if a==b:
#     print("siz kiritgan son teng")
# else:
#     print("siz kiritgan son teng emas")
#------------------------------------
# foy='umid','ali','vali','kali'
# print("g'olib=",random.choice(foy))
#------------------------------------
# a=[5,8,9,10,25]
# random.shuffle(a)
# print(a)
#------------------------------------
# a=str(input("kiriting="))
# a2=str(input("kiriting="))
# a3=str(input("kiriting="))
# a4=str(input("kiriting="))
# a5=str(input("kiriting="))
# a6=str(input("kiriting="))
# a7=str(input("kiriting="))
# a8=str(input("kiriting="))
# list=[a,a2,a3,a4,a5,a6,a7,a8]
# x=random.shuffle(list)
# print(list)
#------------------------------------
