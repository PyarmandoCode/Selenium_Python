class CajeroAutomatico:
    def __init__(self,saldo_inicial):
        self.saldo=saldo_inicial
    def consultar_saldo(self):
        return self.saldo
    def depositar(self,monto):
        if monto>0:
            self.saldo += monto
            return f"Deposito exitoso.Saldo actual : {self.saldo}"
        else:
            return f"El Monto a depositar debe ser mayor que cero"
    def retirar(self,monto):
        if monto>0 and monto<=self.saldo:
            self.saldo -=monto
            return f"Retiro exitoso.Saldo actual : {self.saldo}"
        elif monto> self.saldo:
            return "Fondos Insuficientes"
        else:
            return "El Monto a retirar debe ser mayor que cero"

#todo crear una instancia del Cajero Automatico 1000
cajero=CajeroAutomatico(1000)
#print(cajero.__dict__)
#print(cajero.depositar(800))
#print(cajero.retirar(200))
#print(cajero.retirar(2200))


while True:
    print("Opciones")
    print("1:-Consultar Saldo")
    print("2:-Depositar")
    print("3:-Retirar")
    print("4:-Salir")

    opcion = input("Seleccione una opcion")
    if opcion == "1":
        print(f"Saldo actual: ${cajero.consultar_saldo()}")
    elif opcion =="2":
        monto=float(input("Ingrese el monto a depositar:"))
        print(cajero.depositar(monto))
    elif opcion == "3":
        monto = float(input("Ingrese el monto a Retirar:"))
        print(cajero.retirar(monto))
    elif opcion == "4":
        print("Gracias por utilizar el cajero Automatico")
        break
    else:
        print("Opcion No Valida")


