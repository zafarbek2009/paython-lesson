# gradus=[-15,21,-8,-23,25,65,10,-2]

# for g in gradus:
#     if g>0:
#         print("bu musbat son")
#     else:
#         print("manfiy son")






# input va int - userdan malumot olish
# f string



# a=input("iltimos ismingizni yozing >>")

# print(a)



avto=input("yoqtirgan avtomobilni tanlang [malibu,damas,nexia,jentra,epica,spark,onix] :")

if avto=="malibu":
    print(f"{avto}-22.000$")
elif avto=="damas":
    print(f"{avto}-7.000$")
elif avto=="onix":
    print(f"{avto}-20.000$")
elif avto=="spark":
    print(f"{avto}-5.000$")
else:
    print(f"{avto} - degan avtomobil bizda mavjud emas")




kassa=int(input("yoshingizni kiriting  >>"))

if kassa>=18:
    print("sizga kirish narxi 40.000 so'm")
elif kassa<18:
    print("sizga kirish bepul !")
else:
    print("xatolik yoz berdi iltimos amalingizni boshqattan kiriting")










































