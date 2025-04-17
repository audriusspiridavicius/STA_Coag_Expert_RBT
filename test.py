import ctypes
import tkinter as tk
import threading
import time
from pywinauto.application import Application
from pywinauto import application

def show_overlay_message(parent_rect, text="Automation in Progress..."):
    overlay = tk.Tk()
    overlay.overrideredirect(True)  # Remove window borders
    overlay.attributes('-topmost', True)
    overlay.attributes('-alpha', 0.7)  # Transparency: 0 (invisible) to 1 (opaque)
    overlay.configure(bg='black')

    # Set window size
    width, height = 300, 50
    x = parent_rect.left + (parent_rect.width() - width) // 2
    y = parent_rect.top + (parent_rect.height() - height) // 2
    overlay.geometry(f"{width}x{height}+{x}+{y}")

    # Add label
    label = tk.Label(overlay, text=text, fg='white', bg='black', font=('Arial', 14))
    label.pack(expand=True)

    # Prevent closing
    overlay.protocol("WM_DELETE_WINDOW", lambda: None)

    overlay.mainloop()


if __name__ == "__main__":
    try:    # === Your pywinauto automation starts here ===
        app = application.Application(backend="uia")
        app.connect(best_match="STAGO_DM_Application")
        dlg = app.window(best_match="STAGO_DM_Application", control_type="Window")
        dlg.set_focus()
        ctypes.windll.user32.BlockInput(True)
        # Wait for the window to be ready
        # dlg.wait('ready', timeout=10)

        # Get the app window's rectangle (screen position)
        rect = dlg.rectangle()

        # Show the overlay in a separate thread
        threading.Thread(target=show_overlay_message, args=(rect, "Please wait"), daemon=True).start()
        time.sleep(5)
        ctypes.windll.user32.BlockInput(False)
        time.sleep(5)
        
        

        ctypes.windll.user32.BlockInput(True)
        time.sleep(5)
        raise ValueError("An error occurred during automation.")
    except Exception as e:
        print(f"Error: {e}")
        ctypes.windll.user32.BlockInput(False)
    # Simulate some automation task
    # time.sleep(10)
    finally:
        print("Automation finished.")