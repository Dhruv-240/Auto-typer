import pyautogui
import time
import random
import threading

# Function to save every 120 seconds
def background_save():
    while True:
        time.sleep(120)
        # Trigger Ctrl+S to save
        pyautogui.hotkey("ctrl", "s")
        print("\n[SYSTEM] Auto-saved file.")

def autotype(text):
    print("\n[!!!] 5 SECONDS TO CLICK INTO testing.py EDITOR [!!!]")
    time.sleep(5)

    # Start the background saving thread
    # daemon=True ensures the thread dies when the main script ends
    save_thread = threading.Thread(target=background_save, daemon=True)
    save_thread.start()

    # Clear file first
    pyautogui.hotkey("ctrl", "a")
    time.sleep(0.2)
    pyautogui.press("backspace")

    for char in text:
        pyautogui.write(char)
        # Typing speed logic
        time.sleep(random.uniform(0.50, 0.75))

        if char in {'.', ',', '!', '?', ';', ':'}:
            time.sleep(random.uniform(0.75, 1))

    pyautogui.write('\n')
    pyautogui.hotkey("ctrl", "s") # Final save after typing is done
    print("[DONE] Typing complete and final save performed.")

while True:
    autotype("print('Hello, World!')")