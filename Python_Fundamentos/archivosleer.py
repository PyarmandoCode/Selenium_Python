import csv
#todo Crear una lista vacia para almacenar los datos

datos=[]

#todo Abrir el Archivo CSV en modo lectura
with open('testing.csv',newline='') as archivo_csv:
    lector_csv=csv.DictReader(archivo_csv)

    #iterar a travez de las filas del archico CSV y agregarlas a la lista
    for fila in lector_csv:
        datos.append(fila)

#todo imprimir la lista de datos
for fila in datos:
    print(fila)
