import sys
from pywinauto import application
from pywinauto.timings import TimeoutError as PywinautoTimeoutError 

app = application.Application(backend="uia")

try:
    app.connect(best_match="STAGO_DM_Application", timeout=10)
    app.wait_cpu_usage_lower(threshold=5, timeout=10)

    dm_app = app.window(best_match="STAGO_DM_Application", control_type="Window")

except PywinautoTimeoutError as e:
    print("unable to connect to the application")
    sys.exit()



dm_app.set_focus()
# app.top_window().print_control_identifiers()
# dm_app.print_control_identifiers()


home_button = dm_app.child_window(control_type="Pane", auto_id="btnHome")
if home_button.exists(timeout=2):
    print("home button found")
    home_button.click_input()




refresh_button = dm_app.child_window(control_type="Pane", auto_id="picRafraichir")
dashboard_text = dm_app.child_window(title="Dashboard", control_type="Text")


if dashboard_text.exists(timeout=2):
    print("dashboard text found")
    dashboard_text.click_input()
else:
    print("dashboard text not found")
# print(refresh_button.print_control_identifiers())
dm_app.set_focus()
dm_app.print_control_identifiers()


if refresh_button.exists(timeout=2):

    print("refresh button found")
    refresh_button.click_input()
else:
    print("refresh button not found")

