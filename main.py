# main.py

from ui import main_menu

def main():
    while True:
        """
        Función principal que inicia la aplicación.
        """
        print("\n")
        print("=== Sistema de Consulta de Datos de Laboratorio de Suelo ===")
        main_menu()
        if input("Desea realizar otra consulta? (s/n): ") == "n":
            break


if __name__ == "__main__":
    main()