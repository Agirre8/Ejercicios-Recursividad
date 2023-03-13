
def esPalindromo(word):
    if len(word) < 2: 
        print("La palabra es un palíndromo")
    if word[0] != word[-1]: 
        print("La palabra NO es un palíndromo")
    else:
        print("La palabra es un palíndromo")


esPalindromo(palabra)