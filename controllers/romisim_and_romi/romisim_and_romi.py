"""romi_test controller."""
#import the sys library so we can get path above
import sys
#add ES302 directory to path because Romi.py is there
sys.path.append("../ES302_Romi")
#now import the Romi library
from Romi import Romi
#import sine function to use
from math import sin

#open a file so we can save data
f = open("simdata.txt","w")

# create the Robot instance.
#instantiating a Romi library object in simulation mode
#automatically loads proper WeBots libraries.
#the webots robot class lives inside of romi.simromi
romi = Romi(sim=True)
#create a second object to talk to REAL romi!
romi2 = Romi(port='COM5')

# get the time step of the current world.
timestep = int(romi.simromi.getBasicTimeStep())
#initialize a simulation time for us to use
simtime = 0

# Main loop:
# - perform simulation steps until Webots is stopping the controller
while romi.simromi.step(timestep) != -1:
    simtime+=(timestep/1000.0)

    #send a sine wave motor command to the wheels
    motorspeed_amp = 75
    #send a sine wave velocity to both motors
    wheelcmd = int(motorspeed_amp*sin(simtime))
    #send sine waves to each servo too!
    s1cmd = int(10*sin(simtime)+90)
    s2cmd = int(90+90*sin(simtime))
    s3cmd = int(20*sin(simtime)+90)
    #update the simulated Romi with our commands:
    #commands: motor_left,motor_right,servo_1,servo_2,servo_3
    romi.update(wheelcmd,wheelcmd,s1cmd,s2cmd,s3cmd)
    romi2.update(wheelcmd,wheelcmd,s1cmd,s2cmd,s3cmd)
    #now collect data from the romi's sensors and save to a file!

    #make first few columns echo the commands:
    #write time and commands to file so we know what we asked the robot to do:
    string1 = format(simtime,'0.3f')+","+format(wheelcmd,'d')+","+format(wheelcmd,'d')+","+format(s1cmd,'d')+','+format(s2cmd,'d')+','+format(s3cmd,'d')+','
    #now write the feedback from the actual robot's sensors:
    #simulated:
    f.write(romi.datastring.strip()+",")
    #real:
    f.write(romi2.datastring)
