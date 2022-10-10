# import cv2
# import pytesseract
# from PIL import Image
# from matplotlib import cm
# import numpy as np
#
#
# image = cv2.imread('ManifoldTesting.png')
# image = cv2.blur(image,(10,10))
#
# gry = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# thr = cv2.adaptiveThreshold(gry, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 61, 9)
#
# im = Image.fromarray(np.uint8(cm.gist_earth(thr)*255))
# im.show()
# ManifoldNumberText =  pytesseract.image_to_string(thr, config='--psm 13 -c tessedit_char_whitelist=0123456789')[:-2]
#
#
# print(ManifoldNumberText)




from PIL import Image
from matplotlib.pyplot import imread
from scipy.linalg import norm
import numpy as np


Img1 = Image.open("Test1.png")
Img2 = Image.open("Test2.png")
Img3 = Image.open("Test3.png")
Img4 = Image.open("Test4.png")
ManiComp1 = Image.open("ManiComp1.png")
ManiComp2 = Image.open("ManiComp2.png")
ManiComp3 = Image.open("ManiComp3.png")
ManiComp4 = Image.open("ManiComp4.png")
ManiComp5 = Image.open("ManiComp5.png")
ManiComp6 = Image.open("ManiComp6.png")
ManiComp7 = Image.open("ManiComp7.png")
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
    print("Manhattan norm:", n_m, "/ per pixel:", n_m / img1.size)
    print("Zero norm:", n_0, "/ per pixel:", n_0 * 1.0 / img1.size)
    return round((n_0 * 1.0 / img1.size), 2) * 10



print(f'Compareing ManiComp1 and ManiComp1: {GetImageDifference(ManiComp1, ManiComp1)}\n')

print(f'Compareing ManiComp1 and ManiComp2: {GetImageDifference(ManiComp1, ManiComp2)}\n')

print(f'Compareing ManiComp1 and ManiComp3: {GetImageDifference(ManiComp1, ManiComp3)}\n')

print(f'Compareing ManiComp1 and ManiComp4: {GetImageDifference(ManiComp1, ManiComp4)}\n')

print(f'Compareing ManiComp1 and ManiComp5: {GetImageDifference(ManiComp1, ManiComp5)}\n')

print(f'Compareing ManiComp1 and ManiComp6: {GetImageDifference(ManiComp1, ManiComp6)}\n')

print(f'Compareing ManiComp1 and ManiComp7: {GetImageDifference(ManiComp1, ManiComp7)}\n')

print(f'Compareing ManiComp4 and ManiComp6: {GetImageDifference(ManiComp4, ManiComp6)}\n')
