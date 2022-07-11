"""romi_test controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot, Motor
from math import sin

# create the Robot instance.
robot = Robot()

Motor3 = robot.getDevice('motor_3')
Motor2 = robot.getDevice('motor_2')

# leftMotor.setPosition(float('inf'))
# rightMotor.setPosition(float('inf'))


# get the time step of the current world.
timestep = int(robot.getBasicTimeStep())
simtime = 0

# You should insert a getDevice-like function in order to get the
# instance of a device of the robot. Something like:
#  motor = robot.getDevice('motorname')
#  ds = robot.getDevice('dsname')
#  ds.enable(timestep)

# Main loop:
# - perform simulation steps until Webots is stopping the controller
while robot.step(timestep) != -1:
    simtime+=(timestep/1000.0)
    # Read the sensors:
    # Enter here functions to read sensor data, like:
    #  val = ds.getValue()
    # leftMotor.setVelocity(1)
    # rightMotor.setVelocity(1)
    # Process sensor data here.
    Motor3.setPosition(0.2*sin(simtime)+1)
    Motor2.setPosition(-0.2*sin(simtime)+1)

    # Enter here functions to send actuator commands, like:
    #  motor.setPosition(10.0)
    pass

# Enter here exit cleanup code.
