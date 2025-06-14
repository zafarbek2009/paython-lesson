# str methods

# 1
s=("salom")

print(s.capitalize())

# 2
f="hammaga salom"

print(f.casefold())

# 3
print(s.center(50))

# 4
a=("olma","olcha","banan","nok")

print(a.count("olcha"))

# 5
a="bugum hamma maktabga keladi"

print(a.encode())
# list methods

# 2


meva = ["olma", "banan", "olcha"]

meva.append("apelsin")

print(meva)

# 3
meva.clear()
print(meva) 

# 4


s = ["bexruz", "munis", "firdavs"]

x = s.copy()

print(x)

# 5

x = s.count("munis")

print(x)

# 6
m = ["anisa", "shaxzoda","hilola"]

d = ["amir","azim","muhammad"]

m.extend(d)

print(m)
# 7
m = ["anisa", "shaxzoda","hilola"]

d = m.index("shaxzoda")

print(d)

# dictionary -lug'atlar 

# 1

s={"jentra":12000,"onix":13000}

print(s)

# 2
print(s.keys())

print(s.get("jentra"))

print(s.get("onix"))































