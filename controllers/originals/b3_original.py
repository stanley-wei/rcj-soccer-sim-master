team = 'BLUE'
# rcj_soccer_player controller - ROBOT B3

###### REQUIRED in order to import files from B1 controller
import sys
from pathlib import Path
sys.path.append(str(Path('.').absolute().parent))
# You can now import scripts that you put into the folder with your
# robot B1 controller
if team == 'BLUE':
    from rcj_soccer_player_b1 import rcj_soccer_robot, utils
else:
    from rcj_soccer_player_y1 import rcj_soccer_robot, utils
######

# Feel free to import built-in libraries
import math


class MyRobot(rcj_soccer_robot.RCJSoccerRobot):
    def run(self):
        frame = 0
        facing = False
        shoot = False
        followBall = True
        togoDict = {'x':-1,'y':-1}
        arrived_score_angle=False
        shootBall=False
        while self.robot.step(rcj_soccer_robot.TIME_STEP) != -1:
            if self.is_new_data():
                frame += 1

                data = self.get_new_data()
                # print('data: ', data)
                # Get the position of our robot
                robot_pos = data[self.name]
                # Get the position of the ball
                ball_pos = data['ball']

                # Get angle between the robot and the ball and between the robot and the north
                if ball_pos['x']<=-0.5:
                    shoot=True
                    followBall=False
                else:
                    shoot=False
                    followBall=True

                if followBall:
                    # print('hi')
                    ball_angle, robot_angle = self.get_angles(ball_pos, data[self.name])
                    if facing:
                        self.left_motor.setVelocity(-10)
                        self.right_motor.setVelocity(-10)
                    if not facing:
                        if abs(360-ball_angle)<ball_angle:
                            self.left_motor.setVelocity(8)
                            self.right_motor.setVelocity(-8)
                        if ball_angle<abs(360-ball_angle):
                            self.left_motor.setVelocity(-8)
                            self.right_motor.setVelocity(8)
                        if abs(ball_angle)<=(12):
                            facing=True

                    if frame % 25==0:
                        facing=False
                # if shoot:
                #     angle_ball_to_goal=math.degrees(math.atan(abs(ball_pos['y'])/abs(ball_pos['x']-(-0.75))))
                #     print('angle_ball_to_goal: ',angle_ball_to_goal)
                #     # if togoDict['x']==-1 and togoDict['y']==-1:
                #     if ball_pos['y']>=0:
                #         togoDict['x']=ball_pos['x']+math.cos(angle_ball_to_goal)*0.125
                #         togoDict['y']=ball_pos['y']+math.sin(angle_ball_to_goal)*0.125
                #     else:
                #         togoDict['x']=ball_pos['x']+math.cos(angle_ball_to_goal)*0.125
                #         togoDict['y']=ball_pos['y']-math.sin(angle_ball_to_goal)*0.125
                #     # else:
                #         togo_angle, robot_angle = self.get_angles(togoDict, data[self.name])
                #         if abs(robot_pos['x']-togoDict['x'])<=0.05 and abs(robot_pos['y']-togoDict['y'])<=0.05:
                #             shootBall=True
                #             shoot=False
                #         if arrived_score_angle:
                #             self.left_motor.setVelocity(-10)
                #             self.right_motor.setVelocity(-10)
                #         else:
                #             if abs(360-togo_angle)<togo_angle:
                #                 self.left_motor.setVelocity(8)
                #                 self.right_motor.setVelocity(-8)
                #             if togo_angle<abs(360-togo_angle):
                #                 self.left_motor.setVelocity(-8)
                #                 self.right_motor.setVelocity(8)
                #             # if togo_angle>=85 and togo_angle<=95:
                #             #     self.left_motor.setVelocity(8)
                #             #     self.right_motor.setVelocity(-8)
                #             # if abs(360-togo_angle)>=85 and abs(360-togo_angle)<=95:
                #             #     self.left_motor.setVelocity(-8)
                #             #     self.right_motor.setVelocity(8)
                #             if abs(togo_angle)<=(12):
                #                 arrived_score_angle=True
                #
                # if shootBall:
                #     angle_to_ball, robot_angle=self.get_angles(ball_pos, data[self.name])
                #     if abs(360-angle_to_ball)<angle_to_ball:
                #         self.left_motor.setVelocity(8)
                #         self.right_motor.setVelocity(-8)
                #     if angle_to_ball<abs(360-angle_to_ball):
                #         self.left_motor.setVelocity(-8)
                #         self.right_motor.setVelocity(8)
                #     if angle_to_ball>=85 and angle_to_ball<=95:
                #         self.left_motor.setVelocity(8)
                #         self.right_motor.setVelocity(-8)
                #     if abs(360-angle_to_ball)>=85 and abs(360-angle_to_ball)<=95:
                #         self.left_motor.setVelocity(-8)
                #         self.right_motor.setVelocity(8)
                #     if abs(angle_to_ball)<=(12):
                #         self.left_motor.setVelocity(-10)
                #         self.right_motor.setVelocity(10)


                        # goto togo
                    # if ball_angle>=40:
                    #     # print('pee')
                    #     facing=False

my_robot = MyRobot()
my_robot.run()
