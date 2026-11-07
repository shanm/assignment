# Logging
import logging

# defin file handler and formatter
logger = logging.basicConfig(
    filename='./app.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

logger.info("This is an info message")