import pyautogui

import numpy as np
import time

from dino import Dino


# https://elgoog.im/t-rex/

def is_game_over():
    restart_button_area = pyautogui.screenshot(region=(dino.x + 245 + dino.width, dino.y - 15, 1, 1))

    arr_restart = np.array(restart_button_area)
    return arr_restart.mean() == 83


if __name__ == '__main__':
    # Time to switch to the game window
    time.sleep(2)

    dino = Dino()

    while 1:

        if dino.detect_obstacle():
            dino.jump()
            dino.adjust_scan_area()

        if is_game_over():
            dino.reset_jumps_count()
            dino.reset_scan_area()
            time.sleep(1)
            pyautogui.click(dino.x + dino.width + 245, dino.y - 15)

        print(dino.jumps)
