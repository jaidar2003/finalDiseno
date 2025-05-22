class PersonaView:
    def listar_facturas(self, persona):
        from controllers.persona_controller import PersonaController
        
        persona_controller = PersonaController()
        
        facturas = persona_controller.get_facturas(persona)
        
        if not facturas:
            print(f"{persona.nombre} {persona.apellido} no tiene facturas asociadas.")
            return
        
        print(f"Facturas de {persona.nombre} {persona.apellido}:")
        for i, factura in enumerate(facturas, 1):
            print(f"{i}. Factura tipo {factura.tipo} - Fecha: {factura.fecha} - Total: ${factura.controlador.total(factura)}")