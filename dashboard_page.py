from dataclasses import dataclass
from typing import List, Optional

@dataclass
class DashboardPage:

    refresh_button: str = "Refresh"
    home_button: str = "Home"
