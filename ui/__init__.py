# ui/__init__.py

from statistics import median
import api

def _parse_float(val):
    """Convierte valores a float si es posible, manejando strings con coma decimal y símbolos <, >."""
    if val is None:
        return None
    if isinstance(val, (int, float)):
        try:
            return float(val)
        except Exception:
            return None
    try:
        string = str(val).strip()
        if not s:
            return None
        # eliminar símbolos de comparación
        if string[0] in ('<', '>'):
            string = string[1:].strip()
        # soportar coma decimal
        string = string.replace(',', '.')
        return float(string)
    except Exception:
        return None

def _show_results_table_and_medians(resultados: list):
    if not resultados:
        print("\nNo se encontraron resultados.")
        return

    #Determina la clave de Topografía según el archivo
    topografia_key = 'Topografía' if 'Topografía' in resultados[0] else ('Topografia' if 'Topografia' in resultados[0] else 'Topografía')

    #Define columnas a mostrar en la tabla (B, C, D, G)
    headers = ['Departamento', 'Municipio', 'Cultivo', topografia_key]

    #Calcula anchos de columna
    column_widths = []
    for header in headers:
        max_lenght = max([len(str(header))] + [len(str(r.get(header, '') or '')) for r in resultados])
        column_widths.append(max_lenght)

    #Imprime la tabla
    print("\nResultados de la búsqueda:")
    header_line = " | ".join(header.ljust(width) for header, width in zip(headers, column_widths))
    separation_line = "-+-".join('-' * width for width in column_widths)
    print(header_line)
    print(separation_line)
    for row in resultados:
        row_vals = [str(row.get(header, '') or '') for header in headers]
        print(" | ".join(val.ljust(width) for val, width in zip(row_vals, column_widths)))

    #Calcula medianas de variables edáficas (pH, Fosforo, Potasio)
    ph_vals = [val for val in (_parse_float(r.get('pH')) for r in resultados) if val is not None]
    fosforo_vals = [val for val in (_parse_float(r.get('Fosforo')) for r in resultados) if val is not None]
    potasio_vals = [val for val in (_parse_float(r.get('Potasio')) for r in resultados) if val is not None]

    def _median_or_none(values):
        try:
            return float(median(values)) if values else None
        except Exception:
            return None

    m_ph = _median_or_none(ph_vals)
    m_fosforo = _median_or_none(fosforo_vals)
    m_potasio = _median_or_none(potasio_vals)

    print("\nMedianas de variables edáficas:")
    print(f"  pH: {m_ph:.2f}" if m_ph is not None else "  pH: N/A")
    print(f"  Fósforo: {m_fosforo:.2f}" if m_fosforo is not None else "  Fósforo: N/A")
    print(f"  Potasio: {m_potasio:.2f}" if m_potasio is not None else "  Potasio: N/A")

# --------------------------------------------------------------------

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

    resultados = api.search_data(search_data)

    if resultados:
        _show_results_table_and_medians(resultados)
    else:
        print("\nNo se encontraron resultados.")

if __name__ == "__main__":
    main_menu()
