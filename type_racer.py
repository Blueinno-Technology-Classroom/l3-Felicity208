import pyautogui as gui
from PIL import ImageGrab
import pytesseract as tes
from type_racer_helper import find_white


changeFormatBox = None
while changeFormatBox is None:
    try:
        changeFormatBox = gui.locateOnScreen(
            'change_format.png',
            confidence = 0.8
            )
    except Exception as e:
        print(e)
        continue    
print(f'changeFormatBox: {changeFormatBox}')

screenshot = ImageGrab.grab()
screenshot.save('screenshot.png')
screenshot_data = screenshot.load()
print(f'Screenshot size: {screenshot.size}')

start_point = (changeFormatBox.left, changeFormatBox.top)
bottom = changeFormatBox.top + changeFormatBox.height 
top = find_white(
    direction = 'up',
    start_point = start_point,
    screenshot = screenshot
)

left = find_white(
    direction='left',
    start_point = start_point,
    screenshot = screenshot
)

right = find_white(
    direction='right',
    start_point = start_point,
    screenshot = screenshot
)

print(f'left = {left}, top = {top}, bottom = {bottom}, right = {right}')

left = int(left/2)
top = int(top/2)
bottom = int(bottom/2)
right = int(right/2)

paragraph = ImageGrab.grab(bbox= (left, top, bottom, right))
paragraph.save('paragraph.png')


text = tes.image_to_string('paragraph.png')
#gui.click(x = left, y = bottom+20)
#gui.typewrite(text)

for t in text:
    if t.isupper():
        gui.keyDown('shift')
        gui.press(t)
        gui.keyUp('shift')
    else:
        gui.press(t)