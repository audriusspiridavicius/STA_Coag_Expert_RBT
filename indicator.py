
from pywinauto import Application
import tkinter as tk
import threading


class Indicator:
    """
    Base class for all indicators.
    """


    def apply(self, app:Application) -> None:
        pass


class MessageIndicator(Indicator):
    """
    Class for message indicators.
    """

    def __init__(self, message: str) -> None:
        """
        Initialize the MessageIndicator class.

        :param message: The message to be displayed.
        """
        self.message = message

    def apply(self, app:Application) -> None:
        """
        Apply the message indicator.
        """
        
        # get window rectangle
        dlg = app.window(best_match="STAGO_DM_Application", control_type="Window")
        
        # Get the app window's rectangle (screen position)
        rect = dlg.rectangle()

        threading.Thread(target=self._show_overlay_message, args=(rect, ), daemon=True).start()
        
        print(f"Message: {self.message}")

    def _show_overlay_message(self, parent_rect):
        
        bg_color = '#5c8691'
        
        overlay = tk.Tk()
        overlay.overrideredirect(True)  # Remove window borders
        overlay.attributes('-topmost', True)
        overlay.attributes('-alpha', 0.9)  # Transparency: 0 (invisible) to 1 (opaque)
        overlay.configure(bg=bg_color)

        # Set window size
        width, height = 400, 80
        x = parent_rect.left + (parent_rect.width() - width) // 2
        y = parent_rect.top + (parent_rect.height() - height) // 2
        overlay.geometry(f"{width}x{height}+{x}+{y}")

        # Add label
        # label = tk.Label(overlay, text=self.message, fg='white', bg=bg_color, font=('Arial', 18))
        # label = tk.Label(overlay, text=self.message, fg='white', bg=bg_color, font=('Segoe UI', 18, 'bold'))
        label = tk.Label(overlay, text=self.message, fg='white', bg=bg_color, font=('Helvetica', 18, 'bold'))
        label.pack(expand=True)

        # Prevent closing
        overlay.protocol("WM_DELETE_WINDOW", lambda: None)

        overlay.mainloop()    