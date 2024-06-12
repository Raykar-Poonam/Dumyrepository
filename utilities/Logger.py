import inspect
import logging

class Logging_Class():

    @staticmethod
    def log_generator():
        name = inspect.stack()[1][3]
        logger = logging.getLogger(name)
        logfile = logging.FileHandler(".\\Logs\\credkart_logfile.logs")
        logformat = logging.Formatter("%(asctime)s : %(levelname)s: %(levelno)s : %(pathname)s : %(filename)s : %(module)s : %(name)s  : %(funcName)s : %(message)s")
        logfile.setFormatter(logformat)
        logger.addHandler(logfile)
        logger.setLevel(logging.INFO)
        return logger




# import logging
#
# class Logging_Class():
#
#     @staticmethod
#     def log_generator():
#         logger = logging.getLogger()
#         logfile = logging.FileHandler(".\\Logs\\credkart_logfile.logs")
#         logformat = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(funcName)s : %(message)s")
#         logfile.setFormatter(logformat)
#         logger.addHandler(logfile)
#         logger.setLevel(logging.INFO)
#         return logger
#
