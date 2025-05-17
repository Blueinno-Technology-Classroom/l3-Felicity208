import pyautogui as gui
from PIL import ImageGrab
import numpy as np
#gui.displayMousePosition()

gui.PAUSE = 0

 ###PREP###

left = 281
right = 535
top = 608
bottom = 621

screenshot = ImageGrab.grab(
    bbox =(left, top, right, bottom)
)

screenshot.save('gray area.png')
keys = [
    "s",
    "d",
    "f",
    "space",
    "j",
    "k",
    "l"
]

div_width = (right - left) // len(keys)
initial_space = []   #grayscale img data
for i in range(len(keys)):
    start_x = i *div_width
    end_x = (i+1) * div_width

    div = screenshot.crop((start_x, 0, end_x, screenshot.height))
    div.save(f'div{i}.png')

    div_gray = div.convert("L")
    div.save(f'div_gray_{i}.png')

    img_data = np.array(div_gray)
    initial_space.append(img_data)
    
##PREP DONE###

print("You may start the game now")
while True:
    latest_img = ImageGrab.grab(bbox = (left, top, right, bottom))
    latest_img.save('latest.png')
    latest_divs = []  #latest grayscale img data
    for i in range(len(keys)):
        start_x = i *div_width
        end_x = (i+1) * div_width

        div = latest_img.crop((start_x, 0, end_x, latest_img.height))

        div_gray = div.convert("L")
        img_data = np.array(div_gray)
        
        latest_divs.append(img_data)
    
    for i in range (len(keys)):
        img1 = initial_space[i]
        img2 = latest_divs[i]

        diff = np.sum((img1.astype('float') - img2.astype('float')) ** 2)

        #estimation of percentage of change: 0 < diff < 1 (the value will be under 1)

        diff /= float(img1.shape[0] * img2.shape[1])
        #print(f'area{i}, diff: {int(diff)}')

        if diff > 1300:
            gui.keyDown(keys[i])
            #gui.typewrite(keys[i])
        else:
            gui.keyUp(keys[i])

