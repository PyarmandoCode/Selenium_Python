class Person:
    def __init__(self,nom,ape,edad=None):
        self.nombre=nom
        self.apellido=ape
        self.edad = edad



# TODO OBJETO  --INSTANCIAR
persona_jose = Person("Jose","Perez")
persona_pedro = Person("Pedro","Rios",edad=23)
# print(persona_jose.__dict__)
# print(persona_pedro.__dict__)
# print(persona_jose.apellido)
# print(persona_pedro.nombre)
# print(persona_pedro.edad)


class boton:
    def __init__(self,color,ancho,alto,etiqueta,nroclick,res):
        self.color=color
        self.ancho=ancho
        self.alto=alto
        self.etiqueta=etiqueta
        self.nroclick=nroclick
        self.res=res
    def metodoclick(self):
        print(f"El Usuario Pulso {self.nroclick} Veces Click!!!!!")
    def esresponsivo(self):
        if self.res=="1":
            print("El Boton es Responsivo")
        else:
            print("El Boton No es Responsivo")


btnaceptar=boton(color="Gris",ancho="100%",alto="100%",etiqueta="Aceptar",nroclick=8,res="1")
btncerrarr=boton(color="Gris",ancho="100%",alto="100%",etiqueta="Cerrar",nroclick=8,res="0")
print(btncerrarr.__dict__)
print(btnaceptar.__dict__)

#todo invocar metodo
btnaceptar.metodoclick()
btnaceptar.esresponsivo()