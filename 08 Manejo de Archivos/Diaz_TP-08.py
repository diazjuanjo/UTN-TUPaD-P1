print("Ejercicio 2")

with open("./08 Manejo de Archivos/productos.txt", "r") as file:
    for line in file:
        producto, precio, cantidad = line.strip().split(',')
        print(f'Producto: {producto} | Precio: ${precio} | Cantidad: {cantidad}')

print()

# --------------------------------------------------------------------------------------------------

print("Ejercicio 3")

with open('./08 Manejo de Archivos/productos.txt', 'a') as file:
    producto = input('Ingrese el nombre del producto: ')
    precio = input('Ingrese el precio del producto: ')
    cantidad = input('Ingrese la cantidad del producto: ')
    file.write(f'{producto},{precio},{cantidad}\n')

print()

# --------------------------------------------------------------------------------------------------

print("Ejercicio 4")

productos = []

with open('./08 Manejo de Archivos/productos.txt', 'r') as file:
    for line in file:
        producto, precio, cantidad = line.strip().split(',')
        productos.append({'nombre': producto, 'precio': precio, 'cantidad': cantidad})

print(productos)

print()

# --------------------------------------------------------------------------------------------------

print("Ejercicio 5")

def leer_productos():
    productos = []
    with open('./08 Manejo de Archivos/productos.txt', 'r') as file:
        for line in file:
            producto, precio, cantidad = line.strip().split(',')
            productos.append({'nombre': producto, 'precio': precio, 'cantidad': cantidad})
    return productos

def buscar_producto(productos, nombre_producto):
    for producto in productos:
        if producto['nombre'].lower() == nombre_producto.lower():
            return producto
    return None


productos = leer_productos()
nombre_producto = input('Ingrese el nombre del producto: ')
producto = buscar_producto(productos, nombre_producto)

if producto:
    print(producto)
else:
    print('El producto no existe')

print()

# --------------------------------------------------------------------------------------------------

print("Ejercicio 6")

def leer_productos():
    productos = []
    with open('./08 Manejo de Archivos/productos.txt', 'r') as file:
        for line in file:
            producto, precio, cantidad = line.strip().split(',')
            productos.append({'nombre': producto, 'precio': precio, 'cantidad': cantidad})
    return productos

def buscar_producto(productos, nombre_producto):
    for producto in productos:
        if producto['nombre'].lower() == nombre_producto.lower():
            return producto
    return None

def guardar_productos(productos):
    with open('./08 Manejo de Archivos/productos.txt', 'w') as file:
        for producto in productos:
            file.write(f'{producto["nombre"]},{producto["precio"]},{producto["cantidad"]}\n')

def agregar_producto(productos):
    nombre = input('Ingrese el nombre del producto: ')
    precio = input('Ingrese el precio del producto: ')
    cantidad = input('Ingrese la cantidad del producto: ')
    productos.append({'nombre': nombre, 'precio': precio, 'cantidad': cantidad})
    return productos

productos = leer_productos()
print(productos)

producto = buscar_producto(productos, 'Lapicera')
print(producto)

producto = agregar_producto(productos)
guardar_productos(productos)