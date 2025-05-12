from proxy import ProxyDocumento

def main():
    doc_admin = ProxyDocumento("Plan estratégico 2025", "admin")
    doc_invitado = ProxyDocumento("Plan estratégico 2025", "invitado")

    print("Intento de acceso como admin:")
    doc_admin.mostrar()

    print("\nIntento de acceso como invitado:")
    doc_invitado.mostrar()

if __name__ == "__main__":
    main()
