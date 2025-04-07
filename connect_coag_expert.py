import sys
from pywinauto import application
from pywinauto.timings import TimeoutError as PywinautoTimeoutError 

app = application.Application(backend="uia")

try:
    app.connect(best_match="STAGO_DM_Application", timeout=10)
    app.wait_cpu_usage_lower(threshold=5, timeout=10)

    dm_app = app.window(best_match="STAGO_DM_Application", control_type="Window")
    dm_app.set_focus()

    print("Application connected and focused.")

except PywinautoTimeoutError as e:
    print("unable to connect to the application")
    sys.exit()