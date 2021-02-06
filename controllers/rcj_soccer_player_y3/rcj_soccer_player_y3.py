team = 'BLUE'
# rcj_soccer_player controller - ROBOT Y1

# Feel free to import built-in libraries
import math

import sys
from pathlib import Path
sys.path.append(str(Path('.').absolute().parent))
# You can also import scripts that you put into the folder with controller
if team == 'BLUE':
    from rcj_soccer_player_b1 import rcj_soccer_robot, utils
else:
    from rcj_soccer_player_y1 import rcj_soccer_robot, utils


class MyRobot(rcj_soccer_robot.RCJSoccerRobot):
    def run(self):
        frameCounter = 0
        while self.robot.step(rcj_soccer_robot.TIME_STEP) != -1:
            if self.is_new_data():
                data = self.get_new_data()

                # Get the position of our robot
                robot_pos = data[self.name]
                # Get the position of the ball
                ball_pos = data['ball']

                # Get angle between the robot and the ball
                # and between the robot and the north
                ball_angle, robot_angle = self.get_angles(ball_pos, robot_pos)

                # # Compute the speed for motors
                direction = utils.get_direction(ball_angle)
                #
                # # If the robot has the ball right in front of it, go forward,
                # # rotate otherwise
                # # 0 forward, -1 right, 1 left
                # if direction == 0:
                #     left_speed = -5
                #     right_speed = -5
                # else:
                #     left_speed = direction * 4
                #     right_speed = direction * -4

                status = ""
                target_x = -0.07
                idle_speed = 2
                if robot_pos['y'] > -0.06 and robot_pos['y'] < 0.06:
                    if ball_pos['y'] > -0.05 and ball_pos['y'] < 0.05 and robot_pos['x'] < ball_pos['x']:
                        if direction == 0:
                            left_speed = -10
                            right_speed = -10
                            status = "charging"
                        else:
                            left_speed = direction * 4
                            right_speed = direction * -4
                            status = "aiming"
                    else:
                        if ball_pos['y'] < 0.3 and ball_pos['y'] > -0.3 and robot_pos['x'] < ball_pos['x']:
                            target_x = ball_pos['x'] - 0.08
                            idle_speed = 10
                        if robot_angle < ((math.pi / 2) - 0.05):
                            left_speed = 2
                            right_speed = -2
                            status = "turning"
                        elif robot_angle > ((math.pi / 2) + 0.05):
                            left_speed = -2
                            right_speed = 2
                            status = "turning"
                        else:
                            if robot_pos['x'] < target_x:
                                left_speed = -idle_speed
                                right_speed = -idle_speed
                            else:
                                left_speed = idle_speed
                                right_speed = idle_speed
                            status = "idling"
                else:
                    if robot_angle < (math.pi - 1):
                        left_speed = 0
                        right_speed = 0
                        status = "turning back"
                    elif robot_angle > (math.pi +1):
                        left_speed = 0
                        right_speed = 0
                        status = "turning back"
                    else:
                        left_speed = -5
                        right_speed = -5
                        status = "returning"

                # Set the speed to motors
                self.left_motor.setVelocity(left_speed)
                self.right_motor.setVelocity(right_speed)
                frameCounter += 1
                if frameCounter % 60 == 0:
                    print("Frame counter: " + str(frameCounter))
                    print("Robot pos: " + str(robot_pos))
                    print("Ball angle: " + str(ball_angle))
                    print("Robot angle: " + str(robot_angle))
                    print("Status: " + str(status))

my_robot = MyRobot()
my_robot.run()
