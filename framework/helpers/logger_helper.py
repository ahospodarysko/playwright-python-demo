import inspect
import sys

import allure
from loguru import logger


class LoggerHelper:

    @staticmethod
    def configure_logger():
        """Configure Loguru for the entire project."""
        logger.remove()  # Remove default Loguru handlers to prevent duplicates
        logger.add(
            sys.stderr,
            format="<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | "
                   "<level>{level: <8}</level> | "
                   "<cyan>{module}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>",
            level="INFO",
        )

    @staticmethod
    def log_step(message: str):
        """Logs a message both to the console and Allure report with caller details."""
        caller = inspect.stack()[1]  # Get caller method info
        class_name = caller.frame.f_locals.get("self",
                                               None).__class__.__name__ if "self" in caller.frame.f_locals else "UnknownClass"  # Get the class name
        method_name = caller.function  # Get the method name
        line_number = caller.lineno  # Get the line number

        formatted_message = f"{class_name}.{method_name}:{line_number} - {message}"

        logger.info(formatted_message)
        with allure.step(message):
            pass  # Ensures step appears in Allure report
