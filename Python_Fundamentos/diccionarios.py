colores = {"Yellow":"Amarillo",
           "Blue":"Azul",
           "Black":"Negro",
           "Pink":"Rosado"
}


print(colores["Pink"])

colores["Green"]="Verde"
colores["Pink"]="Rojo"
del colores["Pink"]
print(colores)

for valores in colores.items():#keys,#values
    print(valores)