import pyautogui
import time
import random

with open('passwords.txt', 'r') as file:
    passwords = file.readlines()

time.sleep(5)

for password in passwords:
    password = password.strip()

    pyautogui.typewrite(password)

    pyautogui.press('enter')

    pyautogui.hotkey('ctrl', 'a')
    pyautogui.press('backspace')

for _ in range(99999999999):
    random_password = ''.join(random.choices(password.strip(), k=random.randint(1, 32)))
    pyautogui.typewrite(random_password)
    pyautogui.press('enter')
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.press('backspace')
