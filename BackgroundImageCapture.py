#Background capture Package
import win32gui
import win32ui
from ctypes import windll
from PIL import Image
import sys

#Background click Package
import pywinauto
import pyautogui

from PIL import ImageDraw
from PIL import ImageChops
from PIL import ImageStat


class customEX(BaseException): pass

try:
    # hwnd = win32gui.FindWindow(None, 'LDPlayer(64)')
    hwnd = win32gui.FindWindow(None, 'abc.txt - Windows 메모장')

    if hwnd == 0:
        print("앱 실행 안됨")
        raise customEX
        
    # Change the line below depending on whether you want the whole window
    # or just the client area. 
    #left, top, right, bot = win32gui.GetClientRect(hwnd)
    left, top, right, bot = win32gui.GetWindowRect(hwnd)
    w = right - left
    h = bot - top

    print (left)
    print (top)
    print (w)

    hwndDC = win32gui.GetWindowDC(hwnd)
    mfcDC  = win32ui.CreateDCFromHandle(hwndDC)
    saveDC = mfcDC.CreateCompatibleDC()

    saveBitMap = win32ui.CreateBitmap()
    saveBitMap.CreateCompatibleBitmap(mfcDC, w, h)

    saveDC.SelectObject(saveBitMap)

    # Change the line below depending on whether you want the whole window
    # or just the client area. 
    #result = windll.user32.PrintWindow(hwnd, saveDC.GetSafeHdc(), 1)
    result = windll.user32.PrintWindow(hwnd, saveDC.GetSafeHdc(), 0)
    print (result)

    bmpinfo = saveBitMap.GetInfo()
    bmpstr = saveBitMap.GetBitmapBits(True)

    im = Image.frombuffer(
        'RGB',
        (bmpinfo['bmWidth'], bmpinfo['bmHeight']),
        bmpstr, 'raw', 'BGRX', 0, 1)

    win32gui.DeleteObject(saveBitMap.GetHandle())
    saveDC.DeleteDC()
    mfcDC.DeleteDC()
    win32gui.ReleaseDC(hwnd, hwndDC)

    if result == 1:
        #PrintWindow Succeeded
        im.save("test.png")


    



    # x = -1400
    # y = 390
    # pyautogui.doubleClick(x, y)
    # pyautogui.lo
except customEX:
    pass

