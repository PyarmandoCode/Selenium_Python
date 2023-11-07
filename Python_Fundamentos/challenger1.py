"""
# todo
En este ejercicio, crearemos una lista vacía y luego pediremos al usuario
que ingrese números hasta que decida detenerse. Luego, mostraremos la suma
de los números ingresados.
"""
numeros = list()

#todo variable que controle el bucle

continuar=True
while continuar:
   try:
        numero=float(input("Ingrese un numero o cualquier letra para detenerlo:"))
        numeros.append(numero)
   except ValueError:
       continuar=False
suma=sum(numeros)

#todo Mostramos los resultados
print(f"La suma de los numeros {suma}")
