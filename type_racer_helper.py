from typing import Literal
from PIL import Image


def find_white(
        direction: Literal['up', 'down', 'left', 'right'],
        start_point: tuple[int, int],
        screenshot: Image
) -> int or None:
    '''
    Given a direction, a starting point, and a screenshot, find the first white pixel in that direction.
    If no white pixel is found, return None.
    else return the index of the white pixel of the screenshot in the given direction.
    '''

    screenshot_data = screenshot.load()

    start = None
    stop = None
    step = None

    if direction == 'up':
        start = start_point[1]
        stop = 0
        step = -1
    elif direction == 'down':
        start = start_point[1]
        stop = screenshot.height
        step = 1
    elif direction == 'left':
        start = start_point[0]
        stop = 0
        step = -1
    elif direction == 'right':
        start = start_point[0]
        stop = screenshot.width
        step = 1

    if start is None or stop is None or step is None:
        raise Exception(f'Invalid direction: {direction}')

    for i in range(start, stop, step):
        if (direction == 'left') or (direction == 'right'):
            pixel = screenshot_data[i, start_point[1]]
        elif (direction == 'up') or (direction == 'down'):
            pixel = screenshot_data[start_point[0], i]
        r = pixel[0]
        g = pixel[1]
        b = pixel[2]

        if r >= 250 and g >= 250 and b >= 250:
            return i

    return None