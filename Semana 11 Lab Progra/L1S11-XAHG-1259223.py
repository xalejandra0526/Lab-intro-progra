print("Ejercicio 11")

cadena = input("Ingrese una cadena de caracteres: ")

contador = 0
for i in cadena:
    if i == '1':
        contador = 1 + contador

print(f"La cantidad de '1' en la cadena es: {contador}")


contador2 = 0
for i in cadena:
    if i == '0':
        contador2 = 1 + contador2

print(f"La cantidad de '0' en la cadena es: {contador2}")

contador3 = 0
for i in cadena:
    if i != '0' and i != '1':
        contador3 = 1 + contador3

print(f"La cantidad de otros caracteres en la cadena es: {contador3}")
   
   

