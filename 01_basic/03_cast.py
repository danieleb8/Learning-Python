## Casting de Types 
# Transformación de  un tipo de valor a otro
##

print(type(int("102")))
print(str(int("100")+2))
print(float("3.1716"))

print(bool(1))
print(bool(0))
print(bool(-8))

print(bool(""))
print(bool("hola"))
print(bool("False"))

# Para convertir una cadena con decimal a entero primero hay que pasarla por float
print(int(float("2.5")))

##Cuando Utilizamos la Función round y colocamos 
# .5, el sistema siempre va a aproximar a par más cercano
print(round(2.5))
print(round(3.5))

