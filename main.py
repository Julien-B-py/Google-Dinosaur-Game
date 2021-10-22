import pyautogui

import numpy as np
import time

from dino import Dino


# https://elgoog.im/t-rex/

def is_game_over() -> bool:
    """
    Check if the replay button is displayed on the screen to determine if the game is over.
        Returns:
            bool: True if the game is over
    """
    # Take a screenshot of a single pixel (1x1).
    # The x and y values have been determined manually after some testing.
    # This specific pixel will change color depending on the restart button visibility.
    restart_button_area = pyautogui.screenshot(region=(dino.x + dino.width + 245,
                                                       dino.y - 15,
                                                       1,
                                                       1))
    # Convert the image as array
    arr_restart = np.array(restart_button_area)
    # If the mean value is 83 it means the restart button is visible.
    # Button is composed of pixels which RGB values are (83, 83, 83).
    return arr_restart.mean() == 83


if __name__ == "__main__":
    # Time to allow the user to switch to the game window
    time.sleep(2)

    dino = Dino()

    # Make the dinosaur jump
    # Auto restart when game is over
    while 1:

        # If an obstacle is detected make the dino jump
        # Adjust the scanned area coordinates to compensate for the game speed up over time
        if dino.detect_obstacle():
            dino.jump()
            dino.adjust_scan_area()

        # If the replay button is visible reset the dino jump count
        # Reset the scanned area coordinates we previously adjusted to compensate for the game speed up over time
        # Finally click the restart button after 1 sec
        if is_game_over():
            dino.reset_jumps_count()
            dino.reset_scan_area()
            time.sleep(1)
            pyautogui.click(dino.x + dino.width + 245, dino.y - 15)


