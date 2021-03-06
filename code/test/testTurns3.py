# IMPORT MODULES FROM SUBFOLDERS #
""" It's neccesary in order to import modules not in the same folder, but in a different one.
This is the way to tell python the location on those subfolders: """
import os, sys, inspect

cmd_folder = os.path.realpath(os.path.abspath(os.path.split(inspect.getfile( inspect.currentframe() ))[0]))
if cmd_folder not in sys.path:
	sys.path.insert(0, cmd_folder)

sys.path.append('../')
# ------------------------------ #

from tortoise import Tortoise
import enums
import time

t = Tortoise()

while(True):

    t.shuffle45degrees(enums.Direction.clockwise)
    t.shuffle45degrees(enums.Direction.clockwise)
    time.sleep(1)

    t.shuffle45degrees(enums.Direction.counterClockwise)
    t.shuffle45degrees(enums.Direction.counterClockwise)
    time.sleep(1)

