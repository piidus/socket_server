import logging

def create_logger(name='app', level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                   file_path='app.log'):
    """
    Creates a logger with specified configuration.

    Args:
        name: Logger name.
        level: Logging level.
        format: Log format.
        file_path: Path to log file.

    Returns:
        Logger instance.
    """

    logger = logging.getLogger(name)
    logger.setLevel(level)

    formatter = logging.Formatter(format)  # Create the formatter

    if file_path:
        file_handler = logging.FileHandler(file_path)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    return logger


# Create the logger
log = create_logger()

# # Use f-string formatting for log message
# SERVER = 9999
# log.info(f"Server listening on port {SERVER}")  # Corrected using f-string