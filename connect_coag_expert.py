import sys
from pywinauto import application
from pywinauto.timings import TimeoutError as PywinautoTimeoutError 
import time
import ctypes

app = application.Application(backend="uia")

try:
    ctypes.windll.user32.BlockInput(True)

    app.connect(best_match="STAGO_DM_Application", timeout=10)
    app.wait_cpu_usage_lower(threshold=5, timeout=10)

    dm_app = app.window(best_match="STAGO_DM_Application", control_type="Window")
    dm_app.set_focus()
    dm_app.print_control_identifiers()
    print("Application connected and focused.")
    time.sleep(5)


except PywinautoTimeoutError as e:
    print("unable to connect to the application")
    ctypes.windll.user32.BlockInput(False)
    sys.exit()
finally:
    ctypes.windll.user32.BlockInput(False)
    print("Automation completed.")