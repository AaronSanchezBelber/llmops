# Importa el módulo os para interactuar con el sistema operativo
import os

# Importa la excepción BoxValueError del paquete box
# Se usa para manejar errores relacionados con ConfigBox
from box.exceptions import BoxValueError

# Importa yaml para leer archivos de configuración en formato YAML
import yaml

# Importa el logger personalizado del proyecto
from src.textSummarizer.logging import logger

# Importa ensure_annotations para asegurar que se respeten las anotaciones de tipos
from ensure import ensure_annotations

# Importa ConfigBox, que permite acceder a diccionarios usando notación de punto
from box import ConfigBox

# Importa Path para manejar rutas de archivos de forma más segura
from pathlib import Path

# Importa Any para anotaciones de tipo genéricas
from typing import Any


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    Lee un archivo YAML y lo devuelve como un objeto ConfigBox

    Args:
        path_to_yaml (Path): ruta del archivo YAML de entrada

    Raises:
        ValueError: si el archivo YAML está vacío
        e: cualquier otra excepción que pueda ocurrir

    Returns:
        ConfigBox: contenido del archivo YAML en formato ConfigBox
    """
    try:
        # Abre el archivo YAML en modo lectura
        with open(path_to_yaml) as yaml_file:
            # Carga el contenido del archivo YAML
            content = yaml.safe_load(yaml_file)
            
            # Registra en el log que el archivo YAML se cargó correctamente
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            
            # Devuelve el contenido como un objeto ConfigBox
            return ConfigBox(content)

    # Captura el error específico cuando el YAML está vacío
    except BoxValueError:
        raise ValueError("el archivo yaml está vacío")

    # Captura cualquier otra excepción y la relanza
    except Exception as e:
        raise e
    

@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """
    Crea una lista de directorios

    Args:
        path_to_directories (list): lista de rutas de directorios a crear
        verbose (bool, opcional): si es True, muestra mensajes en el log. Por defecto True
    """
    # Recorre cada ruta de directorio
    for path in path_to_directories:
        # Crea el directorio (no falla si ya existe)
        os.makedirs(path, exist_ok=True)
        
        # Si verbose está activado, registra el mensaje en el log
        if verbose:
            logger.info(f"directorio creado en: {path}")
