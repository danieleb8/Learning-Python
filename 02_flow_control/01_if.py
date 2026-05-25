###
# 01 - sentencias condicionales (if,else,elif)
#permite ejecutar diferentes bloques de código dependiendo de si una condición es verdadera o falsa.

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