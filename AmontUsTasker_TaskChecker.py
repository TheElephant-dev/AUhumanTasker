# Controls Imports
import keyboard
import pyautogui

# General Imports
from PIL import Image
from time import sleep
import datetime


# Own Imports
import AmontUsTasker_TaskDoer as AU_Tasker
import AmontUsTasker_UtilFunc as AU_Util


# ['Taskname', [pixallocations], [pixalvalues], colortocheckon]
Tasks = [
    ['Boarding Pass', [1078, 1088, 1225], [115, 82, 57], 0],
    ['Swipe Card', [335, 347, 367], [43, 55, 55], 0],
    ['Download/Upload', [67, 76, 99], [17, 107, 165], 0],
    ['Wires', [1100, 1196, 1416], [12, 19, 123], 0],
    ['Astroids', [1125, 1138, 1311], [22, 22, 22], 0],
    ['Trash', [335, 1680, 1766], [86, 93, 24], 0],
    ['Water Jug', [183, 255, 1130], [24, 49, 51], 0],
    ['Water Wheel', [1093, 1105, 1135], [46, 107, 163], 0],
    ['Monitor Tree', [86, 129, 255], [63, 43, 129], 0],
    ['Reboot Wifi', [94, 128, 426], [60, 41, 24], 0],
    ['Sabotage - Lights', [335, 357, 402], [90, 99, 159], 0],
    ['Chart Course', [113, 126, 156], [107, 132, 176], 0],
    ['Keys', [33, 67, 289], [159, 90, 156], 0],
    ['Drill', [633, 739, 808], [0, 55, 231], 0],
    ['Record Temperature ', [72, 84, 100], [33, 99, 123], 0],
    ['Telescope ', [647, 960, 1479], [198, 198, 198], 0],
    ['Inspect Samples', [344, 378, 505], [121, 173, 165], 0],
    ['Store Artifacts', [619, 640, 657], [44, 181, 41], 0],
    ['Store Manifolds', [344, 360, 372], [66, 99, 148], 0],
    ['Start reactor', [41, 69, 137], [90, 66, 99], 0],
    ['Node Maze', [8, 29, 62], [57, 22, 66], 0],
    ['Node Finish', [45, 98, 265], [41, 211, 211], 0],
    ['Refuel Station', [627, 743, 829], [41, 74, 231], 0],
    ['Fuel Engine', [626, 720, 1040], [41, 74, 231], 0],
    ['Clean Filter', [347, 390, 531], [145, 123, 40], 0],
    ['Clean vent', [87, 208, 312], [34, 148, 85], 0],
    ['Stabilize Steering Aim', [334, 336, 347], [99, 101, 131], 0],
    ['Calibrate Distributor', [347, 369, 392], [66, 88, 99], 0],
    ['Align Engine', [342, 359, 382], [90, 99, 153], 0],
    ['Divert Power End', [108, 149, 197], [65, 60, 72], 0],
    ['Run Diagnostics', [174, 248, 277], [198, 156, 231], 0],
    ['Assemble Crystal', [300, 400, 500], [65, 68, 71], 0],
    ['Sort Samples', [16, 38, 61], [239, 90, 142], 0],
    ['Process Data', [12, 25, 56], [104, 125, 86], 0],
    ['Enter ID Code', [163, 265, 288], [218, 137, 161], 0],
    ['Water Plants Start', [1113, 1210, 1454], [99, 74, 74], 0],
    ['Masure Weather', [52, 56, 105], [0, 90, 112], 0],
    ['Buy Bevrege', [329, 356, 383], [158, 187, 31], 0],
    ['Sabotage - Comms', [477, 559, 567], [90, 132, 33], 0],
    ['Sabotage - Comms - Mira', [104, 124, 154], [90, 99, 159], 0],
    ['Sabotage - Oxygen - Mira', [572, 586, 609], [90, 99, 159], 0],
    ['Divert Power Start', [1950, 1978, 1989], [247, 127, 90], 0],
    ['Divert Power Alt Start', [1950, 1978, 1989], [242, 30, 100], 0],
    ['Prime Shields', [347, 392, 472], [101, 30, 104], 0],
    ['Prime Shields Alt', [347, 392, 472], [102, 82, 139], 0],
    ['Polus Door', [389, 531, 544], [132, 178, 72], 0],
    ['Airship Door', [379, 498, 576], [129, 170, 189], 0],
    ['Fill Canister', [73, 148, 215], [118, 211, 173], 0]
]

CT = [47, 81, 132]

def CheckForTask():
    ###################################################################################################################
    ### Screenshot and save the image information.
    TaskCheckerImage = pyautogui.screenshot(region=(700, 1100, 2000, 100))
    # TaskCheckerImage = Image.open('./images/TaskChecker.png')
    TCI_Values = []
    for x in range(2000):
        TCI_Values.append(TaskCheckerImage.getpixel((x, 0)))
    ###################################################################################################################









    ###################################################################################################################
    ### Detect the task
    for Task in Tasks:
    # for DEBUG_TESTING in range(1):
    #     Task = Tasks[-1]#DEBUG_TESTING

        # Get the task name
        TaskName = Task[0]

        # Get the locations of the pixals to check for this task
        Loc = Task[1]
        #print(Loc)

        # Get the Values those locations should have
        TaskExpectedValues = Task[2]
        #print(TaskExpectedValues)


        # Get the Values those locations actually have
        c = Task[3] # get the R\G\B value to compare against
        TaskActualValues = [TCI_Values[Loc[0]][c], TCI_Values[Loc[1]][c], TCI_Values[Loc[2]][c]]
        #print(TaskActualValues)

        # print(f'{TaskName},  ', end='')
        if TaskExpectedValues == TaskActualValues:
            AU_Util.printupdate(f'{TaskName} Task Panel Open!')

            # Do Task
            AU_Tasker.DoTask(TaskName)

        # else:
        #     print(f'    {TaskName} Not Found!\n     -TaskExpectedValues {TaskExpectedValues}\n     -TaskActualValues {TaskActualValues}\n')






def ShowTaskCordsLocationOnTempImage():

    TaskCheckerImage = pyautogui.screenshot(region=(700, 1100, 2000, 100))


    ###################################################################################################################
    ### # # # show the locations checked on the image
    Task = Tasks[-1]#DEBUG_TESTING

    # Get the locations of the pixals to check for this task
    Loc = Task[1]
    # print(Loc)
    IM = TaskCheckerImage

    for x in range(2000):
        if x in Loc:
            IM = AU_Util.DEBUG_return_IMAGE_withMarkerOn_Cords(IM, x=x, y=0)
            IM.save('./images/Temp.png')
    ###################################################################################################################

    for x in range(2000):
        CurrentColorValues = TaskCheckerImage.getpixel((x, 0))

        if CurrentColorValues[0] == CT[0] and CurrentColorValues[1] == CT[1] and CurrentColorValues[2] == CT[2]:
            print(f'On Pixal Num #{x}, the values are {CurrentColorValues}\n^^^ <-----------------------------------------------------')

        if CurrentColorValues[0] == CT[0]:
            # print('Color 1 Valid')
            if CurrentColorValues[1] == CT[1]:
                # print('Color 2 Valid')
                if CurrentColorValues[2] == CT[2]:
                    # print('Color 3 Valid')
                    # IM = AU_Util.DEBUG_return_IMAGE_withMarkerOn_Cords(IM, x=x, y=0, AltColor=True)
                    # IM.save('./images/Temp.png')
                    # print(CurrentColorValues[2])
                    pass

        # else:
        #     print(f'At location ({x}) the value for color R is {CurrentColorValues[0]}')











def CheckIfDoorPanel():
    # Take a screenshot of the top section of panel
    IsOnDoorPanelImage = pyautogui.screenshot(region=(1223, 140, 20, 1))

    # Validate Pixal Values in image to match door panel
    ValidArray = [132, 176, 72]
    CurrentArray = []
    for x in range(3):
        r, g, b = IsOnDoorPanelImage.getpixel((x * 9, 0))
        CurrentArray.append(r)

    if ValidArray == CurrentArray:  # Pass If door panel is open
        AU_Util.printupdate('Polus Door Panel Open!')
        AU_Tasker.UnlockDoor()
        AU_Util.ProcessEndTask()


def CheckIfLightsPanel():
    # Take a screenshot of the top section of panel
    IsOnDoorPanelImage = pyautogui.screenshot(region=(1230, 590, 20, 1))

    # Validate Pixal Values in image to match door panel
    ValidArray = [89, 145, 197]
    CurrentArray = []
    for x in range(3):
        r, g, b = IsOnDoorPanelImage.getpixel((x * 9, 0))
        CurrentArray.append(r)

    if ValidArray == CurrentArray:  # Pass If lights panel is open
        AU_Util.printupdate('Lights Panel Open!')
        AU_Tasker.TurnOnLights()
        AU_Util.ProcessEndTask()


def CheckForUnlockManifoldsTask():
    # Take a screenshot of the top section of panel
    IsOnManifoldsTaskImage = pyautogui.screenshot(region=(1033, 700, 20, 1))

    # Validate Pixal Values in image to match door panel
    ValidArray = [16, 66, 74]
    CurrentArray = []
    for x in range(3):
        r, g, b = IsOnManifoldsTaskImage.getpixel((x * 9, 0))
        CurrentArray.append(r)
    #print(f'ValidArray({ValidArray}) VS ({CurrentArray}) CurrentArray')

    if ValidArray == CurrentArray:  # Pass If lights panel is open
        AU_Util.printupdate('Reactor Task Panel Open!')
        AU_Tasker.UnlockManifolds()
        # AU_Util.ProcessEndTask()


def CheckForStoreArtifactsTask():
    # Take a screenshot of the top section of panel
    IsOnStoreArtifactsTaskImage = pyautogui.screenshot(region=(1330, 700, 20, 1))

    # Validate Pixal Values in image to match door panel
    ValidArray = [41, 181, 76]
    CurrentArray = []
    for x in range(3):
        r, g, b = IsOnStoreArtifactsTaskImage.getpixel((x * 9, 0))
        CurrentArray.append(r)
    #print(f'ValidArray({ValidArray}) VS ({CurrentArray}) CurrentArray')

    if ValidArray == CurrentArray:  # Pass If lights panel is open
        AU_Util.printupdate('Store Artifacts Task Panel Open!')
        AU_Tasker.StoreArtifacts()
        AU_Util.ProcessEndTask()


def CheckForWiresTask():
    # Take a screenshot of the top section of panel
    IsOnWiresTaskImage = pyautogui.screenshot(region=(1129, 700, 20, 1))

    ValidArray = [57, 36, 8]
    CurrentArray = []
    for x in range(3):
        r, g, b = IsOnWiresTaskImage.getpixel((x * 9, 0))
        CurrentArray.append(r)

    # print(f'ValidArray({ValidArray}) VS ({CurrentArray}) CurrentArray')


    if ValidArray == CurrentArray:  # Pass If lights panel is open
        AU_Util.printupdate('Wires Task Panel Open!')
        AU_Tasker.WiresTask()
        AU_Util.ProcessEndTask()


def CheckTempTask():
    # Take a screenshot of the top section of panel
    IsOnCheckTempTaskImage = pyautogui.screenshot(region=(1000, 1550, 20, 1))


    ValidArray = [[122, 104, 124], [122, 104, 121]]
    CurrentArray = []
    for x in range(3):
        r, g, b = IsOnCheckTempTaskImage.getpixel((x * 9, 0))
        CurrentArray.append(r)

    # print(f'ValidArray({ValidArray[0]} OR {ValidArray[1]}) VS ({CurrentArray}) CurrentArray')


    if ValidArray[0] == CurrentArray or ValidArray[1] == CurrentArray:  # Pass If lights panel is open
        DrillLocation = 'None'
        if ValidArray[0] == CurrentArray:
            DrillLocation = 'Lab'
        else:
            DrillLocation = 'Lava'
        AU_Util.printupdate(f'Temperature({DrillLocation}) Task Panel Open!')
        AU_Tasker.ChangeTempTask(DrillLocation)
        AU_Util.ProcessEndTask()


def CheckPolusDrillTask():
    # Take a screenshot of the top section of panel
    IsOnCheckPolusDrillTaskImage = pyautogui.screenshot('images/CheckPolusDrill.png', region=(1810, 1200, 20, 1))


    ValidArray = [56, 85, 56]
    CurrentArray = []
    for x in range(3):
        r, g, b = IsOnCheckPolusDrillTaskImage.getpixel((x * 9, 0))
        CurrentArray.append(r)


    # print(f'ValidArray({ValidArray}) VS ({CurrentArray}) CurrentArray')


    if ValidArray == CurrentArray:  # Pass If lights panel is open
        AU_Util.printupdate('Polus Drill Task Panel Open!')
        AU_Tasker.DoPolusDrillTask()
        AU_Util.ProcessEndTask()


def CheckNodeTask():
    # Take a screenshot of the top section of panel
    IsOnCheckForNodeTaskImage = pyautogui.screenshot(region=(1810, 1500, 20, 1))


    ValidArray = [72, 82, 73]
    CurrentArray = []
    for x in range(3):
        r, g, b = IsOnCheckForNodeTaskImage.getpixel((x * 9, 0))
        CurrentArray.append(r)

    # print(f'ValidArray({ValidArray}) VS ({CurrentArray}) CurrentArray')


    if ValidArray == CurrentArray:  # Pass If lights panel is open
        AU_Util.printupdate('Node Task Panel Open!')
        AU_Tasker.DoNodeTask()
        AU_Util.ProcessEndTask()


def CheckCompleteNodeTask():
    IsOnCheckForCompleteNodeTaskImage = pyautogui.screenshot(region=(2750, 270, 20, 20))


    ValidArray = [89, 117, 137]
    CurrentArray = []
    for x in range(3):
        r, g, b = IsOnCheckForCompleteNodeTaskImage.getpixel((x * 9, 0))
        CurrentArray.append(r)

    # print(f'ValidArray({ValidArray}) VS ({CurrentArray}) CurrentArray')


    if ValidArray == CurrentArray:  # Pass If lights panel is open
        AU_Util.printupdate('Complete Node Task Panel Open!')
        AU_Tasker.CompleteNodeTask()
        # AU_Util.ProcessEndTask()


def CheckChartCourse():
    # Take a screenshot of the top section of panel
    IsOnCheckForChartCourseTaskImage = pyautogui.screenshot(region=(900, 550, 20, 1))


    ValidArray = [33, 82, 44]
    CurrentArray = []
    for x in range(3):
        r, g, b = IsOnCheckForChartCourseTaskImage.getpixel((x * 9, 0))
        CurrentArray.append(r)

    # print(f'ValidArray({ValidArray}) VS ({CurrentArray}) CurrentArray')


    if ValidArray == CurrentArray:  # Pass If lights panel is open
        AU_Util.printupdate('Chart Course Task Panel Open!')
        AU_Tasker.DoChartCourseTask()
        AU_Util.ProcessEndTask()


def CheckKeysTask():
    # Take a screenshot of the top section of panel
    IsOnCheckForKeysTaskImage = pyautogui.screenshot(region=(1020, 450, 20, 1))


    ValidArray = [153, 96, 33]
    CurrentArray = []
    for x in range(3):
        r, g, b = IsOnCheckForKeysTaskImage.getpixel((x * 9, 0))
        CurrentArray.append(r)

    # print(f'ValidArray({ValidArray}) VS ({CurrentArray}) CurrentArray')


    if ValidArray == CurrentArray:  # Pass If lights panel is open
        AU_Util.printupdate('Keys Task Panel Open!')
        AU_Tasker.DoKeysTask()
        AU_Util.ProcessEndTask()


def CheckSwipeCardTask():

    # Take a screenshot of the top section of panel
    IsOnCheckForSwipeCardTaskImage = pyautogui.screenshot(region=(1030, 450, 20, 1))


    ValidArray = [0, 45, 81]
    CurrentArray = []
    for x in range(3):
        r, g, b = IsOnCheckForSwipeCardTaskImage.getpixel((x * 9, 0))
        CurrentArray.append(r)

    # print(f'ValidArray({ValidArray}) VS ({CurrentArray}) CurrentArray')


    if ValidArray == CurrentArray:  # Pass If lights panel is open
        AU_Util.printupdate('Swipe Card Task Panel Open!')
        AU_Tasker.DoSwipeCardTask()
        AU_Util.ProcessEndTask()


def CheckBoardingPassTask():

    # Take a screenshot of the top section of panel
    IsOnCheckForBoardingPassTaskImage = pyautogui.screenshot(region=(2015, 450, 20, 1))


    ValidArray = [104, 195, 228]
    CurrentArray = []
    for x in range(3):
        r, g, b = IsOnCheckForBoardingPassTaskImage.getpixel((x * 9, 0))
        CurrentArray.append(r)

    # print(f'ValidArray({ValidArray}) VS ({CurrentArray}) CurrentArray')


    if ValidArray == CurrentArray:  # Pass If lights panel is open
        AU_Util.printupdate('Boarding Pass Task Panel Open!')
        AU_Tasker.DoBoardingPassTask()
        AU_Util.ProcessEndTask()