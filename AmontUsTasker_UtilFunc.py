# Controls   Imports
import keyboard
import pyautogui

# General Imports
import os
from PIL import Image, ImageFont, ImageDraw
from time import sleep
import datetime
from scipy.linalg import norm
import numpy as np
import PIL
import cv2
import pytesseract

#Load up Pixaled Images Database
PixalatedNumbersPath = './images/PixaletedNums/'
PixalatedNumberImages = []
for ImgName in os.listdir(PixalatedNumbersPath):
    NumImg = Image.open(PixalatedNumbersPath + ImgName)
    PixalatedNumberImages.append([NumImg, ImgName[:-4]])

# Load up Smooth Images Database
SmoothNumbersPath = './images/SmoothNums/'
SmoothNumberImages = []
for ImgName in os.listdir(SmoothNumbersPath):
    NumImg = Image.open(SmoothNumbersPath + ImgName)
    SmoothNumberImages.append([NumImg, ImgName[:-4]])

# Load up Manifold Images Database
ManifoldNumbersPath = './images/ManifoldNums/'
ManifoldNumberImages = []
for ImgName in os.listdir(ManifoldNumbersPath):
    NumImg = Image.open(ManifoldNumbersPath + ImgName)
    ManifoldNumberImages.append([NumImg, ImgName[:-4]])


def printupdate(Text = ''):
    print(f'  >[{datetime.datetime.now().strftime("%H:%M:%S")}] - {Text}')



def getRGBofCords(x, y):
    return pyautogui.screenshot(region=(x, y, 1, 1)).getpixel((0, 0))


def ProcessImageForDetection(IMAGE: PIL.Image):
    IMAGE_RGB = IMAGE.convert('RGB')
    IMAGE_np_Array = np.array(IMAGE_RGB)
    IMAGE_Blurr = cv2.blur(IMAGE_np_Array, (11, 11))
    IMAGE_Gray = cv2.cvtColor(IMAGE_Blurr, cv2.COLOR_BGR2GRAY)
    IMAGE_Thresh = 255 - cv2.threshold(IMAGE_Gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    return IMAGE_Thresh

def DEBUG_return_IMAGE_withMarkerOn_Cords(IMG:PIL.Image, x:int = 0, y:int = 0, Big:bool = False, AltColor:bool = False, Text:str = False):
    MarkerPath = "./images/"

    if Big == True:
        MarkerPath = MarkerPath + 'Marker_Big.png'
    else:
        MarkerPath = MarkerPath + 'Marker_Small_'
        if AltColor == True:
            MarkerPath = MarkerPath + 'Blue.png'
        else:
            MarkerPath = MarkerPath + 'Red.png'

    Marker = Image.open(MarkerPath)
    if Big == True:
        IMG.paste(Marker, (x + 50, y + 50), Marker)
    else:
        IMG.paste(Marker, (x, y), Marker)


    if Text != False:

        draw = ImageDraw.Draw(IMG)
        # font = ImageFont.truetype(<font-file>, <font-size>)
        font = ImageFont.truetype("Ubuntu-B.ttf", 24)
        # draw.text((x, y),"Sample Text",(r,g,b))
        draw.text((x + 15, y + 10), Text, (200, 200, 200), font=font)

    return IMG


# Should prolly cache manifold database and compare to that but lazy
def GetImageDifference(Image_1, Image_2):
    def compare_images(img1, img2):
        # normalize to compensate for exposure difference
        img1 = normalize(img1)
        img2 = normalize(img2)
        # calculate the difference and its norms
        diff = img1 - img2  # elementwise for scipy arrays
        m_norm = np.sum(abs(diff))  # Manhattan norm
        z_norm = norm(diff.ravel(), 0)  # Zero norm
        return (m_norm, z_norm)

    def to_grayscale(arr):
        "If arr is a color image (3D array), convert it to grayscale (2D array)."
        if len(arr.shape) == 3:
            return np.average(arr, -1)  # average over the last axis (color channels)
        else:
            return arr

    def normalize(arr):
        rng = arr.max()-arr.min()
        amin = arr.min()
        return (arr-amin)*255/rng

    file1 = np.array(Image_1)
    file2 = np.array(Image_2)
    # read images as 2D arrays (convert to grayscale for simplicity)
    img1 = to_grayscale(file1.astype(float))
    img2 = to_grayscale(file2.astype(float))
    # compare
    n_m, n_0 = compare_images(img1, img2)
    # print("Manhattan norm:", n_m)
    # print("^^^^ per pixel:", n_m / img1.size)
    # print("Zero norm:", n_0)
    # print("^^^^ per pixel:", n_0 * 1.0 / img1.size)
    Rounder = round((n_0 * 1.0 / img1.size), 2) * 10
    # print(f'returnValue = {[Rounder, n_0]} --- ', end='')
    return [Rounder, n_0]

X = 0
def CompareImageToPixalatedDatabase(InputImage):
    global X
    X = 0
    for PixalatedImage in PixalatedNumberImages:
        DifferenceScore = 1001 # Default it incase of fail
        try:
            DifferenceScore = GetImageDifference(PixalatedImage[0], InputImage)[1]
        except ValueError as E:
            printupdate(f'Image Compare failed - likely due to panel closing.(Pixalated Compare)')
        X = X + 1
        # print(DifferenceScore)
        if DifferenceScore < 1000:
            return PixalatedImage[1]


X = 0
def CompareImageToSmoothDatabase(InputImage):
    global X
    X = 0
    for SmoothImage in SmoothNumberImages:
        DifferenceScore = 1001 # Default it incase of fail
        try:
            DifferenceScore = GetImageDifference(SmoothImage[0], InputImage)[1]
        except ValueError as E:
            printupdate(f'Image Compare failed - likely due to panel closing.(Smooth Compare)')
        # print(f'              At #{X} score was {DifferenceScore}')
        X = X + 1
        if DifferenceScore < 2300:
            return SmoothImage[1]

X = 0
def CompareImageToManifoldDatabase(InputImage):
    global X
    X = 0
    for ManifoldImage in ManifoldNumberImages:
        DifferenceScore = 1001 # Default it incase of fail
        try:
            DifferenceScore = GetImageDifference(ManifoldImage[0], InputImage)[1]
        except ValueError as E:
            printupdate(f'Image Compare failed - likely due to panel closing.(Manifold Compare)')
        # print(f'              At #{X} score was {DifferenceScore}')
        X = X + 1
        if DifferenceScore < 2300:
            return ManifoldImage[1]