import pyautogui

import numpy as np
import time

# https://elgoog.im/t-rex/

jumps = {'count': 0}
pause = {'time': 0.1}


def check_for_obstacle():
    ahead = pyautogui.screenshot(region=rectangle_area_to_scan)

    arr_ahead = np.array(ahead)

    if arr_ahead.mean() < 247:
        jump()


def is_game_over():
    restart_button_area = pyautogui.screenshot(region=(dino_x + 245 + dino_width, dino_y - 15, 1, 1))

    arr_restart = np.array(restart_button_area)
    if arr_restart.mean() == 83:
        return True


def jump():
    pyautogui.press('up')
    jumps['count'] += 1

    if pause['time'] > 0:
        time.sleep(pause['time'])

    if jumps['count'] % 5 == 0:
        pause['time'] -= 0.01


if __name__ == '__main__':
    time.sleep(2)

    dino_x, dino_y, dino_width, dino_height = pyautogui.locateOnScreen('images/dino.png', confidence=0.8)

    time.sleep(2)

    rectangle_area_to_scan = ((dino_x + dino_width) + 10, dino_y, dino_width / 2, dino_height - 10)

    while 1:
        check_for_obstacle()

        if jumps['count'] < 20:
            rectangle_area_to_scan = (
                (dino_x + dino_width) + 20 + 5 * jumps['count'], dino_y, dino_width / 2, dino_height - 10)

        else:
            rectangle_area_to_scan = ((dino_x + dino_width) + 20 + 6 * 20, dino_y, dino_width / 2, dino_height - 10)

        print(jumps['count'])

        if is_game_over():
            jumps['count'] = 0
            pause['time'] = 0.1
            time.sleep(1)
            pyautogui.click(dino_x + 245 + dino_width, dino_y - 15)
