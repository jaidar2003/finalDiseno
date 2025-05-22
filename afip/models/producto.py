from controllers.producto_controller import ProductoController

class Producto:
    """
    Clase que representa un producto en el sistema.

    Los productos son entidades que pueden ser incluidas en los detalles de las facturas.
    Cada producto tiene un nombre, precio y una cantidad en stock que se reduce cuando
    se incluye en una factura.

    Atributos:
        nombre (str): Nombre del producto
        precio (float): Precio unitario del producto
        stock (int): Cantidad disponible del producto
        controlador (ProductoController): Controlador asociado que maneja la lógica de negocio
    """
    def __init__(self, nombre, precio, stock):
        """
        Constructor de la clase Producto.

        Args:
            nombre (str): Nombre del producto
            precio (float): Precio unitario del producto
            stock (int): Cantidad disponible del producto
        """
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

        # Asociación con el controlador - Implementa el patrón de diseño Composition
        # El controlador maneja operaciones como descontar stock
        self.controlador = ProductoController()
