import logging
import os


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
            
            system_drive = os.environ.get('SYSTEMDRIVE', 'C:')
            
            if not os.path.exists(f'{system_drive}\\coag_exp_logs'):
                os.makedirs(f'{system_drive}\\coag_exp_logs')
            file_handler = logging.FileHandler(f'{system_drive}\\coag_exp_logs\\coag_expert_robot_logs.log', mode='a+')
            file_handler.setLevel(logging.DEBUG)
    
            file_handler.setFormatter(formatter)
            logger.addHandler(file_handler)
    
            return logger