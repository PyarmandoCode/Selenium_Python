#todo tipo de datos primitivo
from datetime import datetime

# todo cadenas
nombre_usuario="Armando" #str
apellido_usuario='Ruiz' #str

# todo numericos
edad_usuario=28 #int
peso_usuario=78.20 #float

#todo boolean
estado_civil = True  #bool

# todo obtener la fecha y hora actual
fecha_hora_actual=datetime.now()
fecha_formateada=fecha_hora_actual.strftime("%d%m%Y")
print("Fecha y Hora Actual",fecha_hora_actual)
print("Fecha Actual",fecha_formateada)

# print("Hola desde Python Testing")
# print(type(nombre_usuario))
# print(type(edad_usuario))
# print(type(peso_usuario))
# print(type(estado_civil))

