##valores logicos: True o False
#fundamental para el control de flujo en la programación, ya que permiten tomar decisiones y 
# ejecutar diferentes bloques de código dependiendo de si una condición es verdadera o falsa.
print("\n valores booleanos basicos")
print(True)
print(False)

print("\n valores de comparacion")
print("5 > 3", 5>3)
print("5 < 3", 5<3)
print("5 == 5", 5==5)
print("5 != 3", 5!=3)
print("5 >= 3", 5>=3)
print("5 <= 3", 5<=3)

print("\n Comparacion de cadenas")
print("manzana"<"pera") # La comparación de cadenas se basa en el orden lexicográfico, es decir, se comparan carácter por carácter 
                        #según su valor Unicode.
print("Hola == Hola", "Hola"=="Hola")
print("Hola == hola", "Hola"=="hola")
print("Hola != Adios", "Hola"!="Adios")

numero = 10
if numero:
    print(f"El número {numero} es considerado verdadero en un contexto booleano.")

numero = 0
if not numero:
    print(f"El número {numero} es considerado falso en un contexto booleano.")

nombre = "Danieleb01"
if nombre:
    print(f"El nombre '{nombre}' es considerado verdadero en un contexto booleano.")

nombre_vacio = ""
if not nombre_vacio:
    print("Esta cadena vacía es considerada falsa en un contexto booleano.")
