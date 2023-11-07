

#todo el cuerpo del programa que se va a evaluar
try:
    l = 20 / 2
    print(l)
except Exception as err:
    #todo cuando el programa encuentre un error entrara a este bloque
    print("Ha ocurrido un error",err)
else:
    #todo cuando no encuentra ningune error
    print("No Ha existido ninguan excepcion")
finally:
    #todo seiempre se ejecuta
    print("el bloque try-except termino correctamente")



