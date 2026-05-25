###
# EJERCICIOS
###

# Ejercicio 1: Determinar el mayor de dos números
# Pide al usuario que introduzca dos números y muestra un mensaje
# indicando cuál es mayor o si son iguales

a=int(input("Introduce el primer número: "))
b=int(input("Introduce el segundo número: "))
if a > b:
    print(f"El número {a} es mayor que {b}.")
elif b > a:
    print(f"El número {b} es mayor que {a}.")
else:
    print(f"Los números {a} y {b} son iguales.")

# Ejercicio 2: Calculadora simple
# Pide al usuario dos números y una operación (+, -, *, /)
# Realiza la operación y muestra el resultado (maneja la división entre zero)
a=int(input("Introduce el primer número: "))
b=int(input("Introduce el segundo número: "))
operador=input("Introduce la operación (+, -, *, /): ")
if operador == "+":
    resultado = a + b
    print(f"El resultado de {a} + {b} es {resultado}.")
elif operador == "-":
    resultado = a - b
    print(f"El resultado de {a} - {b} es {resultado}.")
elif operador == "*":
    resultado = a * b
    print(f"El resultado de {a} * {b} es {resultado}.")
elif operador == "/":
    if b != 0:
        resultado = a / b
        print(f"El resultado de {a} / {b} es {resultado}.")
    else:
        print("Error: No se puede dividir entre cero.")
else:
    print("Error: Operación no válida.")    

# Ejercicio 3: Año bisiesto
# Pide al usuario que introduzca un año y determina si es bisiesto.
# Un año es bisiesto si es divisible por 4, excepto si es divisible por 100 pero no por 400.
ano=int(input("Introduce un año: "))
if (ano % 4 == 0):
    if (ano % 100 == 0 and ano % 400 != 0):
        print(f"El año {ano} no es bisiesto.")
    elif (ano % 100 == 0 and ano % 400 == 0):
         print(f"El año {ano} es bisiesto.")
    else:
        print(f"El año {ano} es bisiesto.")
else:
    print(f"El año {ano} no es bisiesto.")
# Ejercicio 4: Categorizar edades
# Pide al usuario que introduzca una edad y la clasifique en:
# - Bebé (0-2 años)
# - Niño (3-12 años)
# - Adolescente (13-17 años)
# - Adulto (18-64 años)
# - Adulto mayor (65 años o más)
edad=int(input("Introduce una edad: "))
if edad >= 0 and edad <= 2:
    print(f"Edad {edad} años: Bebé")
elif edad >= 2 and edad <= 12:
    print(f"Edad {edad} años: Niño")
elif edad >= 13 and edad <= 17:
    print(f"Edad {edad} años: Adolescente")
elif edad >= 18 and edad <= 64:
    print(f"Edad {edad} años: Adulto")  
elif edad >= 65:    
    print(f"Edad {edad} años: Adulto mayor")
else:
    print("Error: Edad no válida.")
