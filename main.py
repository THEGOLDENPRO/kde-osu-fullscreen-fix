#!/usr/bin/python

# This is the daemon that should run as a service in the background.
# It will detect osu! lazer launching and attempt to full screen it with the "F11" key bind.
# 
# It requires "dotool" (NOT "xdotool"!), which only supports Wayland. :(

import os
import time
import psutil
from subprocess import PIPE, Popen
from logging import getLogger, DEBUG, basicConfig

logger = getLogger("koff-daemon")
basicConfig(level = DEBUG)

F11_DELAY = int(os.environ.get("KOFF_DELAY", "4")) # Adjust this if osu! is taking longer than expected to spawn a focused window.
F11_REPEAT_AMOUNT = int(os.environ.get("KOFF_REPEAT_AMOUNT", "3")) # NOTE: Make sure full screen is already toggled in osu!

POLLING_RATE = int(os.environ.get("KOFF_POLLING_RATE", "4")) # Every x seconds it will scan all process and check if osu! has launched.

PROCESS_NAME = "osu!"

osu_is_up = False

def did_osu_launch():
    global osu_is_up

    logger.debug("Checking if osu! has launched...")

    for process in psutil.process_iter():

        if PROCESS_NAME == process.name().lower():
            if osu_is_up is True:
                return False, process

            osu_is_up = True
            return True, process

    osu_is_up = False
    return False, None


if __name__ == "__main__":

    

    while True:
        has_launched, process = did_osu_launch()

        if has_launched:
            logger.info("osu! launch detected!")
            logger.info(f"Triggering full screen in '{F11_DELAY}' seconds...")

            time.sleep(F11_DELAY) # Takes time for the window to actually spawn.

            popen = Popen(
                args = ["dotool"], 
                stdout = PIPE, 
                stdin = PIPE, 
                stderr = PIPE, 
                text = True
            )

            popen.communicate("key f11\n" * F11_REPEAT_AMOUNT)

            logger.info("Triggered!")

        time.sleep(POLLING_RATE)