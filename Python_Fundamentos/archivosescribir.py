import csv

#todo datos que deseas escribir en el archivo csv
nuevos_datos = [
    {"Nombre":"David","Edad":"30","Ciudad":"Miami"},
    {"Nombre":"Eva","Edad":"26","Ciudad":"San Francisco"},
    {"Nombre":"Joaquin","Edad":"46","Ciudad":"Boston"}
]

#todo abrir el archivo CSV en modo escritura=W
with open('nuevos_datos.csv','w',newline='') as archivo_csv:
    campos=["Nombre","Edad","Ciudad"]
    escritor_csv = csv.DictWriter(archivo_csv,fieldnames=campos)

    #todo escribir los encabezados
    escritor_csv.writeheader()

    #todo escribir los datos desde la lista
    for fila in nuevos_datos:
        escritor_csv.writerow(fila)

print("Los Datos han sido escritos en nuevos_datos.csv")
