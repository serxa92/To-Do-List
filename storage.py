import json
from pathlib import Path

# Archivo donde están las tareas en formato JSON.

DATA_FILE = Path("tasks.json")

def read_tasks():
    """
    Esta función lee las tareas desde el archivo JSON.
    Si el archivo no existe, devuelve una lista vacía.

    Returns:
        list: Lista de tareas.
    """
    if DATA_FILE.exists():
        with DATA_FILE.open("r", encoding="utf-8") as f:
            return json.load(f)
    return []
    


# Función para escribir las tareas en el JSON.

def write_tasks(tasks):
    """
    Esta función escribe las tareas en el archivo JSON. Abre el archivo en modo escritura y guarda la lista de tareas en formato JSON.

    Args:
        tasks (list): Lista de tareas a escribir.
    """
    
    with DATA_FILE.open("w", encoding="utf-8") as f:
        json.dump(tasks, f, ensure_ascii=False, indent=2)
        