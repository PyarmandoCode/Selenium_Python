clientes = [
    {'cuenta':'234455','apellido':'ruiz','nombre':'armando','saldo':7000},
    {'cuenta':'234456','apellido':'gomez','nombre':'oscar','saldo':6000},
    {'cuenta':'234457','apellido':'lopez','nombre':'carlos','saldo':2000},
    {'cuenta':'234458','apellido':'cespedes','nombre':'miguel','saldo':17000},
    {'cuenta':'234459','apellido':'tapia','nombre':'sonia','saldo':9000},
]

#todo crear un script que me permita averiguar cual el saldo actual de un cliente
continuar=True
while continuar:
    nrocuenta=input("Ingrese el Numero de Cuenta:")
    estado=True #todo flag
    for item in clientes:
        if nrocuenta==item['cuenta']:
            print(f" Sr ..{item['apellido']} su saldo actual es {item['saldo']}")
            estado=False
    if estado == True:
        print("No se encuenta la Cuenta")
    respuesta = input("Desea Continuar:")
    if respuesta=="n":
        break


#todo Crear un script que me permita mostrar los datos de un cliente como
#todo su saldo y apellido . para esto debera ingresar su numero de cuenta
#todo si existe mostrar la informacion
#todo en caso contrario mostrar el mensaje no se encuentra la cuenta
#todo este script se debe ejecutar hasta que se pulse ls tecla "n"

