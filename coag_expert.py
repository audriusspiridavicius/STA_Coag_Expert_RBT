from dashboard_page import DashboardPage
from dataclasses import dataclass

from pywinauto import WindowSpecification, Application
from pywinauto.timings import TimeoutError as PywinautoTimeoutError
from pywinauto import application
import sys

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
        if close_button.exists(timeout=1):
            print("Close button found")
            close_button.click_input()
            print("close button (titre) clicked successfully")

        another_close_button = self.stago_dm_app.child_window(control_type="Pane", auto_id="picQuitter")
        if another_close_button.exists(timeout=1):
            print("Close button found")
            another_close_button.click_input()
            print("close button (picQuitter) clicked successfully")

        third_close_button = self.stago_dm_app.child_window(control_type="Pane", auto_id="picFermer")
        if third_close_button.exists(timeout=1):
            print("Close button found")
            third_close_button.click_input()
            print("close button (picFermer) clicked successfully")
    
    def _go_to_home_page(self) -> None:
        """
        Navigate to the home page of the CoagExpert application.
        This method simulates a click on the home button to access the home page.
        """
        home_button = self.stago_dm_app.child_window(control_type="Pane", auto_id="btnHome")
        if home_button.exists(timeout=1):
            print("home button found")
            home_button.click_input()
        else:
            print("home button not found")


    def __init__(self) -> None:
        """
        Initialize the CoagExpert class
        """
        try:

            self.app = application.Application(backend="uia")
            self.app.connect(best_match="STAGO_DM_Application", timeout=10)
        
        except PywinautoTimeoutError as e:

            print("Unable to connect to the coag expert application")
            sys.exit()

        self.stago_dm_app = self.app.window(best_match="STAGO_DM_Application", control_type="Window")
        self.stago_dm_app.set_focus()

        self._close_unwanted_dialogs()
        self._go_to_home_page()

    def go_to_dashboard_page(self)-> DashboardPage:
        """
        Navigate to the dashboard page of the CoagExpert application.
        This method simulates a click on the home button and refresh button to access the dashboard.
        """
        pass


if __name__ == "__main__":
    coag_expert = CoagExpert()

        