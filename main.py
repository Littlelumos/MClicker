import os
import time

import win32api
import win32con
import win32gui

window = None
finding = True

if __name__ == "__main__":
    os.system("mode con cols=30 lines=6")
    os.system("title MineCraft 后台工具人")
    print("Please input 1 or 2")
    a = input()
    while True:
        if a == "1" or a == "2":
            break
        a = input()
    print("Click the game Window")
    while finding:
        window = win32gui.GetForegroundWindow()
        procName = win32gui.GetWindowText(window)
        if "Minecraft" in procName:
            print("Process Start")
            finding = False
        time.sleep(0.05)
    startTime = time.time()
    while True:
        if window != win32gui.GetForegroundWindow():
            pos = win32api.MAKELONG(100, 100)
            if a == "1":
                win32api.SendMessage(window, win32con.WM_MOUSEMOVE, win32con.MK_LBUTTON, pos)
                win32api.SendMessage(window, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, pos)
                time.sleep(10)
                # win32api.SendMessage(window, win32con.WM_LBUTTONUP, win32con.MK_LBUTTON, pos)
            else:
                win32api.SendMessage(window, win32con.WM_MOUSEMOVE, win32con.MK_RBUTTON, pos)
                win32api.SendMessage(window, win32con.WM_RBUTTONDOWN, win32con.MK_RBUTTON, pos)
                win32api.SendMessage(window, win32con.WM_RBUTTONUP, win32con.MK_RBUTTON, pos)
            i = os.system("cls")
            workTime = time.time() - startTime
            print("已经工作 ", workTime, "秒")
            time.sleep(0.01)

# pyinstaller -F -i beta/src/mcClicker/mcClicker.ico beta/src/mcClicker/main.py
# use this command in cmd to create .exe file!
