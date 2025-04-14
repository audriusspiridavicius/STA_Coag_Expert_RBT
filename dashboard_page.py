from dataclasses import dataclass, field
from typing import List, Optional
from pywinauto import WindowSpecification
from pywinauto.keyboard import SendKeys
from pywinauto.mouse import scroll
from pywinauto.keyboard import send_keys
@dataclass
class DashboardPage:

    refresh_button: WindowSpecification
    home_button: WindowSpecification 

    samples_to_be_validated: List[WindowSpecification]

    def __init__(self, wnd: WindowSpecification) -> None:
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

        # uncheck the pending checkbox if it is checked
        if self.pending_checkbox.get_toggle_state() == 1:
            self.pending_checkbox.toggle()
            print("Pending checkbox unchecked")

        # uncheck rerun checkbox if it is checked
        if self.rerun_checkbox.get_toggle_state() == 1:
            self.rerun_checkbox.toggle()
            print("Rerun checkbox unchecked")
        
        # uncheck validated checkbox if it is checked
        if self.validated_checkbox.get_toggle_state() == 1:
            self.validated_checkbox.toggle()
            print("Validated checkbox unchecked")



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
        
        first_row = self.dashboard.child_window(title="Status Row 0")
        if first_row.exists(timeout=1):
            print("Sample ID found")
            first_row.click_input()
        self.get_sample_status()
        for sample in self.samples_to_be_validated:
            
            while not sample.is_visible():
                page_down_button = self.dashboard.child_window(title="DataGridView")
                if page_down_button.exists(timeout=1):
                    send_keys("{PGDN}")
                    print("Page down button clicked")

                # self.dashboard.send_keys("{PGDN}")    
                # SendKeys("{PGDN}")
            
            
            if sample.is_visible():
                print(f"Sample {sample} is visible")
                # self.refresh_button.click_input()
                sample.double_click_input()

                save_button = self.dashboard.child_window(control_type="Button", title="Save")
                save_button.click_input()
                self.get_sample_status()
            else:
                print(f"Sample {sample} is not visible")

        if self.pending_checkbox.get_toggle_state() == 0:
            self.pending_checkbox.toggle()

        if self.rerun_checkbox.get_toggle_state() == 0:
            self.rerun_checkbox.toggle()

        if self.validated_checkbox.get_toggle_state() == 0:
            self.validated_checkbox.toggle()
