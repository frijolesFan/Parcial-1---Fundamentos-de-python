# main.py

from ui import main_menu

def main():
    print("=== Sistema de Consulta de Datos de Laboratorio de Suelo ===")
    while True:
        """
        Función principal que inicia la aplicación.
        """
        main_menu()
        if input("Desea realizar otra consulta? (s/n): ") == "n":
            break
        print("\n")


if __name__ == "__main__":
    main()