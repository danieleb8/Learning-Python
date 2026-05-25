###
# 01 - sentencias condicionales (if,else,elif)
#permite ejecutar diferentes bloques de código dependiendo de si una condición es verdadera o falsa.

import os
os.system("clear") 

print("\n Sentencia simple condicional")

edad=18
if edad >= 18:
    print("Eres mayor de edad") #la tabulaciónm es importante para indicar que este bloque de código pertenece a la sentencia if
    print("Felicidades")

print("\n Sentencia simple condicional con elif")
edad=15
if edad >= 18:
    print("Eres mayor de edad")
elif edad >= 13:
    print("Eres un adolescente")

print("\n Sentencia simple condicional con else")
edad=10
if edad >= 18:
    print("Eres mayor de edad")
elif edad >= 13:           
    print("Eres un adolescente")
else:
    print("Eres un niño")


print("\n Sentencia condicional multiples")
### JavaScript
#&& -> and
#|| -> or
#! -> not
#== -> igualdad
edad=25
tiene_carnet = True
if edad >= 18 and tiene_carnet:
    print("Puedes conducir")
else:    
    print("No puedes conducir")

es_fin_de_semana = False
if not es_fin_de_semana:
    print("Tengo que trabajar")


print("\n Anidar Condicionales")

edad=15
tiene_dinero = True
if edad >= 18:
    if tiene_dinero:
        print("Puedes salir a divertirte")
    else:
        print("No tienes dinero para salir")
else:   
    print("Eres menor de edad, no puedes salir de fiesta")