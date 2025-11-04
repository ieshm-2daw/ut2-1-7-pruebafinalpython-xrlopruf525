"""
Examen: Gestión de Inventario con Persistencia JSON y Programación Orientada a Objetos
Autor/a: _______________________________________
Fecha: __________________________________________

Objetivo:
Desarrollar una aplicación orientada a objetos que gestione un inventario de productos
con persistencia de datos en ficheros JSON y uso de listas y diccionarios anidados.

Clases requeridas:
- Proveedor
- Producto
- Inventario

"""

import json
import os


# ======================================================
# Clase Proveedor
# ======================================================

class Proveedor:
    def __init__(self, nombre, contacto):
        self.nombre = nombre
        self.contacto = contacto

    def __str__(self):
        return f'{self.nombre}, Contacto: {self.contacto}'


# ======================================================
# Clase Producto
# ======================================================

class Producto:
    def __init__(self, codigo, nombre, precio, stock, proveedor):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
        self.proveedor = proveedor

    def __str__(self):
        return f'[{self.codigo}] {self.nombre} - {self.precio} ({self.stock}) | {self.proveedor.nombre} ({self.proveedor.contacto})'


# ======================================================
# Clase Inventario
# ======================================================

class Inventario:
    def __init__(self, nombre_fichero):
        self.nombre_fichero = nombre_fichero
        self.productos = []

    def cargar(self):
        if os.path.exists(self.nombre_fichero):
            with open(self.nombre_fichero, 'r', encoding='utf-8') as f:
                datos = json.load(f)

            for p in datos:
                pro_data = p.get('proveedor', {})
                proveedor = Proveedor(pro_data.get('nombre'), pro_data.get('contacto'))
                producto = Producto(
                    p['codigo'],
                    p['nombre'],
                    p['precio'],
                    p['stock'],
                    proveedor
                )
                self.productos.append(producto)


    def guardar(self):

        prod_dicc = []
        for p in self.productos:
            prod_dicc.append({
                'codigo': p.codigo,
                'nombre': p.nombre,
                'precio': p.precio,
                'stock': p.stock,
                'proveedor': {
                    'nombre': p.proveedor.nombre,
                    'contacto': p.proveedor.contacto
                }
            })

        with open(self.nombre_fichero, 'w', encoding='utf-8') as f:
            json.dump(prod_dicc, f, ensure_ascii=False, indent=4)


    def anadir_producto(self, producto):
        for p in self.productos:
            if producto.codigo == p.codigo:
                print("Producto existente.")
                return
        self.productos.append(producto)
        print("Producto añadido correctamente.")

    def mostrar(self):
        for p in self.productos:
            print(p)

    def buscar(self, codigo):

        for p in self.productos:
            if p.codigo == codigo:
                return p
        return None

    def modificar(self, codigo, nombre=None, precio=None, stock=None):
        producto = self.buscar(codigo)
        if producto:
            if nombre:
                producto.nombre = nombre
            if precio:
                producto.precio = float(precio)
            if stock:
                producto.stock = int(stock)
            print("Producto modificado correctamente.")
        else:
            print("El producto no existe.")


    def eliminar(self, codigo):
        self.productos = [p for p in self.productos if p.codigo != codigo]

    def valor_total(self):
        total = 0.0
        for p in self.productos:
            try:
                total += float(p.precio) * int(p.stock)
            except ValueError:
                print(f"Error los datos tienen otros valores")
        return total


    def mostrar_por_proveedor(self, nombre_proveedor):
        encontrados = [p for p in self.productos if p.proveedor.nombre.lower() == nombre_proveedor.lower()]

        if not encontrados:
            print(f"No hay productos del proveedor")
        else:
            print(f"Productos del proveedor '{nombre_proveedor}':")
            for p in encontrados:
                print(p)



# ======================================================
# Función principal (menú de la aplicación)
# ======================================================

def main():
    inventario = Inventario("inventario.json")
    inventario.cargar()
    while True:
        print("\n=== GESTIÓN DE INVENTARIO ===")
        print("1. Añadir producto")
        print("2. Mostrar inventario")
        print("3. Buscar producto")
        print("4. Modificar producto")
        print("5. Eliminar producto")
        print("6. Calcular valor total")
        print("7. Mostrar productos de un proveedor")
        print("8. Guardar y salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            codigo = input("Introduce el codigo: ")
            nombre = input("Introduce el nombre: ")
            precio = input("Introduce el precio: ")
            stock = input("Introduce el stock: ")
            nombre_pro = input("Introduce el nombre del proveedor: ")
            contacto_pro = input("Introduce el contacto del proveedor: ")
            proveedor = Proveedor(nombre_pro, contacto_pro)
            producto = Producto(
                codigo,
                nombre,
                precio,
                stock,
                proveedor
            )
            inventario.anadir_producto(producto)
        elif opcion == '2':
            inventario.mostrar()

        elif opcion == '3':
            codigo = input("Introduce el codigo del producto a buscar: ")
            res = inventario.buscar(codigo)
            print(res)
        elif opcion == '4':
            codigo = input("Introduce el código del producto a modificar: ")
            nombre = input("Nuevo nombre: ")
            precio = input("Nuevo precio: ")
            stock = input("Nuevo stock: ")
            inventario.modificar(
                codigo,
                nombre if nombre else None,
                float(precio) if precio else None,
                int(stock) if stock else None
            )

        elif opcion == '5':
            codigo = input("Introduce el codigo del producto a eliminar: ")
            inventario.eliminar(codigo)
        elif opcion == '6':
            print(f' El valor total es de:  {inventario.valor_total()}')
        elif opcion == '7':
            nombre_pro = input("Introduce el nombre del proveedor a buscar: ")
            inventario.mostrar_por_proveedor(nombre_pro)
        elif opcion == '8':
            inventario.guardar()
            print("Datos guardados  y saliendo.")
            break
        else:
            print("Opcion incorrecta")


if __name__ == "__main__":
    main()
