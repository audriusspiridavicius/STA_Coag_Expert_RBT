from dataclasses import dataclass
from typing import List, Optional
from pywinauto import WindowSpecification, Application


@dataclass
class Page:

    """
    Base class for all pages.
    """

    def __init__(self, app:Application) -> None:
        pass
    
    def open(self) -> None:
        """
        Open the page.
        """
        pass

    def execute_automation(self) -> None:
        """
        Execute automation on the page.
        """
        pass