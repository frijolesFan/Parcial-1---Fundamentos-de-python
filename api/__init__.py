# api/__init__.py (fragmento)

import unicodedata
from openpyxl import load_workbook
from pathlib import Path

#Crea la direccion con pathlib ya que genera problemas usando rutas convencionales

#Carpeta raíz del proyecto (dos niveles arriba desde api/)
BASE_DIR = Path(__file__).resolve().parent.parent

#Construye la ruta al archivo en data/
file_path = BASE_DIR / "data" / "resultado_laboratorio_suelo.xlsx"

#------------------------------------------------------------------------------

def _normalize_text(input_text: str) -> str:
    if input_text is None:
        return None
    input_text = ''.join(c for c in unicodedata.normalize('NFKD', input_text) if not unicodedata.combining(c))
    return input_text.lower()

#------------------------------------------------------------------------------

#Abre el archivo
work_book = load_workbook(file_path)
work_sheet = work_book.active   #Hoja activa


#------------------------------------------------------------------------------

def search_data(search_data: dict) -> list:
    """
    Busca datos en el archivo Excel basados en los criterios proporcionados.
    """
    # Obtener los encabezados de la hoja de cálculo
    headers = [cell.value for cell in work_sheet[1]]