# Importa el módulo os para interactuar con el sistema operativo
# (por ejemplo, crear directorios o manejar rutas de archivos)
import os

# Importa el módulo sys para acceder a funcionalidades del sistema
# como la salida estándar (stdout)
import sys

# Importa el módulo logging para gestionar logs (registros) de la aplicación
import logging

# Define el nombre del directorio donde se guardarán los logs
log_dir = "logs"

# Define el formato que tendrán los mensajes de log
# Incluye: fecha y hora, nivel del log, módulo y mensaje
logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

# Construye la ruta completa del archivo de logs
# El archivo se llamará "continuos_logs.log" dentro del directorio "logs"
log_filepath = os.path.join(log_dir, "continuos_logs.log")

# Crea el directorio de logs si no existe
# exist_ok=True evita errores si el directorio ya existe
os.makedirs(log_dir, exist_ok=True)

# Configura el sistema de logging
logging.basicConfig(
    # Nivel mínimo de los mensajes que se registrarán (INFO y superiores)
    level=logging.INFO,
    
    # Formato que tendrán los mensajes de log
    format=logging_str,

    # Define los manejadores (handlers) del logging
    handlers=[
        # Guarda los logs en un archivo
        logging.FileHandler(log_filepath),
        
        # Muestra los logs por la salida estándar (consola)
        logging.StreamHandler(sys.stdout)
    ]
)

# Crea un logger con nombre personalizado
# Este logger se puede usar en otros módulos del proyecto
logger = logging.getLogger("summarizerlogger")
