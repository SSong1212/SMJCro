import pyautogui
import time
import os

ButtonImageSetPath = "ButtonImageSet/"
buttonClickWait = 3

def getImageCenter(imageFileName):
    imageCenter = pyautogui.locateCenterOnScreen(ButtonImageSetPath + imageFileName, confidence=0.9)
    return imageCenter

def getCoordinate():
    appName = getImageCenter('appName.png')
    lobbyStart = getImageCenter('lobbyStart.png')
    chooseGame = getImageCenter('chooseGame.png')
    moveMap = getImageCenter('moveMap.png')
    chooseMap = getImageCenter('chooseMap.png')
    confirmChooseMap = getImageCenter('confirmChooseMap.png')
    startButton = getImageCenter('StartButton.png')
    confirmStart = getImageCenter('confirmStart.png')
    secondRun = getImageCenter('secondRun.png')
    AfterRun_first = getImageCenter('AfterRun_first.png')
    AfterRun_Second = getImageCenter('AfterRun_Second.png')
    appBrake = getImageCenter('appBrake.png')
    AbnormalConfirm = getImageCenter('AbnormalConfirm.png')
    return appName, lobbyStart, chooseGame, moveMap, chooseMap, confirmChooseMap, startButton, confirmStart, secondRun, AfterRun_first, AfterRun_Second, appBrake, AbnormalConfirm

def deleteCoordinate():
    appName = None
    lobbyStart = None
    chooseGame = None
    moveMap = None
    chooseMap = None
    confirmChooseMap = None
    startButton = None
    confirmStart = None
    secondRun = None
    AfterRun_first = None
    AfterRun_Second = None
    appBrake = None
    AbnormalConfirm = None
    return appName, lobbyStart, chooseGame, moveMap, chooseMap, confirmChooseMap, startButton, confirmStart, secondRun, AfterRun_first, AfterRun_Second, appBrake, AbnormalConfirm

def checkIsDifferentAppRunning():
    isAppRunning = getImageCenter('isAppRunning.png')
    if isAppRunning == None:
        print("다른 앱 실행 감지")
        exitButton = pyautogui.locateOnScreen(ButtonImageSetPath + 'exitButton.png', confidence=0.9)
        if exitButton != None:
            while pyautogui.locateOnScreen(ButtonImageSetPath + 'LDTitle.png', confidence=0.9) == None:
                print("실행중인 모든 앱 종료")
                pyautogui.click(exitButton)
    else:
        print("앱 정상 동작중")

appName, lobbyStart, chooseGame, moveMap, chooseMap, confirmChooseMap, startButton, confirmStart, secondRun, AfterRun_first, AfterRun_Second, appBrake, AbnormalConfirm = deleteCoordinate()

count = 1

preImage = None

currentImage = None

checkAppError = 0

print("SONGCro 실행중")

while True:
    appName, lobbyStart, chooseGame, moveMap, chooseMap, confirmChooseMap, startButton, confirmStart, secondRun, AfterRun_first, AfterRun_Second, appBrake, AbnormalConfirm = getCoordinate()

    if appName != None:
        pyautogui.click(appName)
        print("쿠키런 앱 실행")
        appName == None
    
    if lobbyStart != None:
        if AbnormalConfirm == None:
            pyautogui.click(lobbyStart)
            print("로비에서 시작 클릭")
            lobbyStart == None
        else:
            pyautogui.click(AbnormalConfirm)
            print("비정상 종료 점수 확인")
            AbnormalConfirm == None
    
    if chooseGame != None:
        time.sleep(1)
        pyautogui.click(chooseGame)
        print("경기장 입장")
        chooseGame == None
   
    if moveMap != None:
        if startButton == None:
            pyautogui.click(moveMap)
            print("랜드 이동하기 클릭")
            moveMap == None
    
    if chooseMap != None:
        if confirmChooseMap != None:
            pyautogui.click(chooseMap)
            print("랜드1 선택")
            time.sleep(2)
            chooseMap == None
            pyautogui.click(confirmChooseMap)    
            print("랜드1 입장")
            time.sleep(2)
            confirmChooseMap == None
        
    if startButton != None:
        pyautogui.click(startButton)
        print("달리기 시작 버튼 클릭")
        startButton == None
    
    if confirmStart != None:
        pyautogui.click(confirmStart)
        print("달리기 시작 버튼 확인")
        confirmStart == None
    
    if secondRun != None:
        pyautogui.click(secondRun)
        print("이어달리기 시작")
        secondRun == None
    
    if AfterRun_first != None:
        pyautogui.click(AfterRun_first)
        print("점수 확인")
        AfterRun_first == None
    
    if AfterRun_Second != None:
        pyautogui.click(AfterRun_Second)
        print("주머니 확인")
        AfterRun_Second == None

    if appBrake != None:
        pyautogui.click(appBrake)
        print("앱 중단됨 발생")
        appBrake == None

    if count - checkAppError == 3:
        if preImage != None:
            currentImage = pyautogui.locateOnScreen(preImage)
            if currentImage != None:
                print("인앱 오류 발생(정지상태, 블랙 현상 등)으로 재시작")
                exitButton = pyautogui.locateOnScreen(ButtonImageSetPath + 'exitButton.png', confidence=0.9)
                if exitButton != None:
                    while pyautogui.locateOnScreen(ButtonImageSetPath + 'LDTitle.png', confidence=0.9) == None:
                        print("실행중인 모든 앱 종료")
                        pyautogui.click(exitButton)
                        checkAppError = 0
                        count = 1
                else:
                    print("종료 버튼을 찾을 수 없음")
            else:
                print("인앱 오류 발생 안함")
        else:
            print("인앱 오류 체크용 이미지가 없음")
            
    if count % 29 == 0:
        preImage = pyautogui.screenshot()
        checkAppError = count
        print("인앱 오류 체크용 이전 이미지 저장")      

    if count > 5:
        if count % 10 == 0:
            checkIsDifferentAppRunning()

    count = count + 1  

    print(count)

    appName, lobbyStart, chooseGame, moveMap, chooseMap, confirmChooseMap, startButton, confirmStart, secondRun, AfterRun_first, AfterRun_Second, appBrake, AbnormalConfirm = deleteCoordinate()

    time.sleep(1)
    

os.system("pause")