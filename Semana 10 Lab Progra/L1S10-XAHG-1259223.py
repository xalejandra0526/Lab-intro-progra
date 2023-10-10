
def decihexa(numero):
    if numero==0:
        return "0"
    valoreshexa="0123456789ABCDEF"
    resultado=""
    while numero>0:
        residuo=numero%16
        resultado=valoreshexa[residuo]+resultado
        numero=numero//16
    return resultado

numerodecimal=int(input("Por favor ingrese un número: "))
if numerodecimal<0:
    print("Por favor ingresa un número positivo")
else:
    resultadohex=decihexa(numerodecimal)
    print("El número decimal", numerodecimal, "en hexadecimal es", resultadohex )
