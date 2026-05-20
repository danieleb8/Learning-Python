## Las variables son utilies para guardar datos en memoría y reutilizarlos
#  a lo largo del programa. En Python, no es necesario declarar el tipo de variable, 
# ya que es un lenguaje de tipado dinámico.
My_Name = "Danieleb01"
print(My_Name)

## tipado dinámico: el tipo de variable se determina en tiempo de ejecución
# Esto significa que puedes asignar un valor de cualquier tipo a una variable sin necesidad
#  de declararla previamente.
My_Age = 27
print(type(My_Age))

## Tipado fuerte: Python no permite operaciones entre tipos de datos incompatibles sin una 
# conversión explícita.
# Por ejemplo, no puedes sumar un número entero y una cadena de texto sin convertir uno de 
# ellos:
# Esto generará un error:
# print(My_Age + My_Name)
print(f"Mi nombre es {My_Name} y tengo {My_Age + 8} años.")
## No recomendada forma de asignar variables
My_Name, My_Age, My_City = "Danieleb01", 27, "Colombia"

#conveniente forma de asignar variables
Mi_nombre_de_variable = "Danieleb01" #snake_case
MiNombreDeVariable= "Danieleb01" #PascalCase
minombredevariable = "Danieleb01" #camelCase
MI_CONSTANTE = 3.14 #UPPER_CASE PARA CONSTANTES 

## Nombres no validos de variables
# 1. No pueden comenzar con un número 1234My_Variable = "Danieleb01" 
# 2. No pueden contener espacios My Variable = "Danieleb01" 
# 3. No pueden contener caracteres especiales My-Variable = "Danieleb01"
# 4. No pueden ser palabras reservadas de Python (como "if", "for", "while", etc.)
# [False, None, True, and, or, not, if, elif, else, for, while, break, continue, pass, 
# def, return, import, from, as, class, try, except, finally, with, lambda, yield, global, 
# #nonlocal, assert, del, raise]
#5. No pueden contener guiones bajos al principio o al final de la variable _My_V


is_user_logged_in : bool = False
print(is_user_logged_in)
is_user_logged_in = 42
print(is_user_logged_in)