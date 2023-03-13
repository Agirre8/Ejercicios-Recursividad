palabra = input("Introduzca una palabra: ")

def esPalindromo(palabra):
    palabra = palabra.lower()
    a,b = 'áéíóúü','aeiouu'
    trans = str.maketrans(a,b)
    print(palabra.translate(trans))
    palabra = palabra.translate(trans)

    if len(palabra) < 2: 
        print("La palabra es un palíndromo")
    if palabra[0] != palabra[-1]: 
        print("La palabra NO es un palíndromo")
    else:
        print("La palabra es un palíndromo")
        
esPalindromo(palabra)
