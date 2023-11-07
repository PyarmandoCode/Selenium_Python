for vuelta in range(1,20):
    print(vuelta,"Curso de Selenium Python")
print("fin del bucle")

mi_lista=["FLASK","DJANGO","FASTAPI","PYTHON"]


for valores in mi_lista:
    print(valores)

#todo uso de break
tot=0
cont=0
precios=[1200.80,1700.20,1800.50,34.90]
for item in precios:
    if item>1800:
        break#Finalizar el bucle
    else:
        tot +=item #acumulando
    cont +=1
print(f"La Cantidad a pagar sera {tot} y el numero de items {cont}")


#todo uso de continue
for i in range(1,101):
    if i % 3 ==0:#todo el % captura el residuo de la division
        continue
    if i % 5 ==0:#todo el % captura el residuo de la division
        continue
    else:
        print(i)



