import numpy as np

import pyautogui


class Dino:
    def __init__(self):
        self.x, self.y, self.width, self.height = pyautogui.locateOnScreen('images/dino.png', confidence=0.8)

        self.reset_jumps_count()
        self.reset_scan_area()

    def adjust_scan_area(self):
        if 5 < self.jumps < 20:
            self.rectangle_area_to_scan = ((self.x + self.width) + 15 + 5 * self.jumps,
                                           self.y,
                                           self.width / 2,
                                           self.height - 10)

        elif self.jumps >= 20:
            self.rectangle_area_to_scan = ((self.x + self.width) + 25 + 6 * 20,
                                           self.y,
                                           self.width / 2,
                                           self.height - 10)

    def detect_obstacle(self):
        arr_ahead = np.array(pyautogui.screenshot(region=self.rectangle_area_to_scan))
        return arr_ahead.mean() < 247

    def jump(self):
        pyautogui.press('up')
        self.jumps += 1

    def reset_jumps_count(self):
        self.jumps = 0


    def reset_scan_area(self):
        self.rectangle_area_to_scan = (self.x + self.width + 10,
                                       self.y,
                                       self.width // 2,
                                       self.height - 10)