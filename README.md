[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/mxvxuYnp)
[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-2e0aaae1b6195c2367325f4f02e2d04e9abb55f0b24a779b69b11b9e10269abc.svg)](https://classroom.github.com/online_ide?assignment_repo_id=21459932&assignment_repo_type=AssignmentRepo)
# GestionInventario 

Desarrolla una aplicación en **Python** llamada **`gestion_inventario.py`** que permita **gestionar un inventario de productos** utilizando **programación orientada a objetos (POO)**.

El programa deberá permitir **añadir, mostrar, buscar, modificar y eliminar productos**, así como **calcular el valor total del inventario y consultar todos los productos de un proveedor determinado**.
Los datos deberán **almacenarse en un fichero JSON**, de forma que se mantengan entre ejecuciones (persistencia de datos).

La aplicación deberá implementarse siguiendo el **paradigma orientado a objetos** e incluir **tres clases principales**:

* `Proveedor`: representa los datos de un proveedor.
* `Producto`: representa un producto individual.
* `Inventario`: gestiona la colección de productos y la persistencia en JSON.

**Podrás implementar los métodos `to_dict()` y `from_dict()`.**
Opcionalmente podrás realizar la conversión entre los objetos y los datos en formato JSON a través de la implementación de estos métodos (no es obligatorio).

---

## Estructura general del programa

### 1. Clases a implementar

#### Clase `Proveedor`

* Atributos:

  * `nombre` (cadena)
  * `contacto` (cadena, puede ser correo electrónico o teléfono)
* Métodos:

  * Constructor `__init__`
  * Método `__str__()` para representar los datos del proveedor de forma legible.

---

#### Clase `Producto`

* Atributos:

  * `codigo` (cadena, único)
  * `nombre` (cadena)
  * `precio` (float)
  * `stock` (entero)
  * `proveedor` (objeto de la clase `Proveedor`)
* Métodos:

  * Constructor `__init__`
  * Método `__str__()` para mostrar el producto con su información completa (incluido el proveedor).

---

#### Clase `Inventario`

* Atributos:

  * `nombre_fichero` (cadena con el nombre del fichero JSON).
  * `productos` (lista de objetos de tipo `Producto`).
* Métodos:

  * `__init__(self, nombre_fichero)`: inicializa la clase e intenta cargar los datos del fichero.
  * `cargar(self)`: lee los datos del fichero JSON (si existe) y crea los objetos `Producto` y `Proveedor` correspondientes.
  * `guardar(self)`: recorre la lista de productos y genera la estructura de diccionarios necesaria para guardar los datos en JSON.
  * `anadir_producto(self, producto)`: añade un nuevo producto si no existe otro con el mismo código. 
  * `mostrar(self)`: muestra por pantalla todos los productos del inventario.
  * `buscar(self, codigo)`: busca y devuelve un producto por su código (si existe).
  * `modificar(self, codigo, ...)`: permite cambiar el nombre, precio o stock de un producto existente.
  * `eliminar(self, codigo)`: elimina un producto por su código.
  * `valor_total(self)`: calcula el valor total del inventario sumando el resultado de `precio * stock` de cada producto.
  * `mostrar_por_proveedor(self, codigo_proveedor)`: muestra todos los productos pertenecientes a un proveedor concreto.
    * Si no existen productos de ese proveedor, debe mostrar un mensaje indicándolo.

---

### 2. Interfaz del usuario (menú en consola)

El programa deberá mostrar un menú con las siguientes opciones:

```
=== GESTIÓN DE INVENTARIO ===
1. Añadir producto
2. Mostrar inventario
3. Buscar producto
4. Modificar producto
5. Eliminar producto
6. Calcular valor total
7. Mostrar productos de un proveedor
8. Guardar y salir
```

El menú deberá estar dentro de un bucle `while True`, y terminar solo cuando el usuario seleccione la opción **“Guardar y salir”**.
Al salir, los datos deberán guardarse automáticamente en el fichero JSON.

---

## Requisitos técnicos

* El fichero JSON deberá llamarse **`inventario.json`**.
* Si el fichero no existe, debe crearse automáticamente con una lista vacía (`[]`).
* No se permite el uso de librerías externas (solo el módulo estándar `json`).
* El programa debe ejecutarse en consola (`python3 gestion_inventario.py`).
* Los datos deben conservarse entre ejecuciones.
* El código debe estar correctamente modularizado y comentado.

---

## Estructura de datos esperada en el fichero JSON

Ejemplo del contenido del fichero `inventario.json` tras ejecutar el programa:

```json
[
    {
        "codigo": "P001",
        "nombre": "Teclado mecánico",
        "precio": 45.99,
        "stock": 10,
        "proveedor": {
            "codigo": "PR01",
            "nombre": "TechZone",
            "contacto": "ventas@techzone.com"
        }
    },
    {
        "codigo": "P002",
        "nombre": "Ratón óptico",
        "precio": 19.95,
        "stock": 25,
        "proveedor": {
            "codigo": "PR01",
            "nombre": "TechZone",
            "contacto": "ventas@techzone.com"
        }
    }
]
```

---

## Criterios de evaluación y puntuación (10 puntos)

| Apartado  | Descripción                                                                                     | Puntuación |
| --------- | ----------------------------------------------------------------------------------------------- | ---------- |
| 1         | Definición de las clases `Proveedor`, `Producto` e `Inventario`, con sus atributos y relaciones | **1 punto**   |
| 2         | Implementación de la persistencia de datos en formato JSON dentro de `Inventario`               | **2 puntos**  |
| 3         | Creación del menú principal y control de flujo de la aplicación                                 | **1 punto**   |
| 4         | Implementación de operaciones CRUD (añadir, buscar, modificar, eliminar)                        | **4 puntos**  |
| 5         | Cálculo del valor total del stock                                                               | **1 punto**   |
| 6         | Método para mostrar productos de un proveedor                                                   | **1 puntos**  |
| **Total** |                                                                                                 | **10 puntos** |

---

## Entrega

* El alumno/a deberá entregar un único archivo **`gestion_inventario.py`** y el fichero **`inventario.json`** generado tras la ejecución.
* El programa deberá ejecutarse sin errores desde la línea de comandos.
* Se valorará especialmente la claridad, modularidad y el uso correcto de clases y relaciones entre objetos, así como la eficiencia del código entregado.



