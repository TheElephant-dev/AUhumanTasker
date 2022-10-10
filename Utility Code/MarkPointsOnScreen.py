import pyautogui


from PIL import Image


PanelXStart = 1250
PanelYStart = 1330







MarkSpot = Image.open("images/MarkSpot.png").convert('RGBA')
def write_pixal_Location_On_Image(X = 100, Y = 100): ## RGB Values of pixal:
    LocationsImage.paste(MarkSpot, (X-50, Y-50), MarkSpot)
    LocationsImage.save('images/LocationsImage.png')






#ScreenshotImage = Image.open("images/OriginalPanel.png")
ScreenshotImage = pyautogui.screenshot('images/LightsPanel.png', region=(1750,500, 300, 1000))
LocationsImage = ScreenshotImage
# ## RGB Values of pixal:
# r, g, b = ScreenshotImage.getpixel((1, 1))






X_Marker = 0
for x in range(2):
    Y_Marker = 0
    for x in range(4):
        r, g, b = ScreenshotImage.getpixel((X_Marker, Y_Marker))
        print(f'(r={r}, g={g}, b={b})')
        write_pixal_Location_On_Image(X=X_Marker, Y=Y_Marker)
        Y_Marker = Y_Marker + 333
    X_Marker = X_Marker + 295



