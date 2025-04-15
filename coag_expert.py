from logging import Logger
from dashboard_page import DashboardPage
from dataclasses import dataclass, field

from pywinauto import WindowSpecification, Application
from pywinauto.timings import TimeoutError as PywinautoTimeoutError
from pywinauto import application
from pywinauto.findbestmatch import MatchError
import sys
from log import BasicLog, Log, FileLog

@dataclass
class CoagExpert:

    app: Application
    stago_dm_app: WindowSpecification

    def _close_unwanted_dialogs(self) -> None:
    
        """
        Close any unwanted dialogs that may be open in the CoagExpert application.
        This method simulates a click on the close button of any unwanted windows.
        """

        close_button = self.stago_dm_app.child_window(control_type="Pane", title="titre")
        if close_button.exists():
            self.log.info("Close button found")
            close_button.click_input()
            self.log.info("close button (titre) clicked successfully")

        another_close_button = self.stago_dm_app.child_window(control_type="Pane", auto_id="picQuitter")
        if another_close_button.exists():
            self.log.info("Close button found")
            another_close_button.click_input()
            self.log.info("close button (picQuitter) clicked successfully")

        third_close_button = self.stago_dm_app.child_window(control_type="Pane", auto_id="picFermer")
        if third_close_button.exists():
            self.log.info("Close button found")
            third_close_button.click_input()
            self.log.info("close button (picFermer) clicked successfully")
    
    def _go_to_home_page(self) -> None:
        """
        Navigate to the home page of the CoagExpert application.
        This method simulates a click on the home button to access the home page.
        """
        home_button = self.stago_dm_app.child_window(control_type="Pane", auto_id="btnHome")
        if home_button.exists():
            self.log.info("home button found")
            home_button.click_input()
        else:
            self.log.warning("home button not found")


    def __init__(self, loggin_settings:Log = BasicLog.set_up_logging()) -> None:
        """
        Initialize the CoagExpert class
        """
        self.log = loggin_settings
        try:

            self.app = application.Application(backend="uia")
            self.app.connect(best_match="STAGO_DM_Application")
        
            self.stago_dm_app = self.app.window(best_match="STAGO_DM_Application", control_type="Window")
            self.stago_dm_app.set_focus()

            self._close_unwanted_dialogs()
            self._go_to_home_page()

        except (PywinautoTimeoutError, MatchError) as e:

            self.log.error("Unable to connect to the coag expert application")
            sys.exit()

        """ connected to the coag expert application but login window appears """
        
        user_login = self.stago_dm_app.child_window(control_type="Edit", auto_id="tboxUserLogin")
        if user_login.exists(timeout=2):
            self.log.warning("login window found. please enter your credentials")
            sys.exit()


    def go_to_dashboard_page(self)-> DashboardPage:
        """
        Navigate to the dashboard page of the CoagExpert application.
        This method simulates a click on the home button and refresh button to access the dashboard.
        """

        self.stago_dm_app.window(title="Dashboard", control_type="Text").click_input()
        self.log.info("dashboard text found")
        return DashboardPage(self.stago_dm_app, self.log)


if __name__ == "__main__":
    
    file_logger = FileLog.set_up_logging()
    
    coag_expert = CoagExpert(loggin_settings=file_logger)

    dashboard = coag_expert.go_to_dashboard_page()
    dashboard.automate_to_be_validated()




        