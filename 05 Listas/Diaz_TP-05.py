print("Ejercicio 1")

notas=[9, 8, 8, 6, 7, 5, 2, 4, 7, 4]

print("Notas: ")
for nota in notas :
    print(nota)

promedio = sum(notas) / len(notas)
print(f"Promedio: {promedio}")

nota_alta = max(notas)
nota_baja = min(notas)
print(f"Nota más alta: {nota_alta}")
print(f"Nota más baja: {nota_baja}")

print()

# --------------------------------------------------------------------------------------------------

print("Ejercicio 2")

productos = []
for i in range(5):
    producto = input(f"Ingrese el producto { i + 1 }: ")
    productos.append(producto)

print("Lista de Productos ordenada: ")
print(sorted(productos))

eliminar = input("Ingresar el producto que desea eliminar: ")

if eliminar in productos:
    productos.remove(eliminar)
    print(f"{ eliminar } fué eliminado de la lista")
else:
    print(f" El producto { eliminar } no está en la lista")

print()

# --------------------------------------------------------------------------------------------------

print("Ejercicio 3")

from random import randint

numeros = []
cantidad = 15
pares = []
impares = []

for _ in range(cantidad):
    numeros.append(randint(1, 100))

for idx in range(len(numeros)):
    numero = numeros[idx]
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

print('Lista de numeros: ', numeros)
print(f'Pares ({len(pares)}): ', pares)
print(f'Impares ({len(impares)}): ', impares)

print()

# --------------------------------------------------------------------------------------------------

print("Ejercicio 4")

datos = [1, 3, 5, 3, 7, 1, 9, 5, 3]
nuevos_datos = []

for dato in datos:
    if not (dato in nuevos_datos):
        nuevos_datos.append(dato)

print('Los datos son:', nuevos_datos)

print()

# --------------------------------------------------------------------------------------------------

print("Ejercicio 5")

estudiantes = ['Juan', 'Pedro', 'Carlos', 'Cecilia', 'Lourdes', 'Marisol', 'Jacobo', 'Fabian']

print('Los estudiantes de la comision 4 de UTN TUPaD 2025 son:', ', '.join(estudiantes))

operacion = int(input('Queres agregar un nuevo estudiante (1) o eliminar uno existente (2)?: '))

if operacion == 1:
    estudiante = input('Nombre de estudiante nuevo: ')
    estudiantes.append(estudiante)
elif operacion == 2:
    estudiante = input('Nombre de estudiante a eliminar: ')
    if estudiante in estudiantes:
        estudiantes.remove(estudiante)
    else:
        print('No existe el estudiante')
else:
    print('Operacion invalida. Saludos.')

print('Los estudiantes de la comision 4 de UTN TUPaD 2025 son:', ', '.join(estudiantes))

print()

# --------------------------------------------------------------------------------------------------

print("Ejercicio 6")

numeros = [1, 2, 3, 4, 5, 6, 7]
nuevos_numeros = []
rotacion_cantidad = -1

for idx in range(rotacion_cantidad, len(numeros) + rotacion_cantidad):
   nuevos_numeros.append(numeros[idx])

print('Lista antes:', numeros)
print('Lista despues:', nuevos_numeros)

print()

# --------------------------------------------------------------------------------------------------

print("Ejercicio 7")

temperaturas = [
    [4, 16],
    [3, 16],
    [5, 14],
    [6, 15],
    [4, 20], # Mayor amplitud acá
    [10, 20],
    [15, 22]
]

# NOTE: Uso None como valor default para posibles errores (que no los hay, pero peco de precavido)
promedios = [None, None] # NOTE: promedios = [min, max]
mayor_amplitud = [None, None] # NOTE: mayor_amplitud = [dia, amplitud]
temps_min = []
temps_max = []

for dia, temp_dia in enumerate(temperaturas):
    temps_min.append(temp_dia[0])
    temps_max.append(temp_dia[1])
    amplitud_term = temp_dia[1] - temp_dia[0]
    
    if mayor_amplitud[1] == None or mayor_amplitud[1] < amplitud_term:
        mayor_amplitud = [dia, amplitud_term]

promedios[0] = sum(temps_min)/len(temps_min)
promedios[1] = sum(temps_max)/len(temps_max)

print('Promedio maximo:', promedios[0])
print('Promedio minimo:', promedios[1])
print(f'Mayor amplitud termica registrada: Dia {mayor_amplitud[0]} (con {mayor_amplitud[1]})')

print()

# --------------------------------------------------------------------------------------------------

print("Ejercicio 8")

notas = [
    [2, 3, 4], # Estudiante 1
    [6, 3, 7],
    [7, 3, 8],
    [5, 3, 7],
    [1, 3, 7]
]  # ^ materia 1 

print('Promedios de los estudiantes:')
for idx, estudiante in enumerate(notas):
    print(f"El promedio del estudiante {idx + 1} es {round(sum(estudiante)/len(estudiante), 2)}")

print('\nPromedios de las materias:')
materias = [[], [], []]
for estudiante in notas:
    for idx, materia in enumerate(estudiante):
        materias[idx].append(materia)

for idx, materia in enumerate(materias):
    print(f"El promedio de la materia {idx + 1} es {round(sum(materia)/len(materia), 2)}")

print()

# --------------------------------------------------------------------------------------------------

print("Ejercicio 9")

tablero = [
    ['-', '-', '-'],
    ['-', '-', '-'],
    ['-', '-', '-']
]

print('Tablero inicial:')
for fila in tablero:
    print(fila)

jugador_turno = 1 # 1 = X, 2 = O
cantidad_jugadas = 0
hay_ganador = False

while True:
    fila = int(input("Ingrese la fila (0, 1, 2): "))
    columna = int(input("Ingrese la columna (0, 1, 2): "))

    # NOTE: Validacion de la posicion
    if fila < 0 or fila > 2 or columna < 0 or columna > 2:
        print('Posicion invalida. Ingrese nuevamente.')
        continue
    if tablero[fila][columna] != '-':
        print('Posicion ocupada. Ingrese nuevamente.')
        continue

    # NOTE: Colocacion de la ficha
    ficha = None
    if jugador_turno == 1:
        ficha = 'X'
    else:
        ficha = 'O'

    tablero[fila][columna] = ficha

    # NOTE: Mostrar el tablero actualizado
    print('Tablero actualizado:')
    for fila in tablero:
        print(fila)

    # NOTE: Verificacion de ganador
    # Horizontal y Vertical
    for i in range(3):
        if tablero[i][0] == ficha and tablero[i][1] == ficha and tablero[i][2] == ficha:
            print('El jugador', jugador_turno, 'ha ganado')
            hay_ganador = True
            break
        if tablero[0][i] == ficha and tablero[1][i] == ficha and tablero[2][i] == ficha:
            print('El jugador', jugador_turno, 'ha ganado')
            hay_ganador = True
            break
    
    if hay_ganador: # NOTE: Si hay ganador por fila o columna, salgo del bucle while
        break

    # Diagonal
    if tablero[0][0] == ficha and tablero[1][1] == ficha and tablero[2][2] == ficha:
        print('El jugador', jugador_turno, 'ha ganado')
        break
    if tablero[0][2] == ficha and tablero[1][1] == ficha and tablero[2][0] == ficha:
        print('El jugador', jugador_turno, 'ha ganado')
        break

    # NOTE: Verificacion de empate
    cantidad_jugadas += 1
    if cantidad_jugadas == 9:
        print('Empate')
        break

    # NOTE: Cambio de turno
    if jugador_turno == 1:
        jugador_turno = 2
    else:
        jugador_turno = 1
    print('\nTurno del jugador', jugador_turno)

print('Fin del juego')

print()

# --------------------------------------------------------------------------------------------------

print("Ejercicio 10")

ventas = [
    [140, 220, 3040, 4100], # Dia 1
    [40, 20, 150, 590],
    [0, 20, 30, 1],
    [1200, 260, 340, 460],
    [4, 0, 0, 50],
    [10, 2, 0, 4],
]  # ^ Producto 1
productos_nombre = ['Taza de Spiderman', 'Termo Stanley 1L', 'Feastables', 'Alpine A525 de Colapinto']

ventas_producto_por_dia = [[], [], [], []]

for dia in ventas:
    for idx, producto in enumerate(dia):
        ventas_producto_por_dia[idx].append(producto)

print('Total vendido por cada producto:')
for idx, ventas_producto in enumerate(ventas_producto_por_dia):
    print(f'\t{productos_nombre[idx]}: {sum(ventas_producto)}')


mayor_ventas_dia = [None, None] # NOTE: mayor_ventas_dia = [dia, ventas]
for idx, dia in enumerate(ventas):
    total_ventas = sum(dia)
    if mayor_ventas_dia[1] == None or mayor_ventas_dia[1] < total_ventas:
        mayor_ventas_dia = [idx, total_ventas]

print(f'\nDía con mayores ventas totales: {mayor_ventas_dia[0] + 1} (con {mayor_ventas_dia[1]})')


mayor_ventas_producto = [None, None] # NOTE: mayor_ventas_producto = [producto, ventas]
for idx, producto in enumerate(ventas_producto_por_dia):
    total_ventas = sum(producto)
    if mayor_ventas_producto[1] == None or mayor_ventas_producto[1] < total_ventas:
        mayor_ventas_producto = [idx, total_ventas]

print(f'\nProducto más vendido en la semana: {productos_nombre[mayor_ventas_producto[0]]} (con {mayor_ventas_producto[1]})')

