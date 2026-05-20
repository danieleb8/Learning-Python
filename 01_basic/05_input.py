###
# 05 -entrada de usuario (input()) - Versión Simplificada
## La función input() se utiliza para obtener datos del usuario a través de la consola.

from shlex import split


print("hola, ¿cómo te llamas?")
name = input()  # La función input() espera a que el usuario ingrese algo y presione Enter
print(f"¡Hola, {name}! Encantado de conocerte.")
## También puedes proporcionar un mensaje dentro de la función input() para que el usuario sepa qué se espera de él:
age = int(input("¿Cuántos años tienes? "))  # Aquí pedimos al usuario que ingrese su edad 
#y la convertimos a un entero

print(f"Tienes {age + 2} años.") 

print("para obteber multiples valores a la vez")
country, city = input("¿En qué país vives y en qué ciudad?\n").split()  # Aquí pedimos al 
#usuario que ingrese su país y ciudad separados por un espacio
print(f"Hola {name}, tenggo {age} años y vives en {city}, {country}.")