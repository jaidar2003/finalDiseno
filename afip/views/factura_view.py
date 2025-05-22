class FacturaView:
    def mostrar_factura(self, factura):
        print(f"Factura tipo {factura.tipo} - Fecha: {factura.fecha}")
        print(f"Cliente: {factura.cliente.nombre} {factura.cliente.apellido} ({factura.cliente.tipo_responsable})")
        print(f"Emitida por: {factura.administrativo.nombre} {factura.administrativo.apellido} ({factura.administrativo.cargo})")
        
        print("\nDetalle:")
        for d in factura.detalles:
            print(f"- {d.producto.nombre} x{d.cantidad} = ${d.subtotal}")
        
        print(f"\nTOTAL: ${factura.controlador.total(factura)}")

    def mostrar_stock_restante(self, producto):
        print(f"Stock restante de {producto.nombre}: {producto.stock}")