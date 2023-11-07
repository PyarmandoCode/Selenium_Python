#todo condicionales multiples
valor= input("Ingrese el valor:")

match valor:
    case 'A':
        print("Esta en el Rango Uno")
    case 'B':
        print("Esta en el Rango Dos")
    case 'C':
        print("Esta en el Rango Tres")
    case _:
        print("Esta en el Rango Cuatro")
