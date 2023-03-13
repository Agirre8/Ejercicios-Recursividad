import random as rd

tabla = []
for i in range(1,50):
    x = rd.randint(1,200)
    tabla.append(x)

tabla.sort()
print (tabla)

def busquedaDicotómica(tabla, x, low, high):

    while low <= high:
        mid = low + (high - low)//2
        if tabla[mid] == x:
            return mid
        elif tabla[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1

result = busquedaDicotómica(tabla, x, 0, len(tabla)-1)

if result != -1:
    print("Element is present at index " + str(result))
else:
    print("Not found")