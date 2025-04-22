from pynput import mouse, keyboard
import threading
import time
import sys

# Flag to track if input was detected
input_detected = threading.Event()

def on_mouse_move(x, y):
    input_detected.set()

def on_mouse_click(x, y, button, pressed):
    input_detected.set()

def on_key_press(key):
    input_detected.set()

def start_listeners(seconds=5):
    mouse_listener = mouse.Listener(on_move=on_mouse_move, on_click=on_mouse_click)
    keyboard_listener = keyboard.Listener(on_press=on_key_press)
    
    mouse_listener.start()
    keyboard_listener.start()
    
    # Wait for given seconds or until input is detected

    input_detected.wait(timeout=seconds)


    mouse_listener.stop()
    keyboard_listener.stop()

    if input_detected.is_set():
        print("User input detected. Exiting.")
        sys.exit()
    else:
        print(f"No input detected after {seconds} seconds. Exiting.")

if __name__ == "__main__":
    secs = 10
    print(f"Monitoring for user input for {secs} seconds...")
    start_listeners(secs)