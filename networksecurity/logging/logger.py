import logging
import os
from datetime import datetime

# Use a safe timestamp (no slashes) for the log filename
LOG_FILE = datetime.now().strftime('%Y_%m_%d_%H_%M_%S') + '.log'

# Ensure the logs directory exists (don't include the filename here)
logs_dir = os.path.join(os.getcwd(), "logs")
os.makedirs(logs_dir, exist_ok=True)

LOG_FILE_PATH = os.path.join(logs_dir, LOG_FILE)

# Configure logging to write to the full path
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

# Provide a convenience logger object
logger = logging.getLogger(__name__)