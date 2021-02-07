team = 'BLUE'
# rcj_soccer_player controller - ROBOT B1

# Feel free to import built-in libraries
import math

# You can also import scripts that you put into the folder with controller
import rcj_soccer_robot
import utils


class MyRobot(rcj_soccer_robot.RCJSoccerRobot):
    def run(self):
        frame = 0
        facing = False
        shoot = False
        followBall = True
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

                if followBall:
                    # print('hi')
                    ball_angle, robot_angle = self.get_angles(ball_pos, data[self.name])
                    if facing:
                        self.left_motor.setVelocity(-10)
                        self.right_motor.setVelocity(-10)
                    if not facing:
                        # print('hi')
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
                    # if ball_angle>=40:
                    #     # print('pee')
                    #     facing=False

my_robot = MyRobot()
my_robot.run()
