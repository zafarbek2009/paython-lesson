#num=2 type(nume)=?
#a)str
#b)int  <
#c)bool

# 2 

#a=2 b=3 c=4 a=b and c=a or cb?
#a)True
#b)False  <
#c)Error

# 3 
def reverse_digits(n):
    return int(str(n)[::-1])
print("3:", reverse_digits(154), reverse_digits(710))

# 4
def print_digits(n):
    for digit in str(n)[::-1]:
        print(digit)
print("4:")
print_digits(154)

# 5
first_letter = lambda word: word[0]
print("5:", first_letter("python"))

# 6
last_letter = lambda word: word[-1]
print("6:", last_letter("python"))

# 7
first_last = lambda word: word[0] + word[-1]
print("7:", first_last("python"))

# 8
# x = int(input("x ni kiriting: "))
# n = int(input("n ni kiriting: "))
# print("8:", x  n)

# 9
print("9: For loop")
for i in range(1, 11):
    print(i, end=" ")
print("\nWhile loop")
i = 1
while i <= 10:
    print(i, end=" ")
    i += 1
print()

# 10
# text = input("Matn kiriting: ")
# print("10:", len(text.split()))

# 11
# name = input("Ismingiz: ")
# age = int(input("Yoshingiz: "))
# data = {"name": ism, "yosh": age}
# print("11:", data)

# 12
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
common = list(set(list1) & set(list2))
print("12:", common)

# 13
# masofa = float(input("Masofa (km): "))
# vaqt = int(input("Vaqt (min): "))
# if masofa > 3 and vaqt > 10:
#     print("13: Taxi kerak")
# else:
#     print("13: Taxi kerak emas")

# 14
# ism = input("Ism: ")
# yosh = int(input("Yosh: "))
# email = input("Email: ")
# sizning yoshingiz < 18 or "@" not in email or "." not in email:
#     print("14: Xatolik!")
# else:
#     print("14: Qabul qilindi")

# 15
# num = int(input("Son kiriting: "))
# print("15:", "Juft" if num % 2 == 0 else "Toq")

#16
# kun = int(input("Kun raqamini kiriting (1-7): "))
# kunlar = ["Dushanba", "Seshanba", "Chorshanba", "Payshanba", "Juma", "Shanba", "Yakshanba"]
# if 1 <= day <= 7:
#     print("16:", kunlar[day - 1])
# else:
#     print("16: Xato")

# 17
# while True:
#     val = input("Son kiriting yoki 'exit' deb yozing: ")
#     if val.lower() == "exit":
#         break
#     else:
#         print("Darajasi:", int(val)  2)

# 18
my_list = [5, 2, 8, 1, 9]
print("18:", my_list[::-1])

# 19
my_list = [3, 6, 2, 1, 7, 9]
print("19:", sum(my_list)/len(my_list))

# 20
my_list = [5, 2, 7, 5, 9]
print("20:", sum(my_list))

# 21
my_list = [3, 8, 2, 6, 1, 9]
print("21: Min =", min(my_list), "Max =", max(my_list))

# 22
my_list = [1, 5, 2, 4, 3, 7]
juft = [x for x in my_list if x % 2 == 0]
print("22:", juft)

# 23
toq = [x for x in my_list if x % 2 != 0]
print("23:", toq)

# 24
# a = int(input("1-son: "))
# b = int(input("2-son: "))
# print("24:", (a + b) / 2)

# 25
print("25:", sum(i for i in range(1, 101) if i % 2 != 0))

# 26
# a = int(input("1-son: "))
# b = int(input("2-son: "))
# c = int(input("3-son: "))
# print("26:", max(a, b, c))

# 27
print("27:", [i for i in range(1, 101) if i % 3 == 0])

# 28
my_list = [1, 4, 7, 6, 3, 2]
yangi_juft = [x for x in my_list if x % 2 == 0]
print("28:", yangi_juft)

# 29
print("29:", sum(my_list))

# 30
for _ in range(10):
    print("30: salom yaxshimisiz")



