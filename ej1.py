import random as rd

tabla = []
for i in range(1,50):
    x = rd.randint(1,200)
    tabla.append(x)

tabla.sort()
print (tabla)
