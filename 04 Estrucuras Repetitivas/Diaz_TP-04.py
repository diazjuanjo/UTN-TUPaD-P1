print("Ejercicio 1")
print("Numeros enteros de 0 hasta 100")
for numero in range(1, 101):
    print(numero)
print()

# ------------------------------------------------------------------------

print("Ejercicio 2")
numero = int(input("Ingrese un número entero: "))
contador = 0
while numero > 0:
    numero = numero // 10
    contador += 1
print(f"El número ingresado tiene {contador} dígitos")
print()

# ------------------------------------------------------------------------

print("Ejercicio 3")
numeroA = int(input("Ingrese un número entero: "))
numeroB = int(input("Ingrese otro número entero: "))

if numeroA > numeroB :
    numeroAuxiliar = numeroA
    numeroA = numeroB
    numeroB = numeroAuxiliar

suma = 0
for numero in range(numeroA + 1, numeroB):
    suma += numero

print(f"La suma entre {numeroA} y {numeroB} es: {suma}")
print()

# ------------------------------------------------------------------------

print("Ejercicio 4")
suma = 0

while True :
    numero = int(input("Ingrese un número entero(0 para terminar): "))
    if numero == 0 :
        break
    suma += numero

print(f"La suma total es: {suma}")
print()

# ------------------------------------------------------------------------

print("Ejercicio 5")
import random
numero_random = random.randint(0,9)

cantidad_intentos = 0
adivinado = False

print("Tenes que adivinar un número entre 0 y 9")

while not adivinado :
    intento = int(input("Ingresa el número: "))
    cantidad_intentos += 1

    if intento == numero_random :
        adivinado = True
    else:
        print("Incorrecto")

print(f"Adivinaste el número {numero_random} en {cantidad_intentos} intentos")
print()

# ------------------------------------------------------------------------

print("Ejercicio 6")
print("Numeros pares enteros de 100 hasta 0")
for numero in range(100, -1, -2):
    print(numero)
print()

# ------------------------------------------------------------------------

print("Ejercicio 7")
numero = int(input("Ingrese un número entero positivo: "))

suma = 0
for i in range(0, numero + 1):
    suma += i

print(f"La suma entre 0 y {numero} es: {suma}")
print()

# ------------------------------------------------------------------------

print("Ejercicio 8")
CANTIDAD = 100
pares = 0
impares = 0
positivos = 0
negativos = 0

for i in range(CANTIDAD):
    numero = int(input(f"Ingrese un número {i + 1}: "))

    if numero % 2 == 0 :
        pares += 1
    else :
        impares += 1
    
    if numero > 0 :
        positivos += 1
    elif numero < 0 :
        negativos += 1

print()
print(f"La cantidad de pares: {pares}")
print(f"La cantidad de impares: {impares}")
print(f"La cantidad de positivos: {positivos}")
print(f"La cantidad de negativos: {negativos}")
print()

# ------------------------------------------------------------------------

print("Ejercicio 9")

CANTIDAD = 100

suma = 0

for i in range(CANTIDAD) :
    numero = int(input(f"Ingrese un número {i + 1}: "))
    suma += numero

media = suma / CANTIDAD

print()
print(f"La media de los {CANTIDAD} números ingresados es: {media}")
print()

# ------------------------------------------------------------------------

print("Ejercicio 10")

numero = int(input("Ingrese un número entero: "))

invertido = 0

while numero > 0 :
    digito = numero % 10
    invertido = invertido * 10 + digito
    numero = numero // 10

print(f"Número invertido: {invertido}")
print()
