import pyautogui
import sys
import time

class customEX(BaseException): pass

ButtonImageSetPath = "ButtonImageSet/"
buttonClickWait = 3

def getImageCenter(imageFileName):
    imageCenter = pyautogui.locateCenterOnScreen(ButtonImageSetPath + imageFileName, confidence=0.6)
    return imageCenter



try:

    # while True:
        appName = getImageCenter('appName.png')
        if appName == None:
            print("앱 못 찾음")
            raise customEX
        else:
            pyautogui.click(appName)
        


        while getImageCenter('lobbyStart.png') == None:
            print("앱 로딩 대기중")
            time.sleep(3)

        time.sleep(buttonClickWait)

        lobbyStart = getImageCenter('lobbyStart.png')
        if lobbyStart == None:
            print("로비버튼 못 찾음")
            raise customEX
        else:
            pyautogui.click(lobbyStart)

        time.sleep(buttonClickWait)
        
        chooseGame = getImageCenter('chooseGame.png')
        if chooseGame == None:
            print("경기장 못 찾음")
            raise customEX
        else:
            pyautogui.click(chooseGame)

        time.sleep(buttonClickWait)

        moveMap = getImageCenter('moveMap.png')
        if moveMap == None:
            print("랜드 이동하기 못 찾음")
            raise customEX
        else:
            pyautogui.click(moveMap)

        time.sleep(buttonClickWait)


        chooseMap = getImageCenter('chooseMap.png')
        if chooseMap == None:
            print("랜드 1 못 찾음")
            raise customEX
        else:
            pyautogui.click(chooseMap)

        time.sleep(buttonClickWait)


        confirmChooseMap = getImageCenter('confirmChooseMap.png')
        if confirmChooseMap == None:
            print("랜드 1 입장 버튼 못 찾음")
            raise customEX
        else:
            pyautogui.click(confirmChooseMap)

        time.sleep(buttonClickWait)


        startButton = getImageCenter('StartButton.png')
        if startButton == None:
            print("시작 버튼 못 찾음")
            raise customEX
        else:
            pyautogui.click(startButton)

        time.sleep(buttonClickWait)
        

        confirmStart = getImageCenter('confirmStart.png')
        if confirmStart == None:
            print("시작 확인 버튼 못 찾음")
            raise customEX
        else:
            pyautogui.click(confirmStart)

        time.sleep(buttonClickWait)

        while getImageCenter('secondRun.png') == None:
            print("이어달리기 버튼 대기중")
            time.sleep(0.5)


        time.sleep(1)
        
        secondRun = getImageCenter('secondRun.png')
        if secondRun == None:
            print("이어달리기 버튼 못 찾음")
            raise customEX
        else:
            pyautogui.click(secondRun)

        time.sleep(buttonClickWait)


        while getImageCenter('AfterRun_first.png') == None:
            print("달리기 종료 대기중")
            time.sleep(0.5)

        AfterRun_first = getImageCenter('AfterRun_first.png')
        if AfterRun_first == None:
            print("종료 후 점수 확인 못 찾음")
            raise customEX
        else:
            pyautogui.click(AfterRun_first)

        time.sleep(buttonClickWait)


        while getImageCenter('AfterRun_Second.png') == None:
            print("주머니 확인 대기중")
            time.sleep(0.5)

        AfterRun_Second = getImageCenter('AfterRun_Second.png')
        if AfterRun_Second == None:
            print("주머니 확인 못 찾음")
            raise customEX
        else:
            pyautogui.click(AfterRun_Second)

        time.sleep(buttonClickWait)

except customEX:
    pass
