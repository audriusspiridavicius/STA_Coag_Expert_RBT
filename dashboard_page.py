from dataclasses import dataclass
import time
from typing import List
from pywinauto import WindowSpecification
import logging



@dataclass
class DashboardPage:

    refresh_button: WindowSpecification
    home_button: WindowSpecification 

    samples_to_be_validated: List[WindowSpecification]

    def __init__(self, wnd: WindowSpecification, logger:logging.Logger) -> None:
        """
        Initialize the DashboardPage class.
        """
        self.dashboard = wnd
        self.refresh_button = self.dashboard.child_window(control_type="Pane", auto_id="picRafraichir")
        self.home_button = self.dashboard.child_window(control_type="Pane", auto_id="btnHome")
        self.samples_to_be_validated = []
        self.refresh_button.click_input()

        self.pending_checkbox = self.dashboard.child_window(control_type="CheckBox", title="Pending")
        self.rerun_checkbox = self.dashboard.child_window(control_type="CheckBox", title="Selected To Be Rerun")
        self.validated_checkbox = self.dashboard.child_window(control_type="CheckBox", title="Validated")

        self.logger = logger
        
        
        # uncheck the pending checkbox if it is checked
        if self.pending_checkbox.get_toggle_state() == 1:
            self.pending_checkbox.toggle()
            logger.info("Pending checkbox unchecked")

        # uncheck rerun checkbox if it is checked
        if self.rerun_checkbox.get_toggle_state() == 1:
            self.rerun_checkbox.toggle()
            logger.info("Rerun checkbox unchecked")
        
        # uncheck validated checkbox if it is checked
        if self.validated_checkbox.get_toggle_state() == 1:
            self.validated_checkbox.toggle()
            logger.info("Validated checkbox unchecked")



    def get_sample_status(self) -> None:
        """
        Get the status of the sample.
        """
        self.samples_to_be_validated = []
        # self.refresh_button.click_input()
        sample_status_list = self.dashboard.descendants(control_type="DataItem")
        for status in sample_status_list:
            status_value = status.legacy_properties().get('Value').lower()
           
            if status_value == "to be validated":
                self.samples_to_be_validated.append(status)

    def automate_to_be_validated(self) -> None:
        
        """
        Automate the process to be validated.
        """
        time.sleep(1)
        first_row = self.dashboard.child_window(title="Status Row 0")

        if first_row.exists(timeout=1):
            self.logger.info("there is at least 1 sample with status -> to be validated")
            first_row.click_input()
        else:
            self.logger.warning("there is no samples with status -> to be validated")
        
        self.get_sample_status()

        i= 0
        while i < len(self.samples_to_be_validated) and i <= 10:
            sample = self.samples_to_be_validated[i]
            
            if sample.is_visible():

                sample.double_click_input()

                save_button = self.dashboard.child_window(control_type="Button", title="Save")
                save_button.click_input()
                self.get_sample_status()
                i = 0

        if self.pending_checkbox.get_toggle_state() == 0:
            self.pending_checkbox.toggle()

        if self.rerun_checkbox.get_toggle_state() == 0:
            self.rerun_checkbox.toggle()

        if self.validated_checkbox.get_toggle_state() == 0:
            self.validated_checkbox.toggle()
