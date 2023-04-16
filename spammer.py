import time
import pyautogui as kb
import pydirectinput as input

class Spammer():
    def __init__(self, delay: int, filepath: str):
        self.delay = delay
        self.path = filepath

    def countdown(self, length: int):
        while length > 0:
            self.log("Countdown at " + str(length))
            time.sleep(1)
            length = length - 1

        self.log("Countdown complete.")

    def spam(self):
        file = open(self.path, "r")
        lines = file.readlines()

        for line in lines:
            # kb.typewrite("/")
            kb.typewrite(line.strip())
            input.press("enter")
            time.sleep(self.delay)
        
        self.log("Done typing file.")
        
    def log(self, text: str):
        print(f"[Spammer ({self}) reading {self.path}] says:\n {text}")

