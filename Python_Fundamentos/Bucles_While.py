
"""
while True:
    respuesta = input("Deseas Continuar ? (S/N):")
    if respuesta.lower()=='n':
        print("Saliendo del bucle")
        break #false
"""

numero=int(input("Ingrese un numero para ver su tabla:"))
i=1
while i<=12:
    resultado = numero * i
    print(f"{numero} * {i} = {resultado}")
    i +=1

