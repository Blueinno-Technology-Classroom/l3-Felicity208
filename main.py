import pyautogui as gui
from PIL import ImageGrab
import pytesseract as tes

#gui.displayMousePosition()


left = 46
top = 426
right = 685
bottom = 469
size = bottom - top

gui.click(x=left, y=top)
screenshot = ImageGrab.grab(bbox=(left, top, right, bottom))
screenshot.save('line1.png')
text = tes.image_to_string('line1.png')
gui.typewrite(text + ' ')

while True:
    screenshot2 = ImageGrab.grab(bbox =(left, top + size, right, bottom+size))
    screenshot2.save('line2.png')
    text = tes.image_to_string('line2.png')
    gui.typewrite(text + ' ')






