###
# exercises.py
# Ejercicios para practicar los conceptos aprendidos en las lecciones.
###

from os import system
if system("clear") != 0: system("cls")

print("\nEjercicio 1: Imprimir mensajes")
print("Escribe un programa que imprima tu nombre y tu ciudad en líneas separadas.")

### Completa aquí
print("Mi nombre es Daniel")
print("Vivo en Itagui, Colombia")


print("\nEjercicio 2: Muestra los tipos de datos de las siguientes variables:")
print("Usa el comando 'type()' para determinar el tipo de datos de cada variable.")
a = 15
b = 3.14159
c = "Hola mundo"
d = True
e = None

### Completa aquí
print(type(a)) # int
print(type(b)) # float
print(type(c)) # str
print(type(d)) # bool
print(type(e)) # NoneType


print("\nEjercicio 3: Casting de tipos")
print("Convierte la cadena \"12345\" a un entero y luego a un float.")
print("Convierte el float 3.99 a un entero. ¿Qué ocurre?")

### Completa aquí
num_str = "12345"
num_str_=int(num_str)
num_float = float(num_str_)
float_str = 3.99
float_int = int(float_str)
print(num_str_)
print(num_float)
print(float_int)


print("--------------")

print("\nEjercicio 4: Variables")
print("Crea variables para tu nombre, edad y altura.")
print("Usa f-strings para imprimir una presentación.")

# "Hola! Me llamo midudev y tengo 39 años, mido 1.70 metros"

### Completa aquí
nombre, edad, altura= "Daniel", 27, 1.75
print(f"Hola! Me llamo {nombre} y tengo {edad} años, mido {altura} metros")

print("\nEjercicio 5: Números")
print("1. Crea una variable con el número PI (sin asignar una variable)")
print("2. Redondea el número con round()")
print("3. Haz la división entera entre el número que te salió y el número 2")
print("4. El resultado debería ser 1")

### Completa aquí
pi = 3.14159
pi_rounded = round(pi)
dividir=pi_rounded//2
print(pi_rounded)