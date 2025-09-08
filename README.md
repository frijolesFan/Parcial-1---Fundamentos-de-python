# Parcial-1 - Fundamentos-de-python

Permite consultar datos de laboratorio de suelo almacenados en un archivo Excel, filtrando por departamento, municipio y cultivo.

## Estructura del Proyecto

```
├── api/              # Módulo para acceso a datos
├── data/             # Datos de laboratorio de suelo en Excel
├── ui/               # Interfaz de usuario
├── main.py           # Punto de entrada principal
└── README.md         # Este archivo
```

## Funcionalidades

- Búsqueda de datos por departamento, municipio y cultivo
- Visualización de resultados con todos los campos disponibles
- Limitación del número de resultados a mostrar

## Módulos

### api/

Contiene la lógica para acceder y filtrar los datos del archivo Excel.

### ui/

Contiene la interfaz de usuario para interactuar con la aplicación.

## Requisitos

- Python 3.6 o superior
- openpyxl (para manejo de archivos Excel)
- numpy

### Información para el desarrollador
El documento de excel contiene las siguientes columnas relevanes:
- B: Departamento
- C: Municipio
- D: Cultivo
- M - AF: Datos de laboratorio (Variables edáficas)