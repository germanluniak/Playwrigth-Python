import json
import os

def load_config_json(file_name):
    # Construir la ruta absoluta al archivo de configuración
    file_path = os.path.join(os.path.dirname(__file__), '..', 'config', file_name)

    # Verificar si el archivo existe
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"El archivo de configuración {file_path} no se encuentra.")

    # Leer el archivo JSON
    with open(file_path, 'r') as file:
        return json.load(file)
