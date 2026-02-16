from modelos.producto import Producto


class Inventario:
    """
    Clase encargada de gestionar los productos.
    """

    def __init__(self):
        self.productos = []

    def agregar_producto(self, id_producto, nombre, cantidad, precio):
        if self.buscar_por_id(id_producto):
            print("Ya existe un producto con ese ID.")
            return

        producto = Producto(id_producto, nombre, cantidad, precio)
        self.productos.append(producto)
        print("Producto agregado correctamente.")

    def eliminar_producto(self, id_producto):
        producto = self.buscar_por_id(id_producto)

        if producto:
            self.productos.remove(producto)
            print("Producto eliminado.")
        else:
            print("Producto no encontrado.")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        producto = self.buscar_por_id(id_producto)

        if producto:
            if cantidad is not None:
                producto.set_cantidad(cantidad)
            if precio is not None:
                producto.set_precio(precio)
            print("Producto actualizado.")
        else:
            print("Producto no encontrado.")

    def buscar_por_id(self, id_producto):
        for producto in self.productos:
            if producto.get_id() == id_producto:
                return producto
        return None

    def buscar_por_nombre(self, nombre):
        resultados = []
        for producto in self.productos:
            if nombre.lower() in producto.get_nombre().lower():
                resultados.append(producto)
        return resultados

    def mostrar_inventario(self):
        if not self.productos:
            print("Inventario vacío.")
            return

        for producto in self.productos:
            print(producto)
