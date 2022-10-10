# Controls Imports
import keyboard


# General Imports
import os
from PIL import Image, ImageOps
from time import sleep
import datetime
import cv2
from matplotlib import cm
import numpy as np
import random
import pytesseract
import pyautogui

# Own Imports
import AmontUsTasker_UtilFunc as AU_Util

pyautogui.PAUSE = 0.02




def DoTask(Taskname):
    TaskKnown = False
    Mos_x, Mos_y = pyautogui.position()

    if Taskname == 'Polus Door':
        UnlockDoorPolus()
        pass
    elif Taskname == 'Airship Door':
        UnlockDoorAirship()
    elif Taskname == 'Boarding Pass':
        DoBoardingPassTask()
    elif Taskname == 'Swipe Card':
        DoSwipeCardTask()
    elif Taskname == 'Download/Upload':
        DoDownloadUpload()
    elif Taskname == 'Wires':
        WiresTask()
    elif Taskname == 'Astroids':
        pass
    elif Taskname == 'Trash':
        DoTrashTask()
    elif Taskname == 'Water Jug':
        pass
    elif Taskname == 'Water Wheel':
        pass
    elif Taskname == 'Fill Canister':
        FillCanister()
    elif Taskname == 'Monitor Tree':
        MonitorTree()
    elif Taskname == 'Reboot Wifi':
        pass
    elif Taskname == 'Sabotage - Lights':
        TurnOnLights()
    elif Taskname == 'Chart Course':
        DoChartCourseTask()
    elif Taskname == 'Keys':
        DoKeysTask()
    elif Taskname == 'Drill':
        DoPolusDrillTask()
        pass
    elif Taskname == 'Record Temperature ':
        ChangeTempTask()
    elif Taskname == 'Telescope ':
        pass
    elif Taskname == 'Inspect Samples':
        pass
    elif Taskname == 'Store Artifacts':
        StoreArtifacts()
    elif Taskname == 'Store Manifolds':
        UnlockManifolds()
        pass
    elif Taskname == 'Start reactor':
        StartReactor_Simon()
    elif Taskname == 'Node Maze':
        DoNodeTask()
    elif Taskname == 'Node Finish':
        CompleteNodeTask()
    elif Taskname == 'Refuel Station':
        pass
    elif Taskname == 'Fuel Engine':
        pass
    elif Taskname == 'Clean Filter':
        pass
    elif Taskname == 'Clean vent':
        pass
    elif Taskname == 'Stabilize Steering Aim':
        pass
    elif Taskname == 'Calibrate Distributor':
        pass
    elif Taskname == 'Align Engine':
        pass
    elif Taskname == 'Divert Power End':
        pass
    elif Taskname == 'Run Diagnostics':
        pass
    elif Taskname == 'Assemble Crystal':
        pass
    elif Taskname == 'Sort Samples':
        pass
    elif Taskname == 'Process Data':
        pass
    elif Taskname == 'Enter ID Code':
        pass
    elif Taskname == 'Water Plants Start':
        pass
    elif Taskname == 'Masure Weather':
        pass
    elif Taskname == 'Buy Bevrege':
        pass
    elif Taskname == 'Sabotage - Comms':
        pass
    elif Taskname == 'Sabotage - Comms - Mira':
        pass
    elif Taskname == 'Sabotage - Oxygen - Mira':
        pass
    elif Taskname == 'Divert Power Start':
        pass
    elif Taskname == 'Divert Power Alt Start':
        pass
    elif Taskname == 'Prime Shields':
        pass
    elif Taskname == 'Prime Shields Alt':
        pass


    if TaskKnown == True:
        AU_Util.ProcessEndTask()
    pyautogui.moveTo(Mos_x, Mos_y)
    sleep(2)









def UnlockDoorPolus():
    # AU_Util.printupdate('Unlocking Polus Door')
    PanelInit_X = 1750
    PanelInit_Y = 500
    ScreenshotImage = pyautogui.screenshot(region=(PanelInit_X, PanelInit_Y, 300, 1000))


    X_Marker = 0
    for x in range(2):
        Y_Marker = 0
        for x in range(4):

            # print current Markers
            #print(f'On X_Marker({X_Marker}), amd Y_Marker({Y_Marker}), ', end='')

            # Get RGB Values
            r, g, b = ScreenshotImage.getpixel((X_Marker, Y_Marker))
            #print(f'(r={r}, g={g}, b={b})')

            # Move Mouse To All VALID Points
            if r in [187, 160, 104]:
                # print('Valid!')
                if X_Marker == 0:
                    pyautogui.moveTo(PanelInit_X + X_Marker, PanelInit_Y + Y_Marker, duration=0.0,
                                     tween=pyautogui.easeOutQuad)
                    pyautogui.click()
                else:
                    pyautogui.moveTo(PanelInit_X + X_Marker + 370, PanelInit_Y + Y_Marker, duration=0.0,
                                     tween=pyautogui.easeOutQuad)
                    pyautogui.click()
            # else:
            #     print('failed to find door switch')

            # sleep
            # sleep(0.2)

            Y_Marker = Y_Marker + 333
        X_Marker = X_Marker + 295

def UnlockDoorAirship():
    # Click to pull card from belt
    pyautogui.click(2000, 1600)
    sleep(0.3)

    #Drag card across
    pyautogui.moveTo(1400, 350, duration=0.0, tween=pyautogui.easeOutQuad)
    pyautogui.mouseDown()
    pyautogui.moveTo(1400, 1700, duration=1.3, tween=pyautogui.easeOutQuad)
    pyautogui.mouseUp()

def TurnOnLights():

    AU_Util.printupdate('Turning on lights')
    PanelInit_X = 1250
    PanelInit_Y = 1800
    LightsPanel = pyautogui.screenshot(region=(PanelInit_X, PanelInit_Y, 1350, 1))

    X_Marker = 0
    for x in range(5):
        r, g, b = LightsPanel.getpixel((X_Marker, 0))
        # print(f'(r={r}, g={g}, b={b})')

        if g != 255:
            pyautogui.moveTo(PanelInit_X + X_Marker, 1600, duration=0.0, tween=pyautogui.easeOutQuad)
            pyautogui.click()
        X_Marker = X_Marker + 333



def UnlockManifolds():
    AU_Util.printupdate('Unlocking Manifolds')
    ManifoldsOrder = []

    def DetectM(IMG):
        return AU_Util.CompareImageToManifoldDatabase(IMG)

    #Screenshot every manifold and process it
    ManifoldOrder = []
    for row in range(2):
        for col in range(5):
            #Screensot each number
            ManifoldNumberImage = pyautogui.screenshot(region=(1210 + (306*col), 820 + (306*row), 200, 200))

            # Process the image
            Proc_PIL_ManifoldNumberImage = Image.fromarray(AU_Util.ProcessImageForDetection(ManifoldNumberImage))

            # Detect the number
            AssumedValue = int(DetectM(Proc_PIL_ManifoldNumberImage))

            # Add Nyumber and its cords to The ManifoldOrder.
            ManifoldOrder.append([AssumedValue, [1210 + (306*col), 820 + (306*row)]])
    # print(ManifoldOrder)


    # click manifolds by order
    for i in range(10):
        # print(f'Trying to get to manifold {i+1}')
        for Manifold in ManifoldOrder:
            if i+1 == Manifold[0]:
                Cords = Manifold[1]

                pyautogui.moveTo(Cords[0], Cords[1], duration=0, tween=pyautogui.easeOutQuad)
                pyautogui.click()


def StoreArtifacts():
    # Move Skull
    pyautogui.moveTo(1000, 750)
    pyautogui.dragTo(1700, 600, button='left', duration=0.4)

    # Move Crystal
    pyautogui.moveTo(1000, 750)
    pyautogui.dragTo(2250, 800, button='left', duration=0.4)

    # Move Diamond
    pyautogui.moveTo(1000, 1400)
    pyautogui.dragTo(2200, 1500, button='left', duration=0.4)

    # Move Leaf
    pyautogui.moveTo(1000, 1400)
    pyautogui.dragTo(1750, 1100, button='left', duration=0.4)


def WiresTask():
    #print('Doing Wires')


    ## get color values of all the wires

    #Left Wires
    LWC = [[1120, 550], [1120, 920], [1120, 1280], [1120, 1660]]
    LeftWireColors = [AU_Util.getRGBofCords(LWC[0][0], LWC[0][1]), AU_Util.getRGBofCords(LWC[1][0], LWC[1][1]), AU_Util.getRGBofCords(LWC[2][0], LWC[2][1]), AU_Util.getRGBofCords(LWC[3][0], LWC[3][1])]

    #Right Wires
    RWC = [[2680, 550], [2680, 920], [2680, 1280], [2680, 1660]]
    RightWireColors = [AU_Util.getRGBofCords(RWC[0][0],RWC[0][1]), AU_Util.getRGBofCords(RWC[1][0],RWC[1][1]), AU_Util.getRGBofCords(RWC[2][0],RWC[2][1]), AU_Util.getRGBofCords(RWC[3][0], RWC[3][1])]



    for L_WNum in range(4):
        for R_WNum in range(4):

            # print(f'Checking {L_W} VS {R_W}')
            if LeftWireColors[L_WNum] == RightWireColors[R_WNum]:
                pyautogui.moveTo(LWC[L_WNum][0], LWC[L_WNum][1])
                pyautogui.dragTo(RWC[R_WNum][0], RWC[R_WNum][1], button='left', duration=0.5)
                #print('Wire Color Matched.')


def DoPolusDrillTask():
    # print('NYI Drill Task')

    DrillPoints = [[1600, 450], [2250, 450], [1650, 1600], [2250, 1600]]


    for point in DrillPoints:
        pyautogui.moveTo(point[0], point[1], duration=random.randint(1, 3) / 10, tween=pyautogui.easeOutQuad)
        for x in range(5):
            # print(point)
            pyautogui.click()


def ChangeTempTask():
    # Get the task location
    r, g, b = AU_Util.getRGBofCords(2000, 1400)
    if b == 96:
        TempTaskLocation = 'Lab'
    elif r == 96:
        TempTaskLocation = 'Lava'


    # print(f'Changing temp at {TempTaskLocation}...')
    # Detect the numbers on each side
    def DetectP(IMG):
        return AU_Util.CompareImageToPixalatedDatabase(IMG)
    def DetectS(IMG):
        return AU_Util.CompareImageToSmoothDatabase(IMG)

    # Change what part of the screen is being captured based on the location of the temp checker.
    if TempTaskLocation == 'Lab':
        CurrentTempImage = pyautogui.screenshot(region=(1150, 895, 240, 160)) # Take Screenshot
    elif TempTaskLocation == 'Lava':
        CurrentTempImage = pyautogui.screenshot(region=(1090, 895, 360, 160)) # Take Screenshot
    Proc_PIL_CurrentTempImage = Image.fromarray(AU_Util.ProcessImageForDetection(CurrentTempImage))

    CurrentTemp = 0 # Default it incase of fail
    # Detect Lab current temp
    if TempTaskLocation == 'Lab':
        # Split images into Nums
        Num1 = Proc_PIL_CurrentTempImage.crop((60, 0, 180, 160))
        Num1_D = DetectP(Num1)
        if Num1_D != None:
            CurrentTemp = int(Num1_D)
        else:

            # Cut image up into Nums
            Num1 = Proc_PIL_CurrentTempImage.crop((0, 0, 120, 160))
            Num2 = Proc_PIL_CurrentTempImage.crop((120, 0, 240, 160))
            try:
                CurrentTemp = int(f'{DetectP(Num1)}{DetectP(Num2)}') # Detect Nums and combine result
            except ValueError as E:
                AU_Util.printupdate(f'Image Compare failed - likely due to panel closing.(Lab Current)')





    # Detect Lava Current Temp
    elif TempTaskLocation == 'Lava':

        # Cut image up into Nums
        Num1 = Proc_PIL_CurrentTempImage.crop((0, 0, 120, 160))
        Num2 = Proc_PIL_CurrentTempImage.crop((120, 0, 240, 160))
        Num3 = Proc_PIL_CurrentTempImage.crop((240, 0, 360, 160))
        try:
            CurrentTemp = int(f'{DetectP(Num1)}{DetectP(Num2)}{DetectP(Num3)}') # Detect Nums and combine result
        except ValueError as E:
            AU_Util.printupdate(f'Image Compare failed - likely due to panel closing.(Lava Current)')

    # Print Current temp
    #print(f'CurrentTemp is of type({type(CurrentTemp)}) and Value ({CurrentTemp})')







    ####################################################################################################################################################

    ReadingTemp = 0  # Default it incase of fail
    # Detect Lab Reading Temp
    if TempTaskLocation == 'Lab':
        ReadingTempImage = pyautogui.screenshot(region=(2100, 890, 240, 180)) # Take Screenshot
        Proc_PIL_ReadingTempImage = Image.fromarray(AU_Util.ProcessImageForDetection(ReadingTempImage)) # Process the image

        # Cut image up into Nums
        Num1 = Proc_PIL_ReadingTempImage.crop((0, 0, 120, 180))
        Num2 = Proc_PIL_ReadingTempImage.crop((120, 0, 240, 180))

        try:
            ReadingTemp = int(f'{DetectS(Num1)}{DetectS(Num2)}') # Detect Nums and combine result
        except ValueError as E:
            AU_Util.printupdate(f'Image Compare failed - likely due to panel closing.(Lab Smooth)')




    # Detect Lava Current Temp
    elif TempTaskLocation == 'Lava':
        ReadingTempImage = pyautogui.screenshot(region=(1980, 890, 360, 180)) # Take Screenshot
        Proc_PIL_ReadingTempImage = Image.fromarray(AU_Util.ProcessImageForDetection(ReadingTempImage))  # Process the image
        # Proc_PIL_ReadingTempImage.show()

        # Cut image up into Nums
        Num1 = Proc_PIL_ReadingTempImage.crop((10, 0, 130, 180))
        Num2 = Proc_PIL_ReadingTempImage.crop((120, 0, 240, 180))
        Num3 = Proc_PIL_ReadingTempImage.crop((240, 0, 360, 180))

        try:
            ReadingTemp = int(f'{DetectS(Num1)}{DetectS(Num2)}{DetectS(Num3)}') # Detect Nums and combine result
        except ValueError as E:
            AU_Util.printupdate(f'Image Compare failed - likely due to panel closing.(Lava Smooth)')

    # Print Reading temp
    #print(f'ReadingTemp is of type({type(ReadingTemp)}) and Value ({ReadingTemp})')





    ####################################################################################################################################################

    # Move mouse to arrow location
    MouseY = 600
    if TempTaskLocation == 'Lab':
        MouseY = 1200
    pyautogui.moveTo(1200, MouseY, duration=random.randint(1, 3) / 10, tween=pyautogui.easeOutQuad)

    # Click the correct amount of times depending Lav\Lava Temp
    ClickTimes = 0
    if TempTaskLocation == 'Lab':
        ClickTimes = (ReadingTemp + CurrentTemp) * 2
    elif TempTaskLocation == 'Lava':
        ClickTimes = (ReadingTemp - CurrentTemp) * 2

    for click in range(ClickTimes):
        pyautogui.click()


def DoNodeTask():
    # print('Doing Node!')

    ### ----------------------------------------------------------------------------- ###
    ### Convert panel into usable python grid.
    PIL_NodeMazeImage = pyautogui.screenshot(region=(840, 590, 2160, 815))  # Take Screenshot
    # PIL_NodeMazeImage = Image.open('./images/NodeMaze.png')


    ### ----------------------------------------------------------------------------- ###
    ### Generate Maze Image
    InitialPoint = [55, 55]

    MazeMap = np.zeros((7, 19, 3), dtype=np.uint8)

    MMC_Y = 0
    MMC_X = 0

    for Y in range(7):
        MMC_X = 0
        for X in range(19):
            CropWidth, CropHeight = InitialPoint[0] + round(X * 111.5), InitialPoint[1] + round(Y * 110)
            Square = PIL_NodeMazeImage.crop((CropWidth, CropHeight, CropWidth + 1, CropHeight + 1))
            r, g, b = Square.getpixel((0, 0))
            if b == 99 or b == 66 or b == 168:
                MazeMap[MMC_Y][MMC_X] = [255,255,255]


            MMC_X = MMC_X + 1
        MMC_Y = MMC_Y + 1

    # print(MazeMap)


    # Create an RGBA PIL image and place it on the border Backround template
    background = Image.open("./images/Node/NodeMazeTemplate.png")
    foreground = ImageOps.invert(Image.fromarray(MazeMap)).convert("RGBA")
    # foreground.save('./images/Node/LatestNodeMaze.png')
    background.paste(foreground, (1, 1), foreground)

    background.save('./images/Node/LatestNodeMaze_WithEdge.png')


    ### ----------------------------------------------------------------------------- ###
    ### Solve the maze

    os.system('mazesolver -i ./images/Node/LatestNodeMaze_WithEdge.png')
    PILK_SolvedMaze = Image.open('./images/Node/LatestNodeMaze_WithEdge_Solution.png')
    # PILK_SolvedMaze.save('./images/Temp.png')

    ### ----------------------------------------------------------------------------- ###
    ### Convert Solution into Text-Form Solution

    def ConvertImageIntoNMap(MazeImage):
        Map = ''
        Width, Height = MazeImage.size
        for Y in range(Height):
            for X in range(Width):
                P_Color = MazeImage.getpixel((X, Y))
                if P_Color[1] == 0:
                    Map = Map + '#'
                elif P_Color[1] == 255 and  P_Color[2] == 0:
                    Map = Map + 'X'
                elif P_Color[1] == 255 and  P_Color[2] == 255:
                    Map = Map + ' '
            Map = Map + '\n'
        return Map



    TM = ConvertImageIntoNMap(PILK_SolvedMaze)


    ### Convert Text-Form Solution into Instructions Set


    def GetInstructionsFromMaze(TextMap):
        InstructionsList = []
        #Turn TextMap into Array of Char Arrays.
        ArrayMap = []
        for Line in TextMap.split('\n'):
            Chars = []
            for Char in Line:
                Chars.append(Char)
            ArrayMap.append(Chars)
        # for LINE in ArrayMap:
        #     print(LINE)

        def TakeStepFromPos(X, Y):
            # turn corrent location into visited step '$'
            ArrayMap[Y][X] = '$'

            PossiblePaths = [[X, Y-1, 'U'], [X, Y+1, 'D'], [X-1, Y, 'L'], [X+1, Y, 'R']]
            # print(f'PossiblePaths = {PossiblePaths}')
            for path in PossiblePaths:
                try:

                    if ArrayMap[path[1]][path[0]] == 'X':
                        InstructionsList.append(path[2])
                        TakeStepFromPos(path[0], path[1])
                        # print('Path Found!')
                    # else:
                    #     print(f'ArrayMap[{path[1]}][{path[0]}] = {ArrayMap[path[0]][path[1]]}')
                except IndexError as E:
                    pass

        TakeStepFromPos(2, 0)

        # for LINE in ArrayMap:
        #     print(LINE)

        # Remove outer border instructions that was added for maze solving
        CorrectedInstructions = ''.join(InstructionsList)[:-1][1:]
        return CorrectedInstructions










    Instructions = GetInstructionsFromMaze(TM)

    AU_Util.printupdate(f'   Doing Node based on InstructionSet {Instructions}')
    ### ----------------------------------------------------------------------------- ###
    ### Move mouse based on maze Instructions!

    MC = [1020, 650]
    pyautogui.moveTo(MC[0], MC[1], duration=0.3, tween=pyautogui.easeOutQuad)

    pyautogui.mouseDown()

    for L in Instructions:
        if L == 'U':
            MC[1] = MC[1] - 110
        elif L == 'D':
            MC[1] = MC[1] + 110
        elif L == 'L':
            MC[0] = MC[0] - 111
        elif L == 'R':
            MC[0] = MC[0] + 111

        pyautogui.moveTo(MC[0], MC[1], duration=0.01, tween=pyautogui.easeOutQuad)
    pyautogui.mouseUp()


def CompleteNodeTask():
    S_X = 1100
    S_Y = 250
    ButtonsImage = pyautogui.screenshot(region=(S_X, S_Y, 200, 1700))
    for Y in range(6):
        r, g, b = ButtonsImage.getpixel((0, Y * 320))
        if r == 121 and g == 143 and b == 148:
            pyautogui.click(S_X, S_Y + (Y * 320))


def DoChartCourseTask():
    # print('Doing Chart Course...')

    # Screenshot the course
    # foreground = Image.open("./images/Marker_Small_Red.png")
    CorsePanelCords = [1100, 625]
    CurrentChartCourseImage = pyautogui.screenshot(region=(CorsePanelCords[0], CorsePanelCords[1], 1650, 900))


    # Find the corect Travel Paths
    ValidTravels = []
    for X in range(5):
        CurrentX = X * 400

        Found_Y = None
        Y = 0
        while Y != 899 and Found_Y == None:
            Y += 1
            r, g, b = CurrentChartCourseImage.getpixel((CurrentX, Y))

            if r == 55 and g == 153 and b == 220:
                pass
            elif (35 <= r <= 45 and 110 <= g <= 125 and 160 <= b <= 180):
                Found_Y = Y
            # else:
            #     print(r, g, b)
        #print(f'-----{X}--------- Found_Y: {Found_Y}')

        ValidTravels.append([CorsePanelCords[0] + CurrentX + 60, CorsePanelCords[1] + Found_Y + 60])
        # CurrentChartCourseImage.paste(foreground, (CurrentX, Found_Y), foreground)
    # CurrentChartCourseImage.save('./images/Temp.png')

    # Travel based on the path!
    # for MovePoint in ValidTravels:
    #     print(MovePoint)

    # Initial Point
    pyautogui.moveTo(ValidTravels[0][0] , ValidTravels[0][1], duration=0.0, tween=pyautogui.easeOutQuad)
    pyautogui.mouseDown()

    # Path
    sleep(0.1)
    pyautogui.moveTo(ValidTravels[1][0], ValidTravels[1][1], duration=0.1, tween=pyautogui.easeOutQuad)
    sleep(0.1)
    pyautogui.moveTo(ValidTravels[2][0], ValidTravels[2][1], duration=0.1, tween=pyautogui.easeOutQuad)
    sleep(0.1)
    pyautogui.moveTo(ValidTravels[3][0], ValidTravels[3][1], duration=0.1, tween=pyautogui.easeOutQuad)
    sleep(0.1)
    pyautogui.moveTo(ValidTravels[4][0] + 30, ValidTravels[4][1], duration=0.1, tween=pyautogui.easeOutQuad)
    pyautogui.mouseUp()

def DoKeysTask():
    # print('Doing Keys...')

    # Grab the kdy from the left
    pyautogui.moveTo(900, 1500, duration=0.0, tween=pyautogui.easeOutQuad)
    pyautogui.mouseDown()

    # Find the correct key slot
    CorrectKeyCords = [0, 0]
    Screenshot_Initial_X = 1630
    Screenshot_Initial_Y = 80
    KeysImage = pyautogui.screenshot(region=(Screenshot_Initial_X, Screenshot_Initial_Y, 1570, 2000))
    Current_X = 212
    for x in range(3):
        Current_Y = 120
        for x in range(5):
            r, g, b = KeysImage.getpixel((Current_X, Current_Y))
            # print(f'at x_{Current_X}  y_{Current_Y} the color values are:', r, g, b )
            if r != 195:
                CorrectKeyCords = [Screenshot_Initial_X + Current_X, Screenshot_Initial_Y + Current_Y + 150]
                break
                break

            # KeysImage = AU_Util.DEBUG_return_IMAGE_withMarkerOn_Cords(IMG=KeysImage, x=Current_X, y=Current_Y)
            Current_Y = Current_Y + 354
        Current_X = Current_X + 576
    # KeysImage.save('./images/Temp.png')



    # Move the key to the correct Slot.
    pyautogui.moveTo(CorrectKeyCords[0], CorrectKeyCords[1], duration=0.1, tween=pyautogui.easeOutQuad)
    pyautogui.mouseUp()
    sleep(0.1)

    # #Turn the key
    pyautogui.moveTo(CorrectKeyCords[0], CorrectKeyCords[1] - 150, duration=0.0, tween=pyautogui.easeOutQuad)
    pyautogui.mouseDown()
    pyautogui.moveTo(CorrectKeyCords[0] - 180, CorrectKeyCords[1] + 30, duration=0.2, tween=pyautogui.easeOutQuad)
    pyautogui.mouseUp()


def DoSwipeCardTask():
    # Click to pull card from belt
    pyautogui.click(1500, 1600)
    sleep(0.5)

    #Drag card across
    pyautogui.moveTo(1000, 850, duration=0.0, tween=pyautogui.easeOutQuad)
    pyautogui.mouseDown()
    pyautogui.moveTo(2800, 850, duration=1.1, tween=pyautogui.easeOutQuad)
    pyautogui.mouseUp()


def DoBoardingPassTask():
    # Click rectangle
    pyautogui.click(1200, 1000)
    sleep(0.3)

    # Click Arrow
    pyautogui.click(1000, 400)

    # Drag the boarding pass to the scanner
    sleep(0.3)
    pyautogui.moveTo(1200, 1000, duration=0.0, tween=pyautogui.easeOutQuad)
    pyautogui.mouseDown()
    pyautogui.moveTo(2500, 1000, duration=0.1, tween=pyautogui.easeOutQuad)
    pyautogui.mouseUp()
    sleep(1)





def DoDownloadUpload():
    pyautogui.click(1900, 1300)
    sleep(8)


def DoTrashTask():
    pyautogui.moveTo(2550, 840)
    pyautogui.mouseDown()
    pyautogui.moveTo(2550, 1500, duration=0.3, tween=pyautogui.easeOutQuad)
    sleep(1.5)
    pyautogui.mouseUp()


def FillCanister():
    pyautogui.moveTo(1800, 550)
    pyautogui.mouseDown()
    pyautogui.moveTo(2250, 1450, duration=0.3, tween=pyautogui.easeOutQuad)
    pyautogui.mouseUp()
    sleep(2.8)
    pyautogui.click()

def MonitorTree():
    ImageX = 1000
    ImageY = 450
    MonitorImage = pyautogui.screenshot(region=(ImageX, ImageY, 1800, 1000))
    MarkerPoints = []
    DraggerPoints = []

    # TESTIMAGE = MonitorImage

    Curent_X = 30
    for x in range(4):
        for Curent_Y in range(1000):
            r, g, b = MonitorImage.getpixel((Curent_X, Curent_Y))
            if r == 49:
                # TESTIMAGE = AU_Util.DEBUG_return_IMAGE_withMarkerOn_Cords(IMG = MonitorImage, x=Curent_X + 150, y= Curent_Y + 65)
                DraggerPoints.append([Curent_X + 150 + ImageX, Curent_Y + 65 + ImageY])
                break
        for Curent_Y in range(1000):
            r, g, b = MonitorImage.getpixel((Curent_X, Curent_Y))
            if r == 209:
                # TESTIMAGE = AU_Util.DEBUG_return_IMAGE_withMarkerOn_Cords(IMG = MonitorImage, x=Curent_X + 150, y= Curent_Y + 20, AltColor=True)
                MarkerPoints.append([Curent_X + 150 + ImageX, Curent_Y + 20 + ImageY])
                break
        Curent_X = Curent_X + 482
    # TESTIMAGE.save('./images/Temp.png')
    # print(MarkerPoints)
    # print(DraggerPoints)


    if len(MarkerPoints) == 4:
        for N in range(4): # for each N (Nutrient)
            D_X, D_Y = DraggerPoints[N]
            M_X, M_Y = MarkerPoints[N]
            pyautogui.moveTo(D_X, D_Y, duration=0.0, tween=pyautogui.easeOutQuad)
            pyautogui.mouseDown()
            pyautogui.moveTo(M_X, M_Y, duration=0.1, tween=pyautogui.easeOutQuad)
            pyautogui.mouseUp()
    else:
        pyautogui.moveTo(3700, 1000, duration=0.0, tween=pyautogui.easeOutQuad)
        pyautogui.click()
        sleep(0.2)
        pyautogui.moveTo(3700, 1900, duration=0.0, tween=pyautogui.easeOutQuad)
        pyautogui.click()











from datetime import datetime
def StartReactor_Simon():
    buttonlocations = [[2250, 950], [2500, 950], [2750, 950], [2250, 1200], [2500, 1200], [2750, 1200], [2250, 1400], [2500, 1400], [2750, 1400]]


    # A Function that will keep screenshotting the reactor simon part untill it detects a signal, then return the location of that signal in digit 0-9 form.
    def ReadScreenUntillBlueFound():
        while True:
            Screenshot = pyautogui.screenshot(region=(960, 850, 700, 700))
            Location = 0
            for y_N in range(3):
                for x_N in range(3):
                    x = 250 * (x_N + 1) - 150
                    y = 250 * (y_N + 1) - 150
                    r, g, b = Screenshot.getpixel((x, y))
                    if r == 68:
                        return Location
                    Location += 1


    for Stage in range(5):
        Stage +=1
        locations = []

        print('         Detecting...')
        # for each stage, collect all simon signals.
        for S in range(Stage):
            locations.append(ReadScreenUntillBlueFound())

            print(f'            Detected {locations}')
            sleep(0.25)
        # print(f'      At Stage #{Stage}, the locations are {locations}')

        sleep(0.5)

        print('         Clicking...')
        # click all signals in locations list.
        for loc in locations:
            x, y = buttonlocations[loc]
            pyautogui.moveTo(x, y, duration=0.3, tween=pyautogui.easeOutQuad)
            pyautogui.click()





