"""zumo_test controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot, Motor

# create the Robot instance.
robot = Robot()
#enable sensors
robot.getDevice('position_left').enable(5)
robot.getDevice('position_right').enable(5)
#TODO move this into library? or no?


#plan is to move zumo interact into a library that is sim-transparent
#this library should end up being its own git repo, then a submodule of this one.
#that will allow for greater abstraction, and means Arduino code can go in there with docu
def zumoInteract(robot,leftCounts,rightCounts):
    lM = robot.getDevice('motor_left')
    rM = robot.getDevice('motor_right')
    lP = robot.getDevice('position_left').getValue()
    rP = robot.getDevice('position_right').getValue()
    lV = lM.getVelocity()
    rV = rM.getVelocity()

    #now calculate omega of motors
    lO = lV/.016 #approximate
    rO = rV/.016

    kt = .05 #Nm/A
    R = 4 #Ohms
    Vbatt = 6 #volts
    r = .016
    #TODO constrain input counts
    Vleft_command = leftCounts/400*Vbatt
    Vright_command = rightCounts/400*Vbatt

    #this should be updated to include Jm,bm
    force_left = kt/(R*r)*(Vleft_command-kt*lO)
    force_right = kt/(R*r)*(Vright_command-kt*rO)

    #set motor force
    lM.setForce(force_left)
    rM.setForce(force_right)

    #update so that these are in encoder counts
    left_feedback = lP
    right_feedabck = rP



    return lP,rP

# get the time step of the current world.
timestep = int(robot.getBasicTimeStep())

# You should insert a getDevice-like function in order to get the
# instance of a device of the robot. Something like:
#  motor = robot.getDevice('motorname')
#  ds = robot.getDevice('dsname')
#  ds.enable(timestep)

# Main loop:
# - perform simulation steps until Webots is stopping the controller
while robot.step(timestep) != -1:
    lP,rP = zumoInteract(robot,-400,400)
    print(lP,rP)


# Enter here exit cleanup code.
