import os.path
from os import makedirs, environ
from loguru import logger
import sys

__all__ = ["logger"]

class EZLogger:
    def __init__(self,
                 log_level: str = None, 
                 log_dir: str = None,
                 log_sys: bool = None,
                 *args, **kwargs):
        
        self.log_level = log_level or environ.get("LOG_LEVEL", "INFO")
        self.log_dir = log_dir or environ.get("LOG_DIR", os.path.join(os.path.expanduser("~"), ".cache", "shiertier", "logs"))
        self.log_sys = log_sys if log_sys is not None else environ.get("LOG_SYS", "True").lower() in ["1", "true"]

        makedirs(self.log_dir, exist_ok=True)
        
        log_file_path = os.path.join(self.log_dir, "file_{time}.log")
        logger.add(log_file_path, rotation="1 MB", level=self.log_level)
        
        if self.log_sys:
            logger.add(sys.stdout, level=self.log_level)

    def __getattr__(self, name):
        return getattr(logger, name)

ez_logger = EZLogger()

# TODO

# try:
#     from shiertier_i18n import i18n
# except ImportError:
#     logger.warning("shiertier_i18n not found, can't use translation support")
#     def i18n(message: str, replace_dict: Dict[str, Any] = None) -> str:
#         if replace_dict:
#             for key, value in replace_dict.items():
#                 message = message.replace(key, value)
#         return message

# class Logger_I18n:
#     def __init__(self, base_logger, i18n_func):
#         self.base_logger = base_logger
#         self.i18n_func = i18n_func

#     def info(self, message: str, replace_dict: Dict[str, Any] = None) -> None:
#         """Logs an info message with translation support."""
#         translated_message = self.i18n_func(message, replace_dict)
#         self.base_logger.info(translated_message)

#     def debug(self, message: str, replace_dict: Dict[str, Any] = None) -> None:
#         """Logs a debug message with translation support."""
#         translated_message = self.i18n_func(message, replace_dict)
#         self.base_logger.debug(translated_message)

#     def warning(self, message: str, replace_dict: Dict[str, Any] = None) -> None:
#         """Logs a warning message with translation support."""
#         translated_message = self.i18n_func(message, replace_dict)
#         self.base_logger.warning(translated_message)

#     def error(self, message: str, replace_dict: Dict[str, Any] = None) -> None:
#         """Logs an error message with translation support."""
#         translated_message = self.i18n_func(message, replace_dict)
#         self.base_logger.error(translated_message)

# easy_logger_i18n = Logger_I18n(logger, i18n)