class Producto:
    def __init__(self, nombre, codigo, precio, año):
        self.nombre = nombre
        self.codigo = codigo
        self.precio = precio
        self.año = año

    def __str__(self):
        return f"{self.nombre} ({self.codigo}) - ${self.precio:.2f} - Año {self.año}"


class Catalogo:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def mostrar_productos(self):
        if not self.productos:
            print("El catálogo está vacío.")
        else:
            for producto in self.productos:
                print(producto)

    def filtrar_por_año(self, año):
        productos_filtrados = [producto for producto in self.productos if producto.año == año]
        if productos_filtrados:
            print(f"Productos del año {año}:")
            for producto in productos_filtrados:
                print(producto)
        else:
            print(f"No hay productos del año {año} en el catálogo.")


if __name__ == "__main__":
    # Ejemplo de uso
    catalogo_autopartes = Catalogo()

    # Agregar productos al catálogo
    producto1 = Producto("Batería", "BT123", 120.50, 2022)
    producto2 = Producto("Filtro de aceite", "FA456", 15.75, 2021)
    producto3 = Producto("Pastillas de freno", "PF789", 50.00, 2022)

    catalogo_autopartes.agregar_producto(producto1)
    catalogo_autopartes.agregar_producto(producto2)
    catalogo_autopartes.agregar_producto(producto3)

    # Mostrar todos los productos en el catálogo
    print("Catálogo completo:")
    catalogo_autopartes.mostrar_productos()

    # Filtrar por año
    año_filtrar = int(input("Ingrese el año para filtrar productos: "))
    catalogo_autopartes.filtrar_por_año(año_filtrar)
