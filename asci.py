
import codecs
from time import sleep
from pyautogui import press, typewrite, hotkey, keyDown, keyUp
import keyboard

sleep(2)

keyboard.press_and_release("t")
keyboard.write("Amazing thing")
keyboard.press_and_release("enter")


def w():
    with codecs.open('print.txt', encoding='utf-8') as f:
        for line in f:
            sleep(0.05)
            keyboard.press_and_release("t")
            keyboard.press_and_release("backspace")
            keyboard.write(line)
            keyboard.press_and_release("enter")
            keyboard.press_and_release("t")
            keyboard.press_and_release("backspace")
            keyboard.write(line)
            keyboard.press_and_release("enter")


def r():
    with codecs.open('text.txt', encoding='utf-8') as f:
        words = f.read().split()
        for line in words:
            sleep(0.05)
            keyboard.press_and_release("t")
            keyboard.press_and_release("backspace")
            keyboard.write(line)
            keyboard.press_and_release("enter")
            keyboard.press_and_release("t")
            keyboard.press_and_release("backspace")
            keyboard.write(line)
            keyboard.press_and_release("enter")


w()
