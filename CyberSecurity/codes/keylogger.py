from pynput import keyboard
import os

log_file = os.path.expanduser(r"C:\Users\Isaac Aires\Downloads\key_log.txt")

def log(message):
    with open(log_file, "a") as f:
        f.write(f"{message}\n")

log("Script iniciado")

def on_press(key):
    try:
        log(f'Alphanumeric key pressed: {key.char}')
    except AttributeError:
        log(f'Special key pressed: {key}')

def on_release(key):
    if key == keyboard.Key.esc:
        log("Listener stopped")
        return False

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
