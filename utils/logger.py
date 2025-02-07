#日志功能

import logging
import os

def setup_logger():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        handlers=[
            logging.FileHandler("reports/test_logs.log"),
            logging.StreamHandler()
        ]
    )