team = 'BLUE'
import sys
from pathlib import Path
from rcj_soccer_player_b1 import rcj_soccer_robot, utils

import math

class MyRobot(rcj_soccer_robot.RCJSoccerRobot):
    def run(self):
        while self.robot.step(rcj_soccer_robot.TIME_STEP) != -1:
            if self.is_new_data():


my_robot = MyRobot()
my_robot.run()
