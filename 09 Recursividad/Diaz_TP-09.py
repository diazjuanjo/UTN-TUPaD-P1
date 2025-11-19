print("Ejercicio 1")

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


num = int(input("Ingrese un número: "))

for i in range(1, num + 1):
    print(f"{i}! = {factorial(i)}")

print()

# --------------------------------------------------------------------------------------------------

print("Ejercicio 2")

def fibonacci(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


num = int(input("Ingrese la cantidad de términos: "))
for i in range(num):
    print(fibonacci(i), end=" ")
print()

print()

# --------------------------------------------------------------------------------------------------

print("Ejercicio 3")

def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente - 1)


b = int(input("Base: "))
e = int(input("Exponente: "))
print(f"{b}^{e} = {potencia(b, e)}")

print()

# --------------------------------------------------------------------------------------------------

print("Ejercicio 4")

def decimal_a_binario(n):
    if n == 0:
        return "0"
    elif n == 1:
        return "1"
    else:
        return decimal_a_binario(n // 2) + str(n % 2)


num = int(input("Ingrese un número decimal: "))
print(f"El número {num} en binario es {decimal_a_binario(num)}")

print()

# --------------------------------------------------------------------------------------------------

print("Ejercicio 5")

def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    if palabra[0] != palabra[-1]:
        return False
    return es_palindromo(palabra[1:-1])


texto = input("Ingrese una palabra: ").lower()
print("Es palíndromo" if es_palindromo(texto) else "No es palíndromo")

print()

# --------------------------------------------------------------------------------------------------

print("Ejercicio 6")

def suma_digitos(n):
    if n < 10:
        return n
    else:
        return (n % 10) + suma_digitos(n // 10)


num = int(input("Ingrese un número: "))
print(f"La suma de sus dígitos es {suma_digitos(num)}")

print()

# --------------------------------------------------------------------------------------------------

print("Ejercicio 7")

def contar_bloques(n):
    if n == 1:
        return 1
    else:
        return n + contar_bloques(n - 1)


niveles = int(input("Ingrese el número de bloques en el nivel inferior: "))
print(f"Total de bloques: {contar_bloques(niveles)}")

print()

# --------------------------------------------------------------------------------------------------

print("Ejercicio 8")

def contar_digito(numero, digito):
    if numero == 0:
        return 0
    elif numero % 10 == digito:
        return 1 + contar_digito(numero // 10, digito)
    else:
        return contar_digito(numero // 10, digito)


num = int(input("Ingrese un número: "))
d = int(input("Ingrese el dígito a contar: "))
print(f"El dígito {d} aparece {contar_digito(num, d)} veces.")