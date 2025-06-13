import subprocess
import logging
from datetime import datetime

basic_logger = logging.getLogger('basic_logger')
basic_handler = logging.FileHandler('basic_logfile.log')
basic_formatter = logging.Formatter('%(asctime)s - %(message)s')
basic_handler.setFormatter(basic_formatter)
basic_logger.addHandler(basic_handler)
basic_logger.setLevel(logging.INFO)

verbose_logger = logging.getLogger('verbose_logger')
verbose_handler = logging.FileHandler('verbose_logfile.log')
verbose_formatter = logging.Formatter('%(asctime)s - %(message)s')
verbose_handler.setFormatter(verbose_formatter)
verbose_logger.addHandler(verbose_handler)
verbose_logger.setLevel(logging.INFO)

def scan_website(url):
    command = ["wsl", "whatweb", "-a", "3", "-v", url]
    command_str = ' '.join(command)

    basic_logger.info(f"User executed command: {command_str}")
    verbose_logger.info(f"User executed command: {command_str}")

    result = subprocess.run(command, capture_output=True, text=True)

    if result.returncode == 0:
        verbose_logger.info(f"Command output:\n{result.stdout}")
    else:
        verbose_logger.error(f"Command failed with error:\n{result.stderr}")

    return result
