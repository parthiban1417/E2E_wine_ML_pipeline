import os
import sys
import logging

logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

log_dir = "logs"
log_filepath = os.path.join(log_dir,"running_logs.log")
os.makedirs(log_dir, exist_ok=True)


logging.basicConfig(
    level= logging.INFO,
    format= logging_str,
    handlers=[
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)
        ]
)

<<<<<<< HEAD
logger = logging.getLogger("mlprojectLogger")
=======
logger = logging.getLogger("mlProjectLogger")
>>>>>>> 1942e1ca8ed2175db5bc9316b345c976c2521f58
