import logging


class Log:

    def set_up_logging() -> logging.Logger:
        
        """
        Placeholder to be overridden.
        """
        raise NotImplementedError("Subclasses must implement this method")


class BasicLog(Log):

    @staticmethod
    def set_up_logging() -> logging.Logger:
        """
        Set up basic logging configuration.
        """

        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

        logger = logging.getLogger(__name__)
        logger.setLevel(logging.DEBUG)
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.DEBUG)

        
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)
        
        return logger
    

class FileLog(Log):
    
        @staticmethod
        def set_up_logging() -> logging.Logger:
            """
            Set up file logging configuration.
            """
            formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    
            logger = logging.getLogger(__name__)
            logger.setLevel(logging.DEBUG)
            file_handler = logging.FileHandler('coag_expert_robot_logs.log')
            file_handler.setLevel(logging.DEBUG)
    
            file_handler.setFormatter(formatter)
            logger.addHandler(file_handler)
    
            return logger