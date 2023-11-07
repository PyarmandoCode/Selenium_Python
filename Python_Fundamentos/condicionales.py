
#todo condicionales simples
noticia="informacion actualizada"
if len(noticia)>0:
    print("Existe informacion que evaluar") #True
else:
    print("No Existe informacion que evaluar") #False


#todo condicionales multiples
valor= int(input("Ingrese el valor:"))
if valor>=0 and valor<=5:
    print("Esta en el Rango Uno")
elif valor>=6 and valor<=10:
    print("Esta en el Rango Dos")
elif valor>=11 and valor<=15:
    print("Esta en el Rango Tres")
else:
    print("Esta en el Rango Cuatro")




