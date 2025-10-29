# Nombre del archivo
archivo = "productos.txt"

# 1. Crear archivo inicial con productos si no existe
try:
    with open(archivo, "x") as f:  # 'x' crea el archivo solo si no existe
        f.write("Lapicera,120.5,30\n")
        f.write("Cuaderno,250.0,50\n")
        f.write("Mochila,1500.0,10\n")
except FileExistsError:
    pass  # Si ya existe, no hacemos nada

# 2 y 4. Leer productos y cargarlos en una lista de diccionarios
productos = []

with open(archivo, "r") as f:
    for linea in f:
        linea = linea.strip()
        if linea:  # Ignorar líneas vacías
            nombre, precio, cantidad = linea.split(",")
            producto = {
                "nombre": nombre,
                "precio": float(precio),
                "cantidad": int(cantidad)
            }
            productos.append(producto)
            # 2. Mostrar productos
            print(f"Producto: {nombre} | Precio: ${precio} | Cantidad: {cantidad}")

# 3. Agregar productos desde teclado
nuevo_nombre = input("Ingrese el nombre del nuevo producto: ")
nuevo_precio = float(input("Ingrese el precio del producto: "))
nueva_cantidad = int(input("Ingrese la cantidad del producto: "))

nuevo_producto = {
    "nombre": nuevo_nombre,
    "precio": nuevo_precio,
    "cantidad": nueva_cantidad
}

productos.append(nuevo_producto)

# 5. Buscar producto por nombre
buscar = input("Ingrese el nombre del producto a buscar: ")
encontrado = False
for prod in productos:
    if prod["nombre"].lower() == buscar.lower():
        print(f"Producto encontrado: {prod['nombre']} | Precio: ${prod['precio']} | Cantidad: {prod['cantidad']}")
        encontrado = True
        break

if not encontrado:
    print("Producto no encontrado.")

# 6. Guardar los productos actualizados en el archivo
with open(archivo, "w") as f:
    for prod in productos:
        f.write(f"{prod['nombre']},{prod['precio']},{prod['cantidad']}\n")

print("Archivo actualizado con éxito.")
