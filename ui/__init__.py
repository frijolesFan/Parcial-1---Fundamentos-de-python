# ui/__init__.py


def main_menu():
    search_data = {
        "Departamento": "",
        "Municipio": "",
        "Cultivo": "",
        "Numero de datos": ""
    }

    search_data["Departamento"] = input("Ingrese el departamento: ").lower()
    search_data["Municipio"] = input("Ingrese el municipio: ").lower()
    search_data["Cultivo"] = input("Ingrese el cultivo: ").lower()
    search_data["Numero de datos"] = input("Ingrese el número de datos a mostrar: ")
    
    # Aquí puedes usar funciones del módulo api para procesar los datos
    # Por ejemplo: resultados = api.buscar_datos(search_data)
    
    print("Datos de búsqueda:")
    for key, value in search_data.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    main_menu()
