import numpy as np

import pyautogui


class Dino:
    def __init__(self):
        # Get the initial position (x, y) and dimensions (width, height) of the dinosaur.
        self.x, self.y, self.width, self.height = pyautogui.locateOnScreen("images/dino.png", confidence=0.8)

        self.reset_jumps_count()
        self.reset_scan_area()

    def adjust_scan_area(self) -> None:
        """
        Adjust area coordinates that we will analyze to determine if an obstacle is on the way.
        Considering the horizontal scrolling speed is increasing over time we have to detect obstacles sooner over time
        To do so we increase the x location over time.
        This is not making pixel perfect runs but we can score more than 500 points pretty easily.
        """
        # In the early game the scrolling speed is kinda slow so we don't have to anticipate that much
        # We use the default location until the dinosaur jumped 5 times.

        # When the dinosaur jumped more than 5 times the speed will increase
        # We add another coefficient to detect obstacles from a longer distance
        if 5 < self.jumps < 20:
            self.rectangle_area_to_scan = (self.x + self.width + 15 + 5 * self.jumps,
                                           self.y,
                                           self.width // 2,
                                           self.height - 10)

        # After a certain amount of time/jumps it seems like the scrolling speed is capped (not sure about that)
        # We set a constant rectangle location much more to the right than the original one
        elif self.jumps >= 20:
            self.rectangle_area_to_scan = (self.x + self.width + 25 + 6 * 20,
                                           self.y,
                                           self.width // 2,
                                           self.height - 10)

    def detect_obstacle(self) -> bool:
        """
        Take a screenshot of the defined rectangle region located to the right of the dinosaur.
        If no obstacle is detected inside this rectangle, the area will be filled with a solid (247, 247, 247) RGB color
        We just have to analyze this area regularly and check for any variation
            Returns:
                bool: True if an obstacle is on the way
        """
        # Take a screenshot of a rectangle with a predetermined x, y, width, height
        # Convert the image as array
        arr_ahead = np.array(pyautogui.screenshot(region=self.rectangle_area_to_scan))
        # If the mean value is less than 247 it means there is an obstacle on the way
        return arr_ahead.mean() < 247

    def jump(self) -> None:
        """
        Makes the dinosaur jump and increase the total jumps value by 1.
        """
        pyautogui.press("up")
        self.jumps += 1

    def reset_jumps_count(self) -> None:
        """
        Reset the total jumps value to 0.
        """
        self.jumps = 0

    def reset_scan_area(self) -> None:
        """
        Reset/initialize the specific area coordinates that we will analyze to determine if an obstacle is on the way.
        Basically we determine a rectangle region that is supposed to remain a solid whitish color.
        This region will be on the right of the dinosaur.
        """
        self.rectangle_area_to_scan = (self.x + self.width + 10,
                                       self.y,
                                       self.width // 2,
                                       self.height - 10)
