# print("Ejercicio 1")
# edad = int(input("Ingrese su edad: "))
# if edad >= 18 :
#     print("Es mayor de edad")
# print()

# print("Ejercicio 2")
# nota = int(input("Ingrese su nota: "))
# if nota >= 6 :
#     print("Aprobado")
# else :
#     print("Desaprobado")
# print()

# print("Ejercicio 3")
# numero = int(input("Ingrese un número: "))
# if numero % 2 == 0 :
#     print("Ha ingresado un número par")
# else :
#     print("Por favor, ingrese un número par")
# print()

# print("Ejercicio 4")
# edad = int(input("Ingrese su edad: "))
# if edad < 12 :
#     print("Niño/a")
# elif edad < 18 :
#     print("Adolescente")
# elif edad < 30 :
#     print("Adulto/a joven")
# else :
#     print("Adulto/a")
# print()

# print("Ejercicio 5")
# password = input("Ingrese su contraseña: ")
# longitud = len(password)
# if  longitud < 8 :
#     print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")
# elif longitud <= 14 :
#     print("Ha ingresado una contraseña correcta")
# else :
#     print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")
# print()

# print("Ejercicio 6")
# from statistics import mode, median, mean
# import random

# numeros_aleatorios = [random.randint(1,100) for i in range(50)]
# print(numeros_aleatorios)

# moda = mode(numeros_aleatorios)
# mediana = median(numeros_aleatorios)
# media = mean(numeros_aleatorios)

# if media > mediana > moda :
#     print("Tiene sesgo positivo o a la derecha")
# elif media < mediana < moda :
#     print("Tiene sesgo negativo o a la izquierda")
# elif media == mediana == moda :
#     print("Sin sesgo")
# else : 
#     print("No se cumplen las condiciones de sesgo")
# print()

# print("Ejercicio 7")
# palabra = input("Ingrese una palabra: ")
# ultima_letra = palabra[-1].lower()
# if ultima_letra == "a" or ultima_letra == "e" or ultima_letra == "i" or ultima_letra == "o" or ultima_letra == "u" :
#     print(f"{palabra}!")
# else :
#     print(palabra)
# print()

print("Ejercicio 8")
nombre = input("Ingrese su nombre: ")
print(''' 
    1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
    2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
    3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
    ''')
opcion = input("Ingrese una opción: ")

if opcion == "1" :
    print(nombre.upper())
elif opcion == "2" :
    print(nombre.lower())
elif opcion == "3" :
    print(nombre.title())
else :
    print(nombre)
print()