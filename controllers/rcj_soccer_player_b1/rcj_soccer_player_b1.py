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
        while self.robot.step(rcj_soccer_robot.TIME_STEP) != -1:
            if self.is_new_data():
                frame += 1
                if robot_pos['x'] < 0.38 and robot_pos['x'] > -0.37 and robot_pos['y'] < 0.05 and robot_pos['y'] > 0.05:
                    center = True
                if frame % 60 == 0:
                    print(center)
                data = self.get_new_data()

                # Get the position of our robot
                robot_pos = data[self.name]
                #print(robot_pos)
                # Get the position of the ball
                ball_pos = data['ball']

                # go to center
                togo = [0.375,0]
                v1 = robot_pos['x']-togo[0]
                v2 = robot_pos['y']-togo[1]

                theta=math.radians(math.atan(float(v2/v1)))

                if center == True:
                    if facing == True:
                        left_speed=-5
                        rights_speed=-5
                    # 0.174 radians is 10 degrees
                    left_speed=-5
                    right_speed=-3
                    if abs(robot_pos['orientation']-theta) <= 0.174:
                        facing=True

                    if (robot_pos['x']-togo[0]) <= 0.05:
                        if robot_pos['y'] <= 0+0.025 and robot_pos['y'] >= 0-0.025:
                            left_speed=-5
                            right_speed=5
                            if robot_pos['orientation']==0:
                                left_speed=0
                                right_speed=0
                                center = False

# If robot isn't centered on x,
                if center == False:
                    if frame % 2 == 0:
                        left_speed=-0.1
                        right_speed=-0.1
                    else:
                        left_speed=0.1
                        right_speed=0.1

                    if ball_pos['x'] == 0 and ball_pos['y'] == 0:
                        left_speed = -10
                        right_speed = -10

                # Get angle between the robot and the ball
                # and between the robot and the north
                ball_angle, robot_angle = self.get_angles(ball_pos, robot_pos)

                # Compute the speed for motors
                direction = utils.get_direction(ball_angle)

                # If the robot has the ball right in front of it, go forward,
                # rotate otherwise

                # if direction == 0:
                #     left_speed = -10
                #     right_speed = -10
                # else:
                #     left_speed = direction * 4
                #     right_speed = direction * -4

                # Set the speed to motors
                self.left_motor.setVelocity(left_speed)
                self.right_motor.setVelocity(right_speed)
                frameCounter += 1


my_robot = MyRobot()
my_robot.run()
